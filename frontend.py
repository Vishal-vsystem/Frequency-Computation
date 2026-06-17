import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

# Initialize the main figure layout with a modern dark/clean look
plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.canvas.manager.set_window_title('Frequency-Based Computational Framework')

# Leave room at the bottom for interactive control widgets
plt.subplots_adjust(bottom=0.22, hspace=0.4, wspace=0.25)

# Assign individual subplots to the architectural modules
ax_freq, ax_mem, ax_diff, ax_bayes = axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]

def process_pipeline(text):
    """Executes the complete 4-module computational pipeline on input text."""
    if not text.strip():
        text = "HELLO"  # Fallback default
        
    # -------------------------------------------------------------
    # MODULE 1: FREQUENCY ENCODING (f = f_0 + k * ASCII)
    # Using f_0 = 100, k = 2 matches your exact example: H(72)->244, E(69)->238...
    # -------------------------------------------------------------
    f_0 = 100
    k = 2
    frequencies = [f_0 + k * ord(char) for char in text]
    
    # Pad single-character strings so math operations don't break
    if len(frequencies) == 1:
        frequencies.append(frequencies[0])
        char_labels = [text[0], text[0] + " (2)"]
    else:
        char_labels = list(text)
        
    indices = np.arange(len(frequencies))

    # -------------------------------------------------------------
    # MODULE 2: NUMERICAL INTEGRATION (Memory Formation)
    # Cumulative Trapezoidal Rule: A = [(f_n + f_n-1) / 2] * dt
    # -------------------------------------------------------------
    memory = [0]
    for i in range(len(frequencies) - 1):
        area = (frequencies[i] + frequencies[i+1]) / 2.0  # dt = 1
        memory.append(memory[-1] + area)

    # -------------------------------------------------------------
    # MODULE 3: DIFFERENTIATION (Computational Activity)
    # D = f_n - f_n-1
    # -------------------------------------------------------------
    activity = [0]
    for i in range(1, len(frequencies)):
        activity.append(frequencies[i] - frequencies[i-1])

    # -------------------------------------------------------------
    # MODULE 4: BAYESIAN REASONING (Dynamic Decision Mapping)
    # Real-time conditional heuristic updates based on user context clues
    # -------------------------------------------------------------
    clean_text = text.upper().strip()
    p_greeting, p_name, p_random = 0.05, 0.05, 0.90  # Prior/default distribution
    
    if any(greet in clean_text for greet in ["HELL", "HI", "HEY", "GREET"]):
        p_greeting, p_name, p_random = 0.85, 0.10, 0.05
    elif any(name in clean_text for name in ["VISHAL", "KAVYA", "CURATOR"]):
        p_greeting, p_name, p_random = 0.10, 0.85, 0.05

    categories = ['Greeting', 'Name', 'Random']
    probabilities = [p_greeting, p_name, p_random]

    # =============================================================
    # RENDERING ENGINE (UI Updates)
    # =============================================================
    for ax in [ax_freq, ax_mem, ax_diff, ax_bayes]:
        ax.clear()

    # Graph 1: Frequency Encoding
    ax_freq.plot(indices, frequencies, marker='o', color='#00adb5', linewidth=2.5)
    ax_freq.set_xticks(indices)
    ax_freq.set_xticklabels(char_labels)
    ax_freq.set_title("Module 1: Frequency Encoding\n$f = 100 + 2 \cdot ASCII$", color='#111111', weight='bold')
    ax_freq.set_ylabel("Frequency (Hz)")

    # Graph 2: Memory Curve (Integration)
    ax_mem.fill_between(indices, memory, color='#00ff7f', alpha=0.2)
    ax_mem.plot(indices, memory, marker='s', color='#10b981', linewidth=2.5)
    ax_mem.set_xticks(indices)
    ax_mem.set_xticklabels(char_labels)
    ax_mem.set_title("Module 2: Integration Memory\n$M = \sum A_i$", color='#111111', weight='bold')
    ax_mem.set_ylabel("Accumulated Energy")

    # Graph 3: Activity Fluctuations (Differentiation)
    ax_diff.bar(indices, activity, color='#ff5722', alpha=0.75, width=0.4, edgecolor='#d03b0d')
    ax_diff.axhline(0, color='#333333', linewidth=1, linestyle='--')
    ax_diff.set_xticks(indices)
    ax_diff.set_xticklabels(char_labels)
    ax_diff.set_title("Module 3: Differentiation Activity\n$D = f_n - f_{n-1}$", color='#111111', weight='bold')
    ax_diff.set_ylabel("Rate of Change ($\Delta f$)")

    # Graph 4: Bayesian Probability Distribution
    bars = ax_bayes.bar(categories, probabilities, color=['#3f51b5', '#e91e63', '#9c27b0'], alpha=0.85, width=0.5)
    ax_bayes.set_ylim(0, 1.1)
    ax_bayes.set_title("Module 4: Bayesian Inference\nPosterior Probabilities", color='#111111', weight='bold')
    ax_bayes.set_ylabel("Probability Value")
    
    # Draw precise labels on top of the bars
    for bar in bars:
        height = bar.get_height()
        ax_bayes.text(bar.get_x() + bar.get_width()/2.0, height + 0.02, f"{height*100:.0f}%", 
                      ha='center', va='bottom', weight='bold', color='#333333')

    plt.draw()

# --- RUN INITIAL AUTOMATED SEED STATE ---
process_pipeline("HELLO")

# =============================================================
# FRONT END INTERACTIVE CONTROLS
# =============================================================
# Formulating precise bounding boxes for Input Text Field and Trigger Button
ax_box = plt.axes([0.22, 0.06, 0.45, 0.05])
text_box = TextBox(ax_box, 'Input String: ', initial="HELLO", color='white', hovercolor='#f3f4f6')

ax_btn = plt.axes([0.70, 0.06, 0.12, 0.05])
btn_simulate = Button(ax_btn, 'Simulate ⚡', color='#1f2937', hovercolor='#4b5563')
btn_simulate.label.set_color('white')
btn_simulate.label.set_weight('bold')

# Wire pipeline callbacks to front-end components
def on_submit_handler(val):
    process_pipeline(val)

text_box.on_submit(on_submit_handler)
btn_simulate.on_clicked(lambda event: process_pipeline(text_box.text))

plt.show()

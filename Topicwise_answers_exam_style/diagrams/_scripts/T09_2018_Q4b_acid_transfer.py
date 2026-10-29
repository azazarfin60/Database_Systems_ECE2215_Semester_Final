"""
Generates T09_2018_Q4b_acid_transfer.jpg
Illustrates the ACID properties using the $50 bank fund transfer transaction:
T1: read(A) -> A:=A-50 -> write(A) -> read(B) -> B:=B+50 -> write(B) -> commit
Highlights:
- Initial state ($1000, $2000; sum=$3000)
- Intermediate state ($950, $2000; sum=$2950, temporary inconsistency)
- Final state ($950, $2050; sum=$3000)
- The four ACID guarantees: Atomicity, Consistency, Isolation, Durability
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

fig, ax = plt.subplots(figsize=(11, 7.5), dpi=200)
ax.set_xlim(0, 110)
ax.set_ylim(0, 75)
ax.axis('off')

# Color palette
bg_box = "#F8FAFC"
tx_box = "#EFF6FF"
tx_edge = "#1D4ED8"
state_init_face = "#ECFDF5"
state_init_edge = "#059669"
state_mid_face = "#FEF2F2"
state_mid_edge = "#DC2626"
state_fin_face = "#ECFDF5"
state_fin_edge = "#059669"
acid_face = "#FFFBEB"
acid_edge = "#D97706"

# Title banner
title_box = patches.FancyBboxPatch((10, 68), 90, 5.5, boxstyle="round,pad=0.5",
                                   facecolor="#1E293B", edgecolor="none")
ax.add_patch(title_box)
ax.text(55, 70.7, "ACID Properties in Fund Transfer Transaction (Transfer $50 from A to B)",
        ha='center', va='center', fontsize=12, fontweight='bold', color="#FFFFFF")

# Left Column: Transaction Steps
tx_rect = patches.FancyBboxPatch((5, 12), 34, 52, boxstyle="round,pad=0.5",
                                 facecolor=tx_box, edgecolor=tx_edge, linewidth=1.8)
ax.add_patch(tx_rect)
ax.text(22, 61.5, "Transaction T1 Steps", ha='center', va='center',
        fontsize=11, fontweight='bold', color="#1E3A8A")

steps = [
    "1.  read(A)",
    "2.  A := A - 50",
    "3.  write(A)   [A becomes $950]",
    "--- (Intermediate State) ---",
    "4.  read(B)",
    "5.  B := B + 50",
    "6.  write(B)   [B becomes $2050]",
    "7.  commit"
]

y_pos = 55.5
for s in steps:
    if "---" in s:
        ax.text(22, y_pos, s, ha='center', va='center',
                fontsize=9, fontweight='bold', color="#DC2626")
        ax.plot([7, 37], [y_pos, y_pos], color="#DC2626", linestyle="--", linewidth=1.0)
    else:
        ax.text(8, y_pos, s, ha='left', va='center',
                fontsize=9.5, color="#0F172A", family="monospace")
    y_pos -= 5.5

# Middle Column: Database State Evolution
ax.text(56, 61.5, "Database State Evolution", ha='center', va='center',
        fontsize=11, fontweight='bold', color="#0F172A")

# 1. Initial State
init_rect = patches.FancyBboxPatch((42, 47), 28, 11, boxstyle="round,pad=0.4",
                                   facecolor=state_init_face, edgecolor=state_init_edge, linewidth=1.5)
ax.add_patch(init_rect)
ax.text(56, 55, "Initial State (Consistent)", ha='center', va='center',
        fontsize=9.5, fontweight='bold', color="#065F46")
ax.text(56, 50.5, "A = $1000,  B = $2000\nTotal (A + B) = $3000", ha='center', va='center',
        fontsize=9, color="#047857")

# Arrow from step 3 to mid state
ax.annotate("", xy=(42, 36), xytext=(39, 44),
            arrowprops=dict(arrowstyle="->", color="#DC2626", lw=1.5))

# 2. Intermediate State
mid_rect = patches.FancyBboxPatch((42, 30), 28, 12, boxstyle="round,pad=0.4",
                                  facecolor=state_mid_face, edgecolor=state_mid_edge, linewidth=1.5, linestyle="--")
ax.add_patch(mid_rect)
ax.text(56, 38.5, "Intermediate State (Inconsistent!)", ha='center', va='center',
        fontsize=9.5, fontweight='bold', color="#991B1B")
ax.text(56, 33.5, "A = $950,  B = $2000\nTotal (A + B) = $2950 ($50 missing!)", ha='center', va='center',
        fontsize=8.8, color="#B91C1C")

# Arrow down to Final state
ax.annotate("", xy=(56, 23.5), xytext=(56, 30),
            arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))

# 3. Final State
fin_rect = patches.FancyBboxPatch((42, 12), 28, 11, boxstyle="round,pad=0.4",
                                  facecolor=state_fin_face, edgecolor=state_fin_edge, linewidth=1.5)
ax.add_patch(fin_rect)
ax.text(56, 20, "Final State (Consistent)", ha='center', va='center',
        fontsize=9.5, fontweight='bold', color="#065F46")
ax.text(56, 15.5, "A = $950,  B = $2050\nTotal (A + B) = $3000", ha='center', va='center',
        fontsize=9, color="#047857")

# Right Column: The 4 ACID Guarantees
acid_titles = ["Atomicity (All or None)", "Consistency (Invariants)", "Isolation (No Interference)", "Durability (Persistence)"]
acid_texts = [
    "If crash happens at step 3, DB aborts and\nrolls back to Initial State ($1000, $2000).\nEnsured by: Recovery System / Log.",
    "Sum A + B = $3000 holds before and\nafter transfer. Money is neither created\nnor destroyed. Ensured by: Programmer.",
    "Concurrent txn T2 cannot read intermediate\nstate ($950, $2000). Must see either all\nor none. Ensured by: Concurrency Control.",
    "Once commit is confirmed at step 7, final\nbalances ($950, $2050) survive power loss\nor crash. Ensured by: Recovery System."
]

y_acid = 58
for title, text in zip(acid_titles, acid_texts):
    box = patches.FancyBboxPatch((74, y_acid - 8), 32, 10.5, boxstyle="round,pad=0.4",
                                 facecolor=acid_face, edgecolor=acid_edge, linewidth=1.4)
    ax.add_patch(box)
    ax.text(75.5, y_acid + 0.8, title, ha='left', va='center',
            fontsize=9.5, fontweight='bold', color="#92400E")
    ax.text(75.5, y_acid - 4, text, ha='left', va='center',
            fontsize=8.2, color="#78350F")
    y_acid -= 13

# Save output
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_expl = "Topicwise_answers_explaination/diagrams"
os.makedirs(out_dir_exam, exist_ok=True)
os.makedirs(out_dir_expl, exist_ok=True)

out_file_exam = os.path.join(out_dir_exam, "T09_2018_Q4b_acid_transfer.jpg")
out_file_expl = os.path.join(out_dir_expl, "T09_2018_Q4b_acid_transfer.jpg")

plt.tight_layout()
plt.savefig(out_file_exam, format='jpg', dpi=200, bbox_inches='tight')
plt.savefig(out_file_expl, format='jpg', dpi=200, bbox_inches='tight')
plt.close()
print("Saved diagrams successfully.")

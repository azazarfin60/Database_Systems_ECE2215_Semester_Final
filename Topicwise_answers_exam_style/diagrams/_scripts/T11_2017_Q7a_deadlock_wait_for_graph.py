import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import os
import shutil

# Set up figure
fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Color palette
bg_box = "#F8FAFC"
node_face = "#EBF3FB"
node_edge = "#2B5B84"
edge_color = "#C0392B"
text_dark = "#1E293B"
card_border = "#CBD5E1"

# Left panel: Interleaved Schedule Box
rect_left = patches.FancyBboxPatch((4, 5), 42, 40, boxstyle="round,pad=0.5",
                                  facecolor=bg_box, edgecolor=card_border, linewidth=1.2)
ax.add_patch(rect_left)

ax.text(25, 41.5, "Interleaved Schedule Execution", ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_dark)

# Column headers
ax.text(14, 36.5, "Transaction T1", ha='center', va='center',
        fontsize=10, fontweight='bold', color="#2B5B84")
ax.text(36, 36.5, "Transaction T2", ha='center', va='center',
        fontsize=10, fontweight='bold', color="#2B5B84")
ax.plot([6, 44], [34.5, 34.5], color=card_border, linewidth=1)

schedule_lines = [
    (14, 30.5, "lock-S(A)  [Granted]", "#166534"),
    (14, 26.5, "read(A)", text_dark),
    (36, 22.5, "lock-S(B)  [Granted]", "#166534"),
    (36, 18.5, "read(B)", text_dark),
    (14, 14.5, "lock-X(B)  [WAIT]", "#C0392B"),
    (36, 10.5, "lock-X(A)  [WAIT]", "#C0392B")
]

for x, y, text, col in schedule_lines:
    fw = 'bold' if 'lock' in text else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight=fw, color=col)

# Right panel: Wait-For Graph Box
rect_right = patches.FancyBboxPatch((50, 5), 46, 40, boxstyle="round,pad=0.5",
                                   facecolor=bg_box, edgecolor=card_border, linewidth=1.2)
ax.add_patch(rect_right)

ax.text(73, 41.5, "Wait-For Graph (Cycle Detected)", ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_dark)

# Draw transaction nodes
node_t1 = patches.Circle((62, 23), 5.5, facecolor=node_face, edgecolor=node_edge, linewidth=2.0)
node_t2 = patches.Circle((84, 23), 5.5, facecolor=node_face, edgecolor=node_edge, linewidth=2.0)
ax.add_patch(node_t1)
ax.add_patch(node_t2)

ax.text(62, 23, "T1", ha='center', va='center', fontsize=12, fontweight='bold', color=text_dark)
ax.text(84, 23, "T2", ha='center', va='center', fontsize=12, fontweight='bold', color=text_dark)

# Directed curved arrow T1 -> T2 (top)
arrow1 = patches.FancyArrowPatch((64, 27.5), (82, 27.5),
                                connectionstyle="arc3,rad=-0.42",
                                arrowstyle="->,head_length=6,head_width=4",
                                color=edge_color, linewidth=2.0)
ax.add_patch(arrow1)
ax.text(73, 33.5, "Waits for B held by T2", ha='center', va='center',
        fontsize=8.5, fontweight='bold', color=edge_color)

# Directed curved arrow T2 -> T1 (bottom)
arrow2 = patches.FancyArrowPatch((82, 18.5), (64, 18.5),
                                connectionstyle="arc3,rad=-0.42",
                                arrowstyle="->,head_length=6,head_width=4",
                                color=edge_color, linewidth=2.0)
ax.add_patch(arrow2)
ax.text(73, 12.5, "Waits for A held by T1", ha='center', va='center',
        fontsize=8.5, fontweight='bold', color=edge_color)

# Deadlock banner
rect_warn = patches.FancyBboxPatch((55, 6.8), 36, 4.2, boxstyle="round,pad=0.2",
                                  facecolor="#FEE2E2", edgecolor="#DC2626", linewidth=1.0)
ax.add_patch(rect_warn)
ax.text(73, 8.9, "Cycle: T1 -> T2 -> T1  =>  DEADLOCK", ha='center', va='center',
        fontsize=9, fontweight='bold', color="#991B1B")

# Save file paths
out_exam = "Topicwise_answers_exam_style/diagrams/T11_2017_Q7a_deadlock_wait_for_graph.jpg"
out_exp = "Topicwise_answers_explaination/diagrams/T11_2017_Q7a_deadlock_wait_for_graph.jpg"

plt.tight_layout()
plt.savefig(out_exam, format='jpg', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# Copy to explanation layer
shutil.copyfile(out_exam, out_exp)

# Write sidecar files
meta_data = {
    "description": "Wait-for graph and schedule execution illustrating deadlock cycle T1 -> T2 -> T1 under 2PL for 2017 Q.7(a)",
    "figure_id": "Fig_T11_2017_Q7a",
    "source_image": "generated",
    "generator": "Topicwise_answers_exam_style/diagrams/_scripts/T11_2017_Q7a_deadlock_wait_for_graph.py"
}

with open(f"{out_exam}.meta.json", "w") as f:
    json.dump(meta_data, f, indent=2)

with open(f"{out_exp}.meta.json", "w") as f:
    json.dump(meta_data, f, indent=2)

print("Diagram and sidecars generated successfully.")

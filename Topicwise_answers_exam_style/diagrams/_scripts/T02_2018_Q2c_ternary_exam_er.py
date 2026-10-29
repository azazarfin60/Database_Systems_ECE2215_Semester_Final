"""
Generates T02_2018_Q2c_ternary_exam_er.jpg
Chen ER diagram showing a Ternary Relationship:
- Entities: STUDENT, COURSE_OFFERING, EXAM
- Ternary Relationship: Scores (with descriptive attribute marks)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(11, 7.5), dpi=200)
ax.set_xlim(0, 110)
ax.set_ylim(0, 75)
ax.axis('off')

entity_face = "#EBF3FB"
entity_edge = "#2B5B84"
rel_face = "#FEF3D6"
rel_edge = "#B78103"
attr_face = "#F2F9EC"
attr_edge = "#4A7C2C"
line_color = "#333333"

def draw_entity(x, y, w, h, text):
    rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0",
                                  facecolor=entity_face, edgecolor=entity_edge, linewidth=1.8)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111111')

def draw_relationship(x, y, w, h, text):
    pts = np.array([[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]])
    poly = patches.Polygon(pts, facecolor=rel_face, edgecolor=rel_edge, linewidth=1.8)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False):
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.2)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#111111')
    if is_pk:
        ax.plot([x - len(text)*0.4, x + len(text)*0.4], [y - 1.3, y - 1.3], color='#111111', linewidth=1.1)

# Placement layout:
# Ternary relationship at center: (x=55, y=42)
# Top: COURSE_OFFERING (x=55, y=65)
# Bottom Left: STUDENT (x=22, y=20)
# Bottom Right: EXAM (x=88, y=20)

draw_relationship(55, 42, 18, 11, "Scores")

draw_entity(55, 65, 24, 8.5, "COURSE_OFFERING")
draw_entity(20, 20, 18, 8.5, "STUDENT")
draw_entity(90, 20, 18, 8.5, "EXAM")

# Connectors for Ternary relationship:
# Center to Top (COURSE_OFFERING)
ax.plot([55, 55], [47.5, 60.7], color=line_color, linewidth=1.6)

# Center to Bottom Left (STUDENT)
ax.plot([47.5, 27], [38, 24.2], color=line_color, linewidth=1.6)

# Center to Bottom Right (EXAM)
ax.plot([62.5, 83], [38, 24.2], color=line_color, linewidth=1.6)

# Descriptive attribute: marks on relationship Scores
draw_attribute(75, 42, 13, 5.5, "marks")
ax.plot([64, 68.5], [42, 42], color=line_color, linewidth=1.2)

# Attributes for COURSE_OFFERING
draw_attribute(28, 70, 14, 5.5, "offering_id", is_pk=True)
draw_attribute(55, 73, 14, 5.5, "semester")
draw_attribute(82, 70, 13, 5.5, "year")

ax.plot([35, 45], [68, 66], color=line_color, linewidth=1.1)
ax.plot([55, 55], [70, 69.2], color=line_color, linewidth=1.1)
ax.plot([75, 65], [68, 66], color=line_color, linewidth=1.1)

# Attributes for STUDENT
draw_attribute(10, 31, 14, 5.5, "student_id", is_pk=True)
draw_attribute(28, 32, 13, 5.5, "name")
draw_attribute(12, 9, 13, 5.5, "dept_name")

ax.plot([14, 17], [28.5, 24.2], color=line_color, linewidth=1.1)
ax.plot([25, 22], [29, 24.2], color=line_color, linewidth=1.1)
ax.plot([15, 18], [11.5, 15.8], color=line_color, linewidth=1.1)

# Attributes for EXAM
draw_attribute(76, 9, 13, 5.5, "exam_id", is_pk=True)
draw_attribute(92, 8, 14, 5.5, "exam_type")
draw_attribute(102, 30, 13, 5.5, "max_marks")

ax.plot([80, 84], [11.5, 15.8], color=line_color, linewidth=1.1)
ax.plot([91, 90], [10.5, 15.8], color=line_color, linewidth=1.1)
ax.plot([98, 95], [27.5, 24.2], color=line_color, linewidth=1.1)

ax.text(55, 3, "Ternary Relationship Model for Student Exam Marks (2018 Q.2(c))",
        ha='center', va='center', fontsize=11, fontweight='bold', color='#2B5B84')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_2018_Q2c_ternary_exam_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2018_Q2c_ternary_exam_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2018_Q2c_ternary_exam_er.jpg")

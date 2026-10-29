"""
Generates T02_2017_Q1b_ruet_student_er.jpg
Chen ER diagram for RUET Student Database:
- Student basic info
- Course advisor info
- Subject registration
- Result info
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(13, 8.5), dpi=200)
ax.set_xlim(0, 130)
ax.set_ylim(0, 85)
ax.axis('off')

entity_face = "#EBF3FB"
entity_edge = "#2B5B84"
rel_face = "#FEF3D6"
rel_edge = "#B78103"
attr_face = "#F2F9EC"
attr_edge = "#4A7C2C"
line_color = "#333333"

def draw_entity(x, y, w, h, text, is_weak=False):
    rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0",
                                  facecolor=entity_face, edgecolor=entity_edge, linewidth=1.8)
    ax.add_patch(rect)
    if is_weak:
        rect2 = patches.FancyBboxPatch((x - w/2 + 0.8, y - h/2 + 0.8), w - 1.6, h - 1.6,
                                       boxstyle="square,pad=0", facecolor="none", edgecolor=entity_edge, linewidth=1.2)
        ax.add_patch(rect2)
    ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color='#111111')

def draw_relationship(x, y, w, h, text):
    pts = np.array([[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]])
    poly = patches.Polygon(pts, facecolor=rel_face, edgecolor=rel_edge, linewidth=1.8)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False):
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.2)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#111111')
    if is_pk:
        ax.plot([x - len(text)*0.4, x + len(text)*0.4], [y - 1.3, y - 1.3], color='#111111', linewidth=1.1)

# Placement layout:
# Top Left: ADVISOR (x=25, y=65)
# Middle: STUDENT (x=65, y=45)
# Top Right: COURSE (x=105, y=65)
# Bottom Middle: RESULT (x=65, y=15)

# Relationships:
# ADVISER -[Advises]-> STUDENT (x=45, y=55)
# STUDENT -[Registers]-> COURSE (x=85, y=55)
# STUDENT -[Has_Result]-> RESULT (x=65, y=30)

draw_entity(25, 68, 18, 9, "ADVISOR")
draw_relationship(45, 56, 16, 10, "Advises")
draw_entity(65, 45, 18, 9, "STUDENT")
draw_relationship(85, 56, 16, 10, "Registers")
draw_entity(105, 68, 18, 9, "COURSE")
draw_relationship(65, 30, 16, 10, "Obtains")
draw_entity(65, 14, 18, 9, "RESULT")

# Connectors:
# Advisor to Advises (1)
ax.plot([31, 39], [64, 60], color=line_color, linewidth=1.6)
ax.text(32, 60, "1", fontsize=11, fontweight='bold', color='#B78103')

# Advises to Student (N, total participation: double line)
ax.plot([51.5, 58.5], [52.8, 48.8], color=line_color, linewidth=1.5)
ax.plot([52.5, 59.5], [51.2, 47.2], color=line_color, linewidth=1.5)
ax.text(56, 52, "N", fontsize=11, fontweight='bold', color='#B78103')

# Student to Registers (M, total participation: double line)
ax.plot([71.5, 78.5], [48.8, 52.8], color=line_color, linewidth=1.5)
ax.plot([70.5, 77.5], [47.2, 51.2], color=line_color, linewidth=1.5)
ax.text(73, 52, "M", fontsize=11, fontweight='bold', color='#B78103')

# Registers to Course (N)
ax.plot([91, 99], [60, 64], color=line_color, linewidth=1.6)
ax.text(96, 60, "N", fontsize=11, fontweight='bold', color='#B78103')

# Student to Obtains (1)
ax.plot([65, 65], [40.5, 35], color=line_color, linewidth=1.6)
ax.text(66.5, 38, "1", fontsize=11, fontweight='bold', color='#B78103')

# Obtains to Result (N, total participation: double line)
ax.plot([64.2, 64.2], [25, 18.5], color=line_color, linewidth=1.5)
ax.plot([65.8, 65.8], [25, 18.5], color=line_color, linewidth=1.5)
ax.text(67, 22, "N", fontsize=11, fontweight='bold', color='#B78103')

# Attributes:
# ADVISOR attributes
draw_attribute(12, 80, 14, 5.5, "advisor_id", is_pk=True)
draw_attribute(28, 80, 13, 5.5, "name")
draw_attribute(10, 68, 14, 5.5, "designation")
draw_attribute(12, 56, 14, 5.5, "department")
ax.plot([16, 21], [77.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([27, 26], [77.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([17, 16], [68, 68], color=line_color, linewidth=1.1)
ax.plot([18, 20], [58, 63.5], color=line_color, linewidth=1.1)

# STUDENT attributes
draw_attribute(45, 43, 13, 5.5, "roll_no", is_pk=True)
draw_attribute(47, 34, 13, 5.5, "name")
draw_attribute(85, 43, 14, 5.5, "dept_name")
draw_attribute(85, 34, 13, 5.5, "series")
ax.plot([51.5, 56], [43, 44], color=line_color, linewidth=1.1)
ax.plot([53, 58], [36, 41], color=line_color, linewidth=1.1)
ax.plot([78, 74], [43, 44], color=line_color, linewidth=1.1)
ax.plot([79, 72], [36, 41], color=line_color, linewidth=1.1)

# COURSE attributes
draw_attribute(103, 80, 14, 5.5, "course_code", is_pk=True)
draw_attribute(119, 80, 14, 5.5, "course_title")
draw_attribute(120, 68, 12, 5.5, "credits")
ax.plot([104, 104], [77.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([115, 110], [77.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([114, 114], [68, 68], color=line_color, linewidth=1.1)

# REGISTERS descriptive attributes (semester, session)
draw_attribute(85, 72, 13, 5.5, "semester")
draw_attribute(71, 67, 13, 5.5, "session")
ax.plot([85, 85], [69, 61], color=line_color, linewidth=1.1)
ax.plot([74, 80], [64.5, 59], color=line_color, linewidth=1.1)

# RESULT attributes
draw_attribute(45, 14, 13, 5.5, "result_id", is_pk=True)
draw_attribute(52, 4, 13, 5.5, "semester")
draw_attribute(78, 4, 12, 5.5, "gpa")
draw_attribute(85, 14, 13, 5.5, "cgpa")
ax.plot([51.5, 56], [14, 14], color=line_color, linewidth=1.1)
ax.plot([56, 61], [6.5, 9.5], color=line_color, linewidth=1.1)
ax.plot([74, 69], [6.5, 9.5], color=line_color, linewidth=1.1)
ax.plot([78.5, 74], [14, 14], color=line_color, linewidth=1.1)

ax.text(65, 82, "RUET Student Database — Conceptual E-R Diagram",
        ha='center', va='center', fontsize=12, fontweight='bold', color='#2B5B84')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_2017_Q1b_ruet_student_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2017_Q1b_ruet_student_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2017_Q1b_ruet_student_er.jpg")

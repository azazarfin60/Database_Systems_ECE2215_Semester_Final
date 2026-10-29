"""
Generates T02_CT02_Q02_university_er.jpg
Chen ER diagram for University Enterprise (CT-02 Q.02):
- STUDENT (M:N with Course via Enrolls)
- COURSE
- TEACHER (1:N with Course via Teaches)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(11, 6), dpi=200)
ax.set_xlim(0, 110)
ax.set_ylim(0, 60)
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
    ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color='#111111')

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
# STUDENT (x=18, y=30) --[Enrolls] (x=42, y=30)-- COURSE (x=68, y=30) --[Teaches] (x=90, y=30)-- TEACHER (x=102, wait, let's space it)
# Let's use x=18, x=42, x=65, x=88, x=102 -> better:
# STUDENT (x=18, y=30) -- [Enrolls] (x=41, y=30) -- COURSE (x=64, y=30) -- [Teaches] (x=86, y=30) -- TEACHER (x=102, y=30)
# Or triangle:
# TEACHER (x=55, y=48)
#    |
# [Teaches] (x=55, y=33)
#    |
# COURSE (x=75, y=18) -- [Enrolls] (x=45, y=18) -- STUDENT (x=18, y=18)
# Triangle is much better for attribute layout without crowding!

draw_entity(55, 50, 18, 8.5, "TEACHER")
draw_relationship(55, 33, 16, 9.5, "Teaches")
draw_entity(82, 18, 18, 8.5, "COURSE")
draw_relationship(50, 18, 16, 9.5, "Enrolls")
draw_entity(18, 18, 18, 8.5, "STUDENT")

# Connectors:
# TEACHER to Teaches (1)
ax.plot([55, 55], [45.7, 37.8], color=line_color, linewidth=1.6)
ax.text(56.5, 41, "1", fontsize=11, fontweight='bold', color='#B78103')

# Teaches to COURSE (N, directed arrow or line with N; each course has 1 teacher, teacher has N courses)
ax.plot([60.5, 75], [29, 21.5], color=line_color, linewidth=1.6)
ax.text(64, 26, "N", fontsize=11, fontweight='bold', color='#B78103')

# STUDENT to Enrolls (M)
ax.plot([27, 42], [18, 18], color=line_color, linewidth=1.6)
ax.text(32, 20, "M", fontsize=11, fontweight='bold', color='#B78103')

# Enrolls to COURSE (N)
ax.plot([58, 73], [18, 18], color=line_color, linewidth=1.6)
ax.text(64, 20, "N", fontsize=11, fontweight='bold', color='#B78103')

# Attributes for TEACHER
draw_attribute(36, 56, 14, 5.5, "teacher_id", is_pk=True)
draw_attribute(55, 59, 13, 5.5, "name")
draw_attribute(74, 56, 14, 5.5, "dept_name")
draw_attribute(80, 47, 13, 5.5, "phone")

ax.plot([42, 48], [54, 52], color=line_color, linewidth=1.1)
ax.plot([55, 55], [56, 54.2], color=line_color, linewidth=1.1)
ax.plot([68, 62], [54, 52], color=line_color, linewidth=1.1)
ax.plot([74, 64], [47, 49], color=line_color, linewidth=1.1)

# Attributes for STUDENT
draw_attribute(10, 31, 14, 5.5, "student_id", is_pk=True)
draw_attribute(26, 32, 13, 5.5, "name")
draw_attribute(10, 6, 13, 5.5, "email")
draw_attribute(26, 5, 14, 5.5, "dept_name")

ax.plot([13, 16], [28, 22.2], color=line_color, linewidth=1.1)
ax.plot([23, 20], [29, 22.2], color=line_color, linewidth=1.1)
ax.plot([13, 16], [8.5, 13.8], color=line_color, linewidth=1.1)
ax.plot([23, 20], [7.5, 13.8], color=line_color, linewidth=1.1)

# Attributes for COURSE
draw_attribute(98, 26, 14, 5.5, "course_id", is_pk=True)
draw_attribute(100, 16, 13, 5.5, "title")
draw_attribute(98, 6, 13, 5.5, "credits")

ax.plot([92, 88], [24, 21.5], color=line_color, linewidth=1.1)
ax.plot([93, 91], [16, 18], color=line_color, linewidth=1.1)
ax.plot([92, 88], [8, 14.5], color=line_color, linewidth=1.1)

ax.text(55, 3, "University Enterprise E-R Diagram (CT-02 Q.02)",
        ha='center', va='center', fontsize=11, fontweight='bold', color='#2B5B84')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_CT02_Q02_university_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_CT02_Q02_university_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_CT02_Q02_university_er.jpg")

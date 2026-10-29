"""
Generates T02_2018_Q3c_many_to_many_er.jpg
Chen ER diagram showing an M:N relationship between Student and Course with descriptive attribute 'grade',
and illustrating the conversion into relational tables.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Colors
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

def draw_relationship(x, y, w, h, text, is_identifying=False):
    pts = np.array([[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]])
    poly = patches.Polygon(pts, facecolor=rel_face, edgecolor=rel_edge, linewidth=1.8)
    ax.add_patch(poly)
    if is_identifying:
        pts2 = np.array([[x, y + h/2 - 0.9], [x + w/2 - 1.2, y], [x, y - h/2 + 0.9], [x - w/2 + 1.2, y]])
        poly2 = patches.Polygon(pts2, facecolor="none", edgecolor=rel_edge, linewidth=1.2)
        ax.add_patch(poly2)
    ax.text(x, y, text, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False, is_multivalued=False, is_derived=False):
    ls = '--' if is_derived else '-'
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.3, linestyle=ls)
    ax.add_patch(ell)
    if is_multivalued:
        ell2 = patches.Ellipse((x, y), w - 1.2, h - 0.8, facecolor="none", edgecolor=attr_edge, linewidth=1.0)
        ax.add_patch(ell2)
    
    # Text
    t = ax.text(x, y, text, ha='center', va='center', fontsize=9.5, color='#111111')
    if is_pk:
        # Underline primary key
        ax.plot([x - len(text)*0.45, x + len(text)*0.45], [y - 1.4, y - 1.4], color='#111111', linewidth=1.1)

# Draw Entities
draw_entity(20, 25, 18, 9, "STUDENT")
draw_relationship(50, 25, 18, 11, "Takes")
draw_entity(80, 25, 18, 9, "COURSE")

# Lines between entities and relationship (M:N)
ax.plot([29, 41], [25, 25], color=line_color, linewidth=1.8)
ax.plot([59, 71], [25, 25], color=line_color, linewidth=1.8)

# Cardinality labels
ax.text(32, 27, "M", fontsize=11, fontweight='bold', color='#B78103')
ax.text(67, 27, "N", fontsize=11, fontweight='bold', color='#B78103')

# Attributes for STUDENT
draw_attribute(10, 40, 14, 6, "student_id", is_pk=True)
draw_attribute(28, 41, 14, 6, "name")
draw_attribute(10, 10, 14, 6, "dept_name")
draw_attribute(28, 9, 14, 6, "tot_cred")

ax.plot([14, 18], [37, 29.5], color=line_color, linewidth=1.1)
ax.plot([25, 22], [38, 29.5], color=line_color, linewidth=1.1)
ax.plot([14, 18], [13, 20.5], color=line_color, linewidth=1.1)
ax.plot([25, 22], [12, 20.5], color=line_color, linewidth=1.1)

# Attribute for Relationship (Takes)
draw_attribute(50, 41, 13, 6, "grade")
ax.plot([50, 50], [38, 30.5], color=line_color, linewidth=1.1)

# Attributes for COURSE
draw_attribute(72, 41, 14, 6, "course_id", is_pk=True)
draw_attribute(90, 40, 14, 6, "title")
draw_attribute(72, 9, 14, 6, "dept_name")
draw_attribute(90, 10, 14, 6, "credits")

ax.plot([75, 78], [38, 29.5], color=line_color, linewidth=1.1)
ax.plot([86, 82], [37, 29.5], color=line_color, linewidth=1.1)
ax.plot([75, 78], [12, 20.5], color=line_color, linewidth=1.1)
ax.plot([86, 82], [13, 20.5], color=line_color, linewidth=1.1)

# Add title annotation
ax.text(50, 4, "Many-to-Many (M:N) Relationship: Student and Course with descriptive attribute 'grade'",
        ha='center', va='center', fontsize=10, style='italic', color='#444444')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"
os.makedirs(out_dir_exam, exist_ok=True)
os.makedirs(out_dir_exp, exist_ok=True)

out_file_exam = os.path.join(out_dir_exam, "T02_2018_Q3c_many_to_many_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2018_Q3c_many_to_many_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2018_Q3c_many_to_many_er.jpg")

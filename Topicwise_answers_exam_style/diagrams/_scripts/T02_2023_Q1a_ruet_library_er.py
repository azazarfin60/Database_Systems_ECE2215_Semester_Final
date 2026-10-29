"""
Generates T02_2023_Q1a_ruet_library_er.jpg
Chen ER diagram for RUET Central Library Management System:
Entities:
- BOOKS
- MEMBERS
- STAFF
- BORROWING (modeled as entity with borrow_id, borrow_date, due_date)
- RESERVATIONS (modeled as entity with res_id, res_date, status)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(14, 9), dpi=200)
ax.set_xlim(0, 140)
ax.set_ylim(0, 90)
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
    ax.text(x, y, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False):
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.2)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=8.5, color='#111111')
    if is_pk:
        ax.plot([x - len(text)*0.38, x + len(text)*0.38], [y - 1.2, y - 1.2], color='#111111', linewidth=1.1)

# Placement layout:
# Top row: STAFF (x=25, y=75), BORROWING (x=70, y=75), BOOKS (x=115, y=50)
# Middle row: MEMBERS (x=25, y=35)
# Bottom row: RESERVATIONS (x=70, y=25)

draw_entity(25, 75, 18, 9, "STAFF")
draw_relationship(48, 75, 15, 9, "Issues")
draw_entity(72, 75, 20, 9, "BORROWING")
draw_relationship(96, 65, 15, 9, "Includes")
draw_entity(118, 50, 18, 9, "BOOKS")

draw_entity(25, 35, 18, 9, "MEMBERS")
draw_relationship(48, 55, 15, 9, "Borrows")

draw_relationship(48, 25, 15, 9, "Reserves")
draw_entity(72, 25, 22, 9, "RESERVATIONS")
draw_relationship(96, 35, 15, 9, "For_Book")

# Connectors and cardinalities:
# 1. STAFF - Issues - BORROWING (1:N)
ax.plot([34, 40.5], [75, 75], color=line_color, linewidth=1.6)
ax.text(36, 77, "1", fontsize=11, fontweight='bold', color='#B78103')
ax.plot([55.5, 62], [75, 75], color=line_color, linewidth=1.6)
ax.text(58, 77, "N", fontsize=11, fontweight='bold', color='#B78103')

# 2. MEMBERS - Borrows - BORROWING (1:N)
ax.plot([29, 41], [39.5, 51], color=line_color, linewidth=1.6)
ax.text(32, 47, "1", fontsize=11, fontweight='bold', color='#B78103')
ax.plot([55, 65], [59, 70.5], color=line_color, linewidth=1.6)
ax.text(62, 63, "N", fontsize=11, fontweight='bold', color='#B78103')

# 3. BORROWING - Includes - BOOKS (N:1)
ax.plot([82, 89], [72, 67.5], color=line_color, linewidth=1.6)
ax.text(83, 72, "N", fontsize=11, fontweight='bold', color='#B78103')
ax.plot([103, 110], [62.5, 54], color=line_color, linewidth=1.6)
ax.text(108, 60, "1", fontsize=11, fontweight='bold', color='#B78103')

# 4. MEMBERS - Reserves - RESERVATIONS (1:N)
ax.plot([32, 40.5], [31, 27], color=line_color, linewidth=1.6)
ax.text(35, 31, "1", fontsize=11, fontweight='bold', color='#B78103')
ax.plot([55.5, 61], [25, 25], color=line_color, linewidth=1.6)
ax.text(57, 27, "N", fontsize=11, fontweight='bold', color='#B78103')

# 5. RESERVATIONS - For_Book - BOOKS (N:1)
ax.plot([83, 89], [27, 32], color=line_color, linewidth=1.6)
ax.text(83, 27, "N", fontsize=11, fontweight='bold', color='#B78103')
ax.plot([103, 110], [38, 46], color=line_color, linewidth=1.6)
ax.text(108, 40, "1", fontsize=11, fontweight='bold', color='#B78103')

# Attributes:
# STAFF
draw_attribute(12, 85, 13, 5, "staff_id", is_pk=True)
draw_attribute(27, 87, 13, 5, "name")
draw_attribute(10, 68, 13, 5, "designation")
ax.plot([16, 21], [83, 79], color=line_color, linewidth=1.1)
ax.plot([26, 25], [84.5, 79.5], color=line_color, linewidth=1.1)
ax.plot([16, 17], [70, 72], color=line_color, linewidth=1.1)

# MEMBERS
draw_attribute(10, 48, 13, 5, "member_id", is_pk=True)
draw_attribute(10, 36, 13, 5, "name")
draw_attribute(10, 24, 13, 5, "type")
draw_attribute(25, 18, 13, 5, "department")
ax.plot([16, 20], [46, 39], color=line_color, linewidth=1.1)
ax.plot([16, 18], [36, 36], color=line_color, linewidth=1.1)
ax.plot([16, 20], [26, 31], color=line_color, linewidth=1.1)
ax.plot([25, 25], [20.5, 30.5], color=line_color, linewidth=1.1)

# BORROWING (modeled as entity per question prompt)
draw_attribute(63, 87, 13, 5, "borrow_id", is_pk=True)
draw_attribute(77, 87, 13, 5, "borrow_date")
draw_attribute(90, 83, 13, 5, "due_date")
draw_attribute(90, 75, 13, 5, "return_date")
ax.plot([65, 68], [84.5, 79.5], color=line_color, linewidth=1.1)
ax.plot([75, 73], [84.5, 79.5], color=line_color, linewidth=1.1)
ax.plot([85, 82], [81, 78], color=line_color, linewidth=1.1)
ax.plot([84, 82], [75, 75], color=line_color, linewidth=1.1)

# RESERVATIONS (modeled as entity per question prompt)
draw_attribute(60, 13, 13, 5, "res_id", is_pk=True)
draw_attribute(74, 12, 13, 5, "res_date")
draw_attribute(88, 14, 13, 5, "status")
ax.plot([63, 67], [15.5, 20.5], color=line_color, linewidth=1.1)
ax.plot([73, 72], [14.5, 20.5], color=line_color, linewidth=1.1)
ax.plot([84, 79], [16, 20.5], color=line_color, linewidth=1.1)

# BOOKS
draw_attribute(131, 62, 13, 5, "book_id", is_pk=True)
draw_attribute(132, 53, 13, 5, "isbn")
draw_attribute(131, 44, 13, 5, "title")
draw_attribute(131, 35, 13, 5, "author")
draw_attribute(118, 30, 13, 5, "edition")
ax.plot([126, 124], [60, 54.5], color=line_color, linewidth=1.1)
ax.plot([126, 126], [53, 52], color=line_color, linewidth=1.1)
ax.plot([126, 126], [45, 48], color=line_color, linewidth=1.1)
ax.plot([126, 124], [37, 45.5], color=line_color, linewidth=1.1)
ax.plot([118, 118], [32.5, 45.5], color=line_color, linewidth=1.1)

ax.text(70, 4, "RUET Central Library Management System — E-R Diagram (Borrowing & Reservations as Entities)",
        ha='center', va='center', fontsize=11, fontweight='bold', color='#2B5B84')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_2023_Q1a_ruet_library_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2023_Q1a_ruet_library_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2023_Q1a_ruet_library_er.jpg")

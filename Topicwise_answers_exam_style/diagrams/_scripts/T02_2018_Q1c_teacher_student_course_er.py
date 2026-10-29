"""
Generates T02_2018_Q1c_teacher_student_course_er.jpg
Chen ER diagram including Teacher, Student, and Course entities with:
- Total participation of Teacher in Teaches (each teacher must take at least one course)
- Partial participation of Course in Teaches (a course may have teacher or not)
- Total participation of Student in Registers (a student can register one or more courses)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(11, 7.5), dpi=200)
ax.set_xlim(0, 110)
ax.set_ylim(-3, 72)
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
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.3)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=9.5, color='#111111')
    if is_pk:
        ax.plot([x - len(text)*0.42, x + len(text)*0.42], [y - 1.4, y - 1.4], color='#111111', linewidth=1.1)

# Placement:
# TEACHER (left, y=45) ---> TEACHES (middle-left, x=55, y=55) ---> COURSE (top/middle, x=85, y=45)
# Or:
# TEACHER (x=25, y=50) -- [Teaches] (x=55, y=50) -- COURSE (x=85, y=35)
# STUDENT (x=25, y=20) -- [Registers] (x=55, y=20) -- COURSE (x=85, y=35)

draw_entity(22, 52, 18, 9, "TEACHER")
draw_relationship(55, 52, 18, 11, "Teaches")

draw_entity(88, 35, 18, 9, "COURSE")

draw_entity(22, 18, 18, 9, "STUDENT")
draw_relationship(55, 18, 18, 11, "Registers")

# 1. TEACHER to TEACHES: TOTAL PARTICIPATION (Double line)
# Constraint (i): Each teacher must take at least one course
ax.plot([31, 46], [53.2, 53.2], color=line_color, linewidth=1.6)
ax.plot([31, 46], [50.8, 50.8], color=line_color, linewidth=1.6)
ax.text(34, 55, "1..*", fontsize=10, fontweight='bold', color='#2B5B84')
ax.text(48, 55, "1", fontsize=11, fontweight='bold', color='#B78103')

# 2. TEACHES to COURSE: PARTIAL PARTICIPATION (Single line)
# Constraint (iii): A course may have teacher or not
ax.plot([64, 80], [48, 39], color=line_color, linewidth=1.6)
ax.text(67, 47, "N", fontsize=11, fontweight='bold', color='#B78103')
ax.text(73, 42, "0..1", fontsize=10, fontweight='bold', color='#2B5B84')

# 3. STUDENT to REGISTERS: TOTAL PARTICIPATION (Double line)
# Constraint (ii): A student can register one or more courses
ax.plot([31, 46], [19.2, 19.2], color=line_color, linewidth=1.6)
ax.plot([31, 46], [16.8, 16.8], color=line_color, linewidth=1.6)
ax.text(34, 21, "1..*", fontsize=10, fontweight='bold', color='#2B5B84')
ax.text(48, 21, "M", fontsize=11, fontweight='bold', color='#B78103')

# 4. REGISTERS to COURSE: PARTIAL PARTICIPATION (Single line, M:N)
ax.plot([64, 80], [22, 31], color=line_color, linewidth=1.6)
ax.text(67, 23, "N", fontsize=11, fontweight='bold', color='#B78103')
ax.text(73, 27, "0..*", fontsize=10, fontweight='bold', color='#2B5B84')

# Attributes for TEACHER
draw_attribute(10, 64, 15, 6, "teacher_id", is_pk=True)
draw_attribute(28, 65, 14, 6, "name")
draw_attribute(10, 40, 14, 6, "dept_name")

ax.plot([14, 19], [61.5, 56.5], color=line_color, linewidth=1.1)
ax.plot([26, 23], [62, 56.5], color=line_color, linewidth=1.1)
ax.plot([14, 18], [42.5, 47.5], color=line_color, linewidth=1.1)

# Attributes for STUDENT
draw_attribute(10, 27, 14, 6, "student_id", is_pk=True)
draw_attribute(28, 6, 14, 6, "name")
draw_attribute(10, 9, 14, 6, "tot_cred")

ax.plot([15, 18], [24.5, 22.5], color=line_color, linewidth=1.1)
ax.plot([25, 23], [9, 13.5], color=line_color, linewidth=1.1)
ax.plot([14, 18], [11.5, 15], color=line_color, linewidth=1.1)

# Attributes for COURSE
draw_attribute(102, 48, 14, 6, "course_id", is_pk=True)
draw_attribute(102, 35, 14, 6, "title")
draw_attribute(102, 22, 14, 6, "credits")

ax.plot([97, 95], [46, 39.5], color=line_color, linewidth=1.1)
ax.plot([95, 97], [35, 35], color=line_color, linewidth=1.1)
ax.plot([97, 95], [24, 30.5], color=line_color, linewidth=1.1)

# Constraint callout box
callout = patches.FancyBboxPatch((40, 2), 65, 8.5, boxstyle="round,pad=0.5",
                                 facecolor="#F9F9F9", edgecolor="#CCCCCC", linewidth=1.0)
ax.add_patch(callout)
ax.text(42, 7.5, "Participation Constraints Enforced:", fontsize=9, fontweight='bold', color='#111111')
ax.text(42, 5.0, "- Double line on TEACHER: Total participation (each teacher must take >= 1 course)", fontsize=8.5, color='#333333')
ax.text(42, 2.7, "- Double line on STUDENT: Total participation (a student registers >= 1 course)", fontsize=8.5, color='#333333')
ax.text(42, 0.4, "- Single line on COURSE: Partial participation (a course may have a teacher or not)", fontsize=8.5, color='#333333')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_2018_Q1c_teacher_student_course_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2018_Q1c_teacher_student_course_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2018_Q1c_teacher_student_course_er.jpg")

"""
Generates T02_EX6_15_hospital_er.jpg
Chen ER diagram for Hospital Management System (Silberschatz 7e Exercise 6.15):
Entities:
- PATIENT (patient_id [PK], name, DOB, blood_group)
- DOCTOR (doctor_id [PK], name, specialty, phone)
- ROOM (room_no [PK], ward_name, bed_count)
- TEST (test_id [PK], test_name, cost)
Relationships:
- admitted_to (PATIENT to ROOM, N:1, descriptive attribute: admission_date)
- treats (DOCTOR to PATIENT, M:N, descriptive attributes: treat_date, notes)
- prescribes (Ternary connecting DOCTOR, PATIENT, TEST; attributes: presc_date, test_result)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import json

fig, ax = plt.subplots(figsize=(15, 11), dpi=200)
ax.set_xlim(0, 150)
ax.set_ylim(0, 110)
ax.axis('off')

# Styling colors matching vault standards
entity_face = "#EBF3FB"
entity_edge = "#2B5B84"
rel_face = "#FEF3D6"
rel_edge = "#B78103"
attr_face = "#F2F9EC"
attr_edge = "#4A7C2C"
line_color = "#333333"

def draw_entity(x, y, w, h, text):
    rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0",
                                  facecolor=entity_face, edgecolor=entity_edge, linewidth=2.0)
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
        text_len = len(text)
        ax.plot([x - text_len*0.38, x + text_len*0.38], [y - 1.2, y - 1.2], color='#111111', linewidth=1.2)

# --- Layout ---
# Upper: ROOM (25, 88) --[admitted_to] (58, 88)-- PATIENT (90, 88)
# Middle: DOCTOR (25, 48) --[treats] (58, 68)-- PATIENT (90, 88)
# Ternary: prescribes (75, 42) connecting DOCTOR (25, 48), PATIENT (90, 88), TEST (125, 42)

draw_entity(24, 90, 18, 9, "ROOM")
draw_relationship(56, 90, 16, 10, "admitted_to")
draw_entity(92, 90, 18, 9, "PATIENT")

draw_entity(24, 48, 18, 9, "DOCTOR")
draw_relationship(56, 68, 16, 10, "treats")

# Ternary diamond for prescribes
draw_relationship(78, 42, 18, 11, "prescribes")
draw_entity(128, 42, 18, 9, "TEST")

# --- Connectors & Cardinalities ---

# 1. PATIENT - admitted_to - ROOM (N:1)
ax.plot([83, 64], [90, 90], color=line_color, linewidth=1.6)
ax.text(80, 92, "N", fontsize=11, fontweight='bold', color='#B78103')

ax.plot([48, 33], [90, 90], color=line_color, linewidth=1.6)
ax.text(35, 92, "1", fontsize=11, fontweight='bold', color='#B78103')

# Descriptive attribute on admitted_to: admission_date
draw_attribute(56, 103, 15, 5, "admission_date")
ax.plot([56, 56], [95, 100.5], color=line_color, linewidth=1.2, linestyle='--')

# 2. DOCTOR - treats - PATIENT (M:N)
ax.plot([30, 48], [52.5, 64.5], color=line_color, linewidth=1.6)
ax.text(32, 59, "M", fontsize=11, fontweight='bold', color='#B78103')

ax.plot([64, 84], [71.5, 85.5], color=line_color, linewidth=1.6)
ax.text(82, 77, "N", fontsize=11, fontweight='bold', color='#B78103')

# Descriptive attributes on treats: treatment_date, notes
draw_attribute(44, 78, 14, 5, "treatment_date")
draw_attribute(68, 79, 11, 5, "notes")
ax.plot([50, 53], [75.5, 71.5], color=line_color, linewidth=1.2, linestyle='--')
ax.plot([64, 60], [76.5, 71.5], color=line_color, linewidth=1.2, linestyle='--')

# 3. Ternary: prescribes connecting DOCTOR, PATIENT, and TEST
# To DOCTOR
ax.plot([69, 33], [43.5, 47.5], color=line_color, linewidth=1.6)
# To PATIENT
ax.plot([81, 89], [47.5, 85.5], color=line_color, linewidth=1.6)
# To TEST
ax.plot([87, 119], [42, 42], color=line_color, linewidth=1.6)
ax.text(78, 33, "(Ternary Relationship)", fontsize=9, fontstyle='italic', color='#B78103', ha='center')

# Descriptive attributes on prescribes: presc_date, test_result
draw_attribute(60, 26, 14, 5, "presc_date")
draw_attribute(96, 26, 14, 5, "test_result")
ax.plot([65, 73], [28.5, 37.5], color=line_color, linewidth=1.2, linestyle='--')
ax.plot([91, 83], [28.5, 37.5], color=line_color, linewidth=1.2, linestyle='--')

# --- Attributes for Entities ---

# ROOM: room_no (PK), ward_name, bed_count
draw_attribute(10, 103, 13, 5, "room_no", is_pk=True)
draw_attribute(26, 104, 13, 5, "ward_name")
draw_attribute(10, 77, 13, 5, "bed_count")

ax.plot([14, 20], [100.5, 94.5], color=line_color, linewidth=1.1)
ax.plot([25, 24], [101.5, 94.5], color=line_color, linewidth=1.1)
ax.plot([14, 20], [79.5, 85.5], color=line_color, linewidth=1.1)

# PATIENT: patient_id (PK), name, DOB, blood_group
draw_attribute(86, 104, 13, 5, "patient_id", is_pk=True)
draw_attribute(102, 104, 11, 5, "name")
draw_attribute(118, 98, 11, 5, "DOB")
draw_attribute(118, 88, 13, 5, "blood_group")

ax.plot([88, 90], [101.5, 94.5], color=line_color, linewidth=1.1)
ax.plot([99, 95], [101.5, 94.5], color=line_color, linewidth=1.1)
ax.plot([113, 101], [96.5, 92.5], color=line_color, linewidth=1.1)
ax.plot([111, 101], [88.5, 89.5], color=line_color, linewidth=1.1)

# DOCTOR: doctor_id (PK), name, specialty, phone
draw_attribute(10, 61, 13, 5, "doctor_id", is_pk=True)
draw_attribute(10, 48, 11, 5, "name")
draw_attribute(10, 35, 13, 5, "specialty")
draw_attribute(24, 28, 12, 5, "phone")

ax.plot([15, 20], [59, 52.5], color=line_color, linewidth=1.1)
ax.plot([15.5, 15.5], [48, 48], color=line_color, linewidth=1.1)
ax.plot([15, 20], [37, 43.5], color=line_color, linewidth=1.1)
ax.plot([24, 24], [30.5, 43.5], color=line_color, linewidth=1.1)

# TEST: test_id (PK), test_name, cost
draw_attribute(143, 56, 13, 5, "test_id", is_pk=True)
draw_attribute(144, 45, 13, 5, "test_name")
draw_attribute(143, 34, 11, 5, "cost")

ax.plot([139, 135], [54, 46.5], color=line_color, linewidth=1.1)
ax.plot([138, 137], [45, 43.5], color=line_color, linewidth=1.1)
ax.plot([139, 135], [36, 39.5], color=line_color, linewidth=1.1)

# Title & Legend
ax.text(75, 108, "Hospital Management System — Entity-Relationship (E-R) Diagram",
        ha='center', va='center', fontsize=12, fontweight='bold', color='#2B5B84')
ax.text(75, 105.5, "(Silberschatz 7e Exercise 6.15 · Includes Binary and Ternary Relationships)",
        ha='center', va='center', fontsize=9, fontstyle='italic', color='#555555')

plt.tight_layout()

out_dirs = [
    "boss_notes/diagrams",
    "Topicwise_answers_exam_style/diagrams",
    "Topicwise_answers_explaination/diagrams",
    "yearly_answers_exam_style/diagrams",
    "yearly_answers_explaination/diagrams"
]

img_name = "T02_EX6_15_hospital_er.jpg"

for d in out_dirs:
    if os.path.exists(d):
        p = os.path.join(d, img_name)
        plt.savefig(p, dpi=200, bbox_inches='tight', pad_inches=0.15)
        print(f"Saved: {p}")
        
        # Write .meta.json sidecar
        meta = {
            "description": "Hospital Management System ER Diagram with patient, doctor, room, and test entities and ternary prescribes relationship (Silberschatz 7e Exercise 6.15)",
            "figure_id": "T02_EX6_15_hospital_er",
            "source_image": "generated",
            "generator": "boss_notes/diagrams/_scripts/T02_EX6_15_hospital_er.py"
        }
        with open(p + ".meta.json", "w") as fp:
            json.dump(meta, fp, indent=2)

plt.close()
print("Done generating T02_EX6_15_hospital_er.jpg")

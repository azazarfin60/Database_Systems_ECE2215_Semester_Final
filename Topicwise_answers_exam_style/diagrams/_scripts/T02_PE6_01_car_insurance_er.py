"""
Generates T02_PE6_01_car_insurance_er.jpg
Chen ER diagram for Car Insurance Enterprise (Silberschatz 7e Practice Exercise 6.1):
Entities:
- CUSTOMER (customer_id [PK], name, address)
- CAR (license_plate [PK], model, year)
- POLICY (policy_id [PK], type, premium_amount)
- ACCIDENT (report_number [PK], date, location)
Relationships:
- owns (CUSTOMER - CAR, 1:N, total participation for CAR)
- covers (POLICY - CAR, 1:N, total participation for CAR)
- participated (CAR - ACCIDENT, M:N, descriptive attribute: damage_amount)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import json

fig, ax = plt.subplots(figsize=(15, 10), dpi=200)
ax.set_xlim(0, 150)
ax.set_ylim(0, 100)
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
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False):
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.2)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#111111')
    if is_pk:
        text_len = len(text)
        ax.plot([x - text_len*0.38, x + text_len*0.38], [y - 1.2, y - 1.2], color='#111111', linewidth=1.2)

# --- Layout ---
# Top/Middle Row: CUSTOMER -- owns -- CAR -- covers -- POLICY
# CUSTOMER at (25, 68)
# owns at (55, 68)
# CAR at (85, 68)
# covers at (115, 68)
# POLICY at (138, 68)
#
# Down from CAR:
# participated at (85, 38)
# ACCIDENT at (85, 14)
# damage_amount (descriptive attribute on participated) at (114, 38)

draw_entity(24, 68, 20, 9, "CUSTOMER")
draw_relationship(55, 68, 16, 10, "owns")
draw_entity(85, 68, 18, 9, "CAR")
draw_relationship(115, 68, 16, 10, "covers")
draw_entity(138, 68, 18, 9, "POLICY")

draw_relationship(85, 38, 18, 10, "participated")
draw_entity(85, 14, 20, 9, "ACCIDENT")

# --- Connectors & Cardinalities ---

# 1. CUSTOMER - owns (1:N)
# CUSTOMER to owns (single line, 1)
ax.plot([34, 47], [68, 68], color=line_color, linewidth=1.6)
ax.text(36, 70.5, "1", fontsize=11, fontweight='bold', color='#B78103')

# owns to CAR (double line = total participation of CAR, N)
ax.plot([63, 76], [68.7, 68.7], color=line_color, linewidth=1.5)
ax.plot([63, 76], [67.3, 67.3], color=line_color, linewidth=1.5)
ax.text(73, 70.5, "N", fontsize=11, fontweight='bold', color='#B78103')

# 2. covers - CAR (N, double line = total participation of CAR)
ax.plot([94, 107], [68.7, 68.7], color=line_color, linewidth=1.5)
ax.plot([94, 107], [67.3, 67.3], color=line_color, linewidth=1.5)
ax.text(96, 70.5, "N", fontsize=11, fontweight='bold', color='#B78103')

# covers to POLICY (single line, 1)
ax.plot([123, 129], [68, 68], color=line_color, linewidth=1.6)
ax.text(126, 70.5, "1", fontsize=11, fontweight='bold', color='#B78103')

# 3. CAR - participated - ACCIDENT (M:N)
# CAR to participated (single line, M or N)
ax.plot([85, 85], [63.5, 43], color=line_color, linewidth=1.6)
ax.text(87, 54, "M", fontsize=11, fontweight='bold', color='#B78103')

# participated to ACCIDENT (single line, N)
ax.plot([85, 85], [33, 18.5], color=line_color, linewidth=1.6)
ax.text(87, 26, "N", fontsize=11, fontweight='bold', color='#B78103')

# Descriptive attribute: damage_amount connected to participated diamond
draw_attribute(116, 38, 17, 5.5, "damage_amount")
ax.plot([94, 107.5], [38, 38], color=line_color, linewidth=1.4, linestyle='--')
ax.text(101, 40, "(descriptive)", fontsize=8, color='#4A7C2C', ha='center')

# --- Attributes ---

# CUSTOMER attributes: customer_id (PK), name, address
draw_attribute(12, 85, 14, 5.5, "customer_id", is_pk=True)
draw_attribute(28, 86, 13, 5.5, "name")
draw_attribute(10, 56, 13, 5.5, "address")

ax.plot([15, 20], [82.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([27, 25], [83.2, 72.5], color=line_color, linewidth=1.1)
ax.plot([15, 19], [58.5, 64], color=line_color, linewidth=1.1)

# CAR attributes: license_plate (PK), model, year
draw_attribute(71, 86, 14, 5.5, "model")
draw_attribute(85, 91, 15, 5.5, "license_plate", is_pk=True)
draw_attribute(99, 86, 13, 5.5, "year")

ax.plot([73, 80], [83.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([85, 85], [88.2, 72.5], color=line_color, linewidth=1.1)
ax.plot([97, 90], [83.5, 72.5], color=line_color, linewidth=1.1)

# POLICY attributes: policy_id (PK), type, premium_amount
draw_attribute(126, 86, 13, 5.5, "type")
draw_attribute(140, 91, 14, 5.5, "policy_id", is_pk=True)
draw_attribute(145, 80, 16, 5.5, "premium_amount")

ax.plot([129, 134], [83.5, 72.5], color=line_color, linewidth=1.1)
ax.plot([139, 138], [88.2, 72.5], color=line_color, linewidth=1.1)
ax.plot([143, 140], [77.5, 72.5], color=line_color, linewidth=1.1)

# ACCIDENT attributes: report_number (PK), date, location
draw_attribute(63, 6, 15, 5.5, "report_number", is_pk=True)
draw_attribute(85, 4, 13, 5.5, "date")
draw_attribute(107, 6, 13, 5.5, "location")

ax.plot([68, 77], [8.5, 11], color=line_color, linewidth=1.1)
ax.plot([85, 85], [6.8, 9.5], color=line_color, linewidth=1.1)
ax.plot([102, 93], [8.5, 11], color=line_color, linewidth=1.1)

# Title and Legend
ax.text(75, 97, "Car Insurance Enterprise Database — Entity-Relationship (E-R) Diagram",
        ha='center', va='center', fontsize=12, fontweight='bold', color='#2B5B84')
ax.text(75, 94.2, "(Silberschatz 7e Practice Exercise 6.1 · Double lines denote Total Participation)",
        ha='center', va='center', fontsize=9, fontstyle='italic', color='#555555')

plt.tight_layout()

out_dirs = [
    "boss_notes/diagrams",
    "Topicwise_answers_exam_style/diagrams",
    "Topicwise_answers_explaination/diagrams",
    "yearly_answers_exam_style/diagrams",
    "yearly_answers_explaination/diagrams"
]

img_name = "T02_PE6_01_car_insurance_er.jpg"

for d in out_dirs:
    if os.path.exists(d):
        p = os.path.join(d, img_name)
        plt.savefig(p, dpi=200, bbox_inches='tight', pad_inches=0.15)
        print(f"Saved: {p}")
        
        # Write .meta.json sidecar
        meta = {
            "description": "Car Insurance Enterprise Database ER Diagram with customer, car, policy, and accident entities and participated descriptive attribute (Silberschatz 7e Practice Exercise 6.1)",
            "figure_id": "T02_PE6_01_car_insurance_er",
            "source_image": "generated",
            "generator": "boss_notes/diagrams/_scripts/T02_PE6_01_car_insurance_er.py"
        }
        with open(p + ".meta.json", "w") as fp:
            json.dump(meta, fp, indent=2)

plt.close()
print("Done generating T02_PE6_01_car_insurance_er.jpg")

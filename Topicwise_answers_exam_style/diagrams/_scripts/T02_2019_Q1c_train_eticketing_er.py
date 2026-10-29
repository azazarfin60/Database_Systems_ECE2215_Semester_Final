"""
Generates T02_2019_Q1c_train_eticketing_er.jpg
Chen ER diagram for Rajshahi High-Tech Authority Train E-Ticketing System:
- PASSENGER
- TICKET
- TRAIN
- STATION
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

fig, ax = plt.subplots(figsize=(13, 8), dpi=200)
ax.set_xlim(0, 130)
ax.set_ylim(0, 80)
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
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#111111')

def draw_attribute(x, y, w, h, text, is_pk=False):
    ell = patches.Ellipse((x, y), w, h, facecolor=attr_face, edgecolor=attr_edge, linewidth=1.2)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, color='#111111')
    if is_pk:
        ax.plot([x - len(text)*0.4, x + len(text)*0.4], [y - 1.3, y - 1.3], color='#111111', linewidth=1.1)

# Placement layout:
# PASSENGER (x=20, y=45) --[Books] (x=45, y=45)-- TICKET (x=70, y=45) --[For_Train] (x=95, y=45)-- TRAIN (x=115, y=45)
# Wait, let's make it a nice 2x2 or T shape:
# PASSENGER (x=25, y=55) --[Books] (x=55, y=55)-- TICKET (x=85, y=55)
#                                                   |
#                                              [For_Train] (x=85, y=35)
#                                                   |
#                                                 TRAIN (x=85, y=18) --[Stops_At] (x=50, y=18)-- STATION (x=20, y=18)

draw_entity(24, 55, 18, 9, "PASSENGER")
draw_relationship(55, 55, 16, 10, "Books")
draw_entity(86, 55, 18, 9, "TICKET")

draw_relationship(86, 36, 16, 10, "For_Train")
draw_entity(86, 18, 18, 9, "TRAIN")

draw_relationship(53, 18, 16, 10, "Stops_At")
draw_entity(22, 18, 18, 9, "STATION")

# Connectors:
# PASSENGER - Books (1:N, total participation for passenger booking)
ax.plot([33, 47], [55, 55], color=line_color, linewidth=1.6)
ax.text(35, 57, "1", fontsize=11, fontweight='bold', color='#B78103')

# Books - TICKET (N, total participation of Ticket: double line)
ax.plot([63, 77], [55.8, 55.8], color=line_color, linewidth=1.5)
ax.plot([63, 77], [54.2, 54.2], color=line_color, linewidth=1.5)
ax.text(73, 57, "N", fontsize=11, fontweight='bold', color='#B78103')

# TICKET - For_Train (N, double line)
ax.plot([85.2, 85.2], [50.5, 41], color=line_color, linewidth=1.5)
ax.plot([86.8, 86.8], [50.5, 41], color=line_color, linewidth=1.5)
ax.text(88, 48, "N", fontsize=11, fontweight='bold', color='#B78103')

# For_Train - TRAIN (1)
ax.plot([86, 86], [31, 22.5], color=line_color, linewidth=1.6)
ax.text(88, 25, "1", fontsize=11, fontweight='bold', color='#B78103')

# TRAIN - Stops_At (M:N)
ax.plot([77, 61], [18, 18], color=line_color, linewidth=1.6)
ax.text(74, 20, "M", fontsize=11, fontweight='bold', color='#B78103')

ax.plot([45, 31], [18, 18], color=line_color, linewidth=1.6)
ax.text(34, 20, "N", fontsize=11, fontweight='bold', color='#B78103')

# Attributes:
# PASSENGER
draw_attribute(12, 70, 13, 5.5, "user_id", is_pk=True)
draw_attribute(28, 71, 13, 5.5, "name")
draw_attribute(10, 42, 13, 5.5, "nid")
draw_attribute(26, 41, 13, 5.5, "phone")

ax.plot([15, 20], [67.5, 59.5], color=line_color, linewidth=1.1)
ax.plot([26, 24], [68, 59.5], color=line_color, linewidth=1.1)
ax.plot([14, 18], [44.5, 50.5], color=line_color, linewidth=1.1)
ax.plot([25, 24], [43.5, 50.5], color=line_color, linewidth=1.1)

# Books attribute: booking_date
draw_attribute(55, 68, 14, 5.5, "booking_date")
ax.plot([55, 55], [65, 60], color=line_color, linewidth=1.1)

# TICKET attributes
draw_attribute(78, 71, 13, 5.5, "ticket_no", is_pk=True)
draw_attribute(94, 71, 13, 5.5, "journey_date")
draw_attribute(108, 62, 13, 5.5, "seat_no")
draw_attribute(108, 51, 13, 5.5, "fare")
draw_attribute(74, 43, 13, 5.5, "class")

ax.plot([80, 83], [68, 59.5], color=line_color, linewidth=1.1)
ax.plot([92, 88], [68, 59.5], color=line_color, linewidth=1.1)
ax.plot([102, 95], [60, 56], color=line_color, linewidth=1.1)
ax.plot([102, 95], [52, 54], color=line_color, linewidth=1.1)
ax.plot([76, 80], [45.5, 50.5], color=line_color, linewidth=1.1)

# TRAIN attributes
draw_attribute(108, 27, 13, 5.5, "train_no", is_pk=True)
draw_attribute(110, 18, 14, 5.5, "train_name")
draw_attribute(108, 9, 14, 5.5, "total_seats")

ax.plot([102, 95], [25, 20], color=line_color, linewidth=1.1)
ax.plot([103, 95], [18, 18], color=line_color, linewidth=1.1)
ax.plot([102, 95], [11, 16], color=line_color, linewidth=1.1)

# Stops_At attributes: arrival_time, dep_time
draw_attribute(53, 31, 13, 5.5, "arrival_time")
draw_attribute(53, 5, 13, 5.5, "dep_time")
ax.plot([53, 53], [28, 23], color=line_color, linewidth=1.1)
ax.plot([53, 53], [8, 13], color=line_color, linewidth=1.1)

# STATION attributes
draw_attribute(12, 31, 14, 5.5, "station_code", is_pk=True)
draw_attribute(28, 32, 14, 5.5, "station_name")
draw_attribute(16, 5, 13, 5.5, "city")

ax.plot([15, 19], [28.5, 22.5], color=line_color, linewidth=1.1)
ax.plot([26, 23], [29, 22.5], color=line_color, linewidth=1.1)
ax.plot([18, 20], [8, 13.5], color=line_color, linewidth=1.1)

ax.text(65, 76, "Train E-Ticketing System — E-R Diagram (Rajshahi High-Tech Authority)",
        ha='center', va='center', fontsize=11.5, fontweight='bold', color='#2B5B84')

plt.tight_layout()
out_dir_exam = "Topicwise_answers_exam_style/diagrams"
out_dir_exp = "Topicwise_answers_explaination/diagrams"

out_file_exam = os.path.join(out_dir_exam, "T02_2019_Q1c_train_eticketing_er.jpg")
out_file_exp = os.path.join(out_dir_exp, "T02_2019_Q1c_train_eticketing_er.jpg")

plt.savefig(out_file_exam, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.savefig(out_file_exp, dpi=200, bbox_inches='tight', pad_inches=0.1)
plt.close()
print("Saved T02_2019_Q1c_train_eticketing_er.jpg")

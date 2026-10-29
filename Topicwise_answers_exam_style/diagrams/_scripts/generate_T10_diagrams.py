"""
Generates clean, publication-quality precedence graph diagrams for Topic T10 (Serializability):
1. T10_2018_Q6c_precedence_graph.jpg
2. T10_2020_Q6ai_precedence_graph.jpg
3. T10_2020_Q6aii_precedence_graph.jpg
4. T10_2021_Q7b_precedence_graph.jpg
5. T10_2021_Q7c_precedence_graph.jpg
6. T10_2023_Q8b_precedence_graph.jpg
7. T10_2024_Q8c_precedence_graph.jpg
8. T10_CT04_Q04_precedence_graph.jpg
9. T10_2017_Q5c_precedence_graph.jpg
10. T10_2019_Q4a_precedence_graph.jpg
11. T10_2020_Q6b_precedence_graph.jpg
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json
import shutil

OUT_DIR_EXAM = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR_EXP = os.path.abspath(os.path.join(OUT_DIR_EXAM, "../../Topicwise_answers_explaination/diagrams"))

os.makedirs(OUT_DIR_EXAM, exist_ok=True)
os.makedirs(OUT_DIR_EXP, exist_ok=True)

def draw_precedence_graph(
    filename,
    title,
    nodes,
    node_pos,
    edges,
    verdict,
    is_serializable=True,
    serial_orders=None,
    cycle_nodes=None,
    note=None
):
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 65)
    ax.axis('off')

    # Background card
    bg = patches.FancyBboxPatch((2, 2), 96, 61, boxstyle="round,pad=1.5",
                                facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.5)
    ax.add_patch(bg)

    # Title header
    header_box = patches.FancyBboxPatch((5, 52), 90, 8.5, boxstyle="round,pad=0.5",
                                        facecolor="#1E293B", edgecolor="none")
    ax.add_patch(header_box)
    ax.text(50, 56.2, title, ha='center', va='center', fontsize=11, fontweight='bold', color="#FFFFFF")

    # Status badge
    if is_serializable:
        badge_face = "#ECFDF5"
        badge_edge = "#059669"
        badge_text = "ACYCLIC · CONFLICT SERIALIZABLE"
        badge_color = "#065F46"
    else:
        badge_face = "#FEF2F2"
        badge_edge = "#DC2626"
        badge_text = "CYCLE DETECTED · NOT CONFLICT SERIALIZABLE"
        badge_color = "#991B1B"

    badge = patches.FancyBboxPatch((20, 44), 60, 5.5, boxstyle="round,pad=0.4",
                                   facecolor=badge_face, edgecolor=badge_edge, linewidth=1.5)
    ax.add_patch(badge)
    ax.text(50, 46.7, badge_text, ha='center', va='center', fontsize=9.5, fontweight='bold', color=badge_color)

    # Draw nodes
    for node in nodes:
        x, y = node_pos[node]
        is_in_cycle = cycle_nodes and (node in cycle_nodes)
        node_face = "#FEE2E2" if is_in_cycle else "#EFF6FF"
        node_edge = "#DC2626" if is_in_cycle else "#1D4ED8"
        
        circle = plt.Circle((x, y), 5.5, facecolor=node_face, edgecolor=node_edge, linewidth=2.0, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, node, ha='center', va='center', fontsize=12, fontweight='bold', color="#0F172A", zorder=4)

    # Draw edges
    # edge tuple: (u, v, label, rad, is_cycle, label_pos)
    for u, v, label, rad, is_cycle, label_pos in edges:
        x1, y1 = node_pos[u]
        x2, y2 = node_pos[v]
        edge_color = "#DC2626" if is_cycle else "#2563EB"
        edge_lw = 2.0 if is_cycle else 1.8
        
        arrow = patches.FancyArrowPatch(
            (x1, y1), (x2, y2),
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=0.7,head_width=0.4",
            color=edge_color,
            linewidth=edge_lw,
            mutation_scale=18,
            shrinkA=32,
            shrinkB=32,
            zorder=5
        )
        ax.add_patch(arrow)

        # Label position
        lx, ly = label_pos
        ax.text(lx, ly, label, ha='center', va='center', fontsize=8.5, fontweight='bold',
                color=edge_color, bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFFFFF", edgecolor=edge_color, alpha=0.95, lw=0.9),
                zorder=6)

    # Bottom notes / serial order
    if is_serializable and serial_orders:
        if len(serial_orders) == 1:
            res_str = f"Equivalent Serial Order: {serial_orders[0]}"
        else:
            res_str = f"Possible Serial Orders ({len(serial_orders)}): " + "  |  ".join(serial_orders)
        ax.text(50, 8.5, res_str, ha='center', va='center', fontsize=9.5, fontweight='bold', color="#1E293B")
    elif not is_serializable and cycle_nodes:
        cycle_str = " → ".join(cycle_nodes) + f" → {cycle_nodes[0]}"
        ax.text(50, 8.5, f"Conflicting Cycle: {cycle_str}", ha='center', va='center', fontsize=9.5, fontweight='bold', color="#DC2626")

    if note:
        ax.text(50, 4.2, note, ha='center', va='center', fontsize=8, fontstyle='italic', color="#64748B")

    plt.tight_layout()
    out_exam = os.path.join(OUT_DIR_EXAM, filename)
    out_exp = os.path.join(OUT_DIR_EXP, filename)
    plt.savefig(out_exam, dpi=200, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close()

    # Copy to explanation dir
    shutil.copy2(out_exam, out_exp)

    # Write sidecars
    meta = {
        "description": f"Precedence graph for {title}: {verdict}",
        "figure_id": filename.replace(".jpg", ""),
        "source_image": "generated",
        "generator": f"Topicwise_answers_exam_style/diagrams/_scripts/{os.path.basename(__file__)}"
    }
    with open(out_exam + ".meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    with open(out_exp + ".meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Generated {filename}")

def main():
    # 1. 2018 Q.6(c)
    draw_precedence_graph(
        filename="T10_2018_Q6c_precedence_graph.jpg",
        title="2018 Q.6(c) Precedence Graph (T1, T2)",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "r1(A)→w2(A), r1(B)→w2(B)", 0.28, True, (50, 35)),
            ("T2", "T1", "w2(A)→w1(A), r2(B)→w1(B)", 0.28, True, (50, 17))
        ],
        verdict="Cycle between T1 and T2",
        is_serializable=False,
        cycle_nodes=["T1", "T2"],
        note="Edges exist in both directions on items A and B."
    )

    # 2. 2020 Q.6(a) (i)
    draw_precedence_graph(
        filename="T10_2020_Q6ai_precedence_graph.jpg",
        title="2020 Q.6(a)(i) Precedence Graph: r1(X); r3(X); w1(X); r2(X); w3(X)",
        nodes=["T1", "T2", "T3"],
        node_pos={"T1": (25, 34), "T2": (50, 16), "T3": (75, 34)},
        edges=[
            ("T1", "T3", "r1(X)→w3(X), w1(X)→w3(X)", -0.25, True, (50, 42)),
            ("T3", "T1", "r3(X)→w1(X)", -0.25, True, (50, 28)),
            ("T1", "T2", "w1(X)→r2(X)", 0.0, False, (33, 22)),
            ("T2", "T3", "r2(X)→w3(X)", 0.0, False, (67, 22))
        ],
        verdict="Cycles: T1 ↔ T3 and T1 → T2 → T3 → T1",
        is_serializable=False,
        cycle_nodes=["T1", "T3"],
        note="Direct 2-cycle between T1 and T3, plus a 3-cycle T1 → T2 → T3 → T1."
    )

    # 3. 2020 Q.6(a) (ii)
    draw_precedence_graph(
        filename="T10_2020_Q6aii_precedence_graph.jpg",
        title="2020 Q.6(a)(ii) Precedence Graph: r1(X); r3(X); w3(X); w1(X); r2(X)",
        nodes=["T1", "T2", "T3"],
        node_pos={"T1": (25, 34), "T2": (50, 16), "T3": (75, 34)},
        edges=[
            ("T1", "T3", "r1(X)→w3(X)", -0.25, True, (50, 42)),
            ("T3", "T1", "r3(X)→w1(X), w3(X)→w1(X)", -0.25, True, (50, 28)),
            ("T1", "T2", "w1(X)→r2(X)", 0.0, False, (33, 21)),
            ("T3", "T2", "w3(X)→r2(X)", 0.0, False, (67, 21))
        ],
        verdict="Cycle between T1 and T3",
        is_serializable=False,
        cycle_nodes=["T1", "T3"],
        note="Direct 2-cycle between T1 and T3 on item X."
    )

    # 4. 2021 Q.7(b)
    draw_precedence_graph(
        filename="T10_2021_Q7b_precedence_graph.jpg",
        title="2021 Q.7(b) Precedence Graph (T1, T2)",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "Conflicts on A & B (T1 before T2)", 0.0, False, (50, 31))
        ],
        verdict="Acyclic, serial order T1 → T2",
        is_serializable=True,
        serial_orders=["T1 → T2"],
        note="All operations of T1 precede conflicting operations of T2."
    )

    # 5. 2021 Q.7(c)
    draw_precedence_graph(
        filename="T10_2021_Q7c_precedence_graph.jpg",
        title="2021 Q.7(c) Precedence Graph (T1, T2)",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "Item A: r1(A),w1(A) before r2(A),w2(A)", 0.28, True, (50, 35)),
            ("T2", "T1", "Item B: r2(B),w2(B) before r1(B),w1(B)", 0.28, True, (50, 17))
        ],
        verdict="Cycle between T1 and T2",
        is_serializable=False,
        cycle_nodes=["T1", "T2"],
        note="Conflict on A directs T1 → T2; conflict on B directs T2 → T1."
    )

    # 6. 2023 Q.8(b)
    draw_precedence_graph(
        filename="T10_2023_Q8b_precedence_graph.jpg",
        title="2023 Q.8(b) Precedence Graph (T1, T2, T3, T4)",
        nodes=["T1", "T2", "T3", "T4"],
        node_pos={"T1": (20, 30), "T3": (48, 30), "T4": (20, 15), "T2": (80, 22.5)},
        edges=[
            ("T1", "T3", "w1(B) → r3(B)", 0.0, False, (34, 34)),
            ("T3", "T2", "r3(A)→w2(A), r3(B)→w2(B)", 0.0, False, (65, 30)),
            ("T4", "T2", "r4(A) → w2(A)", 0.0, False, (50, 15)),
            ("T1", "T2", "w1(B) → w2(B)", -0.24, False, (50, 39.5))
        ],
        verdict="Acyclic DAG (3 possible topological sorts)",
        is_serializable=True,
        serial_orders=["T4 → T1 → T3 → T2", "T1 → T4 → T3 → T2", "T1 → T3 → T4 → T2"],
        note="T1 precedes T3, T3 precedes T2, T4 precedes T2. T4 has no edge with T1/T3."
    )

    # 7. 2024 Q.8(c)
    draw_precedence_graph(
        filename="T10_2024_Q8c_precedence_graph.jpg",
        title="2024 Q.8(c) Precedence Graph (T1, T2)",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "r1(A)→w2(A), r1(B)→w2(B)", 0.28, True, (50, 35)),
            ("T2", "T1", "w2(A)→w1(A), r2(B)→w1(B)", 0.28, True, (50, 17))
        ],
        verdict="Cycle between T1 and T2",
        is_serializable=False,
        cycle_nodes=["T1", "T2"],
        note="Identical conflict structure to 2018 Q.6(c)."
    )

    # 8. CT-04 Q.04
    draw_precedence_graph(
        filename="T10_CT04_Q04_precedence_graph.jpg",
        title="CT-04 Q.04 Precedence Graph (T1, T2, T3)",
        nodes=["T1", "T2", "T3"],
        node_pos={"T1": (25, 34), "T2": (75, 34), "T3": (50, 16)},
        edges=[
            ("T1", "T2", "w1(A)→r2(A), w1(B)→r2(B)", 0.0, False, (50, 38)),
            ("T3", "T1", "step 3 w3(B) → step 4 w1(B)", 0.25, True, (46, 29)),
            ("T1", "T3", "step 4 w1(B) → step 5 w3(B), r3(B)", 0.25, True, (27, 22)),
            ("T3", "T2", "w3(B) → r2(B)", 0.0, False, (67, 23))
        ],
        verdict="Cycle between T1 and T3 on item B",
        is_serializable=False,
        cycle_nodes=["T1", "T3"],
        note="Conflict on item B between T1 and T3 forms a direct 2-cycle."
    )

    # 9. 2017 Q.5(c)
    draw_precedence_graph(
        filename="T10_2017_Q5c_precedence_graph.jpg",
        title="2017 Q.5(c) Interleaved Schedule Precedence Graph",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "r1(A) before w2(A)", 0.28, True, (50, 35)),
            ("T2", "T1", "r2(B) before w1(B)", 0.28, True, (50, 17))
        ],
        verdict="Cycle between T1 and T2",
        is_serializable=False,
        cycle_nodes=["T1", "T2"],
        note="Produces inconsistent state A=1, B=1; not conflict serializable."
    )

    # 10. 2019 Q.4(a)
    draw_precedence_graph(
        filename="T10_2019_Q4a_precedence_graph.jpg",
        title="2019 Q.4(a) Interleaved Schedule Precedence Graph",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "r1(P) before w2(P)", 0.28, True, (50, 35)),
            ("T2", "T1", "r2(Q) before w1(Q)", 0.28, True, (50, 17))
        ],
        verdict="Cycle between T1 and T2",
        is_serializable=False,
        cycle_nodes=["T1", "T2"],
        note="Concurrent read-before-write interleaving forms a cycle T1 ↔ T2."
    )

    # 11. 2020 Q.6(b)
    draw_precedence_graph(
        filename="T10_2020_Q6b_precedence_graph.jpg",
        title="2020 Q.6(b) Precedence Graph (T1, T2)",
        nodes=["T1", "T2"],
        node_pos={"T1": (30, 26), "T2": (70, 26)},
        edges=[
            ("T1", "T2", "Conflicts on X and Y (T1 before T2)", 0.0, False, (50, 31))
        ],
        verdict="Acyclic, serial order T1 → T2 (View & Conflict Serializable)",
        is_serializable=True,
        serial_orders=["T1 → T2"],
        note="All operations of T1 on X and Y precede T2; view equivalent to <T1, T2>."
    )

if __name__ == "__main__":
    main()

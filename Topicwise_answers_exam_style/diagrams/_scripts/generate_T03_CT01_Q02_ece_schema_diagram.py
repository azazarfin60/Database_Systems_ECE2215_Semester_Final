import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_diagram():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=200)
    ax.set_xlim(0, 1100)
    ax.set_ylim(0, 650)
    ax.axis('off')

    # Background
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Styling colors matching Silberschatz 7e
    box_border = '#3182CE'       # Clean professional blue
    header_bg = '#EBF8FF'        # Soft ice-blue header
    header_text_color = '#2B6CB0'# Bold Silberschatz blue title
    body_bg = '#FFFFFF'          # Clean white body
    attr_text_color = '#2D3748'  # Dark slate for attributes
    pk_color = '#1A202C'         # Bold black for PK
    arrow_color = '#E53E3E'      # Clear coral/red arrow for FK

    # Layout coordinates: (name, x, y, width, height, attributes, pks)
    # y is the top coordinate
    tables = {
        'Students': {
            'x': 60, 'y': 600, 'w': 210, 'h': 160,
            'attrs': ['student_id', 'name', 'email', 'dept_name'],
            'pks': ['student_id']
        },
        'Courses': {
            'x': 420, 'y': 600, 'w': 230, 'h': 210,
            'attrs': ['course_id', 'title', 'credits', 'instructor_id', 'building', 'room_number'],
            'pks': ['course_id']
        },
        'Instructors': {
            'x': 800, 'y': 600, 'w': 220, 'h': 160,
            'attrs': ['instructor_id', 'name', 'dept_name', 'salary'],
            'pks': ['instructor_id']
        },
        'Results': {
            'x': 60, 'y': 310, 'w': 210, 'h': 185,
            'attrs': ['student_id', 'course_id', 'semester', 'marks', 'grade'],
            'pks': ['student_id', 'course_id', 'semester']
        },
        'Classroom': {
            'x': 800, 'y': 310, 'w': 220, 'h': 140,
            'attrs': ['building', 'room_number', 'capacity'],
            'pks': ['building', 'room_number']
        }
    }

    attr_coords = {}

    for tname, t in tables.items():
        x, y, w, h = t['x'], t['y'], t['w'], t['h']
        
        # Outer table box
        rect = patches.FancyBboxPatch((x, y - h), w, h,
                                      boxstyle="round,pad=0,rounding_size=3",
                                      facecolor=body_bg, edgecolor=box_border, linewidth=1.5)
        ax.add_patch(rect)

        # Header box
        header_h = 34
        head_rect = patches.FancyBboxPatch((x, y - header_h), w, header_h,
                                           boxstyle="round,pad=0,rounding_size=3",
                                           facecolor=header_bg, edgecolor=box_border, linewidth=1.2)
        ax.add_patch(head_rect)

        # Dividing line
        ax.plot([x, x + w], [y - header_h, y - header_h], color=box_border, linewidth=1.2)

        # Title
        ax.text(x + w / 2, y - header_h / 2, tname,
                ha='center', va='center', fontsize=12, fontweight='bold', color=header_text_color)

        # Attributes
        line_gap = (h - header_h) / (len(t['attrs']) + 0.4)
        for i, attr in enumerate(t['attrs']):
            cur_y = y - header_h - (i + 0.7) * line_gap
            is_pk = attr in t['pks']
            weight = 'bold' if is_pk else 'normal'
            color = pk_color if is_pk else attr_text_color
            
            # Print attribute name
            ax.text(x + 16, cur_y, attr, ha='left', va='center',
                    fontsize=10, fontweight=weight, color=color, family='monospace')
            
            # Underline PK
            if is_pk:
                text_len = len(attr) * 7.2
                ax.plot([x + 16, x + 16 + text_len], [cur_y - 6, cur_y - 6],
                        color=pk_color, linewidth=1.2)

            # Store connection points
            attr_coords[f"{tname}.{attr}"] = {
                'left': (x, cur_y),
                'right': (x + w, cur_y),
                'top': (x + w/2, y),
                'bottom': (x + w/2, y - h),
                'y': cur_y
            }

    # Helper function for drawing nice arrows
    def draw_fk_arrow(start_pt, end_pt, rad=0.0, color=arrow_color):
        ax.annotate('', xy=end_pt, xytext=start_pt,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                                    mutation_scale=13,
                                    connectionstyle=f"arc3,rad={rad}"))

    # 1. Results.student_id -> Students.student_id
    # From top-left of Results at student_id curving up to bottom-left of Students at student_id
    # We can connect left edge of Results to left edge of Students
    p_start = attr_coords['Results.student_id']['left']
    p_end = attr_coords['Students.student_id']['left']
    # Routed nicely on the left margin
    ax.annotate('', xy=p_end, xytext=p_start,
                arrowprops=dict(arrowstyle="-|>", color=arrow_color, lw=1.8,
                                mutation_scale=13,
                                connectionstyle="arc3,rad=-0.32"))

    # 2. Results.course_id -> Courses.course_id
    # From right edge of Results at course_id curving up-right to left edge of Courses at course_id
    p_start = attr_coords['Results.course_id']['right']
    p_end = attr_coords['Courses.course_id']['left']
    draw_fk_arrow(p_start, p_end, rad=-0.18)

    # 3. Courses.instructor_id -> Instructors.instructor_id
    # From right edge of Courses at instructor_id to left edge of Instructors at instructor_id
    p_start = attr_coords['Courses.instructor_id']['right']
    p_end = attr_coords['Instructors.instructor_id']['left']
    draw_fk_arrow(p_start, p_end, rad=-0.08)

    # 4. Courses.building -> Classroom.building
    # From right edge of Courses at building to left edge of Classroom at building
    p_start = attr_coords['Courses.building']['right']
    p_end = attr_coords['Classroom.building']['left']
    draw_fk_arrow(p_start, p_end, rad=0.15)

    # Header title
    ax.text(550, 632, "ECE Relational Database Schema Diagram",
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1A365D')

    # Footer note
    ax.text(550, 45, "* Primary key (PK) attributes are underlined. Red arrows depict Foreign Key (FK) referential integrity references.",
            ha='center', va='center', fontsize=9.5, fontstyle='italic', color='#4A5568')

    plt.tight_layout()
    plt.savefig('Topicwise_answers_exam_style/diagrams/T03_CT01_Q02_ece_schema_diagram.jpg',
                dpi=200, bbox_inches='tight', pad_inches=0.2)
    plt.savefig('Topicwise_answers_explaination/diagrams/T03_CT01_Q02_ece_schema_diagram.jpg',
                dpi=200, bbox_inches='tight', pad_inches=0.2)
    plt.close()
    print("Schema diagrams saved successfully to both layers.")

if __name__ == '__main__':
    generate_diagram()

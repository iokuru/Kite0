import os
import shutil
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from PIL import Image

def build_kite_figure(dpi=128):
    fig, ax = plt.subplots(figsize=(2, 2), dpi=dpi)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax.set_xlim(0, 100)
    ax.set_ylim(100, 0)
    ax.axis('off')

    DARK = '#0f172a'
    GREEN_MAIN = '#10b981'
    GREEN_LIGHT = '#34d399'
    GREEN_ACCENT = '#6ee7b7'

    # 1. Left String
    str_verts = [(37, 49), (35, 62), (25, 76), (8, 92)]
    str_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    ax.add_patch(patches.PathPatch(Path(str_verts, str_codes), facecolor='none', edgecolor='#94a3b8', lw=2.0, capstyle='round'))

    # 2. Right Ribbon Tail
    tail_verts = [
        (66, 58),
        (69, 67), (72, 73), (69, 79),
        (65, 84), (70, 89), (80, 90),
        (88, 90), (92, 91), (94, 93)
    ]
    tail_codes = [
        Path.MOVETO,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
        Path.CURVE4, Path.CURVE4, Path.CURVE4,
        Path.CURVE4, Path.CURVE4, Path.CURVE4
    ]
    tail_path = Path(tail_verts, tail_codes)
    ax.add_patch(patches.PathPatch(tail_path, facecolor='none', edgecolor=DARK, lw=8.0, capstyle='round', joinstyle='round'))
    ax.add_patch(patches.PathPatch(tail_path, facecolor='none', edgecolor=GREEN_MAIN, lw=4.2, capstyle='round', joinstyle='round'))

    # 3. Kite Body Quadrants
    cp = (48, 28)
    tf_verts = [(42, 7), (57, 14), (71, 18), cp, (42, 7)]
    tf_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(tf_verts, tf_codes), facecolor=GREEN_ACCENT, edgecolor=DARK, lw=1.5))

    rf_verts = [(71, 18), (69, 38), (65, 57), cp, (71, 18)]
    rf_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(rf_verts, rf_codes), facecolor=GREEN_MAIN, edgecolor=DARK, lw=1.5))

    bf_verts = [(65, 57), (47, 51), (30, 42), cp, (65, 57)]
    bf_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(bf_verts, bf_codes), facecolor='#059669', edgecolor=DARK, lw=1.5))

    lf_verts = [(30, 42), (35, 23), (42, 7), cp, (30, 42)]
    lf_codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.LINETO]
    ax.add_patch(patches.PathPatch(Path(lf_verts, lf_codes), facecolor=GREEN_LIGHT, edgecolor=DARK, lw=1.5))

    # Inner bridle
    ax.plot([38, 65], [36, 57], color=DARK, lw=1.5, solid_capstyle='round')

    # Cross Spars
    ax.plot([42, 65], [7, 57], color=DARK, lw=3.2, solid_capstyle='round')
    ax.plot([30, 71], [42, 18], color=DARK, lw=3.2, solid_capstyle='round')

    # Outer perimeter frame
    body_verts = [
        (42, 6),
        (57, 14), (72, 17),
        (69, 38), (66, 58),
        (47, 51), (29, 43),
        (35, 23), (42, 6)
    ]
    body_codes = [
        Path.MOVETO,
        Path.CURVE3, Path.CURVE3,
        Path.CURVE3, Path.CURVE3,
        Path.CURVE3, Path.CURVE3,
        Path.CURVE3, Path.CURVE3
    ]
    ax.add_patch(patches.PathPatch(Path(body_verts, body_codes), facecolor='none', edgecolor=DARK, lw=3.6, joinstyle='round'))

    # Center white pin
    ax.plot(cp[0], cp[1], 'o', color='#ffffff', markersize=3.8, markeredgecolor=DARK, markeredgewidth=1.2)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig

def main():
    target_dirs = [
        os.path.join("extension", "public", "icons"),
        os.path.join("extension", "dist", "icons"),
        os.path.join("extension", "dist-chrome", "icons"),
        os.path.join("extension", "dist-firefox", "icons"),
    ]
    
    # Render master high-res image
    fig = build_kite_figure(dpi=256)
    temp_master = os.path.join("extension", "public", "icons", "master_render.png")
    os.makedirs(os.path.dirname(temp_master), exist_ok=True)
    fig.savefig(temp_master, transparent=True, dpi=256)
    plt.close(fig)

    master_img = Image.open(temp_master)

    for target_dir in target_dirs:
        os.makedirs(target_dir, exist_ok=True)
        for s in [16, 48, 128]:
            resized = master_img.resize((s, s), Image.Resampling.LANCZOS)
            out_path = os.path.join(target_dir, f"icon-{s}.png")
            resized.save(out_path, "PNG")
            print(f"Generated {out_path} ({s}x{s})")

    if os.path.exists(temp_master):
        os.remove(temp_master)

if __name__ == "__main__":
    main()

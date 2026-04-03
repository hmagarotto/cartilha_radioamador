import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image
from pathlib import Path

# Parâmetros da senoide
amplitude = 1
frequencia = 1
fase = 0
periodo = 1 / frequencia

# Senoide
t = np.linspace(0, periodo, 1000)
y = amplitude * np.sin(2 * np.pi * frequencia * t + fase)

# Plotagem
# plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(7,4.5))
ax.margins(x=.05, y=.2)
# ax.set_xlim(-0.05, 2.55 * periodo)
# ax.set_ylim(-amplitude - 1.4, amplitude + 1.2)


# Grade e eixos
ax.axhline(color='black', linestyle='-', linewidth=1.5)
ax.grid(True, linewidth=0.1, zorder=0)

# Linhas Vp e -Vp
ax.axhline(amplitude, color="#555", linewidth=1, linestyle="--", alpha=0.5, zorder=2)
ax.axhline(-amplitude, color="#555", linewidth=1, linestyle="--", alpha=0.5, zorder=2)

# Amplitude / Valor de Pico (Vp)
t_vp = periodo / 4
ax.plot(t_vp,         0, "o", color="#000", markersize=4, zorder=5)
ax.plot(t_vp, amplitude, "o", color="#000", markersize=4, zorder=5)
arrow = mpatches.FancyArrowPatch(
    (t_vp, amplitude), 
    (t_vp, 0), 
    arrowstyle='<->', # Double-headed style
    mutation_scale=20 # Adjust the size of the arrow heads
)
ax.add_patch(arrow)
ax.annotate(
    f"Amplitude\nValor de Pico (Vp)",
    xy=(t_vp, amplitude),
    ha='center',              # Horizontal alignment: center
    va='bottom',              # Vertical alignment: center
    textcoords='offset points',
    xytext=(0, +2),
    fontsize=10, color="#000", fontweight="bold",
)

# Valor de Pico a Pico (Vpp)
t_vpp = 3/4 * periodo          # posição x da seta dupla
ax.plot(t_vpp, +amplitude, "o", color="#000", markersize=4, zorder=5)
ax.plot(t_vpp, -amplitude, "o", color="#000", markersize=4, zorder=5)
arrow = mpatches.FancyArrowPatch(
    (t_vpp, amplitude), 
    (t_vpp, -amplitude), 
    arrowstyle='<->', # Double-headed style
    mutation_scale=20 # Adjust the size of the arrow heads
)
ax.add_patch(arrow)
ax.annotate(
    f"Pico a Pico\n(Vpp = 2 x Vp)",
    xy=(t_vpp, amplitude),
    ha='center',              # Horizontal alignment: center
    va='bottom',              # Vertical alignment: center
    textcoords='offset points',
    xytext=(0, +2),
    fontsize=10, color="#000", fontweight="bold",
)

# Periodo (T)
y_periodo = -amplitude-.1
t0, t1 = 0.0, periodo
ax.plot([t0, t0], [- 0.1, - amplitude - 0.3], color="#000", lw=1.5)
ax.plot([t1, t1], [- 0.1, - amplitude - 0.3], color="#000", lw=1.5)
ax.add_patch(mpatches.FancyArrowPatch(
    (t0, - amplitude - 0.2), 
    (t1, - amplitude - 0.2), 
    arrowstyle='<->', # Double-headed style
    mutation_scale=20 # Adjust the size of the arrow heads
))
ax.annotate(
    f"Período (T)\nFrequência = 1/T",
    xy=((t1-t0)/2, -amplitude-0.2),
    ha='center',              # Horizontal alignment: center
    va='top',              # Vertical alignment: center
    textcoords='offset points',
    xytext=(0, -2),
    fontsize=10, color="#000", fontweight="bold",
)

# Desenha Senoide
ax.plot(t, y, label="Senoide")

# Eixos
ax.tick_params(colors="#aaaaaa", labelsize=9)
ax.set_xlabel("Tempo (s)", color="#aaaaaa", fontsize=11)
ax.set_ylabel("Amplitude (V)", color="#aaaaaa", fontsize=11)
# fig.suptitle('Conceitos de onda\nfrequência, período, amplitude', fontsize=16, fontweight="bold")

# Save image
script_path = Path(__file__)
script_stem = script_path.stem
script_dir = script_path.resolve().parent
project_root = script_dir.parent.parent
image_path = project_root / f"src/anexo_03_eletronica/images/{script_stem}.png";
plt.tight_layout()
plt.savefig(image_path)

# Convert to BW
bw_image_path = project_root / f"src/anexo_03_eletronica/images/{script_stem}-bw.png";
Image.open(image_path).convert('L').save(bw_image_path)

print(f"> Updated: {image_path}")

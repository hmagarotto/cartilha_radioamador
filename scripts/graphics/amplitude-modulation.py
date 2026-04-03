import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from  matplotlib.axes import Axes
from pathlib import Path

# Message and Carrier params
message_amplitude=5
message_frequency=2
carrier_amplitude=10
carrier_frequency=50
total_message_cycles=2

# Samples
sample_frequency=carrier_frequency*10
step=1/sample_frequency
t_start=0
t_end=total_message_cycles/message_frequency
t_total=t_end-t_start
t=np.arange(t_start,t_end,step)

# Message Signal
message_signal = message_amplitude * np.sin(2*np.pi*message_frequency*t)

# Carrier Signal
carrier_signal = carrier_amplitude * np.cos(2*np.pi*carrier_frequency*t)

# Modulated Signal
# https://engineerstutor.com/wp-content/uploads/2020/09/AM-Math-Derivation-EngineersTutor.pdf
modulation_index=message_amplitude/carrier_amplitude
if modulation_index > 1: print('Overmodulation')  # Overmodulation: https://youtu.be/I46eP8uZh_Y?t=221&si=-5q_OotpKT7BCADt
# modulated_signal = (carrier_amplitude+message_signal)*np.cos(2*np.pi*carrier_frequency*t)
# modulated_signal = carrier_signal * (1 + modulation_index * np.sin(2*np.pi*message_frequency*t))
# modulated_signal = carrier_signal * (1 + message_signal/carrier_amplitude)
modulated_signal = carrier_signal*(message_signal + carrier_amplitude)/carrier_amplitude


# Envelope
# envelope = (message_amplitude * np.sin(2*np.pi*message_frequency*t)) + carrier_amplitude
envelope = message_signal + carrier_amplitude

# Plot
fig, axs = plt.subplots(3, 1, sharex=True, layout='constrained', figsize=(6, 6))
(ax1, ax2, ax3) = axs
# fig.suptitle('Modulação em Amplitude\nAmplitude Modulation (AM)', fontsize=14)

# set x axis
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1/(2*message_frequency)))
ax3.set_xlabel("Tempo (s)")

# set y axis
ydiv=carrier_amplitude/2
for ax in axs:
    ax.yaxis.set_major_locator(ticker.MultipleLocator(ydiv))
    ax.grid(True)
    ax.set_ylabel("Amplitude (V)")
    ax.tick_params(axis='y', labelleft=True)
    ax.axhline(color='black', linestyle='-', linewidth=1.5)

ax1.set_title('Mensagem')
ax1.plot(t, message_signal)

ax2.set_title('Portadora')
ax2.plot(t, carrier_signal)

ax3.set_title('Sinal modulado')
ax3.plot(t, modulated_signal)
ax3.plot(t,   envelope)
ax3.plot(t,  -envelope)

# ax4.set_title("Log. Magnitude Spectrum")
# ax4.set_xlim(carrier_frequency-(3*message_frequency), carrier_frequency+(3*message_frequency)) 
# ax4.xaxis.set_major_locator(ticker.MultipleLocator(message_frequency))
# ax4.magnitude_spectrum(modulated_signal, Fs=sample_frequency, scale='dB', color='C1')

# Save image
script_path = Path(__file__)
script_stem = script_path.stem
script_dir = script_path.resolve().parent
project_root = script_dir.parent.parent
image_path = project_root / f"src/anexo_01_técnica_e_ética/images/{script_stem}.png";
plt.savefig(image_path)
print(f"> Updated: {image_path}")

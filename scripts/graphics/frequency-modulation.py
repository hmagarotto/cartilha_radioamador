import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from  matplotlib.axes import Axes
from pathlib import Path

# Message and Carrier params
message_amplitude=5;    message_frequency=1
carrier_amplitude=10;   carrier_frequency=20
total_message_cycles=1.5

# Samples
sample_frequency=carrier_frequency*40
step=1/sample_frequency
t_start=0
t_end=total_message_cycles/message_frequency
t_total=t_end-t_start
t=np.arange(t_start,t_end,step)

# Message Signal
message_signal = message_amplitude * np.sin(2*np.pi*message_frequency*t)

# Carrier Signal
carrier_signal = carrier_amplitude * np.sin(2*np.pi*carrier_frequency*t)

# Modulated Signal
# Ref: https://engineerstutor.com/wp-content/uploads/2020/10/FM_Frequency_Modulation_EngineersTutor.pdf
frequency_deviation_sensitivity=10/message_amplitude ## Hertz/Volt
modulated_signal = carrier_amplitude*np.sin(
    2*np.pi*carrier_frequency*t +
    frequency_deviation_sensitivity*message_amplitude*-np.cos(2*np.pi*message_frequency*t)
    )

# Plot
fig, axs = plt.subplots(3, 1, sharex=True, layout='constrained', figsize=(6, 6))
(ax1, ax2, ax3) = axs
# fig.suptitle('Modulação em Frequencia\nFrequency Modulation (FM)', fontsize=14)

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

# Frequency domain
# fig, (ax1) = plt.subplots(1, 1, layout='constrained', figsize=(8, 6))
# ax1.set_title("Log. Magnitude Spectrum")
# # ax1.set_xlim(carrier_frequency-(3*frequency_deviation), carrier_frequency+(3*frequency_deviation)) 
# ax1.set_xlim(0, 2*carrier_frequency) 
# # ax1.xaxis.set_major_locator(ticker.MultipleLocator(carrier_frequency/4 ))
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(carrier_frequency/5))
# ax1.magnitude_spectrum(modulated_signal, Fs=sample_frequency, scale='dB', color='C1')
# plt.show()

# Save image
script_path = Path(__file__)
script_stem = script_path.stem
script_dir = script_path.resolve().parent
project_root = script_dir.parent.parent
image_path = project_root / f"src/anexo_01_técnica_e_ética/images/{script_stem}.png";
plt.savefig(image_path)
print(f"> Updated: {image_path}")

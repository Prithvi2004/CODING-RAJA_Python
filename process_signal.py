import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Generate a Noisy Signal
def generate_noisy_signal(frequency, amplitude, noise_std, duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, noise_std, signal.shape)
    noisy_signal = signal + noise
    return t, noisy_signal

# Design a Low-pass Filter
def design_low_pass_filter(cutoff_frequency, sampling_rate, filter_order=4):
    nyquist_freq = 0.5 * sampling_rate
    normalized_cutoff_freq = cutoff_frequency / nyquist_freq
    b, a = butter(filter_order, normalized_cutoff_freq, btype='low', analog=False)
    return b, a

# Apply the Filter
def apply_filter(signal, b, a):
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

# Parameters
frequency = 1  # Frequency of the sinusoidal signal (Hz)
amplitude = 1  # Amplitude of the sinusoidal signal
noise_std = 0.5  # Standard deviation of the Gaussian noise
duration = 10  # Duration of the signal (seconds)
sampling_rate = 100  # Sampling rate (samples per second)
cutoff_frequency = 5  # Cutoff frequency of the low-pass filter (Hz)
filter_order = 4  # Order of the low-pass filter

# Generate Noisy Signal
t, noisy_signal = generate_noisy_signal(frequency, amplitude, noise_std, duration, sampling_rate)

# Design Low-pass Filter
b, a = design_low_pass_filter(cutoff_frequency, sampling_rate, filter_order)

# Apply the Filter
filtered_signal = apply_filter(noisy_signal, b, a)

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='Noisy Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Noisy Signal and Filtered Signal')
plt.legend()
plt.grid(True)
plt.show()
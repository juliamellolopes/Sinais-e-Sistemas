import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros
N = 24
n = np.arange(N)

# Calculando x[n]
x = 1 + np.sin((np.pi / 12) * n + (3 * np.pi / 8))

# Calculando X[k] usando a DFT
X = np.fft.fft(x)

# Mostrando os resultados
print("x[n]:", x)
print("X[k]:", X)

# Plotando x[n]
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.stem(n, x, basefmt=" ")
plt.title('x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plotando magnitude de X[k]
plt.subplot(1, 2, 2)
plt.stem(n, np.abs(X), basefmt=" ")
plt.title('Magnitude de X[k]')
plt.xlabel('k')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

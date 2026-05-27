import matplotlib.pyplot as plt
import numpy as np

# Datos usando LUZ RESTANTE (%)
x_fresnel = [0, 25, 25, 100]
y_fresnel = [0.5, 0.5, 1e-13, 1e-13]

x_esferica = [0, 40, 40, 100]
y_esferica = [0.5, 0.5, 1e-13, 1e-13]

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Curvas step
ax.step(x_fresnel, y_fresnel, where='post', label='Lente Fresnel',
        color='blue', linewidth=2, alpha=0.85)
ax.step(x_esferica, y_esferica, where='post', label='Lente esférica',
        color='red', linewidth=2, linestyle='--', alpha=0.85)

# Líneas verticales en los umbrales de luz restante
ax.axvline(x=25, color='blue', linestyle=':', alpha=0.5)
ax.axvline(x=40, color='red', linestyle=':', alpha=0.5)

# Etiquetas de luz restante debajo
ax.text(25, 1e-14, '25 % intensidad', ha='center', va='top', color='blue', alpha=0.7)
ax.text(40, 1e-14, '40 % intensidad', ha='center', va='top', color='red', alpha=0.7)

# Línea horizontal en BER = 0.5
ax.axhline(y=0.5, color='orange', linestyle='--', alpha=0.9, linewidth=1.2)
#ax.text(0.5, 0.52, '0.5', transform=ax.get_yaxis_transform(),
#        ha='left', va='bottom', color='orange', fontsize=9, alpha=0.9)

# --- Anotaciones de pérdida (sin flechas) un poco por encima de 0.5 ---
#ax.text(20, 0.58, '80 % pérdida', ha='center', va='bottom',
#        color='blue', fontsize=8, alpha=0.9,
#        bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.5, ec='none'))
#ax.text(40, 0.62, '60 % pérdida', ha='center', va='bottom',
#        color='red', fontsize=8, alpha=0.9,
#        bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.5, ec='none'))

# Escala y límites
ax.set_yscale('log')
ax.set_ylim(1e-15, 1.5)
ax.set_xlim(0, 100)

# Marca 0.5 en el eje Y
yticks = list(ax.get_yticks()) + [0.5]
ax.set_yticks(yticks)
ax.set_yticklabels([f'{tick:.0e}' if tick != 0.5 else '0.5' for tick in yticks])

# Eje X principal (luz restante)
ax.set_xlabel('Intensidad luminosa relativa (%)')
ax.set_ylabel('BER')
ax.set_title('BER en función de la atenuación óptica', y=1.08, pad=20)
ax.grid(True, which='both', linestyle='--', alpha=0.4)
ax.legend(loc='upper right')

# Eje X secundario (pérdida de luz)
secax = ax.secondary_xaxis('top')
secax.set_xlabel('Pérdida de intensidad luminosa por obstrucción (%)')
secax.set_xticks([0, 20, 40, 60, 80, 100])
secax.set_xticklabels(['100', '80', '60', '40', '20', '0'])

plt.savefig('graficaBER.png', dpi=600, transparent=True, bbox_inches='tight')
plt.savefig('graficaBER.pdf', transparent=True, bbox_inches='tight')

plt.show()
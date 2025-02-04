🔌 Conexión del Fotoresistor (LDR)
El LDR cambia su resistencia según la luz:

Más luz → Menos resistencia → Más voltaje
Menos luz → Más resistencia → Menos voltaje
Como la Raspberry Pi Zero no tiene entradas analógicas, usamos un divisor de voltaje con una resistencia fija (10kΩ recomendado) y medimos el tiempo de descarga en un GPIO.

🛠️ Esquema de Conexión
Componente	Conexión
LDR - Pin 1	GPIO 18 (Entrada)
LDR - Pin 2	GND
Resistencia 10kΩ - Pin 1	GPIO 18
Resistencia 10kΩ - Pin 2	3.3V

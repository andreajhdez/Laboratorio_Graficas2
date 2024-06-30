# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Definir los datos del dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje',
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje',
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

# Crear un DataFrame de Pandas
df = pd.DataFrame(data)
# Aplicar el estilo "fivethirtyeight"
plt.style.use('fivethirtyeight')
# Graficar la distribución de notas con un boxplot por cada materia
plt.boxplot([df[df['materia'] == materia]['nota'] for materia in df['materia'].unique()],
            labels=df['materia'].unique(), medianprops={'color': 'orange'})
plt.title('Distribución de Notas')
plt.ylabel('Nota')
plt.grid(True)

# Guardar la figura como archivo PNG
plt.savefig('distribucion_notas_boxplot.png')

# Mostrar el gráfico
plt.show()

# Calcular la cantidad de estudiantes aprobados y no aprobados
aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

# Preparar los datos para el pie chart
sizes = [aprobados, no_aprobados]
labels = ['Aprobados', 'No Aprobados']
colors = ['blue', 'orange']  # Colores para los segmentos (azul y naranja)
# Aplicar el estilo "fivethirtyeight"
plt.style.use('fivethirtyeight')
# Crear el pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Aprobados')

# Guardar la figura como archivo PNG
plt.savefig('distribucionaprobados_piechart.png')

# Mostrar el gráfico
plt.show()

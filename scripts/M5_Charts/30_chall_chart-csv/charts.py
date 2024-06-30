import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  """
  Genera un gráfico de torta a partir de las etiquetas y los valores proporcionados.

  Parámetros:
  - labels: una lista de etiquetas para cada segmento del gráfico.
  - values: una lista de valores numéricos correspondientes a cada segmento del gráfico.

  Ejemplo de uso:
  labels = ['Manzanas', 'Naranjas', 'Plátanos']
  values = [10, 15, 5]
  generate_pie_chart(labels, values)
  """
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
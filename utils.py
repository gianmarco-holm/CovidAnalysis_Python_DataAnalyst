from functools import reduce


def get_kills(data):
  labels = {row['pais'] for row in data}
  values = list()
  for item in labels:
    paises = list(filter(lambda x: x['pais'] == item, data))
    kill_pais = [int(x['total muertes reportadas por covid']) for x in paises]
    kill = reduce(lambda x, y: x + y, kill_pais)
    values.append(kill)
  return labels, values

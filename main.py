import csvCrud
import charts
import utils


def run():
  #Población total
  '''
  data_pob = csvCrud.read_csv('poblacion-por-pais.csv')
  labels_pob = [item['Pais'] for item in data_pob]
  values_pob = [item['Poblacion'] for item in data_pob]
  charts.generate_pie_chart(labels_pob, values_pob)
  '''
  #Muertes por pais
  data_covid = csvCrud.read_csv('muertes-covid-por-pais.csv')
  labels, values = utils.get_kills(data_covid)
  charts.generate_bar_chart(list(labels), values)

if __name__ == '__main__':
  run()

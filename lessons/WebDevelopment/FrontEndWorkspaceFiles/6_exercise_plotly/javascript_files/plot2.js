var year = [2015]
var arable_land_brazil = [33.8100342899258]
var country_name_brazil = 'Brazil'

var arable_land_germany = [47.9592041483809]
var country_name_germany = 'Germany'

var arable_land_china = [56.2229587724434]
var country_name_china = 'China'

var arable_land = []

var trace1 = {
  x: [country_name_brazil, country_name_germany, country_name_china],
  y: [arable_land_brazil[0], arable_land_germany[0], arable_land_china[0]],
  type: 'bar',
  name: 'omar',
}

var layout = {
  title: 'Arable land per country for the year ' + year,
}

var data = [trace1]

Plotly.newPlot('plot2', data, layout)

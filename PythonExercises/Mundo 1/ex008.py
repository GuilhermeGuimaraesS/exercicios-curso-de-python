m = float(input('Digite uma distância em metros: '))
quilômetros = m/1000
hectômetros = m/100
decâmetros = m/10
decímetros = m*10
centímetros = m*100
milímetros = m*1000
print('A Distância de {}m, corresponde a: \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'
      .format(m,quilômetros, hectômetros, decâmetros, decímetros, centímetros, milímetros))

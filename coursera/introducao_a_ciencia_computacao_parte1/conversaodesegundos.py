segundos_str = input("quantos segunos gostaria de coverter: ", )

totalseg=int(segundos_str)

horas= totalseg//3600
seg_restantes= totalseg % 3600
minutos= seg_restantes // 60
seg_restantes_final= seg_restantes % 60

print(horas ,"horas" ,minutos ,"minutos e" , seg_restantes_final ,"segundos")



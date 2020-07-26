v1, v2 = [str(x) for x in input().split()]
dia_i = int(v2)
values = str(input()).split()
hora_i, minuto_i, segundo_i = int(values[0]), int(values[2]), int(values[4])
v1, v2 = [str(x) for x in input().split()]
dia_f = int(v2)
values = str(input()).split()
hora_f, minuto_f, segundo_f = int(values[0]), int(values[2]), int(values[4])

ver_h = False
ver_m = False
ver_s = False
ctr_d = 0
ctr_h = 0
ctr_m = 0
ctr_s = 0

if(hora_i > hora_f):
	ver_h = True
if(minuto_i > minuto_f):
	ver_m = True
if(segundo_i > segundo_f):
	ver_s = True
while(dia_i != dia_f):
	ctr_d += 1
	dia_i += 1
while(hora_i != hora_f):
	ctr_h += 1
	hora_i += 1
	if(hora_i == 25):
		hora_i = 1
while(minuto_i != minuto_f):
	ctr_m += 1
	minuto_i += 1
	if(minuto_i == 61):
		minuto_i = 1
while(segundo_i != segundo_f):
	ctr_s += 1
	segundo_i += 1

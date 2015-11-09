# _*_ coding: utf-8 _*_
import re
f1 = open("/passengerForecast/oriData/gd_line_desc.txt",'r');
try:
	gd_line_desc = f1.read();
finally:
	f1.close()
	print('%s' % gd_line_desc)
	str1=re.split('[,\n]',gd_line_desc)
	#str1=gd_line_desc.split(',')
	print('%s' % gd_line_desc.split(','))
	print(str1[2])
	


with open('/passengerForecast/oriData/gd_line_desc_w.txt', 'w') as f:
    f.write('Hello, world!')


f2 = open("/passengerForecast/oriData/gd_weather_report.txt",'r');
try:
	gd_weather_report = f2.read();
finally:
	f2.close();
#	print('%s' % gd_weather_report)

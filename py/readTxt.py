# _*_ coding: utf-8 _*_
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')  
i=1;
with open('/passengerForecast/oriData/gd_line_desc.txt', 'r') as f1:  
    gd_line_desc = f1.readlines();
    result = list()
#    print('%s' % gd_line_desc)
for eachline in gd_line_desc:
	eachlineSplit =eachline.split(',');
	eachlineSplit[0]=i;
	i=i+1;
	eachlineSplit[1] = int(eachlineSplit[1]);
	eachlineSplit[2] = eachlineSplit[2].strip();#默认删除空白符（包括'\n', '\r',  '\t',  ' ')
	if eachlineSplit[2].decode('utf-8')==u'广州市内':
		eachlineSplit[2]=0;
	else:
	 	eachlineSplit[2]=1;
#	print(eachlineSplit[0],eachlineSplit[1],eachlineSplit[2])
	result.append(eachlineSplit)                                  
	# print result 
with open('/passengerForecast/oriData/gd_line_desc_w.txt','w') as f2:
    f2.write('%s'% str(result).replace('[','').replace('],','\n').replace(']','').replace(' ',''))
################################################################################################
with open('/passengerForecast/oriData/test.txt', 'r') as f3:
	gd_train_data = f3.readlines()
	train_reslut = list()
for eachline_train in gd_train_data:
	eachlineSplit =eachline_train.split(',');
	# print(eachlineSplit[1])
	if eachlineSplit[0].decode('utf-8')==u'广州':
		eachlineSplit[0]=1
	else:
		eachlineSplit[0]=0
	a = eachlineSplit[1]
	a.decode("UTF-8")
	b = "哈哈"
	print (b[0])
	# print(a)



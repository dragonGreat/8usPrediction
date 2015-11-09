				Bus passenger volume forecast


2.data handle

	只做参考用，"/" 前后分别对应的是白天和夜里的天气状况，按照官方的说法： “今天白天”是指上午8：00到晚上20：00这12个小时；“今天夜间”指20：00到次日早上8：00这12个小时；“明天”就是指第二天上午8点到第三天上午八点。
   
   2.1 gd_line_desc:
         线路名称：线路1（line_name=1）
   	 线路站点数：24(lineStationNum)
         线路类型：广州市区(lineType=0)，广州佛山跨区域(linetype=1)
   2.2 gd_weather_report
	 日期：Date_time 20140801
         天气状况：白天weatherD/夜间weatherN
         气温:最高（TemperatureMax） 、最低（TemperatureMin）
	 风力：（wind_direction_force_Day）白天、夜间(wind_direction_force_Night)
   2.3 gd_train_data
          使用地：use_city
  	  线路名称：line_name
          刷卡终端ID：terminal_id
          发卡ID：card_id
          发卡地：create_city
          交易时间：Deal_time
  	  卡类型：card_type
   2.4 选手提交的结果 gd_predict.txt
	 线路名称;line_name
  	 日期：Deal_date
	 小时段：Deal_hour
 	 乘车人次：passenger_count (长整型：bigint)
         例子：线路10，20150101，10，12
  

1.some thing to know

title:
本次大赛要求选手根据广州市内及广佛同城公交线路的历史公交刷卡数据，挖掘固定人群在公共交通中的行为模式。建立公交线路乘车人次预测模型，并用模型预测未来一周每日6:00至21:00每小时段各个线路的乘车人次。Part2将更换一批新数据。

大赛开放20140801至20141231五个月广东部分公交线路岭南通用户刷卡数据，共涉及近200万用户2条线路约800多万条数据记录。同时大赛提供20140801至20150131期间广州市的天气状况信息。


评估指标：
评估指标的设计主要期望选手对未来一周每天6：00至21:00每个小时段各个线路乘车人次的总量数据预测的越准越好，积分公式的计算方法：计算每天每个小时段各个线路预测值的相对误差，然后根据用户预测乘车人次的相对误差，通过得分函数映射得到每个预测记录的得分，最后将所有预测记录得分求和除以理想状况的满分，得到最终评分。



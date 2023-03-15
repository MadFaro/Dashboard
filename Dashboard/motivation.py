import datetime, time




class m_pp:
	def KO(ko_pp):
		if float(ko_pp) > float(96.6):
			ko_pp_i = 100
		elif float(ko_pp) >= float(90):
			ko_pp_i = 75
		elif float(ko_pp) >= float(86.6):
			ko_pp_i = 50
		else:
			ko_pp_i = 0
		return ko_pp_i

	def aht_pp(aht_pp):
		if datetime.datetime.strptime(aht_pp, '%H:%M:%S') == datetime.datetime.strptime("00:00:00", '%H:%M:%S'):
			aht_pp_i = 0	
		elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:08:30", '%H:%M:%S'):
			aht_pp_i = 100
		elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:09:30", '%H:%M:%S'):
			aht_pp_i = 75
		elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:10:30", '%H:%M:%S'):
			aht_pp_i = 50
		else:
			aht_pp_i = 0
		return aht_pp_i

	def aht(aht_not_pp):
		if datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') == datetime.datetime.strptime("00:00:00", '%H:%M:%S'):
			aht_not_pp_i = 0		
		elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:04:30", '%H:%M:%S'):
			aht_not_pp_i = 100
		elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:05:30", '%H:%M:%S'):
			aht_not_pp_i = 75
		elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:06:30", '%H:%M:%S'):
			aht_not_pp_i = 50
		else:
			aht_not_pp_i = 0
		return aht_not_pp_i

	def pp(pp_pp):
		if float(pp_pp) >= float(57):
			pp_i = 100
		elif float(pp_pp) >= float(52):
			pp_i = 75
		elif float(pp_pp) >= float(47):
			pp_i = 50
		else:
			pp_i = 0
		return pp_i

	def csat(csat_pp):
		if float(csat_pp) >= float(94):
			csat_pp_i = 100
		elif float(csat_pp) >= float(93):
			csat_pp_i = 75
		elif float(csat_pp) >= float(92):
			csat_pp_i = 50
		else:
			csat_pp_i = 0
		return csat_pp_i

class premia:
	def PP(greid_pp, ko_pp, aht_pp, aht_not_pp, pp_pp, csat_pp, abn_pp, last_pp, reg_pp, test_pp, error1, error2, error3, error4):
# Качество обслуживания
		try:
			if float(ko_pp) > float(96.6) and int(greid_pp) <= 1:
				ko_pp_i = 6000
			elif float(ko_pp) > float(96.6) and int(greid_pp) > 1:
				ko_pp_i = 7000
			elif float(ko_pp) >= float(90) and int(greid_pp) <= 1:
				ko_pp_i = 4500
			elif float(ko_pp) >= float(90) and int(greid_pp) > 1:
				ko_pp_i = 5250
			elif float(ko_pp) >= float(86.6) and int(greid_pp) <= 1:
				ko_pp_i = 3000
			elif float(ko_pp) >= float(86.6) and int(greid_pp) > 1:
				ko_pp_i = 3500
			else:
				ko_pp_i = 0
		except:
			ko_pp_i = 0

	# AHT по ПП
		try:
			if datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:08:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_pp_i = 1200
			elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:08:30", '%H:%M:%S') and int(greid_pp) > 1:
				aht_pp_i = 1400
			elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:09:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_pp_i = 900
			elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:09:30", '%H:%M:%S') and int(greid_pp) > 1:
				aht_pp_i = 1050
			elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:10:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_pp_i = 600
			elif datetime.datetime.strptime(aht_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:10:30", '%H:%M:%S') and int(greid_pp) > 1:
				aht_pp_i = 700
			else:
				aht_pp_i = 0
		except:
			aht_pp_i = 0

	# AHT без ПП
		try:
			if datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:04:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_not_pp_i = 1800
			elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:04:30", '%H:%M:%S') and int(greid_pp) > 1:
				aht_not_pp_i = 2100
			elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:05:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_not_pp_i = 1350
			elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:05:30", '%H:%M:%S') and int(greid_pp)	> 1:
				aht_not_pp_i = 1575
			elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:06:30", '%H:%M:%S') and int(greid_pp) <= 1:
				aht_not_pp_i = 900
			elif datetime.datetime.strptime(aht_not_pp, '%H:%M:%S') <= datetime.datetime.strptime("00:06:30", '%H:%M:%S') and int(greid_pp) > 1:
				aht_not_pp_i = 1050
			else:
				aht_not_pp_i = 0
		except:
			aht_not_pp_i = 0

	# Эффективность по ПП
		try:
			if float(pp_pp) >= float(57) and int(greid_pp) <= 1:
				pp_i = 1800
			elif float(pp_pp) >= float(57) and int(greid_pp) > 1:
				pp_i = 2100
			elif float(pp_pp) >= float(52) and int(greid_pp) <= 1:
				pp_i = 1350
			elif float(pp_pp) >= float(52) and int(greid_pp) > 1:
				pp_i = 1575
			elif float(pp_pp) >= float(47) and int(greid_pp) <= 1:
				pp_i = 900
			elif float(pp_pp) >= float(47) and int(greid_pp) > 1:
				pp_i = 1050
			else:
				pp_i = 0
		except:
			pp_i = 0

	# CSAT
		try:
			if float(csat_pp) >= float(94) and int(greid_pp) <= 1:
				csat_pp_i = 1200
			elif float(csat_pp) >= float(94) and int(greid_pp) > 1:
				csat_pp_i = 1400
			elif float(csat_pp) >= float(93) and int(greid_pp) <= 1:
				csat_pp_i = 900
			elif float(csat_pp) >= float(93) and int(greid_pp) > 1:
				csat_pp_i = 1050
			elif float(csat_pp) >= float(92) and int(greid_pp) <= 1:
				csat_pp_i = 600
			elif float(csat_pp) >= float(92) and int(greid_pp) > 1:
				csat_pp_i = 700
			else:
				csat_pp_i = 0
		except:
			csat_pp_i = 0

	# Пропущенные
		try:
			abn_pp_i = int(abn_pp) * 100
		except:
			abn_pp_i = 0

	# Опоздания
		try:
			last_pp_i = int(last_pp) * 100
		except:
			last_pp_i = 0

	# Регистрация
		try:
			if float(reg_pp) < float(95):
				reg_pp_i = (ko_pp_i+aht_pp_i+aht_not_pp_i+pp_i+csat_pp_i)*0.05
			else:
				reg_pp_i = 0
		except:
			reg_pp_i = 0

	# Тестирование
		try:
			if float(test_pp) < float(100):
				test_pp_i = (ko_pp_i+aht_pp_i+aht_not_pp_i+pp_i+csat_pp_i)*0.03
			else:
				test_pp_i = 0
		except:
			test_pp_i = 0

	# Ошибки в отзывах
		try:
			otziv_pp_i = int(error1) * 300
		except:
			otziv_pp_i = 0

	# Ошибки в заявках
		try:
			zaivki_pp_i = (ko_pp_i+aht_pp_i+aht_not_pp_i+pp_i+csat_pp_i)*(int(error2)*0.3)
		except:
			zaivki_pp_i = 0

	# Ошибки в ПП
		try:
			error_pp_i = int(error3) * 100
		except:
			error_pp_i = 0

	# Ошибки ACW
		try:
			error_acw_i = (ko_pp_i+aht_pp_i+aht_not_pp_i+pp_i+csat_pp_i)*(int(error4)*0.05)
		except:
			error_acw_i = 0

		return str(ko_pp_i+aht_pp_i+aht_not_pp_i+pp_i+csat_pp_i-abn_pp_i-last_pp_i-reg_pp_i-test_pp_i-otziv_pp_i-zaivki_pp_i-error_pp_i-error_acw_i)
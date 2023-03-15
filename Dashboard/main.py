import pandas as pd
import datetime, time, os
from db import BotDB
from index import gpso
from html_css import css
from function import sql
from pywebio.pin import *
from sqlite3 import connect
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_js
from motivation import m_pp, premia
from pywebio import start_server, config




# Цвета заливки
color = {100: '#0da9b5', 75 : '#ff8800', 50: '#e41515', 0: '#DC143C'}
# БД
BotDS = BotDB('db/GPSO.db')

#Авторизация
@config(theme = 'sketchy', css_style = css.container_output)
async def main():
    try:
        id_select = await input_group("Вход",
                                     [
                                        input('Логин', name='tab'),
                                        input('Пароль', name='password', type=PASSWORD)
                                    ])
        tab = int(id_select['tab'])
        password = id_select['password']
        rezult = BotDS.user_exists(ID=tab)

        if rezult == False:
            BotDS.add_log(tab=tab, tip='Error')
            toast('Для получения доступа обратись к своему ГС', 
                                        duration=0, 
                                        position='center', 
                                        color='error', onclick=lambda :run_js('window.location.reload()'))
        elif rezult == True and BotDS.get_user_pass(ID=tab) == password:
            BotDS.add_log(tab=tab, tip='login')
            toast('Обновление 1 раз в день к 11:00', duration=5, position='center', color='error')
            await gpso_pp(tab=tab, dated='деф', mon='деф')         
        else:
            BotDS.add_log(tab=tab, tip='Error')
            toast('Неверный пароль', 
                                        duration=0, 
                                        position='center', 
                                        color='error', onclick=lambda :run_js('window.location.reload()'))

    except:
        clear()
        toast('Error, обратись к своему ГС', 
                                        duration=0, 
                                        position='center', 
                                        color='error', onclick=lambda :run_js('window.location.reload()'))

# Основная страница
async def gpso_pp(tab, dated, mon):
    try:
        clear()
    except:
        pass

    if dated == 'деф':
        dfd = pd.read_sql(sql.sql_gpsod.replace('замена', str(tab)), connect("Convert/db/GPSO.db"))
    else:
        dfd = pd.read_sql(sql.sql_gpsodd.replace('замена', str(tab)).replace('дата', str(dated)[0:10]), connect("Convert/db/GPSO.db"))
        if dfd.empty == True or dfd.loc[0]["ФИО"] == None:
            toast('Дата отсутствует в БД', duration=2, position='center', color='error')
            dfd = pd.read_sql(sql.sql_gpsod.replace('замена', str(tab)), connect("Convert/db/GPSO.db"))
        else:
            dfd = pd.read_sql(sql.sql_gpsodd.replace('замена', str(tab)).replace('дата', str(dated)[0:10]), connect("Convert/db/GPSO.db"))

    if mon == 'деф':
        df = pd.read_sql(sql.sql_gpsom.replace('замена', str(tab)).replace('номер', '2'), connect("Convert/db/GPSO.db"))
    else:
        BotDS.add_log(tab=tab, tip='last')
        df = pd.read_sql(sql.sql_gpsom.replace('замена', str(tab)).replace('номер', '1'), connect("Convert/db/GPSO.db"))

    if df.empty == True or df.loc[0]["ФИО"] == None:
        toast('Error - Нет данных', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
    else:
        fio = df.loc[0]["ФИО"] if df.loc[0]["ФИО"] != None else 'Нет данных'
        ko = float(str(df.loc[0]["КО"])[0:5]) if df.loc[0]["КО"] != None else 'Нет данных'
        nps = float(str(float(df.loc[0]["Регистрация"])*100)[0:5]) if df.loc[0]["Регистрация"] != None else 0
        pp_calls = int(df.loc[0]["Принято ПП"]) if df.loc[0]["Принято ПП"] != None else 0
        pp_eff = float(str(float(df.loc[0]["Эффективность"])*100)[0:5]) if df.loc[0]["Эффективность"] != None else 'Нет данных'
        pp_aht = df.loc[0]["АНТ по ПП"][0:8] if df.loc[0]["АНТ по ПП"] != None else 'Нет данных'
        aht_not = df.loc[0]["АНТ без ПП"][0:8] if df.loc[0]["АНТ без ПП"] != None else 'Нет данных'
        ring = float(str(df.loc[0]['Ринг'])[0:4]) if df.loc[0]["Ринг"] != None else 0
        hold = float(str(float(df.loc[0]["Холд"])*100)[0:5]) if df.loc[0]["Холд"] != None else 0
        calls = int(df.loc[0]["Принятые"]) if df.loc[0]["Принятые"] != None else 0
        noans = int(df.loc[0]["Пропущенные"]) if df.loc[0]["Пропущенные"] != None else 0
        acw = float(str(float(df.loc[0]["АСВ"])*100)[0:5]) if df.loc[0]["АСВ"] != None else 0
        opros = float(str(float(df.loc[0]["Опросы"])*100)[0:5]) if df.loc[0]["Опросы"] != None else 0
        csat = float(str(float(df.loc[0]["КСАТ"])*100)[0:5]) if df.loc[0]["КСАТ"] != None else 'Нет данных'
        odsat = float(str(float(df.loc[0]["ОДСАТ"])*100)[0:5]) if df.loc[0]["ОДСАТ"] != None else 0
        test = float(str(float(df.loc[0]["Тест"])*100)[0:4]) if df.loc[0]["Тест"] != None else 0
        svzun = str(df.loc[0]["Связуны"]) if df.loc[0]["Связуны"] != None else 0
        mount = str(df.loc[0]["Месяц"]) if df.loc[0]["Месяц"] != None else 'Месяц'
        img = open('img/1.png', 'rb').read() if df.loc[0]["Пол"] == 'М' else open('img/2.png', 'rb').read()

    #Таблица день
        try:
            datad = dfd.loc[0]["Дата"] if dfd.loc[0]["Дата"] != None else 0
            pp_ahtd = dfd.loc[0]["АНТ по ПП"][0:8] if dfd.loc[0]["АНТ по ПП"] != None else 0
            aht_notd = dfd.loc[0]["АНТ без ПП"][0:8] if dfd.loc[0]["АНТ без ПП"] != None else 0
            ringd = float(str(dfd.loc[0]['Ринг'])[0:5]) if dfd.loc[0]["Ринг"] != None else 0
            holdd = float(str(float(dfd.loc[0]["Холд"])*100)[0:5]) if dfd.loc[0]["Холд"] != None else 0
            callsd = int(dfd.loc[0]["Принятые"]) if dfd.loc[0]["Принятые"] != None else 0
            noansd = int(dfd.loc[0]["Пропущенные"]) if dfd.loc[0]["Пропущенные"] != None else 0
            acwd = float(str(float(dfd.loc[0]["АСВ"])*100)[0:5]) if dfd.loc[0]["АСВ"] != None else 0
            oprosd = float(str(float(dfd.loc[0]["Опросы"])*100)[0:5]) if dfd.loc[0]["Опросы"] != None else 0
            csatd = float(str(float(dfd.loc[0]["КСАТ"])*100)[0:5]) if dfd.loc[0]["КСАТ"] != None else 0
            odsatd = float(str(float(dfd.loc[0]["ОДСАТ"])*100)[0:5]) if dfd.loc[0]["ОДСАТ"] != None else 0
        except:
            datad = 'error'
        def dayd(date):
            if date == 'error':
                table = put_table([])
            else:
                table = put_table([
                                [
                                put_button("Назад", 
                                                    onclick=lambda: gpso_pp(
                                                                            tab=tab, 
                                                                            dated=datetime.datetime.strptime(date, '%Y-%m-%d') - datetime.timedelta(days=1), mon=mon), 
                                                    color='primary', 
                                                    outline=True).style('text-align:center;'),
                                put_button("Вперед", 
                                                    onclick=lambda: gpso_pp(
                                                                            tab=tab, 
                                                                            dated=datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=1), mon=mon), 
                                                    color='primary', 
                                                    outline=True).style('text-align:center;'),
                                span(put_text(f'Данные за {date[8:10]}.{date[5:7]}.{date[0:4]}').style('text-align:center;'), col=8)],
                                [
                                put_button("Принято\nзвонков", 
                                                                onclick=lambda: popup("Принятые", gpso.prinatie), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("Пропущено\nзвонков", 
                                                                onclick=lambda: popup("Пропущеные", gpso.noans), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("AHT по ПП\n<=0:09:30", 
                                                                onclick=lambda: popup("АНТ по ПП", gpso.aht_pp), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("AHT без ПП\n<=0:05:00", 
                                                                onclick=lambda: popup("АНТ без ПП", gpso.aht_not), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("Ринг\n<=1,5", 
                                                                onclick=lambda: popup("Ring", gpso.ring), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("Холд\n<=10-15%", 
                                                                onclick=lambda: popup("Hold", gpso.hold), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("ACW\nне более 5%", 
                                                                onclick=lambda: popup("ACW", gpso.acw), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("CSAT\nне менее 94%", 
                                                                onclick=lambda: popup("CSAT", gpso.csat), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("ODSAT\nне более 4,5%", 
                                                                onclick=lambda: popup("ODSAT", gpso.odsat), 
                                                                color='warning', link_style=True, outline=True),
                                put_button("% зап.Опросов\n>= 15%", 
                                                                onclick=lambda: popup("% заполненных опросов", gpso.opros), 
                                                                color='warning', link_style=True, outline=True)
                                ],
                                [
                                put_text(callsd).style('color:#0da9b5;'),
                                put_text(noansd).style(f'color:{"#0da9b5" if noansd == 0 else "#e41515"}'),
                                put_text(pp_ahtd).style(f'color:{"#0da9b5" if datetime.datetime.strptime(pp_ahtd, "%H:%M:%S") <= datetime.datetime.strptime("00:09:30", "%H:%M:%S") else "#e41515"}'), 
                                put_text(aht_notd).style(f'color:{"#0da9b5" if datetime.datetime.strptime(aht_notd, "%H:%M:%S") <= datetime.datetime.strptime("00:05:30", "%H:%M:%S") else "#e41515"}'), 
                                put_text(ringd).style(f'color:{"#0da9b5" if ringd <= 1.5 else "#e41515"}'), 
                                put_text(f"{holdd}%").style(f'color:{"#0da9b5" if holdd <= 15.0 else "#e41515"}'), 
                                put_text(f"{acwd}%").style(f'color:{"#0da9b5" if acwd <= 5.0 else "#e41515"}'),
                                put_text(f"{csatd}%").style(f'color:{"#0da9b5" if csatd >= 94.0 else "#e41515"}'),
                                put_text(f"{odsatd}%").style(f'color:{"#0da9b5" if odsatd <= 4.5 else "#e41515"}'), 
                                put_text(f"{oprosd}%").style(f'color:{"#0da9b5" if oprosd >= 15.0 else "#e41515"}'), 
                                ]])
            return table
    # КО
        if ko == 'Нет данных' or calls == 0:
            tab_ko = put_tabs([{'title': 'КО', 'content':[
                            put_row([
                            put_text(f'Нет данных').style(f'color:black;font-size:1.5vw;text-align:center;'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("Качество обслуживания", gpso.ko), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;')
            ]}])
        else:
            ko_z = m_pp.KO(ko)
            tab_ko = put_tabs([{'title': 'КО >= 96', 'content':[
                        put_column([
                            put_row([
                            put_text(f'{str(ko)}').style(f'color:{color.get(ko_z)};font-size:1.5vw;text-align:center;'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("Качество обслуживания", gpso.ko), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;'),None,
                            put_processbar('bar', 
                                            ko_z/100,
                                            auto_close=False, 
                                            color=color.get(ko_z)).style('height:100%;font-size:1.5vw;')]).style('margin-top:6.5%;')
                                                        ]}])

    # AHT без ПП
        if aht_not == 'Нет данных' or aht_not == '00:00:00':
            tab_aht_not = put_tabs([{'title': 'AHT без ПП', 'content':[
                            put_row([
                            put_text(f'Нет данных').style(f'color:black;font-size:1.5vw;text-align:center;'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("АНТ без ПП", gpso.aht_not), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;')
            ]}])
        else:
            aht_r = m_pp.aht(aht_not)
            tab_aht_not = put_tabs([{'title': 'AHT без ПП <= 0:04:30', 'content':[
                        put_column([
                            put_row([
                            put_text(f'{str(aht_not)}').style(f'color:{color.get(aht_r)};font-size:1.5vw;text-align:center'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("АНТ без ПП", gpso.aht_not), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;'),None,
                            put_processbar('bar', 
                                            aht_r/100, 
                                            auto_close=False, 
                                            color=color.get(aht_r)).style('height:100%;font-size:1.5vw;')]).style('margin-top:6.5%;')]
                                                        }])

    # AHT по сплиту ПП
        if pp_aht == 'Нет данных' or pp_aht == '00:00:00':
            tab_aht_pp = put_tabs([{'title': 'AHT по ПП', 'content':[
                                put_row([
                                put_text(f'Нет данных').style(f'color:black;font-size:1.5vw;text-align:center;'),None,
                                put_button(">>>", 
                                            onclick=lambda: popup("АНТ по ПП", gpso.aht_pp), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;')
            ]}])
        else:
            aht_rp = m_pp.aht_pp(pp_aht)
            tab_aht_pp = put_tabs([{'title': 'AHT по ПП <= 0:08:30', 'content':[
                            put_column([
                                put_row([
                                put_text(f'{str(pp_aht)}').style(f'color:{color.get(aht_rp)};font-size:1.5vw;text-align:center'),None,
                                put_button(">>>", 
                                            onclick=lambda: popup("АНТ по ПП", gpso.aht_pp), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;'),None,
                                put_processbar('bar', 
                                            aht_rp/100, 
                                            auto_close=False, 
                                            color=color.get(aht_rp)).style('height:100%;font-size:1.5vw;')]).style('margin-top:6.5%;')
                                                            ]}])

    # Эффективность работы с ПП
        if pp_eff == 'Нет данных' or pp_calls == 0:
            tab_pp = put_tabs([{'title': 'Эффект.ПП', 'content':[
                            put_row([
                            put_text(f'Нет данных').style(f'color:black;font-size:1.5vw;text-align:center;'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("Эффективность работы с ПП", gpso.pp_ef), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;')
            ]}])
        else:
            rp = m_pp.pp(float(pp_eff))
            tab_pp = put_tabs([{'title': 'Эффект.ПП >= 57%', 'content':[
                        put_column([
                            put_row([
                            put_text(f'{str(float(pp_eff))}%').style(f'color:{color.get(rp)};font-size:1.5vw;text-align:center'),None,
                            put_button(">>>", 
                                            onclick=lambda: popup("Эффективность работы с ПП", gpso.pp_ef), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;'),None,
                            put_processbar('bar', 
                                            rp/100, 
                                            auto_close=False, 
                                            color=color.get(rp)).style('height:100%;font-size:1.5vw;')]).style('margin-top:6.5%;')
                                                        ]}])

    # Csat
        if csat == 'Нет данных' or calls == 0:
            tab_csat = put_tabs([{'title': 'CSAT', 'content':[
                                put_row([
                                put_text(f'Нет данных').style(f'color:black;font-size:1.5vw;text-align:center;'),None,
                                put_button(">>>", 
                                            onclick=lambda: popup("CSAT", gpso.csat), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;')
            ]}])
        else:
            csat_r = m_pp.csat(float(csat))
            tab_csat = put_tabs([{'title': 'CSAT >= 94%', 'content':[
                            put_column([
                                put_row([
                                put_text(f'{str(float(csat))}%').style(f'color:{color.get(csat_r)};font-size:1.5vw;text-align:center'),None,
                                put_button(">>>", 
                                            onclick=lambda: popup("CSAT", gpso.csat), 
                                            color='warning', 
                                            link_style=True, 
                                            outline=True).style('position:absolute;top:1%;right:5%;filter:opacity(0.5);')]).style('grid-template-columns:1fr;'),None,
                                put_processbar('bar', 
                                            csat_r/100, 
                                            auto_close=False, 
                                            color=color.get(csat_r)).style('height:100%;font-size:1.5vw;')]).style('margin-top:6.5%;')
                                                            ]}])

# Расположение:
        put_button(fio, 
                        onclick=lambda: run_js('window.location.reload()'), 
                        color='info').style('position:absolute;left:0%;top:1%;z-index:2147483647')
        if mon == 1:
            put_button(f'Показатели за {mount}' , 
                                                    onclick=lambda: gpso_pp(tab, dated=dated, mon='деф'), 
                                                    color='danger').style('position:absolute;right:0%;top:1%;z-index:2147483647;')
        else:
            put_button(f'Показатели за {mount}' , 
                                                    onclick=lambda: gpso_pp(tab, dated=dated, mon=1), 
                                                    color='danger').style('position:absolute;right:0%;top:1%;z-index:2147483647;')
        put_row([
            #Сайд бар
            put_widget(css.tpl, {'contents':[
                put_row([
            put_button(" Премия  ", 
                                                    onclick=lambda: premia_gpso_pp(tab, ko, nps, pp_eff, pp_aht, aht_not, noans, csat), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:76%;'), None,
            put_button("Связуны  ", 
                                                    onclick=lambda: svz(tab, svzun, img), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:82%;'), None,
            put_button("Обновить", 
                                                    onclick=lambda: gpso_pp(tab=tab, dated='деф', mon='деф'), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:88%;'), None,
            put_image(img).style('background:#051f23;border-radius:100px;position:absolute;width:50%;left:24%;top:15%;font-size:1vw;')])]
                                }).style('position:relative;background:#051f23;z-index:1;filter: drop-shadow(1px 2px 3px #051f23);'), None,
            #Основной контент
            put_column([
                None,
            put_row([
                tab_ko, None, tab_pp, None, tab_csat, None, tab_aht_not, None, tab_aht_pp], 
                size='1fr 0.1fr 1fr 0.1fr 1fr 0.1fr 1fr 0.1fr 1fr').style('font-size:1vw'), None,                                
            put_table([
                    [span(f'Показатели за {mount}', col=10)],
                    [
                    put_button("Принято\nзвонков", 
                                                    onclick=lambda: popup("Принятые", gpso.prinatie), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("Принято\nПП", 
                                                    onclick=lambda: popup("Принятые ПП", gpso.prinatie_pp), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("Пропущено\nзвонков", 
                                                    onclick=lambda: popup("Пропущеные", gpso.noans), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("Ринг\n<=1,5", 
                                                    onclick=lambda: popup("Ring", gpso.ring), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("Холд\n<=10-15%", 
                                                    onclick=lambda: popup("Hold", gpso.hold), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("ACW\nне более 5%", 
                                                    onclick=lambda: popup("ACW", gpso.acw), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("% зап.Опросов\n>= 15%", 
                                                    onclick=lambda: popup("% заполненных опросов", gpso.opros), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("ODSAT\nне более 4,5%", 
                                                    onclick=lambda: popup("ODSAT", gpso.odsat), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("%регистрации\nне менее 95%", 
                                                    onclick=lambda: popup("% Регистрации звонков", gpso.reg), 
                                                    color='warning', link_style=True, outline=True),
                    put_button("Тестирование\nне менее 100%", 
                                                    onclick=lambda: popup("Тестирование", gpso.test_pp), 
                                                    color='warning', link_style=True, outline=True)
                    ],
                    [
                    put_text(calls).style('color:#0da9b5;'),
                    put_text(pp_calls).style('color:#0da9b5;'),
                    put_text(noans).style(f'color:{"#0da9b5" if noans == 0 else "#e41515"}'), 
                    put_text(ring).style(f'color:{"#0da9b5" if ring <= 1.5 else "#e41515"}'),
                    put_text(f"{hold}%").style(f'color:{"#0da9b5" if hold <= 15.0 else "#e41515"}'), 
                    put_text(f"{acw}%").style(f'color:{"#0da9b5" if acw <= 5.0 else "#e41515"}'), 
                    put_text(f"{opros}%").style(f'color:{"#0da9b5" if opros >= 15.0 else "#e41515"}'), 
                    put_text(f"{odsat}%").style(f'color:{"#0da9b5" if odsat <= 4.5 else "#e41515"}'), 
                    put_text(f"{nps}%").style(f'color:{"#0da9b5" if nps >= 95.0 else "#e41515"}'), 
                    put_text(f"{test}%").style(f'color:{"#0da9b5" if test == 100.0 else "#e41515"}'),

                    ]]).style('text-align:center;display:table;'), None,
            dayd(datad).style('text-align:center;display:table')
                    ], size='6% 28% 7% 26% 2% 26%')], 
                    size='9% 5% 81%').style('position: absolute;width: 100%;height: 100%;')

# Расчет премии для ПП
async def premia_gpso_pp(tab, ko, nps, pp_eff, pp_aht, aht_not, noans, csat):
    def check(AHT):
        try:
            datetime.datetime.strptime(AHT, '%H:%M:%S')
        except:
            return 'Неверный формат'
    try:
        clear()
        info = await input_group("Отредактируй\Заполни поля ниже",[
                    input(name = 'Greid', type=NUMBER, label='Грейд', value=1),
                    input(name = 'KO', type=FLOAT, label='KO', value=ko),
                    input(name = 'AHT_PP', type=TEXT, label='AHT по ПП', value=pp_aht, validate=check),
                    input(name = 'AHT', type=TEXT, label='AHT без ПП', value=aht_not, validate=check),
                    input(name = 'EF', type=FLOAT, label='Эффективность по ПП', value=pp_eff),
                    input(name = 'CSAT', type=FLOAT, label='CSAT', value=csat),
                    input(name = 'noans', type=NUMBER, label='Пропущенные', value=noans),
                    input(name = 'last', type=NUMBER, label='Опоздание', value=0),
                    input(name = 'reg', type=FLOAT, label='% регистрации', value=nps),
                    input(name = 'test', type=FLOAT, label='Тестирование', value=100.0),
                    input(name = 'error1', type=NUMBER, label='Ошибка в отзывах', value=0),
                    input(name = 'error2', type=NUMBER, label='Ошибки в заявках', value=0),
                    input(name = 'error3', type=NUMBER, label='Ошибки ПП', value=0),
                    input(name = 'error4', type=NUMBER, label='Ошибки ACW', value=0)
                    ])

        BotDS.add_log(tab=tab, tip='premia')
        
        data = premia.PP(
                            info['Greid'], 
                            info['KO'], 
                            info['AHT_PP'], 
                            info['AHT'], 
                            info['EF'], 
                            info['CSAT'], 
                            info['noans'], 
                            info['last'], 
                            info['reg'], 
                            info['test'], 
                            info['error1'], 
                            info['error2'], 
                            info['error3'], 
                            info['error4'])

        proc = float(data) / (12000.0 if info['Greid'] == 1 else 14000.0)

        if proc == 1:
            color = '#0da9b5'
        elif proc >= 0.75:
            color = '#ff8800'
        elif proc <= 0.75 and proc >= 0.5:
            color = '#e41515'
        else:
            color = '#DC143C'

        popup('Премия', [
            put_html('<h3>Премия без учета отработанных дней<BR>И ошибок, которые вносят ГС</h3>'),
            put_html(f'<h3>{data}</h3>').style(f'text-align: center;color:{color};font-size: 1.5vw;'),
            put_processbar('bar', proc, auto_close=False, color=color).style('height: 3rem;font-size: 1.5vw;')])
        await gpso_pp(tab=tab, dated='деф', mon='деф')
    except:
        toast('Error - что то пошло не по плану:(', duration=0, position='center', color='error', onclick=lambda :run_js('window.location.reload()'))
        

async def svz(tab, svzun, img):
    try:
        clear()
    except:
        pass
    BotDS.add_log(tab=tab, tip='svazyn')
    dfd = pd.read_sql(sql.sql_tovar, connect("Convert/db/GPSO.db"))
    # Расположение:
    if BotDS.get_user_mot(ID=tab) == 'ПП':
        butt = put_button(" Назад  ", 
                                                    onclick=lambda: gpso_pp(tab=tab, dated='деф', mon='деф'), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:88%;')
    elif BotDS.get_user_mot(ID=tab) == 'НП':
        butt = put_button(" Назад  ", 
                                                    onclick=lambda: gpso_not_pp(tab=tab, dated='деф', mon='деф'), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:88%;')
    elif BotDS.get_user_mot(ID=tab) == 'ГОП':
        butt = put_button(" Назад  ", 
                                                    onclick=lambda: gop(tab=tab, dated='деф', mon='деф'), 
                                                    color='info', outline=True).style('position:absolute;left:23%;top:88%;')
    else:
        pass
    def sql_2(p):
        df = pd.read_sql(sql.sql_tov.replace('Замена', str(p)), connect("Convert/db/GPSO.db"))
        return df.loc[0]['Подробное описание']

    put_button(f'Доступно для списания {svzun}', 
                                                    onclick=lambda: run_js('window.location.reload()'), 
                                                    color='info').style('position:absolute;left:0%;top:1%;z-index:2147483647;')
    put_row([
            #Сайд бар
            put_widget(css.tpl, {'contents':[
                put_row([
            butt, None,
            put_image(img).style('background:#051f23;border-radius:100px;position:absolute;width:50%;left:24%;top:15%;font-size:1vw;')])]
                                }).style('position:relative;background:#051f23;z-index:1;filter: drop-shadow(1px 2px 3px #051f23);height:100%;'), None,
            #Основной контент
            put_column([
                put_table([
                    [span('№', col = 1), span(f'Позиция', col = 1), span('Можно списать', col = 1)],
                    [put_button(dfd.loc[0]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[0]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[0]['Позиция'], 
                                put_text(dfd.loc[0]['Можно списать']).style(f"color:{'green' if int(dfd.loc[0]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[1]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[1]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[1]['Позиция'], 
                                put_text(dfd.loc[1]['Можно списать']).style(f"color:{'green' if int(dfd.loc[1]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[2]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[2]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[2]['Позиция'], 
                                put_text(dfd.loc[2]['Можно списать']).style(f"color:{'green' if int(dfd.loc[2]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[3]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[3]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[3]['Позиция'], 
                                put_text(dfd.loc[3]['Можно списать']).style(f"color:{'green' if int(dfd.loc[3]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[4]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[4]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[4]['Позиция'], 
                                put_text(dfd.loc[4]['Можно списать']).style(f"color:{'green' if int(dfd.loc[4]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[5]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[5]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[5]['Позиция'], 
                                put_text(dfd.loc[5]['Можно списать']).style(f"color:{'green' if int(dfd.loc[5]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[6]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[6]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[6]['Позиция'], 
                                put_text(dfd.loc[6]['Можно списать']).style(f"color:{'green' if int(dfd.loc[6]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[7]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[7]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[7]['Позиция'], 
                                put_text(dfd.loc[7]['Можно списать']).style(f"color:{'green' if int(dfd.loc[7]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[8]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[8]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[8]['Позиция'], 
                                put_text(dfd.loc[8]['Можно списать']).style(f"color:{'green' if int(dfd.loc[8]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[9]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[9]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[9]['Позиция'], 
                                put_text(dfd.loc[9]['Можно списать']).style(f"color:{'green' if int(dfd.loc[9]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[10]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[10]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[10]['Позиция'], 
                                put_text(dfd.loc[10]['Можно списать']).style(f"color:{'green' if int(dfd.loc[10]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[11]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[11]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[11]['Позиция'], 
                                put_text(dfd.loc[11]['Можно списать']).style(f"color:{'green' if int(dfd.loc[11]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[12]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[12]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[12]['Позиция'], 
                                put_text(dfd.loc[12]['Можно списать']).style(f"color:{'green' if int(dfd.loc[12]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[13]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[13]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[13]['Позиция'], dfd.loc[13]['Можно списать']],
                    [put_button(dfd.loc[14]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[14]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[14]['Позиция'], 
                                put_text(dfd.loc[14]['Можно списать']).style(f"color:{'green' if int(dfd.loc[14]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[15]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[15]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[15]['Позиция'], 
                                put_text(dfd.loc[15]['Можно списать']).style(f"color:{'green' if int(dfd.loc[15]['Можно списать']) <= int(svzun) else 'red'}")],
                    [put_button(dfd.loc[16]['№'], 
                                                onclick=lambda: popup("Подробное описание", sql_2(str(dfd.loc[16]['№']))), 
                                                color='primary', 
                                                outline=True), 
                                dfd.loc[16]['Позиция'], 
                                put_text(dfd.loc[16]['Можно списать']).style(f"color:{'green' if int(dfd.loc[16]['Можно списать']) <= int(svzun) else 'red'}")]

                ]).style('position:absolute;top:2%;width:70%;height:98%;left:20%;text-align:center;')


                    ])], 
                    size='9% 5% 81%').style('position:absolute;width:100%;height:100%;')


if __name__ == '__main__':
    start_server(main, host = '10.9.16.219', port = 8080, debug=True, cdn=True)
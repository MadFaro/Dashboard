class sql:
    sql_gpsom = """
     SELECT
       a.tab as [Табельный],
       a.fio_ko as [ФИО],
       a.pol as [Пол],
       a.sdep as [Мотивация],
       b."Unnamed: 1" as [КО],
       C."Unnamed: 1" as [Регистрация],
       d."Unnamed: 1" as [Принято ПП],
       d."Unnamed: 2" as [Эффективность],
       f."Unnamed: 2" as [АНТ по ПП],
       f."Unnamed: 3" as [АНТ без ПП],
       f."Unnamed: 4" as [АНТ],
       f."Unnamed: 5" as [Ринг],
       f."Unnamed: 6" as [Холд],
       f."Unnamed: 7" as [Принятые],
       f."Unnamed: 8" as [Пропущенные],
       f."Unnamed: 9" as [АСВ],
       f."Unnamed: 12" as [Опросы],
       f."Unnamed: 13" as [КСАТ],
       f."Unnamed: 14" as [ОДСАТ],
       f."Unnamed: 15" as [ВДСАТ],
       e."Unnamed: 6" as [Тест],
       j.Итого as [Связуны],
       f.B as [Месяц]
       
  FROM users as a
  left join KO as b on a.fio_ko = b.ФИО and b.A = 'номер'
  left join NPS as c on a.fio_nps = c.Дата and c.A = 'номер'
  left join PP as d on a.fio_pp = d.ФИО and d.A = 'номер'
  left join TD_GPSOM as f on a.login = f."Фамилия Имя" and f.A = 'номер'
  left join Test as e on a.fio_ko = e."Unnamed: 1" and e.A = 'номер'
  left join svz as j on a.fio_pp = j."Фамилия Имя"
  Where a.tab = 'замена'
  Order by f."Unnamed: 7" desc
  Limit 1
    """

    sql_gpsod = """
	SELECT
       a.tab as [Табельный],
       a.fio_ko as [ФИО],
       a.sdep as [Мотивация],
       b."Unnamed: 2" as [АНТ по ПП],
       b."Unnamed: 3" as [АНТ без ПП],
       b."Unnamed: 4" as [АНТ],
       b."Unnamed: 5" as [Ринг],
       b."Unnamed: 6" as [Холд],
       b."Unnamed: 7" as [Принятые],
       b."Unnamed: 8" as [Пропущенные],
       b."Unnamed: 9" as [АСВ],
       b."Unnamed: 12" as [Опросы],
       b."Unnamed: 13" as [КСАТ],
       b."Unnamed: 14" as [ОДСАТ],
       b."Unnamed: 15" as [ВДСАТ],
       b.created as [Дата]
  FROM users as a
  left join TD_GPSOD as b on a.login = b."Фамилия Имя" and b."Unnamed: 7" != 0
  Where a.tab = 'замена' and b."Unnamed: 7" not null
  Order by b.created desc
  Limit 1
    """

    sql_gpsodd = """
	SELECT
       a.tab as [Табельный],
       a.fio_ko as [ФИО],
       a.sdep as [Мотивация],
       b."Unnamed: 2" as [АНТ по ПП],
       b."Unnamed: 3" as [АНТ без ПП],
       b."Unnamed: 4" as [АНТ],
       b."Unnamed: 5" as [Ринг],
       b."Unnamed: 6" as [Холд],
       b."Unnamed: 7" as [Принятые],
       b."Unnamed: 8" as [Пропущенные],
       b."Unnamed: 9" as [АСВ],
       b."Unnamed: 12" as [Опросы],
       b."Unnamed: 13" as [КСАТ],
       b."Unnamed: 14" as [ОДСАТ],
       b."Unnamed: 15" as [ВДСАТ],
       b.created as [Дата]
  FROM users as a
  left join TD_GPSOD as b on a.login = b."Фамилия Имя"
  Where b.created = 'дата' and a.tab = 'замена'
  Order by b."Unnamed: 7" desc
  Limit 1
    """ 

    sql_tovar = """
        SELECT 
              №,
              Позиция,
              "Подробное описание",
              "Можно списать"
          FROM tovar;
    """
    sql_tov = """
        SELECT 
              "Подробное описание"
          FROM tovar
          WHERE № = 'Замена'
    """
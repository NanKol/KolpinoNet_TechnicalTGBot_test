"""Запросы и функции для взаимодействия с БД"""
import pymysql, pymysql.cursors
import aiomysql, aiomysql.cursors
import config


# def get_connect_mysql():
#   conf = config.get_config()['DB']
#   return pymysql.connect(database=conf['db'], 
#                          host=conf['host'],  
#                          port=int(conf['port']), 
#                          user=conf['user'], 
#                          password=conf['password'],
#                          charset="utf8",
#                          cursorclass=pymysql.cursors.DictCursor)


async def get_pool_connection():
  conf = config.get_config()['DB']
  pool = await aiomysql.create_pool(maxsize=2,
                                    database=conf['db'], 
                                    host=conf['host'],  
                                    port=int(conf['port']), 
                                    user=conf['user'], 
                                    password=conf['password'],
                                    charset="utf8",
                                    cursorclass=aiomysql.cursors.DictCursor)
  return pool

# вернуть UNIX_TIMESTAMP(t.date_start) и UNIX_TIMESTAMP(t.date_end) и UNIX_TIMESTAMP(t.plan_time)
search_troubles = """SELECT
                      t.id as tid,
                      UNIX_TIMESTAMP(t.date_start) as date_start,
                      UNIX_TIMESTAMP(t.date_end) as date_end,
                      e.brand,e.model,e.ipaddr,e.comment as ecomment,
                      t.objid,
                      ond.location,
                      t.comment,
                      a.adm_fullname,
                      t.eqid,
                      t.plan,
                      UNIX_TIMESTAMP(t.plan_time) as plan_time
                    FROM troubles as t
                      LEFT JOIN admins as a ON (a.adm_id=t.openadm)
                      LEFT JOIN equipment as e ON (e.id=t.eqid)
                      LEFT JOIN objects as o ON (o.id=t.objid)
                      LEFT JOIN objects_nodes as ond ON (ond.id=t.nodeid)
                    WHERE e.online="FALSE" AND t.date_end=0"""
           
search_trouble = """SELECT
                      t.id as tid,
                      t.date_start as date_start,
                      t.date_end as date_end,
                      e.brand,e.model,e.ipaddr,e.comment as ecomment,
                      t.objid,
                      ond.location,
                      t.comment,
                      a.adm_fullname,
                      t.eqid,
                      t.plan,
                      t.plan_time as plan_time
                    FROM troubles as t
                      LEFT JOIN admins as a ON (a.adm_id=t.openadm)
                      LEFT JOIN equipment as e ON (e.id=t.eqid)
                      LEFT JOIN objects as o ON (o.id=t.objid)
                      LEFT JOIN objects_nodes as ond ON (ond.id=t.nodeid)
                    WHERE e.online="FALSE" AND t.date_end=0 AND {reque_param}"""

# вернуть UNIX_TIMESTAMP(t.date_start) и UNIX_TIMESTAMP(t.date_end) и UNIX_TIMESTAMP(t.plan_time)
background_search_troubles = """SELECT t.id as tid, t.sent2tgm,
                                  UNIX_TIMESTAMP(t.date_start) as date_start,
                                  UNIX_TIMESTAMP(t.date_end) as date_end,
                                  e.brand,e.model,e.ipaddr,e.comment as ecomment,
                                  t.objid,
                                  ond.location,
                                  t.comment,
                                  a.adm_fullname,
                                  t.eqid,
                                  t.plan,
                                  UNIX_TIMESTAMP(t.plan_time) as plan_time
                                FROM troubles as t
                                  LEFT JOIN admins as a ON (a.adm_id=t.openadm)
                                  LEFT JOIN equipment as e ON (e.id=t.eqid)
                                  LEFT JOIN objects as o ON (o.id=t.objid)
                                  LEFT JOIN objects_nodes as ond ON (ond.id=t.nodeid)
                                WHERE (e.online=0 AND t.date_end=0 AND t.sent2tgm=0) OR 
	                                    (e.online=1 AND t.date_end>0 AND t.sent2tgm=1)"""

background_search_troubles_confirm = "UPDATE troubles SET sent2tgm=(sent2tgm + 1) WHERE id=%s"

# вернуть UNIX_TIMESTAMP(t.date_start) и UNIX_TIMESTAMP(t.date_end) и UNIX_TIMESTAMP(t.plan_time)
update_trouble = """SELECT 
                      t.id as tid,
                      UNIX_TIMESTAMP(t.date_start) as date_start,
                      UNIX_TIMESTAMP(t.date_end) as date_end,
                      e.brand,e.model,e.ipaddr,e.comment as ecomment,
                      t.objid,
                      ond.location,
                      t.comment,
                      a.adm_fullname,
                      t.eqid,
                      t.plan,
                      UNIX_TIMESTAMP(t.plan_time) as plan_time
                    FROM troubles as t
                      LEFT JOIN admins as a ON (a.adm_id=t.openadm)
                      LEFT JOIN equipment as e ON (e.id=t.eqid)
                      LEFT JOIN objects as o ON (o.id=t.objid)
                      LEFT JOIN objects_nodes as ond ON (ond.id=t.nodeid)
                    WHERE t.id=%s"""
           
count_troubles = """SELECT COUNT(*) AS count_trouble from troubles as t 
                    LEFT JOIN equipment as e ON (e.id=t.eqid)
                    WHERE e.online="FALSE" AND t.date_end=0"""
        

count_fl = """SELECT  COUNT(*) AS fl FROM equipment_ports AS ep
                LEFT JOIN users_services AS us ON (us.id=ep.serviceid)
                LEFT JOIN users AS u ON (us.uid=u.id)
                WHERE ep.eqid=%s AND ep.porttype!='FREE' AND u.cli_type=0"""


count_yl = """SELECT  COUNT(*) AS yl FROM equipment_ports AS ep
                LEFT JOIN users_services AS us ON (us.id=ep.serviceid)
                LEFT JOIN users AS u ON (us.uid=u.id)
                WHERE ep.eqid=%s AND ep.porttype!='FREE' AND u.cli_type=1"""

                
get_street = """SELECT ost.streettype, os.street,oc.name as cityname FROM objects_streets as os
                  LEFT JOIN objects_streets_types as ost ON (os.streettype=ost.id)
                  LEFT JOIN objects_city as oc ON (oc.id=os.city)
                WHERE os.id={streetid}"""
         
get_street_elm = "SELECT * FROM objects WHERE id={objid} LIMIT 1"
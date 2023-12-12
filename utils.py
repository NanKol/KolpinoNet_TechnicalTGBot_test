"""Внешнии функции"""
import db


def getobjectname(cursor, objid) -> str:
    """Возвращает полный адрес"""
    
    if (int(objid) > 0):
        cursor.execute(db.get_street_elm.format(objid = objid))
        
        rows = cursor.fetchall()
        
        for curobj in rows:
            fulladdr = getstreet(cursor, curobj['street']) + curobj['dom']
            if(len(curobj['korp']) > 0):
                fulladdr += curobj ['korp']
            return fulladdr


def getstreet(cursor, streetid) -> str:
    """Возращает улицу"""
    if (int(streetid) > 0):
        cursor.execute(db.get_street.format(streetid = streetid))
        
        rows = cursor.fetchall()
        
        for currstreet in rows:
            strname = currstreet['cityname'] + ", " + currstreet['street']
            if (len(currstreet['streettype']) > 0):
                    strname += " " + currstreet['streettype']
            return strname

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:24:56 2021

@author: Riyaz
"""

import sys
import random
import sqlite3
from contextlib import closing

conn = sqlite3.connect("criminalRecord.db")
class Criminal:
    
    def AddCRRecord(self,crid,crn,crage,crgndr,cradrs,crcellno,crstat,oid,fid):
        if crid==' ' :
            return '0'
        
        with closing(conn.cursor()) as c:
                insertQuery='insert into CRIMINAL(criminal_id,cr_name,age,gender,address,status,cell_no,officer_id,fir_id) values(?,?,?,?,?,?,?,?,?)'
                c.execute(insertQuery,(crid,crn,crage,crgndr,cradrs,crstat,crcellno,oid,fid))
                conn.commit()
                return '1'
                
            
    def UpCRRecord(self,crid,crstat):
        if crid==' ':
            return 0
        
        with closing(conn.cursor()) as c:
                updateQuery='update CRIMINAL set status =? where criminal_id=?'
                c.execute(updateQuery,(crstat,crid))
                conn.commit()
                return '1'
            
    def ViewCRRecord(self):
        
        with closing(conn.cursor()) as c:
                selectQuery='select * from CRIMINAL'
                c.execute(selectQuery)
                rows = c.fetchall() 
                return rows
        
        
class Officer:
    
    def AddOFRecord(self,oid,on,ocon,omail,ps):
        if oid==' ' :
            return '0'
        
        with closing(conn.cursor()) as c:
                insertQuery='insert into OFFICER(officer_id,officer_name,officer_contact,officer_email,police_station) values(?,?,?,?,?)'
                c.execute(insertQuery,(oid,on,ocon,omail,ps))
                conn.commit()
                return '1'
                
            
    def UpOFRecord(self,oid,ps):
        if oid==' ':
            return 0
        
        with closing(conn.cursor()) as c:
                updateQuery='update OFFICER set police_station =? where officer_id=?'
                c.execute(updateQuery,(ps,oid))
                conn.commit()
                return '1'
            
    def ViewOFRecord(self):
        
        with closing(conn.cursor()) as c:
                selectQuery='select * from OFFICER'
                c.execute(selectQuery)
                rows = c.fetchall() 
                return rows  

    def DelOFRecord(self,oid):
        if oid==' ':
            return 0
        
        with closing(conn.cursor()) as c:
                deleteQuery='delete from OFFICER where officer_id=?'
                c.execute(deleteQuery,(oid,))
                conn.commit()
                return '1'        

class Crime:
    
    def AddCRRecord(self,cid,ctype,cdesc):
        
        with closing(conn.cursor()) as c:
            
            insertQuery='insert into CRIME(crime_id,crime_type,crime_desc) values(?,?,?)'
            c.execute(insertQuery,(cid,ctype,cdesc))
            conn.commit()
            return '1'

    
    def Show(self):
        with closing(conn.cursor()) as c:
            query="SELECT * from CRIME"
            c.execute(query)
            rows=c.fetchall()
            return rows
    
            
class HasARecord:
    
    def AddRecord(self,crid,csid):
        with closing(conn.cursor()) as c:
            query="insert into HAS_A_RECORD(criminal_id,cs_id) values(?,?)"
            c.execute(query,(crid,csid))
            rows=c.fetchall()
            return rows
    
    def Show(self):
        with closing(conn.cursor()) as c:
            query="SELECT criminal_id,cs_id from HAS_A_RECORD "
            c.execute(query)
            rows=c.fetchall()
            return rows
    
    
    
class ChargeSheet:    
    
    def AddCSRecord(self,csid,csDate,csType,csDesc,punish,crimTime,crimDate,crimLoc,oid,cid):
        if csid==' ' :
            return '0'
        
        with closing(conn.cursor()) as c:
                insertQuery='insert into CHARGE_SHEET(cs_id, cs_date, cs_type, cs_desc, punishment, crime_time, crime_date, crime_loc, officer_id, crime_id) values(?,?,?,?,?,?,?,?,?,?)'
                c.execute(insertQuery,(csid,csDate,csType,csDesc,punish,crimTime,crimDate,crimLoc,oid,cid))
                conn.commit()
                return '1'
                
            
    def UpCSRecord(self,csid,csType):
        if csid==' ':
            return 0
        
        with closing(conn.cursor()) as c:
                updateQuery='update CHARGE_SHEET set cs_type =? where cs_id=?'
                c.execute(updateQuery,(csType, csid))
                conn.commit()
                return '1'
            
    def ViewCsRecord(self):
        
        with closing(conn.cursor()) as c:
                selectQuery='select * from CHARGE_SHEET'
                c.execute(selectQuery)
                rows = c.fetchall() 
                return rows    
    
    
    
    
class FIR:
    
    def AddFIRecord(self,fid,fin,fit,fidate,fidesc,cid,oid):
        if fid==' ' :
            return '0'
        
        with closing(conn.cursor()) as c:
                insertQuery='insert into FIR(fir_id, fir_name, fir_type, fir_date, fir_desc, crime_id, officer_id) values(?,?,?,?,?,?,?)'
                c.execute(insertQuery,(fid,fin,fit,fidate,fidesc,cid,oid))
                conn.commit()
                return '1'
                
            
    def ViewFIRecord(self):
        
        with closing(conn.cursor()) as c:
                selectQuery='select * from FIR'
                c.execute(selectQuery)
                rows = c.fetchall() 
                return rows
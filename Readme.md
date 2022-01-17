# Import +1M register from Excell to MSSMS

This Script import more than 1M registers from excell to SQL less than 30 minutes.

## Steps to use it
- Connect to DB from db.py
- From the Excell file copy all Headers
- Go to excellRead.py and paste the entity in line 14 where temporal table query is declarated
- In line 30. Insert the entities "##NombreCompleto (nombre, apellido, apellido2)" 
- In values insert "?" for each header 

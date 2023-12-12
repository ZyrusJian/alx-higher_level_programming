-- This script creates the database hbtn_0c_0 if it doesn't already exist
-- Create the database if it doesn't exist
SET @create_query = IF(
	EXISTS(
		SELECT SCHEMA_NAME
		FROM INFORMATION_SCHEMA.SCHEMATA
		WHERE SCHEMA_NAME = 'hbtn_0c_0'
	),
	'',
	'CREATE DATABASE hbtn_0c_0'
);
PREPARE create_stmt FROM @create_query;
EXECUTE create_stmt;
DEALLOCATE PREPARE create_stmt;

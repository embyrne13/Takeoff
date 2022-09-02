-- settings.sql
CREATE DATABASE takeoff;
CREATE USER takeoffuser WITH PASSWORD 'takeoff';
GRANT ALL PRIVILEGES ON DATABASE takeoff TO takeoffuser;
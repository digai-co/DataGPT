create table building (
    building_id      INT PRIMARY KEY,
    building_name    VARCHAR(100)
);
COMMENT ON TABLE building IS 'Building Information';
COMMENT ON COLUMN building.building_name IS 'Building Name';


CREATE TABLE floor (
    floor_id     INT PRIMARY KEY,
    floor_name   VARCHAR(100),
    building_id  INT
);
COMMENT ON TABLE floor IS 'Floor Information';
COMMENT ON COLUMN floor.floor_name IS 'Floor Name';


CREATE TABLE space (
    space_id    INT PRIMARY KEY,
    space_name  VARCHAR(100),
    space_area  FLOAT,
    space_type  VARCHAR(100),
    floor_id    INT
);
COMMENT ON TABLE space IS 'Space Information';
COMMENT ON COLUMN space.space_name IS 'Space Name';
COMMENT ON COLUMN space.space_area IS 'Space Area';
COMMENT ON COLUMN space.space_type IS 'Space Type; eg: Computer Room, Restroom, Parking Spot, Office, Meeting Room, Pantry, Store, etc.';


CREATE TABLE space_ammeter (
    id           INT PRIMARY KEY, 
    space_id     INT,
    meter_value  DECIMAL(10, 2),
    meter_at     TIMESTAMP
);
COMMENT ON TABLE space_ammeter IS 'Space Ammeter Reading';
COMMENT ON COLUMN space_ammeter.space_id IS 'Space ID';
COMMENT ON COLUMN space_ammeter.meter_value IS 'Meter Reading';
COMMENT ON COLUMN space_ammeter.meter_at IS 'Reading Time';


CREATE TABLE space_environment (
    id           INT PRIMARY KEY, 
    space_id     INT,
    temperature  DECIMAL(10, 2),
    humidity     DECIMAL(10, 2),
    co2          DECIMAL(10, 2),
    pm25         DECIMAL(10, 2),
    voc          DECIMAL(10, 2),
    meter_at     TIMESTAMP
);
COMMENT ON TABLE space_environment IS 'Space Environment Sensors';
COMMENT ON COLUMN space_environment.space_id IS 'Space ID';
COMMENT ON COLUMN space_environment.temperature IS 'Temperature';
COMMENT ON COLUMN space_environment.humidity IS 'Humidity';
COMMENT ON COLUMN space_environment.co2 IS 'Carbon Dioxide Concentration';
COMMENT ON COLUMN space_environment.pm25 IS 'PM2.5 Concentration';
COMMENT ON COLUMN space_environment.voc IS 'Volatile Organic Compounds Concentration';
COMMENT ON COLUMN space_environment.meter_at IS 'Monitoring Time';

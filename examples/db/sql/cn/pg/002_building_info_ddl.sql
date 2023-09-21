create table building (
    building_id      INT PRIMARY KEY,
    building_name    VARCHAR(100)
);
COMMENT ON TABLE building IS '楼宇信息';
COMMENT ON COLUMN building.building_name IS '楼宇名称';


CREATE TABLE floor (
    floor_id     INT PRIMARY KEY,
    floor_name   VARCHAR(100),
    building_id  INT
);
COMMENT ON TABLE floor IS '楼层信息';
COMMENT ON COLUMN floor.floor_name IS '楼层名称';


CREATE TABLE space (
    space_id    INT PRIMARY KEY,
    space_name  VARCHAR(100),
    space_area  FLOAT,
    space_type  VARCHAR(100),
    floor_id    INT
);
COMMENT ON TABLE space IS '空间信息';
COMMENT ON COLUMN space.space_name IS '空间名称';
COMMENT ON COLUMN space.space_area IS '面积';
COMMENT ON COLUMN space.space_type IS '空间类型，取值有机房、卫生间、车位、办公室、会议室、茶水间、商铺、总和等';


CREATE TABLE space_ammeter (
    id           INT PRIMARY KEY, 
    space_id     INT,
    meter_value  DECIMAL(10, 2),
    meter_at     TIMESTAMP
);
COMMENT ON TABLE space_ammeter IS '空间电表抄表';
COMMENT ON COLUMN space_ammeter.space_id IS '空间id';
COMMENT ON COLUMN space_ammeter.meter_value IS '电表读数';
COMMENT ON COLUMN space_ammeter.meter_at IS '抄表时间';


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
COMMENT ON TABLE space_environment IS '空间环境传感器';
COMMENT ON COLUMN space_environment.space_id IS '空间id';
COMMENT ON COLUMN space_environment.temperature IS '温度';
COMMENT ON COLUMN space_environment.humidity IS '湿度';
COMMENT ON COLUMN space_environment.co2 IS '二氧化碳浓度';
COMMENT ON COLUMN space_environment.pm25 IS 'PM2.5浓度';
COMMENT ON COLUMN space_environment.voc IS '挥发性有机物浓度';
COMMENT ON COLUMN space_environment.meter_at IS '监测时间';

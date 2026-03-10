CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255) NOT NULL,
    longitude DECIMAL(11,8),
    latitude DECIMAL(11,8),
    bearing INT,
    direction_id TINYINT,
    label VARCHAR(50),
    route_id VARCHAR(50),
    current_stop_sequence INT,
    vehicle_type VARCHAR(20) DEFAULT 'vehicle',
    speed DECIMAL(8,2),
    current_status VARCHAR(50),
    occupancy_status VARCHAR(50),
    revenue VARCHAR(20),
    stop_id VARCHAR(50),
    trip_id VARCHAR(50),
    updated_at DATETIME,

    
    -- Indexes for better performance
    INDEX idx_route_id (route_id),
    INDEX idx_trip_id (trip_id),
    INDEX idx_stop_id (stop_id),
    INDEX idx_current_status (current_status)
);
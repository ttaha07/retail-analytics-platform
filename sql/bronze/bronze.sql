-- Bronze Layer Execution Guide
-- This file documents the Bronze layer execution order.
-- The executable Python pipeline runs the individual SQL files directly.

-- Execution order:
-- 1. sql/bronze/create_tables.sql
-- 2. sql/bronze/load_data.sql
-- 3. sql/bronze/validation.sql

-- Do not execute this file through the Python connector.
-- Snowflake Python Connector does not support SnowSQL-only !source commands.
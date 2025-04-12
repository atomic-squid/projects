CREATE TABLE [dbo].[accel] (
  [item_id] UNIQUEIDENTIFIER PRIMARY KEY FOREIGN KEY REFERENCES item (item_id)
, [item_mult] DECIMAL(6,4) NOT NULL
, [speed_mult] DECIMAL(6,4) NOT NULL
);
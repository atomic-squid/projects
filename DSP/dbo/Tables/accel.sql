CREATE TABLE [dbo].[accel] (
  [item_id]    UNIQUEIDENTIFIER NOT NULL PRIMARY KEY
, [item_mult]  DECIMAL(6,4)     NOT NULL
, [speed_mult] DECIMAL(6,4)     NOT NULL
, CONSTRAINT [FK_accel_item_id] FOREIGN KEY (item_id) REFERENCES item (item_id)
);
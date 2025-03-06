CREATE TABLE [dbo].[mfg] (
  [item_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES item (item_id)
, [mfg_class_id] UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES mfg_class (mfg_class_id)
, [speed_mult] DECIMAL(6,4) NOT NULL
);

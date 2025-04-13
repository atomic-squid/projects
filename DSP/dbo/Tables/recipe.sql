CREATE TABLE [dbo].[recipe] (
  [recipe_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY
, [mfg_class_id] UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES mfg_class (mfg_class_id)
, [item_class_id] UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES item_class (item_class_id)
, [name] VARCHAR(250) NOT NULL
, [cycle_time_s] DECIMAL(4,2) NOT NULL
, [speedup] BIT NOT NULL
, [extra_item] BIT NOT NULL
);
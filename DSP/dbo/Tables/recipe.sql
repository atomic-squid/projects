CREATE TABLE [dbo].[recipe] (
  [recipe_id]     UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [mfg_class_id]  UNIQUEIDENTIFIER NOT NULL 
, [item_class_id] UNIQUEIDENTIFIER NOT NULL 
, [name]          VARCHAR(250)     NOT NULL
, [cycle_time_s]  DECIMAL(4,2)     NOT NULL
, [speedup]       BIT              NOT NULL
, [extra_item]    BIT              NOT NULL
, CONSTRAINT [FK_recipe_mfg_class_id]  FOREIGN KEY (mfg_class_id)  REFERENCES mfg_class (mfg_class_id)
, CONSTRAINT [FK_recipe_item_class_id] FOREIGN KEY (item_class_id) REFERENCES item_class (item_class_id)
);
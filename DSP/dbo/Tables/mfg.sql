CREATE TABLE [dbo].[mfg] (
  [item_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES item (item_id)
, [mfg_class_id] UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES mfg_class (mfg_class_id)
, [mfg_class_ord] TINYINT NOT NULL
, [xport_class_id] UNIQUEIDENTIFIER NOT NULL FOREIGN KEY REFERENCES xport_class (xport_class_id)
, [speed_mult] DECIMAL(6,4) NOT NULL
-- Ensure that no ordnal for a class has a tie
, CONSTRAINT [CNS_Mfg_Class_Ord] UNIQUE (mfg_class_id, mfg_class_ord)
);

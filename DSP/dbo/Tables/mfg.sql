CREATE TABLE [dbo].[mfg] (
  [item_id]        UNIQUEIDENTIFIER NOT NULL PRIMARY KEY
, [mfg_class_id]   UNIQUEIDENTIFIER NOT NULL
, [mfg_class_ord]  TINYINT          NOT NULL
, [xport_class_id] UNIQUEIDENTIFIER NOT NULL
, [speed_mult]     DECIMAL(6,4)     NOT NULL
-- Ensure that no ordnal for a class has a tie
, CONSTRAINT [CNS_mfg_mfg_class_id_ord] UNIQUE (mfg_class_id, mfg_class_ord)
, CONSTRAINT [FK_mfg_item_id]           FOREIGN KEY (item_id)        REFERENCES item (item_id)
, CONSTRAINT [FK_mfg_mfg_class_id]      FOREIGN KEY (mfg_class_id)   REFERENCES mfg_class (mfg_class_id)
, CONSTRAINT [FK_mfg_xport_class_id]    FOREIGN KEY (xport_class_id) REFERENCES xport_class (xport_class_id)
);

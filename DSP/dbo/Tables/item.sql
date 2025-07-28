CREATE TABLE [dbo].[item] (
  [item_id]       UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [item_class_id] UNIQUEIDENTIFIER NOT NULL
, [name]          VARCHAR(250)     NOT NULL
, CONSTRAINT [CNS_item_name]         UNIQUE ([name])
, CONSTRAINT [FK_item_item_class_id] FOREIGN KEY (item_class_id) REFERENCES item_class (item_class_id)
);

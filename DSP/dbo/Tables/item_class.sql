CREATE TABLE [dbo].[item_class] (
  [item_class_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [name]          VARCHAR(250)     NOT NULL
, CONSTRAINT [CNS_item_class_name] UNIQUE ([name])
);
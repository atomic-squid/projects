CREATE TABLE [dbo].[item] (
  [item_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [item_class_id] UNIQUEIDENTIFIER FOREIGN KEY REFERENCES item_class (item_class_id)
, [name] VARCHAR(250)
);

CREATE TABLE [dbo].[xport_class] (
  [xport_class_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [name]           VARCHAR(250)     NOT NULL
, CONSTRAINT [CNS_xport_class_name] UNIQUE ([name])
);

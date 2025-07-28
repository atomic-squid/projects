CREATE TABLE [dbo].[mfg_class] (
  [mfg_class_id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY DEFAULT NEWID()
, [name]         VARCHAR(250)     NOT NULL
, CONSTRAINT [CNS_mfg_class_name] UNIQUE ([name])
);

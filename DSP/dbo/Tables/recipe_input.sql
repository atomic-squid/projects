CREATE TABLE [dbo].[recipe_input] (
  [recipe_id] UNIQUEIDENTIFIER NOT NULL
, [item_id]   UNIQUEIDENTIFIER NOT NULL
, [qty]       INT              NOT NULL
, CONSTRAINT [PK_recipe_input_recipe_id_item_id] PRIMARY KEY (recipe_id, item_id)
);
CREATE TABLE [dbo].[recipe_output] (
  [recipe_id] UNIQUEIDENTIFIER NOT NULL
, [item_id]   UNIQUEIDENTIFIER NOT NULL
, [qty]       INT              NOT NULL
, CONSTRAINT [PK_recipe_output_recipe_id_item_id] PRIMARY KEY (recipe_id, item_id)
);
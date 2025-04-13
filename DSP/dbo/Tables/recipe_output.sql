CREATE TABLE [dbo].[recipe_output] (
  [recipe_id] UNIQUEIDENTIFIER NOT NULL
, [item_id] UNIQUEIDENTIFIER NOT NULL
, [qty] INT NOT NULL
, CONSTRAINT PK_Output_RecipeItem PRIMARY KEY (recipe_id, item_id)
);
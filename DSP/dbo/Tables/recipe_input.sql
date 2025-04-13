CREATE TABLE [dbo].[recipe_input] (
  [recipe_id] UNIQUEIDENTIFIER NOT NULL
, [item_id] UNIQUEIDENTIFIER NOT NULL
, [qty] INT NOT NULL
, CONSTRAINT PK_Input_RecipeItem PRIMARY KEY (recipe_id, item_id)
);
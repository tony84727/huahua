grammar CraftRule;

craftingRule: recipe | recipeCount;
recipe: NAME | quoteRecipe;
quoteRecipe: '"' NAME_WITH_SPACE '"' | '\'' NAME_WITH_SPACE '\'';
recipeCount: recipe 'x' COUNT;
DIGITS: [0-9]+;
COUNT: DIGITS | DIGITS '.' DIGITS;
WS: [\t\r\n]+ -> skip;
grammar CraftRule;

specification: (NEWLINE|craftingRule)+;
craftingRule: target '=' recipe ('+' recipe)*;
target: identifier;
recipe: recipeWithCount | recipeName;
recipeName: identifier;
recipeWithCount: recipeName '*' number;
identifier: quotedIdentifier | NAME;
number: DIGITS;
quotedIdentifier: STRING;

DIGITS: [0-9]+('.'[0-9]+)?;
NEWLINE: '\r'? '\n';
NAME: ~([\r\t\n=+* ])+;
STRING: '\''.*?'\'';
WS: [ \t]+ -> skip;

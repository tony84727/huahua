grammar CraftRule;

craftingRule: target '=' recipe ('+' recipe)*;
target: identifier;
recipe: identifierAndCount | identifier;
identifierAndCount: identifier '*' number;
identifier: quotedIdentifier | NAME;
number: DIGITS;
quotedIdentifier: STRING;

DIGITS: [0-9]+;
NAME: ~[\r\t\n=+* ]+;
STRING: '\''.*?'\'';
WS: [\r\t\n]+ -> skip;

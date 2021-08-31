# Generated from CraftRule.g4 by ANTLR 4.9.2
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\61\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5\31\n\5\r\5")
        buf.write("\16\5\32\3\6\6\6\36\n\6\r\6\16\6\37\3\7\3\7\7\7$\n\7\f")
        buf.write("\7\16\7\'\13\7\3\7\3\7\3\b\6\b,\n\b\r\b\16\b-\3\b\3\b")
        buf.write("\3%\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\5\3\2\62;\7")
        buf.write("\2\13\f\17\17\"\",-??\4\2\13\f\17\17\2\64\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\25\3")
        buf.write("\2\2\2\t\30\3\2\2\2\13\35\3\2\2\2\r!\3\2\2\2\17+\3\2\2")
        buf.write("\2\21\22\7?\2\2\22\4\3\2\2\2\23\24\7-\2\2\24\6\3\2\2\2")
        buf.write("\25\26\7,\2\2\26\b\3\2\2\2\27\31\t\2\2\2\30\27\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\n\3\2\2")
        buf.write("\2\34\36\n\3\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2")
        buf.write("\2\2\37 \3\2\2\2 \f\3\2\2\2!%\7)\2\2\"$\13\2\2\2#\"\3")
        buf.write("\2\2\2$\'\3\2\2\2%&\3\2\2\2%#\3\2\2\2&(\3\2\2\2\'%\3\2")
        buf.write("\2\2()\7)\2\2)\16\3\2\2\2*,\t\4\2\2+*\3\2\2\2,-\3\2\2")
        buf.write("\2-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\b\b\2\2\60\20\3\2")
        buf.write("\2\2\7\2\32\37%-\3\b\2\2")
        return buf.getvalue()


class CraftRuleLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    NAME = 5
    STRING = 6
    WS = 7

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'='", "'+'", "'*'"]

    symbolicNames = ["<INVALID>",
                     "DIGITS", "NAME", "STRING", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "DIGITS", "NAME", "STRING", "WS"]

    grammarFileName = "CraftRule.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

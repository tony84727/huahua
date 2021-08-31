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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("(\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5\27\n\5\r\5\16\5\30\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6 \n\6\3\7\6\7#\n\7\r\7\16\7$\3\7")
        buf.write("\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\4\3\2\62;\4\2")
        buf.write("\13\f\17\17\2*\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3")
        buf.write("\2\2\2\7\23\3\2\2\2\t\26\3\2\2\2\13\37\3\2\2\2\r\"\3\2")
        buf.write("\2\2\17\20\7$\2\2\20\4\3\2\2\2\21\22\7)\2\2\22\6\3\2\2")
        buf.write("\2\23\24\7z\2\2\24\b\3\2\2\2\25\27\t\2\2\2\26\25\3\2\2")
        buf.write("\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\n\3\2")
        buf.write("\2\2\32 \5\t\5\2\33\34\5\t\5\2\34\35\7\60\2\2\35\36\5")
        buf.write("\t\5\2\36 \3\2\2\2\37\32\3\2\2\2\37\33\3\2\2\2 \f\3\2")
        buf.write("\2\2!#\t\3\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2")
        buf.write("\2%&\3\2\2\2&\'\b\7\2\2\'\16\3\2\2\2\6\2\30\37$\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class CraftRuleLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    COUNT = 5
    WS = 6

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'\"'", "'''", "'x'"]

    symbolicNames = ["<INVALID>",
                     "DIGITS", "COUNT", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "DIGITS", "COUNT", "WS"]

    grammarFileName = "CraftRule.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

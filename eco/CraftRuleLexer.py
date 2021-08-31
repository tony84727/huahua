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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5\33\n")
        buf.write("\5\r\5\16\5\34\3\5\3\5\6\5!\n\5\r\5\16\5\"\5\5%\n\5\3")
        buf.write("\6\5\6(\n\6\3\6\3\6\3\7\6\7-\n\7\r\7\16\7.\3\b\3\b\7\b")
        buf.write("\63\n\b\f\b\16\b\66\13\b\3\b\3\b\3\t\6\t;\n\t\r\t\16\t")
        buf.write("<\3\t\3\t\3\64\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\3\2\5\3\2\62;\7\2\13\f\17\17\"\",-??\4\2\13\13\"\"\2")
        buf.write("F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3")
        buf.write("\2\2\2\5\25\3\2\2\2\7\27\3\2\2\2\t\32\3\2\2\2\13\'\3\2")
        buf.write("\2\2\r,\3\2\2\2\17\60\3\2\2\2\21:\3\2\2\2\23\24\7?\2\2")
        buf.write("\24\4\3\2\2\2\25\26\7-\2\2\26\6\3\2\2\2\27\30\7,\2\2\30")
        buf.write("\b\3\2\2\2\31\33\t\2\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35$\3\2\2\2\36 \7\60\2\2\37")
        buf.write("!\t\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2")
        buf.write("#%\3\2\2\2$\36\3\2\2\2$%\3\2\2\2%\n\3\2\2\2&(\7\17\2\2")
        buf.write("\'&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\f\2\2*\f\3\2\2\2")
        buf.write("+-\n\3\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\16")
        buf.write("\3\2\2\2\60\64\7)\2\2\61\63\13\2\2\2\62\61\3\2\2\2\63")
        buf.write("\66\3\2\2\2\64\65\3\2\2\2\64\62\3\2\2\2\65\67\3\2\2\2")
        buf.write("\66\64\3\2\2\2\678\7)\2\28\20\3\2\2\29;\t\4\2\2:9\3\2")
        buf.write("\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\b\t\2\2")
        buf.write("?\22\3\2\2\2\n\2\34\"$\'.\64<\3\b\2\2")
        return buf.getvalue()


class CraftRuleLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    NEWLINE = 5
    NAME = 6
    STRING = 7
    WS = 8

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'='", "'+'", "'*'"]

    symbolicNames = ["<INVALID>",
                     "DIGITS", "NEWLINE", "NAME", "STRING", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "DIGITS", "NEWLINE", "NAME", "STRING",
                 "WS"]

    grammarFileName = "CraftRule.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

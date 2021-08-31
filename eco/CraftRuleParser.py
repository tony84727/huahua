# Generated from CraftRule.g4 by ANTLR 4.9.2
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
	from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\3\3\3\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6")
        buf.write("\'\n\6\3\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2")
        buf.write("(\2\20\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2\b \3\2\2\2\n")
        buf.write("&\3\2\2\2\f(\3\2\2\2\16*\3\2\2\2\20\21\5\4\3\2\21\22\7")
        buf.write("\3\2\2\22\27\5\6\4\2\23\24\7\4\2\2\24\26\5\6\4\2\25\23")
        buf.write("\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\3\3\2\2\2\31\27\3\2\2\2\32\33\5\n\6\2\33\5\3\2\2\2\34")
        buf.write("\37\5\b\5\2\35\37\5\n\6\2\36\34\3\2\2\2\36\35\3\2\2\2")
        buf.write("\37\7\3\2\2\2 !\5\n\6\2!\"\7\5\2\2\"#\5\f\7\2#\t\3\2\2")
        buf.write("\2$\'\5\16\b\2%\'\7\7\2\2&$\3\2\2\2&%\3\2\2\2\'\13\3\2")
        buf.write("\2\2()\7\6\2\2)\r\3\2\2\2*+\7\b\2\2+\17\3\2\2\2\5\27\36")
        buf.write("&")
        return buf.getvalue()


class CraftRuleParser(Parser):
    grammarFileName = "CraftRule.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'='", "'+'", "'*'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "DIGITS", "NAME", "STRING", "WS"]

    RULE_craftingRule = 0
    RULE_target = 1
    RULE_recipe = 2
    RULE_identifierAndCount = 3
    RULE_identifier = 4
    RULE_number = 5
    RULE_quotedIdentifier = 6

    ruleNames = ["craftingRule", "target", "recipe", "identifierAndCount",
                 "identifier", "number", "quotedIdentifier"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    NAME = 5
    STRING = 6
    WS = 7

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class CraftingRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def target(self):
            return self.getTypedRuleContext(CraftRuleParser.TargetContext, 0)

        def recipe(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(CraftRuleParser.RecipeContext)
            else:
                return self.getTypedRuleContext(CraftRuleParser.RecipeContext, i)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_craftingRule

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCraftingRule"):
                listener.enterCraftingRule(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCraftingRule"):
                listener.exitCraftingRule(self)

    def craftingRule(self):

        localctx = CraftRuleParser.CraftingRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_craftingRule)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.target()
            self.state = 15
            self.match(CraftRuleParser.T__0)
            self.state = 16
            self.recipe()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == CraftRuleParser.T__1:
                self.state = 17
                self.match(CraftRuleParser.T__1)
                self.state = 18
                self.recipe()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CraftRuleParser.IdentifierContext, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_target

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTarget"):
                listener.enterTarget(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTarget"):
                listener.exitTarget(self)

    def target(self):

        localctx = CraftRuleParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierAndCount(self):
            return self.getTypedRuleContext(CraftRuleParser.IdentifierAndCountContext, 0)

        def identifier(self):
            return self.getTypedRuleContext(CraftRuleParser.IdentifierContext, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_recipe

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRecipe"):
                listener.enterRecipe(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRecipe"):
                listener.exitRecipe(self)

    def recipe(self):

        localctx = CraftRuleParser.RecipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_recipe)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.identifierAndCount()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierAndCountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CraftRuleParser.IdentifierContext, 0)

        def number(self):
            return self.getTypedRuleContext(CraftRuleParser.NumberContext, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_identifierAndCount

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentifierAndCount"):
                listener.enterIdentifierAndCount(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentifierAndCount"):
                listener.exitIdentifierAndCount(self)

    def identifierAndCount(self):

        localctx = CraftRuleParser.IdentifierAndCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifierAndCount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.identifier()
            self.state = 31
            self.match(CraftRuleParser.T__2)
            self.state = 32
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quotedIdentifier(self):
            return self.getTypedRuleContext(CraftRuleParser.QuotedIdentifierContext, 0)

        def NAME(self):
            return self.getToken(CraftRuleParser.NAME, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_identifier

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentifier"):
                listener.enterIdentifier(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentifier"):
                listener.exitIdentifier(self)

    def identifier(self):

        localctx = CraftRuleParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CraftRuleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.quotedIdentifier()
                pass
            elif token in [CraftRuleParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(CraftRuleParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(CraftRuleParser.DIGITS, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNumber"):
                listener.enterNumber(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNumber"):
                listener.exitNumber(self)

    def number(self):

        localctx = CraftRuleParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CraftRuleParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuotedIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CraftRuleParser.STRING, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_quotedIdentifier

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterQuotedIdentifier"):
                listener.enterQuotedIdentifier(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitQuotedIdentifier"):
                listener.exitQuotedIdentifier(self)

    def quotedIdentifier(self):

        localctx = CraftRuleParser.QuotedIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quotedIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CraftRuleParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2")
        buf.write("\3\3\3\3\5\3\21\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\31\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\35\2\f\3\2\2")
        buf.write("\2\4\20\3\2\2\2\6\30\3\2\2\2\b\32\3\2\2\2\n\r\5\4\3\2")
        buf.write("\13\r\5\b\5\2\f\n\3\2\2\2\f\13\3\2\2\2\r\3\3\2\2\2\16")
        buf.write("\21\7\t\2\2\17\21\5\6\4\2\20\16\3\2\2\2\20\17\3\2\2\2")
        buf.write("\21\5\3\2\2\2\22\23\7\3\2\2\23\24\7\n\2\2\24\31\7\3\2")
        buf.write("\2\25\26\7\4\2\2\26\27\7\n\2\2\27\31\7\4\2\2\30\22\3\2")
        buf.write("\2\2\30\25\3\2\2\2\31\7\3\2\2\2\32\33\5\4\3\2\33\34\7")
        buf.write("\5\2\2\34\35\7\7\2\2\35\t\3\2\2\2\5\f\20\30")
        return buf.getvalue()


class CraftRuleParser(Parser):
    grammarFileName = "CraftRule.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'\"'", "'''", "'x'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "DIGITS", "COUNT", "WS", "NAME", "NAME_WITH_SPACE"]

    RULE_craftingRule = 0
    RULE_recipe = 1
    RULE_quoteRecipe = 2
    RULE_recipeCount = 3

    ruleNames = ["craftingRule", "recipe", "quoteRecipe", "recipeCount"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    COUNT = 5
    WS = 6
    NAME = 7
    NAME_WITH_SPACE = 8

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

        def recipe(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeContext, 0)

        def recipeCount(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeCountContext, 0)

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
        try:
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.recipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.recipeCount()
                pass


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

        def NAME(self):
            return self.getToken(CraftRuleParser.NAME, 0)

        def quoteRecipe(self):
            return self.getTypedRuleContext(CraftRuleParser.QuoteRecipeContext, 0)

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
        self.enterRule(localctx, 2, self.RULE_recipe)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CraftRuleParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(CraftRuleParser.NAME)
                pass
            elif token in [CraftRuleParser.T__0, CraftRuleParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.quoteRecipe()
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

    class QuoteRecipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME_WITH_SPACE(self):
            return self.getToken(CraftRuleParser.NAME_WITH_SPACE, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_quoteRecipe

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterQuoteRecipe"):
                listener.enterQuoteRecipe(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitQuoteRecipe"):
                listener.exitQuoteRecipe(self)

    def quoteRecipe(self):

        localctx = CraftRuleParser.QuoteRecipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_quoteRecipe)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CraftRuleParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(CraftRuleParser.T__0)
                self.state = 17
                self.match(CraftRuleParser.NAME_WITH_SPACE)
                self.state = 18
                self.match(CraftRuleParser.T__0)
                pass
            elif token in [CraftRuleParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(CraftRuleParser.T__1)
                self.state = 20
                self.match(CraftRuleParser.NAME_WITH_SPACE)
                self.state = 21
                self.match(CraftRuleParser.T__1)
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

    class RecipeCountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipe(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeContext, 0)

        def COUNT(self):
            return self.getToken(CraftRuleParser.COUNT, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_recipeCount

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRecipeCount"):
                listener.enterRecipeCount(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRecipeCount"):
                listener.exitRecipeCount(self)

    def recipeCount(self):

        localctx = CraftRuleParser.RecipeCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_recipeCount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.recipe()
            self.state = 25
            self.match(CraftRuleParser.T__2)
            self.state = 26
            self.match(CraftRuleParser.COUNT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

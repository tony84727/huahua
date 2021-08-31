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
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\6\2\27\n\2\r\2\16\2\30\3")
        buf.write("\3\3\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4\3\5")
        buf.write("\3\5\5\5)\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\63\n")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2")
        buf.write("\2\64\2\26\3\2\2\2\4\32\3\2\2\2\6$\3\2\2\2\b(\3\2\2\2")
        buf.write("\n*\3\2\2\2\f,\3\2\2\2\16\62\3\2\2\2\20\64\3\2\2\2\22")
        buf.write("\66\3\2\2\2\24\27\7\7\2\2\25\27\5\4\3\2\26\24\3\2\2\2")
        buf.write("\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2")
        buf.write("\2\31\3\3\2\2\2\32\33\5\6\4\2\33\34\7\3\2\2\34!\5\b\5")
        buf.write("\2\35\36\7\4\2\2\36 \5\b\5\2\37\35\3\2\2\2 #\3\2\2\2!")
        buf.write("\37\3\2\2\2!\"\3\2\2\2\"\5\3\2\2\2#!\3\2\2\2$%\5\16\b")
        buf.write("\2%\7\3\2\2\2&)\5\f\7\2\')\5\n\6\2(&\3\2\2\2(\'\3\2\2")
        buf.write("\2)\t\3\2\2\2*+\5\16\b\2+\13\3\2\2\2,-\5\n\6\2-.\7\5\2")
        buf.write("\2./\5\20\t\2/\r\3\2\2\2\60\63\5\22\n\2\61\63\7\b\2\2")
        buf.write("\62\60\3\2\2\2\62\61\3\2\2\2\63\17\3\2\2\2\64\65\7\6\2")
        buf.write("\2\65\21\3\2\2\2\66\67\7\t\2\2\67\23\3\2\2\2\7\26\30!")
        buf.write("(\62")
        return buf.getvalue()


class CraftRuleParser(Parser):
    grammarFileName = "CraftRule.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'='", "'+'", "'*'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "DIGITS", "NEWLINE", "NAME", "STRING", "WS"]

    RULE_specification = 0
    RULE_craftingRule = 1
    RULE_target = 2
    RULE_recipe = 3
    RULE_recipeName = 4
    RULE_recipeWithCount = 5
    RULE_identifier = 6
    RULE_number = 7
    RULE_quotedIdentifier = 8

    ruleNames = ["specification", "craftingRule", "target", "recipe",
                 "recipeName", "recipeWithCount", "identifier", "number",
                 "quotedIdentifier"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    DIGITS = 4
    NEWLINE = 5
    NAME = 6
    STRING = 7
    WS = 8

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class SpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(CraftRuleParser.NEWLINE)
            else:
                return self.getToken(CraftRuleParser.NEWLINE, i)

        def craftingRule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(CraftRuleParser.CraftingRuleContext)
            else:
                return self.getTypedRuleContext(CraftRuleParser.CraftingRuleContext, i)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_specification

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSpecification"):
                listener.enterSpecification(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSpecification"):
                listener.exitSpecification(self)

    def specification(self):

        localctx = CraftRuleParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CraftRuleParser.NEWLINE]:
                    self.state = 18
                    self.match(CraftRuleParser.NEWLINE)
                    pass
                elif token in [CraftRuleParser.NAME, CraftRuleParser.STRING]:
                    self.state = 19
                    self.craftingRule()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << CraftRuleParser.NEWLINE) | (1 << CraftRuleParser.NAME) | (
                        1 << CraftRuleParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

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
        self.enterRule(localctx, 2, self.RULE_craftingRule)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.target()
            self.state = 25
            self.match(CraftRuleParser.T__0)
            self.state = 26
            self.recipe()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == CraftRuleParser.T__1:
                self.state = 27
                self.match(CraftRuleParser.T__1)
                self.state = 28
                self.recipe()
                self.state = 33
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
        self.enterRule(localctx, 4, self.RULE_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
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

        def recipeWithCount(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeWithCountContext, 0)

        def recipeName(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeNameContext, 0)

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
        self.enterRule(localctx, 6, self.RULE_recipe)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.recipeWithCount()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.recipeName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecipeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CraftRuleParser.IdentifierContext, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_recipeName

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRecipeName"):
                listener.enterRecipeName(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRecipeName"):
                listener.exitRecipeName(self)

    def recipeName(self):

        localctx = CraftRuleParser.RecipeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_recipeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RecipeWithCountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recipeName(self):
            return self.getTypedRuleContext(CraftRuleParser.RecipeNameContext, 0)

        def number(self):
            return self.getTypedRuleContext(CraftRuleParser.NumberContext, 0)

        def getRuleIndex(self):
            return CraftRuleParser.RULE_recipeWithCount

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRecipeWithCount"):
                listener.enterRecipeWithCount(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRecipeWithCount"):
                listener.exitRecipeWithCount(self)

    def recipeWithCount(self):

        localctx = CraftRuleParser.RecipeWithCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_recipeWithCount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.recipeName()
            self.state = 43
            self.match(CraftRuleParser.T__2)
            self.state = 44
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
        self.enterRule(localctx, 12, self.RULE_identifier)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CraftRuleParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.quotedIdentifier()
                pass
            elif token in [CraftRuleParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
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
        self.enterRule(localctx, 14, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
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
        self.enterRule(localctx, 16, self.RULE_quotedIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CraftRuleParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

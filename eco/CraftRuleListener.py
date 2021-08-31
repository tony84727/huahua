# Generated from CraftRule.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CraftRuleParser import CraftRuleParser
else:
    from CraftRuleParser import CraftRuleParser


# This class defines a complete listener for a parse tree produced by CraftRuleParser.
class CraftRuleListener(ParseTreeListener):

    # Enter a parse tree produced by CraftRuleParser#craftingRule.
    def enterCraftingRule(self, ctx: CraftRuleParser.CraftingRuleContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#craftingRule.
    def exitCraftingRule(self, ctx: CraftRuleParser.CraftingRuleContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#recipe.
    def enterRecipe(self, ctx: CraftRuleParser.RecipeContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#recipe.
    def exitRecipe(self, ctx: CraftRuleParser.RecipeContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#quoteRecipe.
    def enterQuoteRecipe(self, ctx: CraftRuleParser.QuoteRecipeContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#quoteRecipe.
    def exitQuoteRecipe(self, ctx: CraftRuleParser.QuoteRecipeContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#recipeCount.
    def enterRecipeCount(self, ctx: CraftRuleParser.RecipeCountContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#recipeCount.
    def exitRecipeCount(self, ctx: CraftRuleParser.RecipeCountContext):
        pass


del CraftRuleParser
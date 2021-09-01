# Generated from CraftRule.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CraftRuleParser import CraftRuleParser
else:
    from CraftRuleParser import CraftRuleParser

# This class defines a complete listener for a parse tree produced by CraftRuleParser.
class CraftRuleListener(ParseTreeListener):

    # Enter a parse tree produced by CraftRuleParser#specification.
    def enterSpecification(self, ctx: CraftRuleParser.SpecificationContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#specification.
    def exitSpecification(self, ctx: CraftRuleParser.SpecificationContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#craftingRule.
    def enterCraftingRule(self, ctx: CraftRuleParser.CraftingRuleContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#craftingRule.
    def exitCraftingRule(self, ctx: CraftRuleParser.CraftingRuleContext):
        pass


    # Enter a parse tree produced by CraftRuleParser#target.
    def enterTarget(self, ctx: CraftRuleParser.TargetContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#target.
    def exitTarget(self, ctx: CraftRuleParser.TargetContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#recipe.
    def enterRecipe(self, ctx: CraftRuleParser.RecipeContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#recipe.
    def exitRecipe(self, ctx: CraftRuleParser.RecipeContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#recipeName.
    def enterRecipeName(self, ctx: CraftRuleParser.RecipeNameContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#recipeName.
    def exitRecipeName(self, ctx: CraftRuleParser.RecipeNameContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#recipeWithCount.
    def enterRecipeWithCount(self, ctx: CraftRuleParser.RecipeWithCountContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#recipeWithCount.
    def exitRecipeWithCount(self, ctx: CraftRuleParser.RecipeWithCountContext):
        pass

    # Enter a parse tree produced by CraftRuleParser#identifier.
    def enterIdentifier(self, ctx: CraftRuleParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#identifier.
    def exitIdentifier(self, ctx: CraftRuleParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CraftRuleParser#number.
    def enterNumber(self, ctx: CraftRuleParser.NumberContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#number.
    def exitNumber(self, ctx: CraftRuleParser.NumberContext):
        pass


    # Enter a parse tree produced by CraftRuleParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx: CraftRuleParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by CraftRuleParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx: CraftRuleParser.QuotedIdentifierContext):
        pass


del CraftRuleParser
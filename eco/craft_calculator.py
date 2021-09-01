from eco.crafting import CraftRuleLookup, RecipeResolver


def init_lookup():
    with open('rules', 'r') as rule_file:
        return CraftRuleLookup(rule_file.read())


def main():
    lookup = init_lookup()
    resolver = RecipeResolver(lookup)
    while True:
        target = input("Enter recipe:")
        recipes = resolver.resolve_all(target)
        for recipe in recipes:
            print(recipe)


if __name__ == '__main__':
    main()

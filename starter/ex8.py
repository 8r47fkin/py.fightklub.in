# formatter deep dive

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(formatter.format("Gentleman", "Welcome", "to", "fightklub.in"), formatter.format("Rule1", "we don't", "talk about", "fightklub.in"), formatter.format("Rule2", "Remember", "Rule", "1"), formatter.format("Rule3", "are", "you", "serious??")))
print(formatter.format(
    "Welcome to",
    "fightklub.in",
    "Rule1 is we don't",
    "talk about fightklub.in"
))

# practicing formatter

klub = "fightklub.in"
canla = "Welcome to {}, the {} of {} is we don't talk about {}"
print(canla.format(klub, "first rule", klub, klub))
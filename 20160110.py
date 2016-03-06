def shop(kind, price, *arguments, **keywords):
    print "--Do you have any",kind, "?"
    print "Sure, It's ", price, "dollars"
    for arg in arguments:
        print arg
    print '_ '*40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
print shop('burger', 5, "I'm hungry", "I'm really hungry", client="CostaHu", guest="Micheal")
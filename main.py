#The women that the men prefer
preferred_rankings_men = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The men that the women prefer
preferred_rankings_women = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake']
}

# This will keep track of the people that are currently engaged (may change)
tentative_engagements = []

# Free men
free_men = [guy for guy in preferred_rankings_men]

def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)

def begin_matching(man):
    print('DEALING WITH %s'%(man))
    for woman in preferred_rankings_men[man]:
        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if (len(taken_match) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('%s is no longer a free man and is not tentatively engaged to %s'%(man, woman))
            break
        elif len(taken_match) > 0:
            print('%s is taken'%(woman))

            current_man = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_man = preferred_rankings_women[woman].index(man)

            if  current_man < potential_man:
                print('%s is satisfied with %s.'%(woman, taken_match[0][0]))
            else:
                print('%s would rather go out with %s. Now removing %s from free men and adding %s.'%s(woman, man, man, taken_match[0][0]))
                # Adding the old man to the free men
                free_men.append(taken_match[0][0])

                # Removing the new man from the free men
                free_men.remove(man)

                # Now making sure that the new guy becomes engaged
                taken_match[0][0] = man
                break

stable_matching()
print('FINAL MATCHES:')
print(tentative_engagements)

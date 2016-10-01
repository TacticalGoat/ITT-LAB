set1 = set(["a","b","c","d"])
set2 = set(["a","b","e","f"])
set3 = set1
set3.update(set2)
print "Union:" + str(set3)
set3 = set1
set3.intersection_update(set2)
print "Intersection:" + str(set3)
set3 = set1
set3.difference_update(set2)
print "Difference:" + str(set3)

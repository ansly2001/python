dic={
    "Bob":24,
    "Charile":36,
    "Alice":72,
    "Eric":18,
    "David":9
}
s=sorted(dic.items())
print( "in ascending order:",s)
s1=sorted(dic.items(),reverse=True)
print ("in descending order:",s1)
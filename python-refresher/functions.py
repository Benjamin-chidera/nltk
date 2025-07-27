# Modify this function to return a list of strings as defined above
def list_benefits(*args):
    list_benefits = []
    
    for benefit in args:
        # print(benefit)
        list_benefits.append(benefit)
        
    return list_benefits

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(info):
    return info

print(list_benefits("More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"))

print(build_sentence(" is a benefit of functions!"))
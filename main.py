def optimize_boolean(expr):
    
    # De Morgan's laws
    expr = expr.replace("not (not ", "")
    expr = expr.replace(") and (not ", " or ")
    expr = expr.replace("not (", "not ")
    
    # absorption and domination laws
    for op in ["and", "or"]:
        for term1 in expr.split(op):
            for term2 in expr.split(op):
                if term1 != term2 and term1 in term2:
                    if op == "and":
                        expr = expr.replace(term1 + " and " + term2, term1)
                    elif op == "or":
                        expr = expr.replace(term1 + " or " + term2, term2)
    
    # identity laws
    expr = expr.replace("0 and ", "0")
    expr = expr.replace("1 or ", "1")
    expr = expr.replace("0 or (", "")
    expr = expr.replace(") or 0", "")
    expr = expr.replace("1 and (", "")
    expr = expr.replace(") and 1", "")
    
    # distributive laws
    for term1 in expr.split("or"):
        for term2 in expr.split("or"):
            if term1 != term2:
                for term3 in expr.split("and"):
                    if term3 in term1 and term3 in term2:
                        expr = expr.replace(term1 + " or " + term2, term3 + " or (" + term1.replace(term3, "") + " and " + term2.replace(term3, "") + ")")
    
    return expr

expr = "not ((A and B) or (not A and C))"
optimized_expr = optimize_boolean(expr)
print(optimized_expr)





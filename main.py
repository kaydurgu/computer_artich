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

'''
iDENTITIES
  
 
A + 1 = 1	A in parallel with
closed = “CLOSED”	laws of boolean algebra universal circuit	Annulment
A + 0 = A	A in parallel with
open = “A”	laws of boolean algebra universal parallel	Identity
A . 1 = A	A in series with
closed = “A”	laws of boolean algebra universal circuit	Identity
A . 0 = 0	A in series with
open = “OPEN”	laws of boolean algebra universal series	Annulment
A + A = A	A in parallel with
A = “A”	idempotent parallel circuit	Idempotent
A . A = A	A in series with
A = “A”	idempotent series circuit	Idempotent
NOT A = A	NOT NOT A
(double negative) = “A”	 	Double Negation
A + A = 1	A in parallel with
NOT A = “CLOSED”	complement parallel circuit	Complement
A . A = 0	A in series with
NOT A = “OPEN”	complement series circuit	Complement
A+B = B+A	A in parallel with B =
B in parallel with A	absorption parallel circuit	Commutative
A.B = B.A	A in series with B =
B in series with A	absorption series circuit	Commutative

'''



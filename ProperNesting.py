def nest(s):
    result = s
    open_brackets = ['{','[','(']
    end_brackets = ['}',']',')']
    makeup = []
    holder = []
    for c in s:
        if c in open_brackets:
            holder.append(c)
        elif c in end_brackets:
            if not len(holder):
                if c == "}":
                    makeup.append("{")
                elif c == "]":
                    makeup.append("[")
                elif c == ")":
                    makeup.append("(")
            else:
                if c == "}" and holder.pop() != "{":
                    return "this is not a valid nest"
                elif c == "]" and holder.pop() != "[":
                    return "this is not a valid nest"
                elif c == ")" and holder.pop() != "(":
                    return "this is not a valid nest"

    for m in makeup:
        result = m + result
    
    for h in holder:
        if h == "(":
            result = result + ")"
        elif h == "{":
             result = result + "}"
        elif h == "[":
             result = result + "]"

    return result

print(26 // 5)
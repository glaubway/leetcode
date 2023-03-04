class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if p == ".*":
            return True
        if p == "." and len(s) == 1:
            return True
        if p[0] == "*":
            return False

        cache = {}
        
        def check_match(s_index, p_index):
            if (s_index, p_index) in cache:
                return cache[(s_index, p_index)]
            
            is_star = p_index+1 < len(p) and p[p_index+1] == "*"
            
            if s_index >= len(s):
                if p_index >= len(p):
                    return True
                elif is_star is True:
                    cache[(s_index, p_index)] = check_match(s_index, p_index+2)
                    return cache[(s_index, p_index)]
                else:
                    cache[(s_index, p_index)] = False
                    return cache[(s_index, p_index)]
                
            if p_index >= len(p):
                return False
            
            match = s[s_index] == p[p_index] or p[p_index] == "."
            
            if is_star is True and match is True:
                cache[(s_index, p_index)] = check_match(s_index, p_index+2) or check_match(s_index+1, p_index)
            elif is_star is True and match is False:
                cache[(s_index, p_index)] = check_match(s_index, p_index+2)
            elif is_star is False and match is True:
                cache[(s_index, p_index)] = check_match(s_index+1, p_index+1)
            elif is_star is False and match is False:
                cache[(s_index, p_index)] = False
				
            return cache[(s_index, p_index)]
        
        return check_match(0, 0)


testcases = [
    { 
        "string": "aa",
        "pattern": "a",
        "result": False
    },
    {
        "string": "aa",
        "pattern": "a*",
        "result": True
    },
    {
        "string": "ab",
        "pattern": ".*",
        "result": True
    },
    {
        "string": "aab",
        "pattern": "aa.",
        "result": True
    },
    {
        "string": "aab",
        "pattern": "c*a*b",
        "result": True
    }
]

for tescase  in testcases:
    result = Solution().isMatch(tescase["string"], tescase["pattern"])
    print("string: {} pattern: {} result: {} expexted result: {}".format(tescase["string"], tescase["pattern"], result, tescase["result"]))
    assert(result == tescase["result"])

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        # s=""
        # temp=[]
        
        # for char in formula:
        #     if char=="(":
        #         temp.append(s)
        #         s=""
        #     else:
        #         s+=char
        # print(temp)



        #####SOLUTION######

        def parse_formula(formula):
            tokens = re.findall(r'([A-Z][a-z]*|\d+|\(|\))', formula)
            return tokens

        def multiply_counts(counts, factor):
            for atom in counts:
                counts[atom] *= factor
            return counts

        def merge_counts(counts1, counts2):
            for atom, count in counts2.items():
                counts1[atom] += count
            return counts1

        tokens = parse_formula(formula)
        stack = []
        counts = collections.defaultdict(int)
        i = 0
        
        while i < len(tokens):
            token = tokens[i]
            
            if token == '(':
                stack.append(counts)
                counts = collections.defaultdict(int)
            elif token == ')':
                temp_counts = counts
                counts = stack.pop()
                i += 1
                factor = 1
                if i < len(tokens) and tokens[i].isdigit():
                    factor = int(tokens[i])
                    i += 1
                multiply_counts(temp_counts, factor)
                merge_counts(counts, temp_counts)
                continue
            elif token.isdigit():
                factor = int(token)
                atom = tokens[i - 1]
                counts[atom] += (factor - 1)
            else:
                counts[token] += 1
            
            i += 1
        
        sorted_atoms = sorted(counts.items())
        result = ''
        for atom, count in sorted_atoms:
            result += atom
            if count > 1:
                result += str(count)
        
        return result

        

class Solution:
    def fractionAddition(self, expression: str) -> str:
        from fractions import Fraction

        fractions = re.findall(r'[+-]?\d+/\d+', expression)
    
        # Step 2: Initialize result as Fraction object
        result = Fraction(0, 1)
        
        # Step 3: Add/Subtract all fractions
        for frac in fractions:
            result += Fraction(frac)
        
        # Step 4: Get the numerator and denominator
        numerator = result.numerator
        denominator = result.denominator
        
        # Step 5: Return the result as a string
        return f"{numerator}/{denominator}"
        
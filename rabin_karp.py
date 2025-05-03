class Solution:
    # Function to find the starting index of all occurrences of pattern in text
    def search(self, pat, txt):
        n = len(pat)
        m = len(txt)
        
        # Primes for Rabin-Karp algorithm
        p = 7
        mod = 101
        
        # To store the hash values of pattern and substring of text
        hashPat = 0
        hashText = 0
        
        pRight = 1
        pLeft = 1
        
        # Computing the initial hash values
        for i in range(n):
            hashPat = (hashPat + ((ord(pat[i]) - ord('a') + 1) * pRight) % mod) % mod
            hashText = (hashText + ((ord(txt[i]) - ord('a') + 1) * pRight) % mod) % mod
            pRight = (pRight * p) % mod
        
        # List to store the result
        ans = []
        
        # Traverse the text string
        for i in range(m - n + 1):
            
            # If the hash value matches
            if hashPat == hashText:
                # Add the index of the result if the substring matches
                if txt[i:i + n] == pat:
                    ans.append(i)
            
            # Updating the hash values
            if i < m - n:
                hashText = (hashText - ((ord(txt[i]) - ord('a') + 1) * pLeft) % mod + mod) % mod
                hashText = (hashText + ((ord(txt[i + n]) - ord('a') + 1) * pRight) % mod) % mod
                hashPat = (hashPat * p) % mod
                
                # Updating the prime multiples
                pLeft = (pLeft * p) % mod
                pRight = (pRight * p) % mod
        
        return ans  # Return the stored result

# Main code
if __name__ == "__main__":
    txt = "ababcabcababc"
    pat = "abc"
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the starting index 
    # of all occurrences of pattern in text
    ans = sol.search(pat, txt)
    
    # Output
    print("The starting indices of all occurrences of", pat, "in", txt, "are:", *ans)
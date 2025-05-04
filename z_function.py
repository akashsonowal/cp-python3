class Solution:
    # Compute the Z array for the combined string
    def computeZarray(self, s):
        n = len(s)  # size of string

        Z = [0] * n  # Z-array

        # Pointers to mark the window
        left, right = 0, 0

        # For every character
        for i in range(1, n):

            # Out of window
            if i > right:
                while i + Z[i] < n and s[i + Z[i]] == s[Z[i]]:
                    Z[i] += 1

            # Else (Inside the window)
            else:
                # Check for inside
                if i + Z[i - left] <= right:
                    Z[i] = Z[i - left]

                # Else compute again using brute force method
                else:
                    Z[i] = right - i + 1  # Take the answer till boundary

                    # Start matching beyond boundary using brute force
                    while i + Z[i] < n and s[i + Z[i]] == s[Z[i]]:
                        Z[i] += 1

            left, right = i, i + Z[i] - 1  # Update the window

        return Z  # Return the computed Z-array

    # Function to find all indices of pattern in text
    def search(self, text, pattern):
        s = pattern + '$' + text  # Combined string

        # Function call to find the Z array for the combined string
        Z = self.computeZarray(s)

        # Length of pattern and text
        n, m = len(text), len(pattern)

        # To store the result
        ans = []

        # Iterate on the combined string after the delimiter
        for i in range(m+1, len(s)):
            if Z[i] == m:
                ans.append(i - (m + 1))

        return ans


if __name__ == "__main__":
    text = "xyzabxyzabxyz"
    pattern = "xyz"

    # Creating an instance of the solution class
    sol = Solution()

    # Function call to find all indices of pattern in text
    ans = sol.search(text, pattern)

    for ind in ans:
        print(ind, end=" ")
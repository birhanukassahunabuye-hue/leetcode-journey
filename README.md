# LeetCode Journey

| Day | Problem | Pattern | Time | Result |
|-----|---------|---------|------|--------|
| 1 | Two Sum | Hashmap | 12 min | Solved (brute force first, rewrote to O(n)) |
| 1 | Palindrome Number | Math | 3 min | Solved (optimal, one trial) |
| 1 | Longest Common Prefix | Strings | 15 min | Solved (optimal, one trial) |
| 1 | Remove Element | Two Pointer | 5 min | Solved (self-caught unreachable duplicate return) |
| 1 | Maximum Subarray | Kadane's / DP-adjacent | 13 min | Solved (derived independently, first trial) |
| 1 | Valid Palindrome | String/Two Pointer | 12 min | Solved (correct but not optimal — used extra space; two-pointer in-place version needed) |
| 1 | Find Numbers with Even Digits | Loop/Math | 16 min | Solved (optimal, checked constraints first) |
| 2 | Contains Duplicate | Hashmap/Set | 10 min (4 min brute force + 6 min optimized) | Solved (self-corrected O(n²) to O(n)) |
| 2 | Valid Anagram | Hashmap | 13 min (sorting one-liner first, then optimized to O(n) hashmap) | Solved |
| 2 | Group Anagrams | Hashmap | 20 min | Solved (sorted-string-as-key, one trial) |
| 3 | Two Sum II (Sorted) | Two Pointer | 20 min | Solved (recognized sorted property → two-pointer immediately, one trial) |
| 3 | Valid Palindrome II | Two Pointer | 30 min | Solved (optimal — try-both-deletions branch on mismatch) |
| 3 | Merge Sorted Array | Two Pointer (merge from back) | 40 min | Solved (optimal — figured out third pointer independently after hint on back-to-front reasoning) |
| 4 | Best Time to Buy/Sell Stock | Sliding Window / Kadane's-adjacent | 25 min | Solved (optimal, single pass) |
| 4 | Longest Substring Without Repeating Chars | Sliding Window | 20 min | Solved (optimal, one trial — first genuine sliding window problem) |
| 4 | Maximum Average Subarray I | Sliding Window (fixed size) | 20 min | Solved (optimal — first attempt from left, pivoted to subtract/add technique) |
| 5 | Subarray Sum Equals K | Hashmap + Prefix Sum | 50 min | Solved (optimal — derived needed=curr_sum-k via paper trials, first prefix-sum problem) |
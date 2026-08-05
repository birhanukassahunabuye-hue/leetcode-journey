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
| 5 | 3Sum | Two Pointer + Sorting | 75 min | Solved (optimal — correctly handled all 3 duplicate-skip locations, abandoned set() approach after trial) |
| 6 | Valid Palindrome II (retention check) | Two Pointer | 6 min | Solved (Day 3 took 30 min — confirms retention, not one-time derivation) |
| 7 | Longest Repeating Character Replacement | Sliding Window | 50 min | Solved (optimal — stale max_freq trick) |
| 7 | Permutation in String | Sliding Window + Hashmap | 60 min | Solved (optimal — combined fixed-window + frequency comparison independently) |
| 8 | Minimum Window Substring | Sliding Window + Hashmap | 80 min | Solved (optimal — incremental formed/required counter, self-derived after two prior struggle sessions) |
| 9 | 4Sum | Two Pointer + Sorting | 60 min | Solved (extended 3Sum structure to two fixed elements, correctly handled nested duplicate-skipping; initially explored O(n) before recognizing O(n³) as necessary) |
| 10 | Reverse Linked List | Linked List | 10 min | Solved (optimal, first linked list problem, one trial) |
| 10 | Merge Two Sorted Lists | Linked List | 30 min | Solved (optimal — dummy node technique, one trial) |
| 11 | Linked List Cycle | Linked List (Floyd's algorithm) | 35 min | Solved (optimal, correctly reasoned through catch-up logic) |
| 11 | Reorder List | Linked List (find-middle + reverse + merge) | 45 min | Solved (optimal — synthesized 3 separate sub-skills independently) |
| 12 | Remove Nth Node From End of List | Linked List (two-pointer gap) | 45 min | Solved (optimal, one-pass, self-initiated dummy node use) |
| 12 | Valid Parentheses | Stack | 30 min | Solved (optimal, first stack problem, correctly handled all 3 edge cases) |
| 13 | Min Stack | Stack (design) | 40 min | Solved (optimal — parallel min-stack technique, self-derived) |
| 13 | Evaluate Reverse Polish Notation | Stack | 40 min | Solved (optimal — correctly reasoned through int() truncation vs floor division for negative numbers) |
| 14 | Daily Temperatures | Stack (monotonic stack) | 40 min | Solved (optimal — brute force first, then derived monotonic stack approach) |
| 14 | Implement Queue using Stacks | Queue (via two stacks) | 35 min | Solved (optimal — amortized O(1), correctly only transfers when stack2 is empty) |
| 15 | Number of Recent Calls | Queue | 20 min | Solved (correct logic; switched from list.pop(0) O(n) to deque O(1) after review) |
| 15 | Maximum Depth of Binary Tree | Tree (recursion) | 30 min | Solved (optimal, first tree problem, clean recursive solve) |
| 16 | Invert Binary Tree | Tree (recursion) | 35 min | Solved (optimal, clean recursive swap) |
| 16 | Same Tree | Tree (recursion, dual-tree comparison) | 40 min | Solved (optimal, correctly handled all 3 base cases) |
| 17 | Subtree of Another Tree | Tree (recursion + reuse) | 40 min | Solved (optimal-standard, correctly reused isSameTree as helper) |
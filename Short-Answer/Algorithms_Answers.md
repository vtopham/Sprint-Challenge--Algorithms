#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear. 
    When n is 1, the loop executes 1 time
    When n is 2, the loop executes 2 times
    When n is 3, the loop executes 3 times
    When n is 4, the loop executes 4 times


b) n^2 - Quadratic.
    When n is greater than one, one loop executes per n, and another inside loop executes per n - 1. n * n = n^2


c) O(n) - Linear. 
    This function recurses one per bunny, returning 2 each time to count the ears. Because it only recurses N times, this is O(n), also linear. There are a total of n function calls.

## Exercise II
---I'll be attaching a picture of this reasoning---
So, we know that there is a floor F, anything equal to or greater than F will result in a broken egg, while anything less than F is a safe egg. So we want to find the lowest floor that will still break the egg, which is F.

I hope this building has an elevator, because ***we're doing a binary search for a runtime complexity of log n!***

Start with a bottom floor possibility and a top floor possibility. We'll call them "lowest" and "highest". 

Repeat these steps until you return the correct floor:
    -If "lowest" = "highest" are next to eachother, then they are pointing to F. Break and return the correct floor.
    -Calculate a "test" floor to drop the egg from. It should be halfway between the "lowest" and the "highest" floor, rounded down.
    -Drop the egg from the "test" floor. 
        -If it doesn't break, set "lowest" to the floor above this floor and repeat these steps.
        -If it does break, then you know you are on a floor that is either your target floor, or above it. So set your "highest" floor to be this floor.
        

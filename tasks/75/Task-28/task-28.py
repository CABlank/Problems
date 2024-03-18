from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        # Initialize the queues with indices of senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            # Get the index of the next senator from each party
            r = radiant.popleft()
            d = dire.popleft()

            # The senator with the lower index (i.e., gets to act first) bans the other
            if r < d:
                # If the radiant senator acts, push them to the end of the queue with an incremented index
                radiant.append(r + len(senate))
            else:
                # If the dire senator acts, push them to the end of the queue with an incremented index
                dire.append(d + len(senate))

        # Whichever party still has senators left wins
        return "Radiant" if radiant else "Dire"
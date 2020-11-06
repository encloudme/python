from random import randint


class LuckyBall:
    def __init__(self):
        self.nums = []
        while len(self.nums) < 6:
            rand_num = randint(1, 69)
            if rand_num not in self.nums:
                self.nums.append(rand_num)

    def __getitem__(self, index):
        return self.nums[index]

    def __len__(self):
        return len(self.nums)


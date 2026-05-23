sweet_tooth = set(input().split())

n = int(input())

friends_likes = set()

for _ in range(n):
    friends_likes.update(input().split())
only_sweet_tooth = sweet_tooth - friends_likes
print(len(only_sweet_tooth))
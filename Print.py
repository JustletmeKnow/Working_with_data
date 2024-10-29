
class Invites:
    lists = ['Dad', 'Mom', 'Sister', 'Girlfriend']
    lists.remove(lists[1])
    lists.insert(1, 'Brother')
    lists.insert(0, 'Friend')
    lists.insert(-1, 'No')
    lists.append('?')
    lists.sort(reverse=True)
    sorted(lists)
    ls = 0
    print(f"Also was invited {len(lists)} people")
    for elem in lists:
        print(f"'Invite for ' {elem}")
        ls += 1
        li = ls - 2
    for i in range(li):
        print(f"Sorry but you was removed :) {lists.pop()}")
    print(f"Also was invited {len(lists)} people")
    squares = [numbers**2 for numbers in range(1,20,2)]
    print(squares)
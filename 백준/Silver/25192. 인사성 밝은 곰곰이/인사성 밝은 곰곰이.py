n = int(input())
records = [input().strip() for _ in range(n)]

def count_gomgom_mentions(records):
    gomgom_count = 0
    current_users = set() #중복 허용 x
    for record in records:
        if record == "ENTER":
            current_users.clear()
        else:
            if record not in current_users:
                current_users.add(record)
                gomgom_count += 1

    return gomgom_count



result = count_gomgom_mentions(records)

print(result)
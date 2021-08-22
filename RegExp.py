import re
def solution(card_numbers):
    answer = []
    num = 0
    a,b = 0, 0
    for numbers in card_numbers:
        
        if re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}').match(numbers) or re.compile(r'\d{16}').match(numbers):
            num = re.sub(r"[^0-9]","",numbers)
            for i in range(len(num)):
                n = int(num[i])
                if i%2 == 0:
                    if n * 2>=10:
                        a =a + ((n*2)%10)+((n*2)//10)
                    else:
                        a= a + (n*2)
                else:
                    b = b + n
            if (a + b) % 10 == 0:
                answer.append(1)
            else:
                answer.append(0)
            num = 0
            a,b = 0, 0
        else:
            answer.append(0)
            continue

    return answer

print(solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]))
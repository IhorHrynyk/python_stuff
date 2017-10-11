#! python
#coding: utf-8

ticketNum = input('ticket number:')
ticketNum = list(map(int, ticketNum))

if len(ticketNum) % 2 == 1:
	ticketNum.remove(ticketNum[ int(len(ticketNum) / 2) ])

#print(''.join(str(ticketNum)))

part1 = []
part2 = []

for i in range(int(len(ticketNum) / 2)):
	part1.append(ticketNum[i])

for i in range(int(len(ticketNum) / 2), len(ticketNum)):
	part2.append(ticketNum[i])


if ticketNum[0] == sum(ticketNum) / len(ticketNum):
	print(True)
elif sum(part1) == sum(part2):
	print(True) 
else:
	print(False)

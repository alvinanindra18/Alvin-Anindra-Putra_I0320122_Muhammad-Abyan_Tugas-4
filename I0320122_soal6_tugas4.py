
x = 4
y = 11

#a bitwise OR (|)
z = x | y
print('\n**********OR**********')
print('nilai :',x,' , binary :', format(x,'08b'))
print('nilai :',y,' , binary :', format(y,'08b'))
print('------------------------------------------ (|)')
print('nilai :',z,' , binary :', format(z,'08b'))

#b shif right (>>)
z = x >> y
print('\n**********>>**********')
print('nilai :',x,' , binary :', format(x,'08b'))
print('nilai :',y,' , binary :', format(y,'08b'))
print('---------------------------------------- (>>)')
print('nilai :',z,' , binary :', format(z,'08b'))

#c bitwise XOR (^)
z = x ^ y
print('\n**********XOR**********')
print('nilai :',x,' , binary :', format(x,'08b'))
print('nilai :',y,' , binary :', format(y,'08b'))
print('----------------------------------------- (^)')
print('nilai :',z,' , binary :', format(z,'08b'))

#d bitwise NOT (~)
y = ~x
print('\n**********NOT**********')
print('nilai :',x,' , binary :', format(x,'08b'))
print('----------------------------------------- (~)')
print('nilai :',z,' , binary :', format(z,'08b'))

#e bitwise AND (&)
z = y & x
print('\n**********AND**********')
print('nilai :',y,' , binary :', format(y,'08b'))
print('nilai :',x,' , binary :', format(x,'08b'))
print('---------------------------------------- (&)')
print('nilai :',z,' , binary :', format(z,'08b'))
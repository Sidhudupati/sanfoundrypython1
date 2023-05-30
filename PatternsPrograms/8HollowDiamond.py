for i in range(1, 6):
    if i == 1 or i == 5:
        print(' ' * (5 - i) + '* ' * i)
    else:
        print(' ' * (5 - i) + '*' + ' ' * (2 * i - 3) + '*')
for i in range(4, 0, -1):
    if i == 1 or i == 5:
        print(' ' * (5 - i) + '* ' * i)
    else:
        print(' ' * (5 - i) + '*' + ' ' * (2 * i - 3) + '*')

'''
    * 
   * *
  *   *
 *     *
* * * * *
 *     *
  *   *
   * *
    *

'''

second = int(input('Введите секунды: '))
hh = second // 3600
mm = (second - hh * 3600) // 60
ss = second - (hh * 3600 + mm * 60)

print('%d:%02d:%02d' % (hh, mm, ss))

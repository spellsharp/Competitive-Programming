a, b = list(map(int, input().split()))
hours_lit_up = 0
candles = a
while candles >= b:
    new_candles = candles // b
    candles = candles % b + new_candles
    #we take (candles % b) as we need to also keep count of the number of spent candles used in making a new candle
    hours_lit_up += new_candles * b
hours_lit_up += candles

print(hours_lit_up)
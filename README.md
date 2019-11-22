# Split the bill

Disclaimer: this is a quick hack to split the bill amongst friends :)

(there is no error handling or unit test, use at the risk of your own friendships)

```python
 bill = Bill('''
    kerry hack litv
    7 stange 4.50 hllkkkk
    2 soave_1dl 5.80 hl
    3 genovese 17.8 hhk
    1 gnocchi 17 l
    1 hofli 17.8 l
    1 pizza_carpaccio 24.8 k
    1 pizza_tonnato 19.8 k
    1 pizza_kids 10.8 hkl
    ''')

  print(bill)
```

outputs

```
# Kerry
4.00 stange 18.00
1.00 genovese 17.80
1.00 pizza_carpaccio 24.80
1.00 pizza_tonnato 19.80
0.33 pizza_kids 3.60
Total = 84.00

# Hack
1.00 stange 4.50
1.00 soave_1dl 5.80
2.00 genovese 35.60
0.33 pizza_kids 3.60
Total = 49.50

# Litv
2.00 stange 9.00
1.00 soave_1dl 5.80
1.00 gnocchi 17.00
1.00 hofli 17.80
0.33 pizza_kids 3.60
Total = 53.20

# Grand total = 186.70
```


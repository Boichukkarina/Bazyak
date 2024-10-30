# Перебираем все столбцы в DataFrame df
for col in df.columns: 
    # Вычисляем долю пропущенных значений в текущем столбце
    pct_missing = np.mean(df[col].isnull()) 
    
    # Выводим название столбца и процент пропущенных значений, округляя до целого числа
    print('{} - {}%'.format(col, round(pct_missing*100)))

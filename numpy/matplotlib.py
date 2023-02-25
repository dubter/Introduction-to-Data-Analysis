def knn(features, train_features, train_target, k=1):
    '''
    Предсказание целевого признака для данных features -- pandas-таблица данных.
    на основе обучающего набора данных train_features, train_target.
    Возвращает pandas.Series с теми же индексами, что и у features.
    Число k -- количество соседей.
    '''

    predicted = pd.Series(index=features.index)

    # Заменяем строки на числа если колонка 'Sex' существует
    try:
        features['Sex'][features['Sex'] == 'male'] = 0
        features['Sex'][features['Sex'] == 'female'] = 1
        train_features['Sex'][train_features['Sex'] == 'male'] = 0
        train_features['Sex'][train_features['Sex'] == 'female'] = 1
    except:
        pass

    # Ищем ближайшие k точек из train_features для каждой точки из features
    nearest_points = find_nearest_points(features.values, train_features.values, k)

    # Для каждой точки из features
    for i in range(features.shape[0]):
        # Находим индексы k ближайших точек из train_features
        nearest_points_indices = nearest_points[i]
        # Находим значения целевого признака для найденных точек
        nearest_points_target = train_target.iloc[nearest_points_indices]
        # Выбираем наиболее часто встречающееся значение целевого признака
        predicted.iloc[i] = nearest_points_target.value_counts().index[0]

    return predicted
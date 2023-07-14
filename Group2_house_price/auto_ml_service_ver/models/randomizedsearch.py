from sklearn.model_selection import RandomizedSearchCV

# Задача регрессии
grid_reg = RandomizedSearchCV(
            lgb.LGBMRegressor(verbose=0),          # Алгоритм, в котором будем подбирать параметры
            param_distributions = {                 # Сетка параметров в виде словаря
                'max_depth': range(2, 7),
                'lr': np.linspace(0.001, 0.3, 100),
            },
            scoring = 'neg_mean_absolute_error',
            cv = 3,                                 # CV для кросс-валидации (число или индексы)
            n_jobs = -1,                            # Число используемых ядер для работы
            return_train_score = True,              # Считать ли метрики на обучающей части
            n_iter=30,                              # Число итераций (сколько будем брать случайных наборов)
            verbose = 5,                            # Чем больше, тем алгоритм разговорчивее
        )

# Обучим сетку на обучающем датасете при помощи метода fit
grid_reg.fit(X_train, y_reg_train)

# Выведем набор лучших параметров (они хранятся в best_params_) и лучшую метрику

print(f"Лучшая метрика:   {grid_reg.best_score_}")
print(f"Лучшие параметры: {grid_reg.best_params_}")

import shap
explainer_reg = shap.TreeExplainer(grid_reg.best_estimator_)
shap_values_reg = explainer_reg.shap_values(X_train)

# Посторим график важности фичей, вызвав summary_plot из библиотеки shap для регрессии
shap.summary_plot(shap_values_reg, X_train, max_display=25, auto_size_plot=True)
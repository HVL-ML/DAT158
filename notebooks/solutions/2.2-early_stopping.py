sgd_reg = SGDRegressor(learning_rate='constant', warm_start="True", eta0=0.0005, random_state=10,
                      max_iter=1000)
sgd_reg.fit(X_train_poly_scaled, y_train)
y_val_predict_best = sgd_reg.predict(X_val_poly_scaled)
print(mean_squared_error(y_val_predict_best, y_val))
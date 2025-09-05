from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler
scaler = StandardScaler()

# Fit and transform the training and test data using the scaler
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train an SGDClassifier
sgd_clf_scaled = SGDClassifier(random_state=20)
sgd_clf_scaled.fit(X_train_scaled, y_train)

# Compute the cross-validation predictions on the scaled training set
y_train_pred = cross_val_predict(sgd_clf, X_train_scaled, y_train, cv=5)

# Print the accuracy, confusion matrix, and F1 score
print("Cross-validation results on the scaled training set:")
print(f"Accuracy: {accuracy_score(y_train, y_train_pred)}")
print(f"Confusion matrix:\n{confusion_matrix(y_train, y_train_pred)}")
print(f"F1 score: {f1_score(y_train, y_train_pred)}")

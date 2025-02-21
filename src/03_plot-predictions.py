# Visualize the model predictions on the testing set
plt.scatter(X_test.loc[y_pred == 0, "feature_1"], X_test.loc[y_pred == 0, "feature_2"], c="b", label="Class 0")
plt.scatter(X_test.loc[y_pred == 1, "feature_1"], X_test.loc[y_pred == 1, "feature_2"], c="r", label="Class 1")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.savefig("predictions.png")  # Save the plot to a PNG file
plt.close()
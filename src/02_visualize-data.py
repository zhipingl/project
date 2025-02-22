# Visualize the dataset
plt.scatter(df.loc[df["target"] == 0, "feature_1"], df.loc[df["target"] == 0, "feature_2"], c="b", label="Class 0")
plt.scatter(df.loc[df["target"] == 1, "feature_1"], df.loc[df["target"] == 1, "feature_2"], c="r", label="Class 1")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.savefig("dataset-image.png")  # Save the plot to a PNG file
plt.close()
plt.show()
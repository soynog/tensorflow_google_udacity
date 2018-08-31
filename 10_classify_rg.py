# Classify data using a simple linear regression model
print("CLASSIFYING...")

from sklearn.linear_model import LogisticRegression

logistic_model = sklearn.linear_model.LogisticRegression()

t_sample_size = 500
v_sample_size = 100

# sample & flatten data into a 2-D matrix
sample_train_data = train_dataset[:t_sample_size].reshape(t_sample_size, 28*28)
sample_train_labels = train_labels[:t_sample_size]
sample_valid_data = valid_dataset[:v_sample_size].reshape(v_sample_size, 28*28)
sample_valid_labels = valid_labels[:v_sample_size]

fit_logistic = logistic.fit(sample_train_data, sample_train_labels)
score = fit_logistic.score(sample_valid_data, sample_valid_labels)

print("SCORE: " + str(score))

# CHECK FOR DUPLICATE IMAGES

# Compares two matrices and returns true if they're within a given tolerance
def compare_matrices(a, b, tolerance=0.0):
    return np.sqrt(sum(sum((a - b)**2))) <= tolerance

# How much of training dataset overlaps with validation dataset?
train_size, valid_size, test_size = len(train_dataset), len(valid_dataset), len(test_dataset)

valid_overlap, test_overlap = 0.0, 0.0
valid_per, test_per = 0.0, 0.0

# take a sample of the training set
sample_size = 100
np.random.shuffle(train_dataset)
train_sample = train_dataset[:sample_size]

for i, train_img in enumerate(train_sample):
    for j, valid_img in enumerate(valid_dataset):
        # print("...with validation img {n} of {size}".format(n=j,             size=valid_size))
        if compare_matrices(train_img,valid_img):
            valid_overlap += 1
            print("VALID OVERLAP %s" % valid_overlap)
            valid_per = valid_overlap / i * 100
            break
    for k, test_img in enumerate(test_dataset):
        # print("...with test img {n} of {size}".format(n=k, size=test_size))
        if(compare_matrices(train_img,test_img)):
            test_overlap += 1
            print("TEST OVERLAP %s" % test_overlap)
            test_per = test_overlap / i * 100
            break
    print("Comparing training img {n} of {size}... valid overlap %{valid_per}, test overlap %{test_per}".format(n=i, size=sample_size, valid_per=valid_per, test_per=test_per))


print("TEST OVERLAP: %s" % test_overlap)
print("VALIDATION OVERLAP: %s" % valid_overlap)

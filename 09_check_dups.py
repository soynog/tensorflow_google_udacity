# CHECK FOR DUPLICATE IMAGES

# Compares two matrices and returns true if they're within a given tolerance
def compare_matrices(a, b, tolerance=0.0):
    if tolerance == 0.0:
        return (a == b).all()
    else:
        return ((a - b) <= tolerance).all()

# Calculates overlap between two lists of matrices, returning a boolean matrix
def calculate_overlap(A, B, log=False):
    overlap = np.zeros([len(A), len(B)])
    for i,a in enumerate(A):
        if log:
            print(i)
        for j,b in enumerate(B):
            overlap[i,j] = int(compare_matrices(a,b))
    return overlap

# Prints out the overlap between two datasets, and returns a matrix of which elements overlap with which
def display_overlap(A,B, a_label="A", b_label="B"):
    print("CALCULATING OVERLAP B/W " + a_label + " AND " + b_label)
    Overlap = calculate_overlap(A,B,log=True)
    a_b_over_per = sum([i.any() for i in Overlap]) / float(len(A)) * 100
    b_a_over_per = sum([i.any() for i in Overlap.T]) / float(len(B)) * 100
    print(a_label + " overlap with " + b_label + ": %" + str(a_b_over_per))
    print(b_label + " overlap with " + a_label + ": %" + str(b_a_over_per))
    return Overlap

# Calculate overlap between TRAINING and VALIDATION
display_overlap(train_dataset,valid_dataset,a_label="TRAIN",b_label="VALID")

# Calculate overlap between TRAINING and TEST
display_overlap(train_dataset,test_dataset,a_label="TRAIN",b_label="TEST")

# Calculate overlap between TEST and VALIDATION
display_overlap(test_dataset,valid_dataset,a_label="TEST",b_label="VALID")

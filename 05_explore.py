# EXPLORE THE DATA

print("EXPLORING...")

# imgs = pickle.load(open(train_datasets[0], 'r'))
print(imgs_a.shape)

# plt.figure()
# plt.imshow(imgs_a[0])
# plt.colorbar()
# plt.gca().grid(False)

letter_labels = ['a','b','c','d','e','f','g','h','i','j']

plt.figure(figsize=(10,10))
for l in range(10):
    imgs = pickle.load(open(train_datasets[l], 'r'))
    for i in range(10):
        plt.subplot(10,10, (l*10 + i + 1) )
        plt.xticks([])
        plt.yticks([])
        plt.grid('off')
        # Display a random sampling of each letter
        plt.imshow(imgs[np.random.randint(0,len(imgs))], cmap=plt.cm.binary)
        plt.xlabel(letter_labels[l])

plt.show()

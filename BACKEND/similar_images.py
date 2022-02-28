from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def check_similarity(I1,I2):

    def mse(imageA, imageB):
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err

    def compare_images(imageA, imageB, title):
        # compute the mean squared error and structural similarity
        # index for the images
        m = mse(imageA, imageB)
        s = ssim(imageA, imageB)
        if s != 1:
            print("dissimilar images")
        else:
            print("similar images")
        # setup the figure
        fig = plt.figure(title)
        plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
        # show first image
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(imageA, cmap=plt.cm.gray)
        plt.axis("off")
        # show the second image
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(imageB, cmap=plt.cm.gray)
        plt.axis("off")
        # show the images
        #plt.show()

    # and the original + photoshop
    original = cv2.imread(I1)
    other = cv2.imread(I2)
    # convert the images to grayscale
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    other = cv2.cvtColor(other, cv2.COLOR_BGR2GRAY)


    # initialize the figure
    fig = plt.figure("Images")
    images = ("Original", original), ("Other", other)
    # loop over the images
    for (i, (name, image)) in enumerate(images):
        # show the image
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")
    # show the figure
    
    # compare the images
    return compare_images(original, other, "Original vs. other")


check_similarity("/Users/cosmos/Desktop/SIH - MAIN/sih ref/datasets/images/NEW/0.jpg","/Users/cosmos/Desktop/SIH - MAIN/sih ref/datasets/images/NEW/1.jpg")
    

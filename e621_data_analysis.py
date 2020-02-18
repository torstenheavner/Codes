from operator import *

import matplotlib.pyplot as plt
from numpy import *
from yippi import *

images = search.post(["order:random"], "order:random", limit=10000)
images2 = search.post([], "order:random", limit=10000, page=2)
images3 = search.post([], "order:random", limit=10000, page=3)
images4 = search.post([], "order:random", limit=10000, page=4)
images5 = search.post([], "order:random", limit=10000, page=5)
images6 = search.post([], "order:random", limit=10000, page=6)
images7 = search.post([], "order:random", limit=10000, page=7)
images8 = search.post([], "order:random", limit=10000, page=8)

s = 0
q = 0
e = 0
sizes = []
sizes_s = []
sizes_q = []
sizes_e = []

all = [images, images2, images3, images4, images5, images6, images7, images8]
authors = {}
tags = {}

for images in all:
    for image in images:
        if image.rating == "s":
            s += 1
            sizes_s.append(image.file_size)
        elif image.rating == "q":
            q += 1
            sizes_q.append(image.file_size)
        elif image.rating == "e":
            e += 1
            sizes_e.append(image.file_size)
        sizes.append(image.file_size)
        try:
            authors[image.author] += 1
        except:
            authors[image.author] = 1
        for tag in image.tags:
            try:
                tags[tag] += 1
            except:
                tags[tag] = 1

# plt.plot([1, 2, 3], [s, q, e])
# plt.show()

mostCommonAuthor = max(authors.items(), key=itemgetter(1))[0]
mostUsedTag = max(tags.items(), key=itemgetter(1))[0]
points = []

print("\n\n")
print("Total............................%s" % (s + q + e))
print("Average Rating...................%s" % (((s * 1) + (q * 2) + (e * 3)) / (s + q + e)))
print("Average File Size................%s" % (mean(sizes) / 10000))
print("Average Safe File Size...........%s" % (mean(sizes_s) / 10000))
print("Average Questionable File Size...%s" % (mean(sizes_q) / 10000))
print("Average Explicit File Size.......%s" % (mean(sizes_e) / 10000))
print("Most Common Author...............%s (%s)" % (mostCommonAuthor, authors[mostCommonAuthor]))
print("Most Used Tag....................%s (%s)" % (mostUsedTag, tags[mostUsedTag]))
print("\n\n")
print("Top 10 Authors")
for i in range(10):
    tempAuthor = max(authors.items(), key=itemgetter(1))[0]
    print("%s - %s" % (authors[tempAuthor], tempAuthor))
    points.append(authors[tempAuthor])
    authors[tempAuthor] = 0
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], points)
plt.show()
points = []
print("\n")
print("Top 100 Tags")
for i in range(100):
    tempTag = max(tags.items(), key=itemgetter(1))[0]
    print("%s - %s" % (tags[tempTag], tempTag))
    points.append(tags[tempTag])
    tags[tempTag] = 0
plt.plot(points)
plt.show()

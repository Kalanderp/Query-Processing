import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
plt.barh(languages, popularity, color='green')
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.show()

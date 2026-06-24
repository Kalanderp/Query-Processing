import matplotlib.pyplot as plt 
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7] 
plt.bar(languages, popularity, color='blue')
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.xlabel('Languages')
plt.ylabel('Popularity') 
plt.show()

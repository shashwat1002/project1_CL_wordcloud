import matplotlib.pyplot as plt
import matplotlib as mp1

mp1.rcParams['font.sans-serif'] = [
    'sans-serif',
    'Lohit Devanagari'
]

def plotter_of_counter(title, counter_obj, number):
    # takes a counter object and plots appropriately
    list_to_plot = counter_obj.most_common(number)
    word_list = []
    frequency_list = []
    for tup in list_to_plot:
        word_list.append(tup[0])
        frequency_list.append(tup[1])

    plt.bar(word_list, frequency_list)
    plt.title(title)
    plt.xlabel("words")
    plt.ylabel("frequency")
    plt.xticks(rotation=45)
    plt.show()

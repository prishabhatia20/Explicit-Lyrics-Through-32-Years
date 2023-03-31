"""
This file contains functions to create all the graphs
for the computational essay
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud


def plot_all_words(csv_file):
    """
    This function plots the history of each curse word we are searching for.
    It takes in a CSV file and outputs a plot.

    Args:
        csv_file: the name of the file that needs to be plotted (output1990-2022.csv)
    """
    # Create an empty list for every curse word
    data = []
    sex = []
    hell = []
    fuck = []
    shit = []
    ass = []
    bitch = []
    cunt = []
    dick = []
    slut = []
    pussy = []
    crap = []
    cock = []
    penis = []
    bussy = []
    motherfucker = []
    hoe = []
    whore = []
    munch = []

    # Open the CSV file and append the data in each row into the corresponding list
    with open(csv_file, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        # row_number = 0
        for row in reader:
            # word_list[row_number].append(int(row[row_number]))
            data.append(int(row[0]))
            sex.append(int(row[1]))
            hell.append(int(row[2]))
            fuck.append(int(row[3]))
            shit.append(int(row[4]))
            ass.append(int(row[5]))
            bitch.append(int(row[6]))
            cunt.append(int(row[7]))
            dick.append(int(row[8]))
            slut.append(int(row[9]))
            pussy.append(int(row[10]))
            crap.append(int(row[11]))
            cock.append(int(row[12]))
            penis.append(int(row[13]))
            bussy.append(int(row[14]))
            motherfucker.append(int(row[15]))
            hoe.append(int(row[16]))
            whore.append(int(row[17]))
            munch.append(int(row[18]))

    # Set the figure size to be 10 x 10
    figure_size = plt.figure()
    figure_size.set_figwidth(10)
    figure_size.set_figheight(10)

    # Plot all the data
    plt.plot(data, sex, label="Sex")
    plt.plot(data, hell, label="Hell")
    plt.plot(data, fuck, label="Fuck")
    plt.plot(data, shit, label="Shit")
    plt.plot(data, ass, label="Ass")
    plt.plot(data, bitch, label="Bitch")
    plt.plot(data, cunt, label="Cunt")
    plt.plot(data, dick, label="Dick")
    plt.plot(data, slut, label="Slut")
    plt.plot(data, pussy, label="Pussy")
    plt.plot(data, crap, label="Crap")
    plt.plot(data, cock, label="Cock")
    plt.plot(data, penis, label="Penis")
    plt.plot(data, bussy, label="Bussy")
    plt.plot(data, motherfucker, label="Motherfucker")
    plt.plot(data, hoe, label="Hoe")
    plt.plot(data, whore, label="Whore")
    plt.plot(data, munch, label="Munch")

    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Bad Words vs Years")
    plt.legend()
    plt.show()


def plot_total_trend(csv_file):
    """
    Same as the function above, this function takes in the output1990-2022
    csv file and returns a graph, this time of the average trend of curse words
    throughout the years

    Args:
        csv_file: a CSV file containing the curse word data for 32 years
    """
    total_per_year = []
    # Open the CSV file
    with open(csv_file, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            word = 0
            for i in range(1, 19):
                word += int(row[i])
            total_per_year.append(word)
    timestep = np.arange(1990, 2023, 1)

    figure_size = plt.figure()
    figure_size.set_figwidth(10)
    figure_size.set_figheight(10)

    plt.plot(timestep, total_per_year)
    plt.xlabel("Time")
    plt.ylabel("Number of Bad Words")
    plt.title("Total Bad Words Over Time")
    plt.show()


def plot_word_bank(csv_file):
    """
    This function takes in the output1990-2022 CSV file and returns
    a word bank. The bigger the word is, the more common it was. The smaller
    the word is, the less common it was in the lyrics.

    Args:
        csv_file: a CSV file containing the curse word data for 32 years
    """

    word_total_bank = []

    for i in range(1, 19):
        word = 0
        with open(csv_file, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                word += int(row[i])
        word_total_bank.append(word)

    bad_word_bank = [
        "sex",
        "hell",
        "fuck",
        "shit",
        "ass",
        "bitch",
        "cunt",
        "dick",
        "slut",
        "pussy",
        "crap",
        "cock",
        "penis",
        "bussy",
        "motherfucker",
        "hoe",
        "whore",
        "munch",
    ]
    word_counter_dict = dict(zip(bad_word_bank, word_total_bank))

    # Create a WordCloud object with font size proportional to the values in the dictionary
    wordcloud = WordCloud(
        width=800, height=800, background_color="white", min_font_size=10
    )
    wordcloud.generate_from_frequencies(frequencies=word_counter_dict)

    # Display the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

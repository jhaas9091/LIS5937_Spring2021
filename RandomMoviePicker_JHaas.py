"""Final Project
Julie Haas
LIS 5937 - Python for Data Sci Prof
Spring 2021"""


import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, QInputDialog
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.initUI()
        self.df = pd.read_excel('Movie_List.xlsx')

    def initUI(self):
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        self.setGeometry(500,500,800,300)
        self.setWindowTitle('Movie Picker Program')

        listbtn = QPushButton("Show List of Movies")  # show list button is 1/2 of one row
        listbtn.clicked.connect(self.list_movies)
        hbox.addWidget(listbtn)

        statsbtn = QPushButton("Show List Analysis")  # show analysis button shares same row with show list
        statsbtn.clicked.connect(self.analyze_list)
        hbox.addWidget(statsbtn)

        addbtn = QPushButton("Add Movie")  # add movie button is 1/2 of another row
        addbtn.clicked.connect(self.add_movie)
        hbox2.addWidget(addbtn)

        rembtn = QPushButton("Remove Movie")  # remove movie button shares same row as add movie
        rembtn.clicked.connect(self.remove_movie)
        hbox2.addWidget(rembtn)

        rndmbtn = QPushButton("Pick Random Movie")    # wide random movie picker button in its own row
        rndmbtn.clicked.connect(self.random_picker)
        vbox.addWidget(rndmbtn)

        btn4 = QPushButton("Quit")  # alternative to closing window through X button
        btn4.clicked.connect(self.exit_program)
        vbox.addWidget(btn4)

        self.show()

    def random_picker(self):
        mbox = QMessageBox()  # enable pop-out message

        message = str(self.df.sample(n=1, replace=False, random_state=None))
        mbox.setText(message)  # pull 1 random row from movie list and show in pop-out window

        mbox.setWindowTitle("Random Pick")  # set title of pop-out window
        mbox.setStandardButtons(QMessageBox.Ok)  # option for user to click ok to close the window

        mbox.exec_()

    def list_movies(self):
        mbox = QMessageBox()  # enable pop-out message

        message = str(self.df)  # turn dataframe into readable string for message window
        mbox.setText(message)

        mbox.setWindowTitle("List of Movies")  # set title of pop-out window
        mbox.setStandardButtons(QMessageBox.Ok)  # user can click ok to close the window

        mbox.exec_()

    def analyze_list(self):
        fig1, ax1 = plt.subplots()  # will allow me to join two pie charts into one
        df1 = pd.value_counts(self.df['Streaming_Service'].values, sort=True).plot.pie()  # shows pie chart with name labels
        df2 = pd.value_counts(self.df['Streaming_Service'].values, sort=True)
        ax1.pie(df2, autopct='%1.1f%%')  # shows pie chart with percentages in wedges
        axis = ('equal')  # keeps pie chart circular
        ax1.set_title("Percentage of Movies per Streaming Service")
        plt.ylabel("")  # hide y label, otherwise it shows "None"
        plt.show()

    def add_movie(self):
        mbox = QMessageBox()  # enable pop-out message

        title, ok = QInputDialog.getText(self, 'Add Movie Title', 'Enter Movie Title:')  # ask user for input
        if ok:
            if any(self.df['Title'] == title):  # check for a duplicate title already in list
                mbox.setWindowTitle("Error!")  # title already exists so don't continue with add
                mbox.setText("Title is already in the list.")
                mbox.setStandardButtons(QMessageBox.Ok)
                mbox.exec_()
            else:
                stream, ok = QInputDialog.getText(self, 'Add Streaming Service', 'Enter Streaming Service:')  # ask user for input
                if ok:  # accept user input and add it as a new row in excel file
                    new_row = {'Title': title, 'Streaming_Service': stream}
                    self.df = self.df.append(new_row, ignore_index=True, verify_integrity=True)
                    self.df.to_excel('Movie&TV_List.xlsx', index=False)

                    mbox.setWindowTitle("Success!")  # confirm successful entry
                    mbox.setText("Title has been added.")
                    mbox.setStandardButtons(QMessageBox.Ok)
                    mbox.exec_()

    def remove_movie(self):
        mbox = QMessageBox()  # enable pop-out message

        title, ok = QInputDialog.getText(self, 'Add Movie Title', 'Enter Movie Title:')  # ask for user input
        if ok:
            if any(self.df['Title'] == title):  # check to see if title is in the list
                title_row = self.df[self.df['Title'] == title].index
                self.df.drop(title_row, inplace=True)
                self.df.to_excel('Movie&TV_List.xlsx', index=False)

                mbox.setWindowTitle("Success!")  # confirm removal of title
                mbox.setText("Title has been removed")
                mbox.setStandardButtons(QMessageBox.Ok)
                mbox.exec_()
            else:
                mbox.setWindowTitle("Error!")  # title doesn't exist so don't continue with remove
                mbox.setText("Title is not in the list.")
                mbox.setStandardButtons(QMessageBox.Ok)
                mbox.exec_()


    def exit_program():
        sys.exit()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')  # add style to make GUI look a little more modern
    main_window = Window()
    sys.exit(app.exec_())

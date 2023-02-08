import pandas as pd
import json


class convertion_csv:
    def __init__(self, file):
        self.df= file

    def json_to_csv_que(self):
        df_csv = pd.DataFrame()
        df_csv1 = pd.DataFrame()
        name1 = []
        timestamp1 = []
        userid1 = []
        location = []
        source = []

        name = []
        timestamp = []
        userid = []
        time_taken = []
        time_to_complete = []

        for i in self.df["IDC"]:
            for j in self.df["IDC"][i]:
                if j == 'dateTime':
                    break
                else:
                    
                    time_taken.append(self.df["IDC"][i][j]["timeSpent"]["timeAI"])
                    time_to_complete.append(self.df["IDC"][i][j]["timeSpent"]["timeHomeScreen"])
                    name.append(self.df["IDC"][i][j]["name"])
                    timestamp.append(self.df["IDC"][i][j]["dateTime"])
                    userid.append(self.df["IDC"][i][j]["userId"])
                    
                    for k in self.df["IDC"][i][j]:
                        if self.df["IDC"][i][j].get("questionsData"):
                            for q in self.df["IDC"][i][j]["questionsData"]:
                                name1.append(self.df["IDC"][i][j]["name"])
                                timestamp1.append(self.df["IDC"][i][j]["dateTime"])
                                userid1.append(self.df["IDC"][i][j]["userId"])
                                location.append(q["location"])
                                source.append(q["source"])

        df_csv1["name"] = name1
        df_csv1["timestamp"] = timestamp1
        df_csv1["userid"] = userid1
        df_csv1["location"] = location
        df_csv1["source"] = source
        df_csv["userid"] = userid
        df_csv["timestamp"] = timestamp
        df_csv["name"] = name
        df_csv["time_taken"] = time_taken
        df_csv["time_to_complete"] = time_to_complete

        return df_csv, df_csv1

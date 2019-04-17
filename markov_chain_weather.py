import numpy as np
import random as rm

# state of weather
states = ["Cloudy", "Sunny", "Rainy"]

# possibles sequences of events
transitionName = [["CC", "CS", "CR"], ["SC", "SS", "SR"], ["RC", "RS", "RR"]]

# probabilities
# if it's cloudy the probabilities are
# 30% Cloudy the next day , 10% Sunny, 60% Rainy
# if it's Sunny
# 20% Cloudy, 70% Sunny, 10% Rainy
# if it's Rainy
# 10% Cloudy, 40% Sunny, 50% Rainy

transitionMatrix = [[0.3, 0.1, 0.6], [0.2, 0.7, 0.1], [0.1, 0.4, 0.5]]

# function to implemente markov chain

def weather(days):
    # choose the starting weather
    weatherToday = "Cloudy"
    print("Start state: " + weatherToday)
    # store the sequence of weather taken
    activityList = [weatherToday]
    i = 0
    # calculate the probability of the activityList
    prob = 1
    while i != days:
        if weatherToday == "Cloudy":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "CC":
                prob = prob * 0.3
                activityList.append("Cloudy")
                pass
            elif change == "CS":
                prob = prob * 0.1
                weatherToday = "Sunny"
                activityList.append("Sunny")
            else:
                prob = prob * 0.6
                weatherToday = "Rainy"
                activityList.append("Rainy")
        elif weatherToday == "Sunny":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "SS":
                prob = prob * 0.7
                activityList.append("Sunny")
                pass
            elif change == "SC":
                prob = prob * 0.2
                weatherToday = "Cloudy"
                activityList.append("Cloudy")
            else:
                prob = prob * 0.1
                weatherToday = "Rainy"
                activityList.append("Rainy")
        elif weatherToday == "Rainy":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Rainy")
                pass
            elif change == "RC":
                prob = prob * 0.1
                weatherToday == "Cloudy"
                activityList.append("Cloudy")
            else:
                prob = prob * 0.4
                weatherToday = "Sunny"
                activityList.append("Sunny")
        i += 1
    print("Possible states: " + str(activityList))
    print("End state after " + str(days) + " days: " + weatherToday)
    print("Probability of the possible sequence of states: " + str(prob))
                                      
# forecasts the possible state for the next 2 days
weather(2)
    
        

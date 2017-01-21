#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    splitIndex = int(len(predictions) * 0.9)

    for i in range( 0, splitIndex ):
        cleaned_data.append( (ages[i], net_worths[i], abs(net_worths[i]-predictions[i])) )

    for i in range( splitIndex, len(predictions) ):
        cleaned_data.append( (ages[i], net_worths[i], abs(net_worths[i]-predictions[i])) )
        maxValue = max( cleaned_data, key=lambda item: item[2] )[2]
        for j in range( 0, len(cleaned_data) ):
            if cleaned_data[j][2] == maxValue:
                del cleaned_data[j]
                break

    return cleaned_data

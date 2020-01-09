# Isaac Lee CS21

# Take the schedules from the .txt file and align them.
# To find the best time period on each day
# And the most popular day


# Establish main function
def main():

    # read this file
    try:
        infile = open('schedules.txt','r')

    # File Error Handling
    except IOError:
        print('Error Opening File.')

    # Misc Error Handling
    except:
        print('Unknown Error Occurred')

    # If no errors...
    else:

        # Establish list for cleaning up each lines
        # (see schedules.txt)
        remove_list = ['\'',
                       ',',
                       ')',
                       '(',
                       '\n'
                       ]

        # Lists for times for each day for later
        monday_times = []
        tuesday_times = []
        wednesday_times = []
        thursday_times = []
        friday_times = []

        # Read the file line by line first
        line = infile.readline()

        # While a line still has stuff in it:
        while line != '':

            # For every item in the list of characters to remove:
            for item in remove_list:

                # Replace them with blanks, i.e. remove them outright
                line = line.replace(item, '')

            # split the resulting string into a list of three items:
            # "day","time1","time2"
            list = line.split()

            # The first item is the day.
            day = list[0]

            # Sort the times by the day they have assigned,
            # Into 5 seperate lists because dictionaries
            # Didn't work for this :C
            if day == 'Monday':
                monday_times.append(list[1])
                monday_times.append(list[2])
            elif day == 'Tuesday':
                tuesday_times.append(list[1])
                tuesday_times.append(list[2])
            elif day == 'Wednesday':
                wednesday_times.append(list[1])
                wednesday_times.append(list[2])
            elif day == 'Thursday':
                thursday_times.append(list[1])
                thursday_times.append(list[2])
            elif day == 'Friday':
                friday_times.append(list[1])
                friday_times.append(list[2])

            # These lists will be used to calculate the
            # popularity of certain times for each weekday

            # Aaaaand, go to the next line.
            # The loop ends once we're out of lines
            # #  in the .txt file
            line = infile.readline()

    # OK now close the program
    finally:
        infile.close()

    # To calculate the most popular day, we will
    # Just read the file into one big string.

    # For some reason, this requires closing and
    # Re-opening the file, so we will do
    # just that
    try:
        infile = open('schedules.txt', 'r')

    # Same error handling as before
    except IOError:
        print('Error Opening File.')
    except:
        print('Unknown Error Occurred')

    # if it works:
    else:

        # Read the whole file into one string
        sched_read = infile.read()

        # Remove all the extraneous characters from
        # the resulting string
        for item in remove_list:
            if item == '\n':
                sched_read = sched_read.replace(item, ' ') # Replace new line w/ space
            else:
                sched_read = sched_read.replace(item, '') # Otherwise replace with NOTHING

        # Print it to see if it looks like "day" "time" "time" "day" "time" "time" ....
        print('Sched Read:',sched_read,'\n\n\n')

        # Establish list for calculating most popular day
        sched_list = []

        # Split the string into a list of days and times
        sched_list = sched_read.split()

        # Establish counter vars
        m = 0
        t = 0
        w = 0
        r = 0
        f = 0

        # Go through the list. If the list item has a day, add to
        # the respective counter by one. If it's a time, nothing
        # will happen or change

        for item in sched_list:
            if item == 'Monday':
                m += 1
            elif item == 'Tuesday':
                t += 1
            elif item == 'Wednesday':
                w += 1
            elif item == 'Thursday':
                r += 1
            elif item == 'Friday':
                f += 1

        # THE OUTPUT/RESULT FOR THIS COUNTING ALGORTIHM IS AT THE END



        #  Establish a list of possible times in intervals of 15 min AGAIN
        #  This is the same code as in the other file.
        possible_times = []
        time = ''
        minute = ''

        #  Ok how do I even explain this
        #  for 12pm in particular, since it comes before 1-11pm:
        for x in range(0, 4):

            #  For every x/4 hour, add "15 *x" to the end of "12:"
            #  to produce 12:00, 12:15, 12:30, and 12:45
            minute = format(x * 15, '2.0f')
            time = '12:' + str(minute)

            #  If the end time is just "12:0" because math,
            #  replace it the zero w/ two zeroes.
            if ' 0' in time:
                time = '12:00'

            #  Add each time to a list
            possible_times.append(time)

        #  Same thing but with hours 1pm-11pm
        for a in range(1, 12):

            #  Every 15 min, etc.
            for x in range(0, 4):
                minute = format(x * 15, '2.0f')
                time = str(a) + ':' + str(minute)

                #  replace single zero with 2 zeroes
                if ' 0' in time:
                    time = str(a) + ':00'

                #  add to list
                possible_times.append(time)


        # Establish more lists!!!
        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []

        monday_count = {}
        tuesday_count = {}
        wednesday_count = {}
        thursday_count = {}
        friday_count = {}


        # EXTRACT ALL POSSIBLE TIMES that are between eacah start/end time
        # For each day. We will be using the weekday_times lists from earlier.

        # FOR EACH DAY:

        # e.g. MONDAY

        # Use this var to switch between interpreting start times and end times.
        # Basically it switches on and off to do something different for every other
        # item.

        first = True

        for item in monday_times:

            # for the starting time (aka first time/time1):
            if first == True:

                # establish it as bound "a"
                a = possible_times.index(item)

                # switch to the other code chunk below
                first = False

            # for the end time (aka second time/time2):
            else:

                # establish as bound "b"
                b = possible_times.index(item)

                # for EVERY SINGLE :15 INTERVAL TIME
                # between "a" (time1) and "b" (time2)
                # add it to the final list for future use.
                for x in range(a,b):
                    monday.append(possible_times[x])
                first = True

        # debug print
        print('\nAll the real times for monday:',monday)

        # TUESDAY - The code works the same for each day, so I'm not re-typing
        # The documentation.
        first = True
        for item in tuesday_times:
            if first == True:
                a = possible_times.index(item)
                first = False
            else:
                b = possible_times.index(item)
                for x in range(a, b):
                    tuesday.append(possible_times[x])
                first = True
        print('\nAll the real times for tuesday:', tuesday)

        # WEDNESDAY
        first = True
        for item in wednesday_times:
            if first == True:
                a = possible_times.index(item)
                first = False
            else:
                b = possible_times.index(item)
                for x in range(a, b):
                    wednesday.append(possible_times[x])
                first = True
        print('\nAll the real times for wednesday:', wednesday)

        # THURSDAY:
        first = True
        for item in thursday_times:
            if first == True:
                a = possible_times.index(item)
                first = False
            else:
                b = possible_times.index(item)
                for x in range(a, b):
                    thursday.append(possible_times[x])
                first = True
        print('\nAll the real times for thursday:', thursday)

        # FRIDAY
        first = True
        for item in friday_times:
            if first == True:
                a = possible_times.index(item)
                first = False
            else:
                b = possible_times.index(item)
                for x in range(a, b):
                    friday.append(possible_times[x])
                first = True
        print('\nAll the real times for friday:', friday)

        #
        #
        # THE FINAL RESULTS AND OUTPUT!!!!

        # For each day:
        # MONDAY
        print('\n\n\nMONDAY TIMES:')

        # For every time listed in the possible times for monday:
        for item in monday:

            # If the item isn't already in this dictionary, add it
            if item not in monday_count:

                # Establish the count starting at 1
                monday_count[item] = 1

            # If it's already there,
            else:

                # Add to the value's key by 1
                monday_count[item] += 1

        # Now for each possible time on monday:
        for item in monday_count:

            #  Print a bar of "A"'s, with one A for each time the time is a viable
            #  Time for a user to meet for the club.
            print(item,': ','A' * monday_count[item],sep='')

        #  Repeat this process for each day,
        #  for a total of 5 histograms for ea. weekday
        #  TUESDAY
        print('\n\nTUESDAY TIMES:')
        for item in tuesday:
            if item not in tuesday_count:
                tuesday_count[item] = 1
            else:
                tuesday_count[item] += 1
        for item in tuesday_count:
            print(item, ': ', 'A' * tuesday_count[item], sep='')

        # WEDNESDAY
        print('\n\nWEDNESDAY TIMES:')
        for item in wednesday:
            if item not in wednesday_count:
                wednesday_count[item] = 1
            else:
                wednesday_count[item] += 1
        for item in wednesday_count:
            print(item, ': ', 'A' * wednesday_count[item], sep='')

        # THURSDAY
        print('\n\nTHURSDAY TIMES:')
        for item in monday:
            if item not in thursday_count:
                thursday_count[item] = 1
            else:
                thursday_count[item] += 1
        for item in thursday_count:
            print(item, ': ', 'A' * thursday_count[item], sep='')

        # FRIDAY
        print('\n\nFRIDAY TIMES:')
        for item in friday:
            if item not in friday_count:
                friday_count[item] = 1
            else:
                friday_count[item] += 1
        for item in friday_count:
            print(item, ': ', 'A' * friday_count[item], sep='')


        #OK so here's the thing that prints the most popular
        #Weekday from the sorting algorithm from waaay before.
        print('\n')
        if m>t and m>w and m>r and m>f:
            print('Mondays are most popular!')
        elif t>m and t>w and t>r and t>f:
            print('Tuesdays are most popular!')
        elif w>m and w>t and w>r and w>f:
            print('Wednesdays are most popular!')
        elif r>m and r>t and r>w and r>f:
            print('Thursdays are most popular!')
        elif f>m and f>t and f>w and f>r:
            print('Fridays are most popular!')

        # If two or more days are most popular,
        # The user is told to look at the total counts themself
        else:
            print('\nTwo or more days have the same count. Here\'s the count for each day.')
            print('Compare it urself lol')

        # Print counts for each weekday
        print('\nMondays =', m, '\nTuesdays =', t, '\nWednesdays =', w, '\nThursdays =', r, '\nFridays =', f,'\n')

    # Aaaaaaaand close the file. We're done here folks.
    finally:
        infile.close()

        #todd howard
        print('\"It just works.\" - Todd Howard')

#Do it.
main()


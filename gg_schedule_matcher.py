# Isaac Lee CS21

# Schedule matcher for the UVM Gaming Guild.
# I will basically have all my friends say when
# They are free during the weekdays and save
# that to a file.

# then, in another .py file, I will take the contents
# of that other file and see
# what period of time makes the most sense.


# Function for later when I am validating multiple inputs
def validate(time,possible_times):

    # If the time is in the "all possible times" list, return false,
    # and furthermore end the validation loop
    if time in possible_times:
        return False

    # Otherwise, say the input is bad and perpertuate the loop
    else:
        print('Invalid Input, must be in the form "X:XX" in intervals of 15 minutes (:00, :15, :30, and :45).')
        return True


# Begin main program
def main():

    # Establish Vars
    loop = True
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    user_days = {}
    prompt = ''
    availability = {}

    # Establish a list of possible times in intervals of 15 min
    possible_times = []
    time = ''
    minute = ''

    # Ok how do I even explain this
    while loop is True:

        # for 12pm in particular, since it comes before 1-11pm:
        for x in range(0,4):

            # For every x/4 hour, add "15 *x" to the end of "12:"
            # to produce 12:00, 12:15, 12:30, and 12:45
            minute = format(x*15,'2.0f')
            time = '12:' + str(minute)

            # If the end time is just "12:0" because math,
            # replace it the zero w/ two zeroes.
            if ' 0' in time:
                time = '12:00'

            # Add each time to a list
            possible_times.append(time)

        # Same thing but with hours 1pm-11pm
        for a in range(1,12):

            # Every 15 min, etc.
            for x in range(0, 4):
                minute = format(x * 15, '2.0f')
                time = str(a) + ':' + str(minute)

                # replace single zero with 2 zeroes
                if ' 0' in time:
                    time = str(a) + ':00'

                # add to list
                possible_times.append(time)

        # Printing this for now so you can see the list of possible times
        # Future code will refer to this list. It's basically every 15 minutes
        # interval from noon to 11:45pm
        #print('Possible times:',possible_times)

        # Welcome
        print('Hello! Welcome to my schedule manager for The UVM Gaming Guild!')
        print('I will start by asking what weekdays you are free, then what times you are free on those days.\n')

        # Get Days Available
        for day in days:

            # Ask if their free on each day in the days list
            prompt = 'Are you free on '+day+' afternoons? (y/n): '
            d = str(input(prompt))

            while d != 'y' and d != 'n':  # Input Validation
                print('Invalid Input, try again')
                d = str(input(prompt))

            if d == 'y':  # Add to list if they're free (answer with "y"), otherwise don't
                user_days[day] = True

        # Get Time Periods Available for each day.

        # VERY specific instructions
        print('\n')
        print('OK! I will now ask what period of time you are available for each day. \n')

        print('PLEASE READ: Enter your times in the form "X:XX" in intervals of 15 minutes (:00, :15, :30, and :45).')
        print('I will assume that you are entering a time in the afternoon.')
        print('For example, if you are free at 4:30pm, simply enter "4:30".')

        # For each day that the user said "y"/yes to:
        for day in user_days:
            if user_days[day] is True:

                # Establish var for chronologicality in start/end times
                chronological = False

                # Validation loop to ensure start time is never AFTER the end time.
                while chronological is False:

                    # Ask what period of time they will be free
                    print('\nWhen will you be free on',day+'?\n')

                    #  It's validation time!
                    validating = True

                    while validating is True:

                        # Get the start time for time-period free that day
                        time1 = str(input('Starting Time: '))

                        # Validate input to ensure it's in a consistent "X:XX" format
                        # If the function returns false, the loop perpetuates.
                        # See the validate() function at the top for more info.
                        validating = validate(time1,possible_times)

                    # Reset validation var
                    validating = True

                    # Do the same thing, but for the END time of the period.
                    while validating is True:
                        time2 = str(input('Ending Time: '))

                        #  Validate input
                        validating = validate(time2,possible_times)

                    # Ensure that start time (time1) is not after end time (time2)
                    # by making sure time1 is listed BEFORE time2 in the possible_times list
                    if possible_times.index(time1) > possible_times.index(time2):

                        # If start time is after end time, loop perpetuates,
                        # Print error message.
                        chronological = False
                        print('\n\nStart time cannot be after End time, please try again.')

                    # Otherwise, if it's good, start before end,
                    # Kill the chronological-validation loop
                    else:
                        chronological = True

                # Record start/end times as values for that day.
                period = time1, time2
                availability[day] = period

        # FILE TIME (READ INPUT INTO A FILE)
        try:
            # Append this file, or create it if it does not exist.
            outfile = open('schedules.txt', 'a')

        # File Error Handling
        except IOError:
            print('Error Opening File.')

        # Misc Error Handling.
        except:
            print('Unknown Error Occurred')

        # If all goes well:
        else:

            # For each item in the availability dict:
            for item in availability:
                output = item,availability.get(item) # print the value w/ the key
                output = str(output) + '\n'  # w/ a "next line" character
                outfile.write(output)  # and then write (append) it into the output file.

        # FIMALLY:
        finally:

            # close file
            outfile.close()

            # Outro message
            print('\n\n\n\n\nThank you for doing this.\nPlease give this computer back to Isaac.\n')
            again = str(input('If everyone is done, he will end the program by using MAGIC! '))

            # type "end" and press enter to end the program,
            # otherwise enter anything (or nothing) to re-run
            # the entire program again.
            if again == 'end':
                loop = False

# Run it.
main()
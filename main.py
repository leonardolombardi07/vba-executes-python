import sys
from datetime import datetime
from time import sleep


def run_this_function_when_VBA_code_asks():
    # This should be something like "C:\\Users\\Leonardo\\Desktop"
    first_argument_passed_by_VBA_code = sys.argv[1]

    seconds = 10
    print(f'''Running "run_this_function_when_VBA_code_asks" for {
          seconds} seconds''')
    print('You may need to keep pressing something on your keyboard for this to work')
    print("A file will be generated on the same folder where the VBA code was run")

    sleep(seconds)

    with open(f'{first_argument_passed_by_VBA_code}/file.txt', 'w') as file:
        now_as_human_readable_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'''Executed on "{now_as_human_readable_str}. Argument: "{
                   first_argument_passed_by_VBA_code}" \n''')

    print("Finished!")


if __name__ == "__main__":
    run_this_function_when_VBA_code_asks()

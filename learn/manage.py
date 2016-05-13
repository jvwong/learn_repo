import os
import sys


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = "config.settings.local"
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

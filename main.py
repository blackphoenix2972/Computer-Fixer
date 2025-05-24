from banner import banner, description, features, permission, sfc_scan_now, is_admin, get_current_username, \
        display_text_letter_by_letter

print("Starting application")
banner()

description()
features()

if not is_admin():
        # Elevate privileges if not running as administrator
        print("=======================================")
        print("\nSYSTEM ERROR - ADMIN MODE NOT ENABLED\n")
        print("Momo: U...Um " + get_current_username() + ". A bit of a problem has occurred...\nMomo: Um...may you please run the program in administrator mode. I won't be abe to help you otherwise\nMomo:...S...Sorry...\n\nPROGRAM ENDED...\n")

        exit()
else:
        permission()
# main()
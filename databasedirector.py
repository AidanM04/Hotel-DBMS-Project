def direct_with_args(function_choice, table_choice, ID):
    result = []
    # Handle cases where user didn't select anything in initial dropdown
    if function_choice == '':
        result = "failed"
        return result
    
    elif function_choice == 'post':
        result.append('post')
        
        # Handle cases where user didn't select anything in table dropdown
        if table_choice == '':
            result = "failed"
            return result
        
        elif table_choice == 'Guest_Cr':
            result.append('add_guest')
            return result

        elif table_choice == 'Room_Cr':
            result.append('add_room')
            return result

        elif table_choice == 'Booking_Cr':
            result.append('add_booking')
            return result

        elif table_choice == 'Payment_Cr':
            result.append('add_payment')
            return result

        elif table_choice == 'Services_Cr':
            result.append('add_service')
            return result

        elif table_choice == 'Reviews_Cr':
            result.append('add_review')
            return result

        elif table_choice == 'Booking_Services_Cr':
            result.append('add_booking_service')
            return result
        
        # Handles all (theoretical) cases where the input for table_choice is input incorrectly
        else:
            result = "failed"
            return result




    elif function_choice == 'get':
        result.append('get')

        # Handle cases where user didn't select anything in table dropdown
        if table_choice == '':
            result = "failed"
            return result
        
        elif table_choice == 'Guest_Re':
            result.append('guests')
            return result

        elif table_choice == 'Room_Re':
            result.append('rooms')
            return result

        elif table_choice == 'Booking_Re':
            result.append('bookings')
            return result

        elif table_choice == 'Payment_Re':
            result.append('get_payments')
            return result

        elif table_choice == 'Services_Re':
            result.append('get_services')
            return result

        elif table_choice == 'Reviews_Re':
            result.append('get_reviews')
            return result

        elif table_choice == 'Booking_Services_Re':
            result.append('get_booking_services')
            return result
        
        # Handles all (theoretical) cases where the input for table_choice is input incorrectly
        else:
            result = "failed"
            return result



    elif function_choice == 'put':
        result.append('put')

        # Handle cases where user didn't select anything in table dropdown
        if table_choice == '':
            result = "failed"
            return result
        
        elif table_choice == 'Guest_Up':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('update_guest')
                result.append(ID.strip())
                return result


        elif table_choice == 'Room_Up':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('update_room')
                result.append(ID.strip())
                return result


        elif table_choice == 'Booking_Up':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('update_booking')
                result.append(ID.strip())
                return result
            

        # Handles all (theoretical) cases where the input for table_choice is input incorrectly
        else:
            result = "failed"
            return result


    elif function_choice == 'delete':
        result.append('delete')
        
        # Handle cases where user didn't select anything in table dropdown
        if table_choice == '':
            result = "failed"
            return result
        
        elif table_choice == 'Guest_Del':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('delete_guest')
                result.append(ID.strip())
                return result


        elif table_choice == 'Room_Del':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('delete_room')
                result.append(ID.strip())
                return result
                

        elif table_choice == 'Booking_Del':
            # Handle Cases where user didn't input anything in ID input box
            if ID == '':
                result = "failed"
                return result
            else:
                result.append('delete_room')
                result.append(ID.strip())
                return result
            
        # Handles all (theoretical) cases where the input for table_choice is input incorrectly
        else:
            result = "failed"
            return result
        
    # Handles all (theoretical) cases where the input for function_choice is input incorrectly
    else:
        result = "failed"
        return result
            


# testing block
if __name__ == "__main__":
    print('\n*** Test direction function ***\n')

    crud = input("\nPlease enter crud function choice: ")
    table = input("\nPlease enter table_crud choice: ")
    identification = input("\nPlease enter ID: ")

    print(direct_with_args(crud, table, identification))
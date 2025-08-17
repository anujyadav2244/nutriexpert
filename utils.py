def get_number_input(prompt, min_val, max_val):
    while True:
        try:
            value = input(prompt).strip()
            # Remove any non-digit characters
            value = ''.join(filter(str.isdigit, value))
            if not value:
                raise ValueError
            value = float(value)
            if min_val <= value <= max_val:
                return value
            print(f"Please enter between {min_val}-{max_val}")
        except ValueError:
            print("Please enter a valid number")

def get_choice_input(prompt, options, numbered=False, multiple=False):
    while True:
        
        choice = input(prompt).strip().lower()
        
        if multiple:
            if "," in choice:
                choices = [c.strip() for c in choice.split(",")]
                if numbered:
                    try:
                        indices = [int(c)-1 for c in choices]
                        selected = [options[i] for i in indices if 0 <= i < len(options)]
                        if selected:
                            return selected
                    except (ValueError, IndexError):
                        pass
                else:
                    selected = [c for c in choices if c in options]
                    if selected:
                        return selected
            elif choice in options:
                return [choice]
        else:
            if numbered:
                try:
                    index = int(choice)-1
                    if 0 <= index < len(options):
                        return options[index]
                except ValueError:
                    pass
            elif choice in options:
                return choice
        
        print(f"Invalid choice. Please select from: {', '.join(options)}")
        
def get_numbered_choices(options, prompt):
    """Get multiple choices using numbered options only"""
    while True:
        choice = input(prompt).strip()
        
        # Handle empty input
        if not choice:
            print("Please enter at least one number")
            continue
            
        # Split and process numbers
        numbers = [num.strip() for num in choice.split(",")]
        selected = []
        
        for num in numbers:
            if not num.isdigit():
                print(f"Invalid number: {num}")
                break
                
            index = int(num) - 1
            if 0 <= index < len(options):
                selected.append(options[index])
            else:
                print(f"Number out of range: {num}")
                break
        else:
            # If we didn't break from the loop
            if "none" in selected:
                return ["none"]  # 'none' overrides other selections
            return selected if selected else ["none"]
            
        # Show options again if there was an error
        print("\nAvailable options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
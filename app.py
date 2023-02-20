from models import (Base, session, Book, engine)

# Import models
# Main menu - add, search, analysis, exit, view
# Add books to the database
# Edit books
# Delete books
# Search books
# Data cleaning
# Loop runs program

if __name__ == '__main__':
    # Create the database
    Base.metadata.create_all(engine)

English README
# Mail-to-Ticket
Mail-to-Ticket is a Python application designed to monitor a mail inbox, extract relevant information from incoming emails, and create tickets in the iTop ticketing system based on specific criteria.

## Features
- Connects to a mail inbox using IMAP for email retrieval.
- Searches for emails with a specific subject, in this case, related to the recording of departures.
- Extracts information such as name, surname, employee identification number, and departure date from the email content.
- Creates tickets in the iTop system with the extracted information.

## Configuration
Ensure that the following environment variables are set in your .env file:

- MAIL-USER: Your mail email address.
- MAIL-PASSWORD: Your mail account password.
- SERVEUR-IMAP-MAIL: IMAP server for mail.
- PORT-IMAP-MAIL: Port number for IMAP server.

## Usage
Modify the search criteria in the search_criteria variable in mail.py according to your specific email subject.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
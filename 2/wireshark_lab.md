# Wireshark Lab: HTTP

## 1. The Basic HTTP GET/response interaction

1. Is your browser running HTTP version 1.0 or 1.1? What version of HTTP is the server running?

    Broswer: 1.1\
    Server: 1.1

2. What languages (if any) does your browser indicate that it can accept to the server?

    en-us

3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?

    Src: 192.168.43.11, Dst: 128.119.245.12

4. What is the status code returned from the server to your browser?

    200

5. When was the HTML file that you are retrieving last modified at the server?

    Sun, 06 Jan 2019 06:59:01 GMT

6. How many bytes of content are being returned to your browser?

    560 bytes.

7. By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window? If so, name one.

    No.

## 2. The HTTP CONDITIONAL GET/response interaction

8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an "IF-MODIFIED-SINCE" line in the HTTP GET?

    No.

9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?

    Yes. There are ten lines of text in "Line-based text data".

10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an "IF-MODIFIED-SINCE:" line in the HTTP GET? If so, what information follows the "IF-MODIFIED-SINCE:" header?

    Yes.\
    If-Modified-Since: Mon, 07 Jan 2019 06:59:01 GMT

11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.

    HTTP/1.1 304 Not Modified\r\n\
    No.\
    The file is not modified, so the server doesn't need to send it again.

## 3. Retrieving Long Documents

12. How many HTTP GET request messages did your browser send? Which packet number in the trace contains the GET message for the Bill or Rights?

    1, 16.

13. Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?

    24.

14. What is the status code and phrase in the response?

    200 OK.

15. How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?

    4.

# Chapter 2 Application Layer Review Questions

## SECTION 2.1

1. List five nonproprietary Internet applications and the application-layer protocols that they use.

    - Shadowsocks: [Shadowsocks protocal](https://shadowsocks.org/en/spec/Protocol.html)

    - Kahla: HTTP, Websocket

    - Youtube-dl: HTTP

    - qBittorrent: BitTorrent

    - git: HTTP, Git protocol

2. What is the difference between network architecture and application architecture?

    - Network architecture: five layers(application, transport, network, link, physical).

    - Application architecture: client-server or p2p.

3. For a communication session between a pair of processes, which process is the client and which is the server?

    Client initiates the communication, server waits to be contacted to begin the session.

4. Why are the terms client and server still used in peer-to-peer applications?

    When a peer downloads file it's a client, when it uploads file it's a server.

5. What information is used by a process running on one host to identify a process running on another host?

    Send message through socket.

6. What is the role of HTTP in a network application? What other components are needed to complete a Web application?

    It's the application-layer protocol. Client and server.

7. Referring to Figure 2.4, we see that none of the applications listed in Figure 2.4 requires both no data loss and timing. Can you conceive of an application that requires no data loss and that is also highly time-sensitive?

    Deposit via an app.

8. List the four broad classes of services that a transport protocol can provide. For each of the service classes, indicate if either UDP or TCP (or both) provides such a service.

9. Recall that TCP can be enhanced with SSL to provide process-to-process security services, including encryption. Does SSL operate at the transport layer or the application layer? If the application developer wants TCP to be enhanced with SSL, what does the developer have to do?

    At the application layer.

    >In particular, if an application wants to use the services of SSL, it needs to include SSL code (existing, highly optimized libraries and classes) in both the client and server sides of the application. SSL has its own socket API that is similar to the traditional TCP socket API. When an application uses SSL, the sending process passes cleartext data to the SSL socket; SSL in the sending host then encrypts the data and passes the encrypted data to the TCP socket.
    >
    > -- <cite>p. 122</cite>

## SECTION 2.2–2.5

10. What is meant by a handshaking protocol?

    >This so-called handshaking procedure alerts the client and server, allowing them to prepare for an onslaught of packets.
    >
    > -- <cite>p. 121</cite>

11. What does a stateless protocol mean? Is IMAP stateless? What about SMTP?

    The server doesn't maintain information about the clients.(p. 128)

    IMAP is not a stateless protocol. 
    
    >An IMAP server maintains user state information across IMAP sessions—for example, the names of the folders and which messages are associated with which folders.
    >
    > -- <cite>p. 154</cite>

    SMTP is a stateless protocol.

12. How can websites keep track of users? Do they always need to use cookies?

    Using cookies. Cookies are mainly used to identify a user.

13. Describe how Web caching can reduce the delay in receiving a requested object. Will Web caching reduce the delay for all objects requested by a user or for only some of the objects? Why?

    As long as the file is not changed, the file will be send from servers near the client or from browser cache.

14. Telnet into a Web server and send a multiline request message. Include in the request message the If-modified-since: header line to force a response message with the 304 Not Modified status code.

    ```
    $ telnet pornhub.com
    GET / HTTP/1.1
    HOST: pornhub.com

    GET / HTTP/1.1
    Host: pornhub.com
    If-modified-since: Wed, 9 Sep 3000 01:00:00
    ```

15. Are there any constraints on the format of the HTTP body? What about the email message body sent with SMTP? How can arbitrary data be transmitted over SMTP?

    ASCII text. Each line followed by a carriage return and a line feed. The last line is followed by an additional carriage return and line feed. The first line of an HTTP request message is called the request line; the subsequent lines are called the header lines. The request line has three fields: the method field, the URL field, and the HTTP version field. The method field can take on several different values, including GET, POST, HEAD, PUT, and DELETE.

    HELO, MAIL FROM, RCPT TO, DATA, and QUIT.

    Send over TCP connection.

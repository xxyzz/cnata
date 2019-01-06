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

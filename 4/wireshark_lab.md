# Wireshark Lab: IP v7.0

1. What is the IP address of your computer?

    192.168.43.11

2. Within the IP packet header, what is the value in the upper layer protocol field?

    Protocol: UDP (17)

3. How many bytes are in the IP header? How many bytes are in the payload *of the IP datagram*? Explain how you determined the number of payload bytes.

    20 bytes. 8(udp header) + 28(udp data) = 36 bytes.

4. Has this IP datagram been fragmented? Explain how you determined whether or not the datagram has been fragmented.

    No. More fragments flag.

5. Which fields in the IP datagram always change from one datagram to the next within this series of ICMP messages sent by your computer?

    Identification and Header checksum

6. Which fields stay constant? Which of the fields must stay constant? Which fields must change? Why?

    Constant: Version, Header Length, Protocol.

    Change: Identification, Header checksum.

7. Describe the pattern you see in the values in the Identification field of the IP datagram.

    Increase one each time.

8. What is the value in the Identification field and the TTL field?

    Identification: 0xa4db (42203)

    Time to live: 64

9. Do these values remain unchanged for all of the ICMP TTL-exceeded replies sent to your computer by the nearest (first hop) router? Why?

    TTL didn't change, but Identification changed.

10. Find the first ICMP Echo Request message that was sent by your computer after you changed the Packet Size in pingplotter to be 2000. Has that message been fragmented across more than one IP datagram?

    Yes.

11. Print out the first fragment of the fragmented IP datagram. What information in the IP header indicates that the datagram been fragmented? What information in the IP header indicates whether this is the first fragment versus a latter fragment? How long is this IP datagram?

    Reassembled IPv4 in frame: 168

    Fragment offset: 185 in Flags.

    1500 bytes.

12. Print out the second fragment of the fragmented IP datagram. What information in the IP header indicates that this is not the first datagram fragment? Are the more fragments? How can you tell?

    Fragment offset flag is not 0.

    Yes. The More Fragments is set.

13. What fields change in the IP header between the first and second fragment?

    Fragment offset flag and Header checksum.

14. How many fragments were created from the original datagram?

    3

15. What fields change in the IP header among the fragments?

    Length, More fragments and Fragment offset flags, Header checksum.

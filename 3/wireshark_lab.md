# Wireshark Lab: TCP

1. What is the IP address and TCP port number used by the client computer (source) that is transferring the file to gaia.cs.umass.edu?

    Source IP address: 192.168.1.102, source port: 1161.

2. What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection?

    IP: 128.119.245.12, port: 80.

3. What is the IP address and TCP port number used by your client computer (source) to transfer the file to gaia.cs.umass.edu?

4. What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? What is it in the segment that identifies the segment as a SYN segment?

    0
    
    yes

5. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment?

    0
    
    1

    set SYN and ACK flag

6. What is the sequence number of the TCP segment containing the HTTP POST command? Note that in order to find the POST command, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with a "POST" within its DATA field.

    1

7. Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST)? At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments? What is the `EstimatedRTT` value (see Section 3.5.3, page 242 in text) after the receipt of each ACK? Assume that the value of the `EstimatedRTT` is equal to the measured RTT for the first segment, and then is computed using the `EstimatedRTT` equation on page 242 for all subsequent segments.

    *Note*: Wireshark has a nice feature that allows you to plot the RTT for each of the TCP segments sent. Select a TCP segment in the "listing of captured packets" window that is being sent from the client to the gaia.cs.umass.edu server. Then select: *Statistics->TCP Stream Graph- >Round Trip Time Graph*.

    1, Aug 21, 2004 21:44:20.596858000 CST, Aug 21, 2004 21:44:20.624318000 CST, 27ms, 27ms

    566, Aug 21, 2004 21:44:20.612118000 CST, Aug 21, 2004 21:44:20.647675000 CST, 36ms, 0.875 * 27 + 0.125 * 36 = 28.125ms

    2026, Aug 21, 2004 21:44:20.624407000 CST, Aug 21, 2004 21:44:20.694466000 CST, 70ms, 0.875 * 28.125 + 0.125 * 70 = 33.36ms

    3486, Aug 21, 2004 21:44:20.625071000 CST, Aug 21, 2004 21:44:20.739499000 CST, 114ms, 0.875 * 33.36 + 0.125 * 114 = 43.44ms

    4946, Aug 21, 2004 21:44:20.647786000 CST, Aug 21, 2004 21:44:20.787680000 CST, 140ms, 0.875 * 43.44 + 0.125 * 140 = 55.51ms

    6406, Aug 21, 2004 21:44:20.648538000 CST, Aug 21, 2004 21:44:20.838183000 CST, 190ms, 0.875 * 55.51 + 0.125 * 190 = 72.32ms

8. What is the length of each of the first six TCP segments?

    565, 1460, 1460, 1460, 1460, 1460

9. What is the minimum amount of available buffer space advertised at the received for the entire trace? Does the lack of receiver buffer space ever throttle the sender?

    5840, yes

10. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?

    No. There will be a "[TCP Retransmission]" in the info column.

11. How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 on page 250 in the text).

    One segment.

12. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.

    Package length / RTT

13. Use the `Time-Sequence-Graph(Stevens)` plotting tool to view the sequence number versus time plot of segments being sent from the client to the gaia.cs.umass.edu server. Can you identify where TCP’s slowstart phase begins and ends, and where congestion avoidance takes over? Comment on ways in which the measured data differs from the idealized behavior of TCP that we’ve studied in the text.

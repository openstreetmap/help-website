+++
type = "question"
title = "Delay in HTTP Status Packet and First TCP Segment"
description = '''Hi, I need help... can&#x27;t figure out what is the cause of a Web Application Slowness Issue. Can&#x27;t think of what else to check anymore. Web Application Server in Site A. Users in Site B &amp;amp; C tries to access the Web Application. Site A, B &amp;amp; C uses Riverbed WANX, however the traffic for this appl...'''
date = "2013-12-12T11:17:00Z"
lastmod = "2013-12-16T05:08:00Z"
weight = 28060
keywords = [ "delay", "http.response", "http", "slowness", "tcp-segment" ]
aliases = [ "/questions/28060" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Delay in HTTP Status Packet and First TCP Segment](/questions/28060/delay-in-http-status-packet-and-first-tcp-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28060-score" class="post-score" title="current number of votes">0</div><span id="post-28060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need help... can't figure out what is the cause of a Web Application Slowness Issue.<br />
Can't think of what else to check anymore.</p><p>Web Application Server in Site A.<br />
Users in Site B &amp; C tries to access the Web Application.<br />
Site A, B &amp; C uses Riverbed WANX, however the traffic for this application is "Passthrough Intentional".<br />
<br />
<br />
</p><p>Site A &lt;------------Tunnel-----------&gt; Central &lt;------------Tunnel-----------&gt; Site B<br />
Site A &lt;-Tunnel-&gt; ISP &lt;-Tunnel-&gt; Central &lt;-Tunnel-&gt; ISP &lt;-Tunnel-&gt; Site B</p><p>Users from Site B, have no issues regardless of Client Operating System.<br />
<br />
<br />
</p><p>Site A &lt;------------Tunnel-----------&gt; Central &lt;------------Tunnel-----------&gt; Site C<br />
Site A &lt;-Tunnel-&gt; ISP &lt;-Tunnel-&gt; Central &lt;-Tunnel-&gt; ISP &lt;-Tunnel-&gt; Site C</p><p>Users from Site C, experience slowness on Windows Vista and 7 only. No issues with Windows XP.<br />
<br />
<br />
</p><p>Initial assumptions:<br />
- OS problem, since XP has no problem<br />
- However, Site B has no issues regardless of Operating System.</p><p>Additional Notes:<br />
- Both Site B &amp; C uses the same model of Routers and Firewall<br />
- Their Firmware version are the same as well<br />
- Both site has MTU of 1500 (Tested using ping, result = 1472)<br />
- The Vista and 7 Machines tested in Site B &amp; C are the same (We move them over)<br />
- The ISP for all sites are the same provider, going through a private MPLS cloud<br />
</p><p>Troubleshooting tried, but doesn't work<br />
- Disabled Autotune on Windows Vista and 7<br />
- Site A ping to Application Server: 100 % (10000/10000), round-trip min/avg/max = 1/1/21 ms<br />
- Site A ping to Site B: 100 % (10000/10000), round-trip min/avg/max = 2/2/23 ms<br />
- Site A ping to Site C: 100 % (10000/10000), round-trip min/avg/max = 2/2/11 ms<br />
- Access application at night where there are no congestion from Site C, results = slow<br />
</p><p>Captured traffic from Site C and Site A, using "Time since previous frame" to check delays:<br />
- Segmented TCP "HTTP GET" has no delay when it leaves Site C (User Site)<br />
- Viewing from Site A (Server Site), 5 sec delay is found ONLY in the first frame of the Segmented TCP "HTTP GET"<br />
- When Segmented TCP "HTTP/1.1 OK" is returned, it has no delay when it leaves Site A (Server Site)<br />
- However viewing from Site C (User Site), 5 sec delay is found "ONLY" in the first frame of "ALL" Segmented TCP "HTTP/1.1 OK"<br />
- Additionally "HTTP/1.1 304 Not Modified" messages that are "NOT" segmented has a 5 seconds delay as well<br />
</p><p><br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_1_2.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_2a.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_3.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_4_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-http.response" rel="tag" title="see questions tagged &#39;http.response&#39;">http.response</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-slowness" rel="tag" title="see questions tagged &#39;slowness&#39;">slowness</span> <span class="post-tag tag-link-tcp-segment" rel="tag" title="see questions tagged &#39;tcp-segment&#39;">tcp-segment</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/3f94ee3f0b331c110d9f5c52dfb461b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RebirthX&#39;s gravatar image" /><p><span>RebirthX</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RebirthX has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '13, 12:15</strong> </span></p></div></div><div id="comments-container-28060" class="comments-container"><span id="28096"></span><div id="comment-28096" class="comment"><div id="post-28096-score" class="comment-score"></div><div class="comment-text"><p>You wrote: Both site has MTU of 1500 (Tested using ping, result = 1472)</p><p>Did you specify the -f option on the ping command? What is the largest size that gets through?</p><p>"-f : Specifies that Echo Request messages are sent with the Don't Fragment flag in the IP header set to 1"</p></div><div id="comment-28096-info" class="comment-info"><span class="comment-age">(13 Dec '13, 23:04)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="28097"></span><div id="comment-28097" class="comment"><div id="post-28097-score" class="comment-score"></div><div class="comment-text"><p>Has this ever performed well and suddenly started to slow down on Site C?</p></div><div id="comment-28097-info" class="comment-info"><span class="comment-age">(13 Dec '13, 23:06)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="28102"></span><div id="comment-28102" class="comment"><div id="post-28102-score" class="comment-score"></div><div class="comment-text"><p>Yes.<br />
I did ping -f -l 1472 [IP Addr.]<br />
1473 will results in packet needs to be fragmented.<br />
</p></div><div id="comment-28102-info" class="comment-info"><span class="comment-age">(14 Dec '13, 02:58)</span> <span class="comment-user userinfo">RebirthX</span></div></div><span id="28103"></span><div id="comment-28103" class="comment"><div id="post-28103-score" class="comment-score"></div><div class="comment-text"><p>They only realised this when the APP Users recently changed from WinXP to Win7.</p></div><div id="comment-28103-info" class="comment-info"><span class="comment-age">(14 Dec '13, 03:00)</span> <span class="comment-user userinfo">RebirthX</span></div></div><span id="28113"></span><div id="comment-28113" class="comment"><div id="post-28113-score" class="comment-score"></div><div class="comment-text"><p>Hmm, still very mysterious... What is the largest segment leaving the WinXP client? What is the largest segment leaving the Win7 client? Is the ip.flags.df bit set? Do you see any retransmissions occuring in the client traces?</p><p>At the server, what is the largest segment that arrives? Is the IP don't fragment bit set when those packets arrive? What is the TTL value?</p></div><div id="comment-28113-info" class="comment-info"><span class="comment-age">(14 Dec '13, 23:02)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="28115"></span><div id="comment-28115" class="comment not_top_scorer"><div id="post-28115-score" class="comment-score"></div><div class="comment-text"><p>Win XP Largest Segment Leave = 536<br />
Win7 Largest Segment Leave = 536<br />
Server Largest Segment Arrive = 536<br />
</p><p>Win XP's IP DF Flag = 0x02<br />
Win7's IP DF Flag = 0x02<br />
</p><p>They seems to be all the same, but only Win7 &amp; Vista is slow.<br />
</p><p>By the way, I've tried accessing another Web server in the same subnet.<br />
The Largest Segment is 1460.<br />
Does that means that the TCP MSS might be a configuration issue in the Server itself?<br />
It is a Win Server 2003 virtualized in a ESXi by the way.</p></div><div id="comment-28115-info" class="comment-info"><span class="comment-age">(15 Dec '13, 01:43)</span> <span class="comment-user userinfo">RebirthX</span></div></div></div><div id="comment-tools-28060" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-28060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="28065"></span>

<div id="answer-container-28065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28065-score" class="post-score" title="current number of votes">0</div><span id="post-28065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The segment size of 536 indicates that you are effectively using the default MTU size of 576. Did you check the SYN and SYN_ACK packet what the negotiated MSS was in the 3-way handshake? If this is a normal offering - 1380 or 1460 then you are suffering from - failing - Path MTU discovery where - if all else fails - windows falls back to 576...</p><p>Did you see any ICMP packets at the client / server side indicating that fragmentation is required?</p><p>Additional Information: The 3-way handshakes indicate the both clients offer a MSS of 1260 on their outbound SYN request. The SYN_ACK from the server shows a MSS of 1460 bytes in both cases.</p><p>As the infrastructure consists of 'tunnels' it is good practice in the network to adjust the MSS values in the SYN packets as they are entering a VPN tunnel to avoid fragmentation problems. This does not happen. Please contact your ISPs and ask them to <strong><code>tcp-adjust-mss</code></strong> to avoid the PMTUD logic which does not seem to work properly as we see 536-bytes segments at the server lateron in the flow.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '13, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '13, 23:08</strong> </span></p></div></div><div id="comments-container-28065" class="comments-container"><span id="28066"></span><div id="comment-28066" class="comment"><div id="post-28066-score" class="comment-score"></div><div class="comment-text"><p>Hmm... Yeah...<br />
I didn't know that the Segmentation size should be around the MTU size...<br />
That may be a problem.<br />
</p><p>But I don't think this is the cause of the problem actually.<br />
Cause the XP Machine's Segmentation is also 536, but the time it takes to load the Web Link is almost instance.<br />
While the Vista/7 Machine takes about a minute...<br />
I do not know how to analyse the MSS in the 3-way, can you tell me what to see?<br />
<br />
</p><p><strong>The following is the TCP SYN/ACK of the XP</strong></p><pre><code>No.     Time           Source                Destination           Protocol Length Delay      Window size scaling factor Info
     10 0.060064000    XP Client IP           Server IP             TCP      62     0.000000000                            1679 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1260 SACK_PERM=1
Frame 10: 62 bytes on wire (496 bits), 62 bytes captured (496 bits) on interface 0
Ethernet II, Src: , Dst: 
Internet Protocol Version 4, Src: XP Client IP IP, Dst: Server IP
Transmission Control Protocol, Src Port: 1679 (1679), Dst Port: 80 (80), Seq: 0, Len: 0
    Source port: 1679 (1679)
    Destination port: 80 (80)
    [Stream index: 1]
    Sequence number: 0    (relative sequence number)
    Header length: 28 bytes
    Flags: 0x002 (SYN)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgment: Not set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 80]
                [Message: Connection establish request (SYN): server port 80]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 65535
    [Calculated window size: 65535]
    Checksum: 0x016d [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (8 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted
        Maximum segment size: 1260 bytes
            Kind: MSS size (2)
            Length: 4
            MSS Value: 1260
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        TCP SACK Permitted Option: True
            Kind: SACK Permission (4)
            Length: 2
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000000000 seconds]
        [Time since previous frame in this TCP stream: 0.000000000 seconds]
No.     Time           Source                Destination           Protocol Length Delay      Window size scaling factor Info
     11 0.065313000    Server IP             XP Client IP           TCP      62     0.005249000                            80 &gt; 1679 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1460 SACK_PERM=1
Frame 11: 62 bytes on wire (496 bits), 62 bytes captured (496 bits) on interface 0
Ethernet II, Src: Alcatel-_39:43:80 (e8:e7:32:39:43:80), Dst: 
Internet Protocol Version 4, Src: Server IP, Dst: XP Client IP
Transmission Control Protocol, Src Port: 80 (80), Dst Port: 1679 (1679), Seq: 0, Ack: 1, Len: 0
    Source port: 80 (80)
    Destination port: 1679 (1679)
    [Stream index: 1]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 28 bytes
    Flags: 0x012 (SYN, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port 80]
                [Message: Connection establish acknowledge (SYN+ACK): server port 80]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 64240
    [Calculated window size: 64240]
    Checksum: 0x8a5a [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (8 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted
        Maximum segment size: 1460 bytes
            Kind: MSS size (2)
            Length: 4
            MSS Value: 1460
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        TCP SACK Permitted Option: True
            Kind: SACK Permission (4)
            Length: 2
    [SEQ/ACK analysis]
    [Timestamps]
        [Time since first frame in this TCP stream: 0.005249000 seconds]
        [Time since previous frame in this TCP stream: 0.005249000 seconds]
No.     Time           Source                Destination           Protocol Length Delay      Window size scaling factor Info
     12 0.068621000    XP Client IP           Server IP             TCP      54     0.003308000 -2                         1679 &gt; 80 [ACK] Seq=1 Ack=1 Win=65535 Len=0
Frame 12: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface 0
Ethernet II, Src: , Dst: 
Internet Protocol Version 4, Src: XP Client IP, Dst: Server IP
Transmission Control Protocol, Src Port: 1679 (1679), Dst Port: 80 (80), Seq: 1, Ack: 1, Len: 0
    Source port: 1679 (1679)
    Destination port: 80 (80)
    [Stream index: 1]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 65535
    [Calculated window size: 65535]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0xb20f [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    [SEQ/ACK analysis]
    [Timestamps]
        [Time since first frame in this TCP stream: 0.008557000 seconds]
        [Time since previous frame in this TCP stream: 0.003308000 seconds]</code></pre><p><br />
<br />
</p><p><strong>The following is the TCP SYN/ACK the Win7 Machine</strong></p><pre><code>No.     Time        Source                Destination           Protocol Length Delay      Window size scaling factor Info
      1 0.000000    Win7 Client IP          Server IP             TCP      66     0.000000000                            49595 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1260 WS=4 SACK_PERM=1
Frame 1: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: , Dst: 
Internet Protocol Version 4, Src: Win7 Client IP, Dst: Server IP
Transmission Control Protocol, Src Port: 49595 (49595), Dst Port: 80 (80), Seq: 0, Len: 0
    Source port: 49595 (49595)
    Destination port: 80 (80)
    [Stream index: 0]
    Sequence number: 0    (relative sequence number)
    Header length: 32 bytes
    Flags: 0x002 (SYN)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgment: Not set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 80]
                [Message: Connection establish request (SYN): server port 80]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 8192
    [Calculated window size: 8192]
    Checksum: 0x10d2 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000000000 seconds]
        [Time since previous frame in this TCP stream: 0.000000000 seconds]
No.     Time        Source                Destination           Protocol Length Delay      Window size scaling factor Info
      2 0.002502    Server IP             Win7 Client IP          TCP      66     0.002502000                            80 &gt; 49595 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1460 WS=1 SACK_PERM=1
Frame 2: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco_c3:af:c3 (00:25:83:c3:af:c3), Dst: 
Internet Protocol Version 4, Src: Server IP, Dst: Win7 Client IP
Transmission Control Protocol, Src Port: 80 (80), Dst Port: 49595 (49595), Seq: 0, Ack: 1, Len: 0
    Source port: 80 (80)
    Destination port: 49595 (49595)
    [Stream index: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 32 bytes
    Flags: 0x012 (SYN, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port 80]
                [Message: Connection establish acknowledge (SYN+ACK): server port 80]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 64240
    [Calculated window size: 64240]
    Checksum: 0x1882 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 1]
        [The RTT to ACK the segment was: 0.002502000 seconds]
    [Timestamps]
        [Time since first frame in this TCP stream: 0.002502000 seconds]
        [Time since previous frame in this TCP stream: 0.002502000 seconds]
No.     Time        Source                Destination           Protocol Length Delay      Window size scaling factor Info
      3 0.003231    Win7 Client IP          Server IP             TCP      60     0.000729000 4                          49595 &gt; 80 [ACK] Seq=1 Ack=1 Win=66780 Len=0
Frame 3: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: , Dst: 
Internet Protocol Version 4, Src: Win7 Client IP, Dst: Server IP
Transmission Control Protocol, Src Port: 49595 (49595), Dst Port: 80 (80), Seq: 1, Ack: 1, Len: 0
    Source port: 49595 (49595)
    Destination port: 80 (80)
    [Stream index: 0]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 16695
    [Calculated window size: 66780]
    [Window size scaling factor: 4]
    Checksum: 0x1307 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 2]
        [The RTT to ACK the segment was: 0.000729000 seconds]
    [Timestamps]
        [Time since first frame in this TCP stream: 0.003231000 seconds]
        [Time since previous frame in this TCP stream: 0.000729000 seconds]</code></pre><code></code></code><p><code></code></p><p><code></code></p></div><div id="comment-28066-info" class="comment-info"><span class="comment-age">(12 Dec '13, 21:35)</span> <span class="comment-user userinfo">RebirthX</span></div></div></div><div id="comment-tools-28065" class="comment-tools"></div><div class="clear"></div><div id="comment-28065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28075"></span>

<div id="answer-container-28075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28075-score" class="post-score" title="current number of votes">0</div><span id="post-28075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Site A, B &amp; C <strong>uses Riverbed WANX</strong>, however the traffic for this application is <strong>"Passthrough Intentional"</strong>.</p></blockquote><p>Well, maybe the traffic is not so 'passthrough' as you expect it to be due to the config option ;-))</p><p>I suggest to capture at several places <strong>in parallel</strong> to rule out some things. Please sync the clocks of the capture devices.</p><pre><code>[SiteC]: client --- WANX -- Router ---- MPLS --- Router --- WANX ---- Server [SiteA]
                   |       |                               |         |
Capture:        here[1]  here[2]                          here[3]  here[4]</code></pre><p>Start with a capture at [1] and [4] in parallel. Then compare the timestamps of the capture files. If you see the delay in [1] but not in [4], it's not the server, but something in the data path.</p><p>Continue with: [2] and [3] in parallel. Then compare the timestamps of the capture files. If you see the delay in [2] but not in [3] it is caused by the MPLS and you can hand over the problem to the ISP :-)</p><p>Continue with: [1] and [3] in parallel. Then compare the timestamps of the capture files. If you see the delay in [1] but not in [3], the problem is WANX[SiteC]. If you see the delay at [3] the problem is WANX[SiteA].</p><p>That's just a rough idea how to find the problem and I did not think through all possible combinations. I leave that up to you ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-28075" class="comments-container"></div><div id="comment-tools-28075" class="comment-tools"></div><div class="clear"></div><div id="comment-28075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28149"></span>

<div id="answer-container-28149" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28149-score" class="post-score" title="current number of votes">0</div><span id="post-28149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi all,<br />
<br />
Thanks for all the help, I've managed to resolved the problem.<br />
I did captures from all points and found out the delay is caused by Site A's External Firewall.<br />
<br />
Site A's External Firewall is using McAfee Enterprise Firewall 8.<br />
Aside from Source/Destination IP and Port, there is this additional thing called "Application Defense Group".<br />
I'm not sure what it does actually,but once it is disabled, the problem got resolved.<br />
No more delays.<br />
<br />
</p><p>The reason why it does not affect Site B but only Site C, is because Site B &amp; C have different Firewall Rules in Site A's Firewall.<br />
The rule for Site C, has the "Application Defense Group" turned on.<br />
The rule for Site B, has the "Application Defense Group" turned off.<br />
Why does it not affect Windows XP but only affect Windows Vista &amp; 7, I still have no idea.<br />
<br />
<img src="https://osqa-ask.wireshark.org/upfiles/App_Defense_Group.png" alt="alt text" /><br />
<br />
<br />
</p><p>As for the TCP MSS, which is a separate issue, is not fixed yet.<br />
Accessing the Server from Site A's Core Switch, the TCP Segment size shows 536.<br />
This will pass through the Server's Firewall in Site A, which is a Palo Alto.<br />
</p><p>We tried using another Server which is in the same subnet as the Application Server and did a capture, bypassing the Server Firewall.<br />
The TCP Segment size shows 1460...<br />
Seems like it only becomes 536 when it passes though the Palo Alto Firewall.<br />
So... is this the Firewall problem or the Server's TCP MSS registry problem?<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/3f94ee3f0b331c110d9f5c52dfb461b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RebirthX&#39;s gravatar image" /><p><span>RebirthX</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RebirthX has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '13, 05:12</strong> </span></p></div></div><div id="comments-container-28149" class="comments-container"></div><div id="comment-tools-28149" class="comment-tools"></div><div class="clear"></div><div id="comment-28149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


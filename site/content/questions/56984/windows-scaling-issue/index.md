+++
type = "question"
title = "Windows Scaling Issue"
description = '''I have an affiliate uploading files to one of our web servers and it&#x27;s running slow according to them. They&#x27;re network is Juniper SRX firewall to Bluecoat ProxySG to our Fortigate. They did a capture on the Bluecoat and sent me their capture file. They&#x27;re saying that they are using scaling windows b...'''
date = "2016-11-04T08:25:00Z"
lastmod = "2016-11-16T02:19:00Z"
weight = 56984
keywords = [ "windows", "scaling" ]
aliases = [ "/questions/56984" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Windows Scaling Issue](/questions/56984/windows-scaling-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an affiliate uploading files to one of our web servers and it's running slow according to them. They're network is Juniper SRX firewall to Bluecoat ProxySG to our Fortigate. They did a capture on the Bluecoat and sent me their capture file. They're saying that they are using scaling windows but that we are not. From what I researched with the scaling factors and their capture file, I can confirm that we actually are doing scaling windows and maybe a server issue?</p><p>From them to us...</p><pre><code>Frame 6318: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Invertex_0c:89:ee (00:d0:83:0c:89:ee), Dst: Netscreen_ff:10:05 (00:10:db:ff:10:05)
Internet Protocol Version 4, Src: 150.198.1.221, Dst: 69.25.25.67
Transmission Control Protocol, Src Port: 65189, Dst Port: 443, Seq: 1337, Ack: 16094, Len: 0
    Source Port: 65189
    Destination Port: 443
    [Stream index: 424]
    [TCP Segment Len: 0]
    Sequence number: 1337    (relative sequence number)
    Acknowledgment number: 16094    (relative ack number)
    Header Length: 32 bytes
    Flags: 0x010 (ACK)
    Window size value: 63156
    [Calculated window size: 63156]
    [Window size scaling factor: 1]
    Checksum: 0xf725 [unverified]
    [Checksum Status: Unverified]
    Urgent pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 6317]
        [The RTT to ACK the segment was: 0.000119999 seconds]
        [iRTT: 0.020690000 seconds]</code></pre><p>Next packet from us to them:</p><pre><code>Frame 6319: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: Netscreen_ff:10:05 (00:10:db:ff:10:05), Dst: Invertex_0c:89:ee (00:d0:83:0c:89:ee)
Internet Protocol Version 4, Src: 69.25.25.67, Dst: 150.198.1.221
Transmission Control Protocol, Src Port: 443, Dst Port: 65189, Seq: 16094, Ack: 1337, Len: 1448
    Source Port: 443
    Destination Port: 65189
    [Stream index: 424]
    [TCP Segment Len: 1448]
    Sequence number: 16094    (relative sequence number)
    [Next sequence number: 17542    (relative sequence number)]
    Acknowledgment number: 1337    (relative ack number)
    Header Length: 32 bytes
    Flags: 0x018 (PSH, ACK)
    Window size value: 31
    [Calculated window size: 7936]
    [Window size scaling factor: 256]
    Checksum: 0x5c8e [unverified]
    [Checksum Status: Unverified]
    Urgent pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
    [SEQ/ACK analysis]
        [iRTT: 0.020690000 seconds]
        [Bytes in flight: 1448]
        [Bytes sent since last PSH flag: 2896]
    TCP segment data (509 bytes)
    TCP segment data (939 bytes)
[12 Reassembled TCP Segments (16437 bytes): #6280(1448), #6283(1448), #6289(1448), #6292(1448), #6293(1448), #6300(1448), #6304(1448), #6305(1448), #6312(1448), #6316(1448), #6317(1448), #6319(509)]
Secure Sockets Layer</code></pre></div><div id="question-tags" class="tags-container tags">windows scaling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/7af3f8836051063838ad040e0b70b4b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sedberg1&#39;s gravatar image" /><p>sedberg1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sedberg1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '16, 08:35</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56984" class="comments-container"></div><div id="comment-tools-56984" class="comment-tools"></div><div class="clear"></div><div id="comment-56984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56992"></span>

<div id="answer-container-56992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several things to look at. First, to "use window scaling" may mean two things:</p><ol><li><p>to use the "window size scaling factor" TCP option field during session establishment phase, indicating that you support the window scaling mechanism,</p></li><li><p>to announce a window size multiplier different from 1 in that TCP option field.</p></li></ol><p>Your two packet dissections indicate indirectly that both the server and the client have declared support of window size scaling mechanism as the scaling factor differs from 1 in at least one of the directions (the one from the client). But as it is 1 in the packet sent by Fortigate to the Bluecoat, either your server or the Fortigate have decided to use a scaling factor of 1 which is equivalent to not using it in the sense of point 2., limiting the throughput in networks with higher round trip times.</p><p>The next thing to look at is whether this behaviour comes from your server or from the Fortigate, so you should capture on the path between them (in worst case, at one of them but on the interface looking towards the other one) to see whether it is not the Fortigate box which reduces the maximum window size this way, e.g. to make its life easier when doing deep packet inspection.</p><p>When you find out which of the boxes is responsible for using a window scaling factor of 1, you can start finding out why it does so and whether that can be changed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '16, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56992" class="comments-container"></div><div id="comment-tools-56992" class="comment-tools"></div><div class="clear"></div><div id="comment-56992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57411"></span>

<div id="answer-container-57411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57411-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Even though window scaling is used (as can be seen in the scaling factors in the two packets), it does not mean that the actually used Receive Window will be increased in size. It just means that the window size field has some extra bits to allow for larger values.</p><p>In the packet send from you to the client, the calculated value is only 7936. Does this value increase during the upload? What is the largest value seen? You might have to re-configure the Maximum Window Size value in your TCP stack. Please note however that on a server, there are a lot of open connections, so setting the value too high could result in a lot of memory being reserved for all the buffers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57411" class="comments-container"></div><div id="comment-tools-57411" class="comment-tools"></div><div class="clear"></div><div id="comment-57411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


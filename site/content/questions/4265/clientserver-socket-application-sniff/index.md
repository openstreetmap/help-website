+++
type = "question"
title = "Client/Server socket application sniff ?"
description = '''I have done a small c# client/server chat with simple auth that runs on the tcp port 8822, I would like to sniff it to learn more about how the packets work and everything, I can capture the packets just fine but I am wondering about what I am seeing at the wireshark. For example the first entry: 00...'''
date = "2011-05-27T21:20:00Z"
lastmod = "2011-05-29T02:52:00Z"
weight = 4265
keywords = [ "sniffing", "capture" ]
aliases = [ "/questions/4265" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Client/Server socket application sniff ?](/questions/4265/clientserver-socket-application-sniff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4265-score" class="post-score" title="current number of votes">0</div><span id="post-4265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have done a small c# client/server chat with simple auth that runs on the tcp port 8822, I would like to sniff it to learn more about how the packets work and everything, I can capture the packets just fine but I am wondering about what I am seeing at the wireshark.</p><p>For example the first entry:</p><pre><code>0000  00 30 b8 d3 d6 30 00 1f  d0 d2 28 52 08 00 45 00   .0...0.. ..(R..E.
0010  00 30 05 d3 40 00 80 06  8b 62 c9 50 d7 cd ae 24   [email protected] .b.P...$
0020  1a 50 6e bc 21 ef 0f c6  bc 34 00 00 00 00 70 02   .Pn.!... .4....p.
0030  ff ff bc e6 00 00 02 04  05 b4 01 01 04 02         ........ ......</code></pre><p>How do I define where it starts and how do I read it ?</p><p>Unrealistic example 00 30 b8 d3 is a 4 byte and translates to 123123 or I should discard the first byte or first 2 bytes as trash data...</p><p>Is the first entry in the above code tag the raw packets or not ?</p><p>PS: if you are going to post books, please instead post links that maybe be hand and readable online without fees, thanks for the understanding.</p><p>EDIT:</p><p>So I have started understanding some of it:</p><pre><code>header ? 00 30 b8 d3 d6 30 00 1f  d0 d2 28 52 08 00 
header size ? 45</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '11, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/cc25a5ff4c4443c9c701a4086da729f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prixone&#39;s gravatar image" /><p><span>Prixone</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prixone has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '11, 22:01</strong> </span></p></div></div><div id="comments-container-4265" class="comments-container"></div><div id="comment-tools-4265" class="comment-tools"></div><div class="clear"></div><div id="comment-4265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4267"></span>

<div id="answer-container-4267" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4267-score" class="post-score" title="current number of votes">2</div><span id="post-4267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Prixone has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the decode pane of Wireshark, or just the hex view? The decode pane will decode most of the packet for you except the payload.</p><p>For example: the byte example 00 30 b8 d3 is neither a 4 byte value nor trash data, it's the first 4 bytes of the receiving MAC address (which is 00 30 b8 d3 d6 30). The sender's MAC is the next 6 bytes (00 1f d0 d2 28 52), and after that comes the 2 byte value for the ethertype (08 00, which means this is an IP packet). The 45 is indeed a combination of the header length as well as the IP protocol type, which is TCP in this case.</p><p>All of this you can see by looking at the decode pane. If you want to know which bytes are decoded to what you can mark them in the hex view and the decode pane will show you exactly what they mean (as far as there's a dissector that understands that part of the packet).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '11, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 May '11, 02:29</strong> </span></p></div></div><div id="comments-container-4267" class="comments-container"><span id="4271"></span><div id="comment-4271" class="comment"><div id="post-4271-score" class="comment-score"></div><div class="comment-text"><p>@Jasper thanks for the compreensive answer, I wasnt aware of the click navigation thing until I read it here then I noticed that not only on the hex but on the bytes I could click and it would iterate with the above window to guide me thru what I was clicking at. Would all the initial data be considered as the header then and the payload the sent information for example ?</p></div><div id="comment-4271-info" class="comment-info"><span class="comment-age">(28 May '11, 11:15)</span> <span class="comment-user userinfo">Prixone</span></div></div><span id="4277"></span><div id="comment-4277" class="comment"><div id="post-4277-score" class="comment-score"></div><div class="comment-text"><p>Payload is what is transported by the packet, or, in short, everything after all protocol headers that are neccessary to transport it. So in your case, if you send application data via TCP, that will be the payload (or "sent information").</p><p>The bytes you quoted are only headers: Ethernet, IP, TCP, with TCP having a payload length of zero, meaning, there is no payload in the packet. Not surprising, since it's a SYN packet, which is used to establish the TCP session as part of the initial TCP three way handshake.</p></div><div id="comment-4277-info" class="comment-info"><span class="comment-age">(29 May '11, 02:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-4267" class="comment-tools"></div><div class="clear"></div><div id="comment-4267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4269"></span>

<div id="answer-container-4269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4269-score" class="post-score" title="current number of votes">1</div><span id="post-4269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As this is the Wireshark Q&amp;A site, I'm sure you have Wireshark installed. You can put your hexadecimal data in a text file and use "File -&gt; Import" in (a recent) release of WIreshark to import it and it will show you exactly what each byte in your stream means...</p><p>Here is what you will see:</p><pre><code>Frame 1: 62 bytes on wire (496 bits), 62 bytes captured (496 bits)
    Arrival Time: May 28, 2011 14:36:15.000000000 CEST
    Epoch Time: 1306586175.000000000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 62 bytes (496 bits)
    Capture Length: 62 bytes (496 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:tcp]
    [Coloring Rule Name: TCP SYN]
    [Coloring Rule String: tcp.flags.syn==1]
Ethernet II, Src: Giga-Byt_d2:28:52 (00:1f:d0:d2:28:52), Dst: Riverdel_d3:d6:30 (00:30:b8:d3:d6:30)
    Destination: Riverdel_d3:d6:30 (00:30:b8:d3:d6:30)
        Address: Riverdel_d3:d6:30 (00:30:b8:d3:d6:30)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Source: Giga-Byt_d2:28:52 (00:1f:d0:d2:28:52)
        Address: Giga-Byt_d2:28:52 (00:1f:d0:d2:28:52)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Type: IP (0x0800)
Internet Protocol Version 4, Src: 201.80.215.205 (201.80.215.205), Dst: 174.36.26.80 (174.36.26.80)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 48
    Identification: 0x05d3 (1491)
    Flags: 0x02 (Don&#39;t Fragment)
        0... .... = Reserved bit: Not set
        .1.. .... = Don&#39;t fragment: Set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 128
    Protocol: TCP (6)
    Header checksum: 0x8b62 [correct]
        [Good: True]
        [Bad: False]
    Source: 201.80.215.205 (201.80.215.205)
    Destination: 174.36.26.80 (174.36.26.80)
Transmission Control Protocol, Src Port: 28348 (28348), Dst Port: 8687 (8687), Seq: 0, Len: 0
    Source port: 28348 (28348)
    Destination port: 8687 (8687)
    [Stream index: 0]
    Sequence number: 0    (relative sequence number)
    Header length: 28 bytes
    Flags: 0x02 (SYN)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgement: Not set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 8687]
                [Message: Connection establish request (SYN): server port 8687]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 65535
    [Calculated window size: 65535]
    Checksum: 0xbce6 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Options: (8 bytes)
        Maximum segment size: 1460 bytes
        No-Operation (NOP)
        No-Operation (NOP)
        TCP SACK Permitted Option: True
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000000000 seconds]
        [Time since previous frame in this TCP stream: 0.000000000 seconds]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '11, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4269" class="comments-container"><span id="4272"></span><div id="comment-4272" class="comment"><div id="post-4272-score" class="comment-score"></div><div class="comment-text"><p>@SYNbit thanks that helps a lot, I just started messing with wireshark and was aware of this panel but not entirely on how it worked until now.</p></div><div id="comment-4272-info" class="comment-info"><span class="comment-age">(28 May '11, 11:15)</span> <span class="comment-user userinfo">Prixone</span></div></div></div><div id="comment-tools-4269" class="comment-tools"></div><div class="clear"></div><div id="comment-4269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


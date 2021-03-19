+++
type = "question"
title = "Lots of TCP Dup ACK &amp; TCP Retransmission messages"
description = '''Hi: I have been experiencing some network issues with connections dropping to various machines. I have a Linux box which is currently sending a large amount of data over SSH to a Synology NAS. I ran a tcpdump on this machine and I&#x27;m seeing what to my noob eyes seems like an inordinate amount of TCP ...'''
date = "2016-12-20T09:12:00Z"
lastmod = "2016-12-20T09:12:00Z"
weight = 58258
keywords = [ "ack", "retransmissions", "tcp" ]
aliases = [ "/questions/58258" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lots of TCP Dup ACK & TCP Retransmission messages](/questions/58258/lots-of-tcp-dup-ack-tcp-retransmission-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58258-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi: I have been experiencing some network issues with connections dropping to various machines. I have a Linux box which is currently sending a large amount of data over SSH to a Synology NAS. I ran a tcpdump on this machine and I'm seeing what to my noob eyes seems like an inordinate amount of TCP Dup ACK &amp; TCP Retransmission messages (see below for an example). Running tcpdump for 2 minutes generated a 2gb capture file, and it's mostly these types of messages. Does anyone have any idea what could be causing this?</p><p>Thanks for any input!</p><p>Example:</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
     35 0.790928       192.168.1.25         192.168.1.19         SSH      15996  Client: Encrypted packet (len=15928)

Frame 35: 15996 bytes on wire (127968 bits), 15996 bytes captured (127968 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.25, Dst: 192.168.1.19
Transmission Control Protocol, Src Port: 58167, Dst Port: 22, Seq: 16437, Ack: 1, Len: 15928
SSH Protocol

No.     Time           Source                Destination           Protocol Length Info
     36 0.790934       192.168.1.25         192.168.1.19         TCP      15996  [TCP Retransmission] 58167â†’22 [ACK] Seq=16437 Ack=1 Win=501 Len=15928 TSval=2496248946 TSecr=1194800600

Frame 36: 15996 bytes on wire (127968 bits), 15996 bytes captured (127968 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.25, Dst: 192.168.1.19
Transmission Control Protocol, Src Port: 58167, Dst Port: 22, Seq: 16437, Ack: 1, Len: 15928

No.     Time           Source                Destination           Protocol Length Info
     37 0.790942       192.168.1.25         192.168.1.19         SSH      576    Client: Encrypted packet (len=508)

Frame 37: 576 bytes on wire (4608 bits), 576 bytes captured (4608 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.25, Dst: 192.168.1.19
Transmission Control Protocol, Src Port: 58167, Dst Port: 22, Seq: 32365, Ack: 1, Len: 508
SSH Protocol

No.     Time           Source                Destination           Protocol Length Info
     38 0.790944       192.168.1.25         192.168.1.19         TCP      576    [TCP Retransmission] 58167â†’22 [PSH, ACK] Seq=32365 Ack=1 Win=501 Len=508 TSval=2496248946 TSecr=1194800600

Frame 38: 576 bytes on wire (4608 bits), 576 bytes captured (4608 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.25, Dst: 192.168.1.19
Transmission Control Protocol, Src Port: 58167, Dst Port: 22, Seq: 32365, Ack: 1, Len: 508

No.     Time           Source                Destination           Protocol Length Info
     39 0.791023       192.168.1.19         192.168.1.25         TCP      68     22â†’58167 [ACK] Seq=1 Ack=4345 Win=5047 Len=0 TSval=1194800602 TSecr=2496248946

Frame 39: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.19, Dst: 192.168.1.25
Transmission Control Protocol, Src Port: 22, Dst Port: 58167, Seq: 1, Ack: 4345, Len: 0

No.     Time           Source                Destination           Protocol Length Info
     40 0.791023       192.168.1.19         192.168.1.25         TCP      68     [TCP Dup ACK 39#1] 22â†’58167 [ACK] Seq=1 Ack=4345 Win=5047 Len=0 TSval=1194800602 TSecr=2496248946

Frame 40: 68 bytes on wire (544 bits), 68 bytes captured (544 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 192.168.1.19, Dst: 192.168.1.25
Transmission Control Protocol, Src Port: 22, Dst Port: 58167, Seq: 1, Ack: 4345, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags">ack retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '16, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/5d9834c931a89abfe90d17d3c9e9ccdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blobby&#39;s gravatar image" /><p>blobby<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blobby has no accepted answers">0%</span></p></div></div><div id="comments-container-58258" class="comments-container"></div><div id="comment-tools-58258" class="comment-tools"></div><div class="clear"></div><div id="comment-58258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


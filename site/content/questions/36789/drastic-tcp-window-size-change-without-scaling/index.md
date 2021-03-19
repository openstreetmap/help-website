+++
type = "question"
title = "drastic tcp window size change without scaling"
description = '''Hopefully someone can help me understand what I&#x27;m seeing here.  A client Syn goes out with a window size of 8190 and no scaling factor. Syn/ACK from server with a window size of 8192 and no scaling factor. Client piggybacks the ACK with data, but suddenly the window size is 64240. Server sends data ...'''
date = "2014-10-02T09:46:00Z"
lastmod = "2014-10-02T14:18:00Z"
weight = 36789
keywords = [ "window", "tcp" ]
aliases = [ "/questions/36789" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [drastic tcp window size change without scaling](/questions/36789/drastic-tcp-window-size-change-without-scaling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36789-score" class="post-score" title="current number of votes">0</div><span id="post-36789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hopefully someone can help me understand what I'm seeing here.</p><ol><li>A client Syn goes out with a window size of 8190 and no scaling factor.</li><li>Syn/ACK from server with a window size of 8192 and no scaling factor.</li><li>Client piggybacks the ACK with data, but suddenly the window size is 64240.</li><li>Server sends data and suddenly it's window size is 64240.</li></ol><p>I don't understand how the window size can change so drastically when initial size is 8K and no scaling is enabled. Any insight is greatly appreciated.</p><pre><code>No.     Time        TCPStrmDelta Source                Destination           Protocol Stream     SeQ        nSeQ       ACK        TCP Len B-flight Length Flags Window Size Info
  10528 181.247065  0.000000000  172.22.0.196          172.22.0.201          TCP      159        0                     0          0                     60     0x0002     8190        63973→443 [SYN] Seq=0 Win=8190 Len=0 MSS=1460

Frame 10528: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: 92:69:13:b7:6d:b0 (92:69:13:b7:6d:b0), Dst: Vmware_98:6a:14 (00:50:56:98:6a:14)
Internet Protocol Version 4, Src: 172.22.0.196 (172.22.0.196), Dst: 172.22.0.201 (172.22.0.201)
Transmission Control Protocol, Src Port: 63973 (63973), Dst Port: 443 (443), Seq: 0, Len: 0
    Source Port: 63973 (63973)
    Destination Port: 443 (443)
    [Stream index: 159]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 0
    Header Length: 24 bytes
    .... 0000 0000 0010 = Flags: 0x002 (SYN)
    Window size value: 8190
    [Calculated window size: 8190]
    Checksum: 0x2f91 [validation disabled]
    Urgent pointer: 0
    Options: (4 bytes), Maximum segment size
        Maximum segment size: 1460 bytes
    [Timestamps]

No.     Time        TCPStrmDelta Source                Destination           Protocol Stream     SeQ        nSeQ       ACK        TCP Len B-flight Length Flags Window Size Info
  10529 181.247170  0.000105000  172.22.0.201          172.22.0.196          TCP      159        0                     1          0                     60     0x0012     8192        443→63973 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460

Frame 10529: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: Vmware_98:6a:14 (00:50:56:98:6a:14), Dst: 92:69:13:b7:6d:b0 (92:69:13:b7:6d:b0)
Internet Protocol Version 4, Src: 172.22.0.201 (172.22.0.201), Dst: 172.22.0.196 (172.22.0.196)
Transmission Control Protocol, Src Port: 443 (443), Dst Port: 63973 (63973), Seq: 0, Ack: 1, Len: 0
    Source Port: 443 (443)
    Destination Port: 63973 (63973)
    [Stream index: 159]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header Length: 24 bytes
    .... 0000 0001 0010 = Flags: 0x012 (SYN, ACK)
    Window size value: 8192
    [Calculated window size: 8192]
    Checksum: 0xf8ce [validation disabled]
    Urgent pointer: 0
    Options: (4 bytes), Maximum segment size
        Maximum segment size: 1460 bytes
    [SEQ/ACK analysis]
    [Timestamps]

No.     Time        TCPStrmDelta Source                Destination           Protocol Stream     SeQ        nSeQ       ACK        TCP Len B-flight Length Flags Window Size Info
  10530 181.247194  0.000024000  172.22.0.196          172.22.0.201          TLSv1    159        1          113        1          112        112        166    0x0018     64240       Client Hello

Frame 10530: 166 bytes on wire (1328 bits), 166 bytes captured (1328 bits) on interface 0
Ethernet II, Src: 92:69:13:b7:6d:b0 (92:69:13:b7:6d:b0), Dst: Vmware_98:6a:14 (00:50:56:98:6a:14)
Internet Protocol Version 4, Src: 172.22.0.196 (172.22.0.196), Dst: 172.22.0.201 (172.22.0.201)
Transmission Control Protocol, Src Port: 63973 (63973), Dst Port: 443 (443), Seq: 1, Ack: 1, Len: 112
    Source Port: 63973 (63973)
    Destination Port: 443 (443)
    [Stream index: 159]
    [TCP Segment Len: 112]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 113    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header Length: 20 bytes
    .... 0000 0001 1000 = Flags: 0x018 (PSH, ACK)
    Window size value: 64240
    [Calculated window size: 64240]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0x26cb [validation disabled]
    Urgent pointer: 0
    [SEQ/ACK analysis]
    [Timestamps]
Secure Sockets Layer

No.     Time        TCPStrmDelta Source                Destination           Protocol Stream     SeQ        nSeQ       ACK        TCP Len B-flight Length Flags Window Size Info
  10531 181.247636  0.000442000  172.22.0.201          172.22.0.196          TLSv1    159        1          146        113        145        145        199    0x0018     64240       Server Hello, Change Cipher Spec, Encrypted Handshake Message

Frame 10531: 199 bytes on wire (1592 bits), 199 bytes captured (1592 bits) on interface 0
Ethernet II, Src: Vmware_98:6a:14 (00:50:56:98:6a:14), Dst: 92:69:13:b7:6d:b0 (92:69:13:b7:6d:b0)
Internet Protocol Version 4, Src: 172.22.0.201 (172.22.0.201), Dst: 172.22.0.196 (172.22.0.196)
Transmission Control Protocol, Src Port: 443 (443), Dst Port: 63973 (63973), Seq: 1, Ack: 113, Len: 145
    Source Port: 443 (443)
    Destination Port: 63973 (63973)
    [Stream index: 159]
    [TCP Segment Len: 145]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 146    (relative sequence number)]
    Acknowledgment number: 113    (relative ack number)
    Header Length: 20 bytes
    .... 0000 0001 1000 = Flags: 0x018 (PSH, ACK)
    Window size value: 64240
    [Calculated window size: 64240]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0x9dc5 [validation disabled]
    Urgent pointer: 0
    [SEQ/ACK analysis]
    [Timestamps]
Secure Sockets Layer</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '14, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/9501a0a9cba9c6ae399345ab0baf8b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsuida&#39;s gravatar image" /><p><span>dsuida</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsuida has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '14, 09:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-36789" class="comments-container"><span id="36790"></span><div id="comment-36790" class="comment"><div id="post-36790-score" class="comment-score"></div><div class="comment-text"><p>Sorry about the formatting of the dissected packets. Looked good in the draft and then got all mushed together when I published it.</p></div><div id="comment-36790-info" class="comment-info"><span class="comment-age">(02 Oct '14, 09:48)</span> <span class="comment-user userinfo">dsuida</span></div></div><span id="36792"></span><div id="comment-36792" class="comment"><div id="post-36792-score" class="comment-score"></div><div class="comment-text"><p>text dumps are always hard to read. I reformatted your quote to make it a little easier, but if you can, post the trace on <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>. Use TraceWrangler (<a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a>) in case you need to sanitize it first.</p></div><div id="comment-36792-info" class="comment-info"><span class="comment-age">(02 Oct '14, 09:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36793"></span><div id="comment-36793" class="comment"><div id="post-36793-score" class="comment-score">1</div><div class="comment-text"><p>Use the "Code Sample" button on the selected text to format it a little better.</p><p>However, text output analysis is never fun, its much easier for folks to assist if you share an actual capture of the traffic as they can then use the tool they know best, Wireshark :-)</p></div><div id="comment-36793-info" class="comment-info"><span class="comment-age">(02 Oct '14, 09:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36789" class="comment-tools"></div><div class="clear"></div><div id="comment-36789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36794"></span>

<div id="answer-container-36794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36794-score" class="post-score" title="current number of votes">0</div><span id="post-36794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you see is normal behavior. Both sides send a small window size and neither announce that they are able to use window scaling. So in the next step they both pull up their TCP window to 64k to allow the other node to send more than just a few packets in case that there is a lot of data to be transferred.</p><p>It's quite normal to see that kind of session behavior - as soon as both know that the connection is established and what the parameters are they simply adjust their window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36794" class="comments-container"><span id="36795"></span><div id="comment-36795" class="comment"><div id="post-36795-score" class="comment-score"></div><div class="comment-text"><p>Thanks. So if that is the case, what's the point in even setting an initial window size and scaling factor in the handshake if both sides end up ignoring it anyhow?</p></div><div id="comment-36795-info" class="comment-info"><span class="comment-age">(02 Oct '14, 10:15)</span> <span class="comment-user userinfo">dsuida</span></div></div><span id="36806"></span><div id="comment-36806" class="comment"><div id="post-36806-score" class="comment-score"></div><div class="comment-text"><p>It is to conserve memory for connection that are not guaranteed to be established yet. The OS/TCP stack needs to reserve as much memory for incoming bytes as promised in the window size (which is essentially just a buffer), so if you waste too much memory on connections from the start you might run out of memory.</p></div><div id="comment-36806-info" class="comment-info"><span class="comment-age">(02 Oct '14, 14:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36794" class="comment-tools"></div><div class="clear"></div><div id="comment-36794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


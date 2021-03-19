+++
type = "question"
title = "TCP ACKed unseen segment"
description = '''Why do wireshark say &quot;TCP ACKed unseen segment&quot; in frame 718 (see below) when the segment has been seen in frame 713 ?? No. Time Source Destination Protocol Length Info   712 14:18:42.604065 10.11.78.193 10.168.1.11 TLSv1 1434 Ignored Unknown Record  Frame 712: 1434 bytes on wire (11472 bits), 1434 ...'''
date = "2012-12-21T06:34:00Z"
lastmod = "2013-01-02T05:29:00Z"
weight = 17132
keywords = [ "acked", "unseen" ]
aliases = [ "/questions/17132" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed unseen segment](/questions/17132/tcp-acked-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17132-score" class="post-score" title="current number of votes">0</div><span id="post-17132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Why do wireshark say "TCP ACKed unseen segment" in frame 718 (see below) when the segment has been seen in frame 713 ??</p><pre><code>No.     Time            Source                Destination           Protocol Length Info                                                            
    712 14:18:42.604065 10.11.78.193          10.168.1.11           TLSv1    1434   Ignored Unknown Record

Frame 712: 1434 bytes on wire (11472 bits), 1434 bytes captured (11472 bits)
Ethernet II, Src: Cisco_ff:fc:f0 (00:08:e3:ff:fc:f0), Dst: Hewlett-_77:98:28 (18:a9:05:77:98:28)
Internet Protocol Version 4, Src: 10.11.78.193 (10.11.78.193), Dst: 10.168.1.11 (10.168.1.11)
Transmission Control Protocol, Src Port: https (443), Dst Port: 39083 (39083), Seq: 494642, Ack: 1, Len: 1380
    Source port: https (443)
    Destination port: 39083 (39083)
    [Stream index: 4]
    Sequence number: 494642    (relative sequence number)
    [Next sequence number: 496022    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
    Window size value: 63531
    [Calculated window size: 63531]
    [Window size scaling factor: -1 (unkown)]
    Checksum: 0x31d7 [validation disabled]

No.     Time            Source                Destination           Protocol Length Info                                                            
    713 14:18:42.604067 10.11.78.193          10.168.1.11           TLSv1    1434   Ignored Unknown Record

Frame 713: 1434 bytes on wire (11472 bits), 1434 bytes captured (11472 bits)
Ethernet II, Src: Cisco_ff:fc:f0 (00:08:e3:ff:fc:f0), Dst: Hewlett-_77:98:28 (18:a9:05:77:98:28)
Internet Protocol Version 4, Src: 10.11.78.193 (10.11.78.193), Dst: 10.168.1.11 (10.168.1.11)
Transmission Control Protocol, Src Port: https (443), Dst Port: 39083 (39083), Seq: 496022, Ack: 1, Len: 1380
    Source port: https (443)
    Destination port: 39083 (39083)
    [Stream index: 4]
    Sequence number: 496022    (relative sequence number)
    [Next sequence number: 497402    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
    Window size value: 63531
    [Calculated window size: 63531]
    [Window size scaling factor: -1 (unkown)]
    Checksum: 0xbb9a [validation disabled]

No.     Time            Source                Destination           Protocol Length Info                                                            
    718 14:18:42.604093 10.168.1.11           10.11.78.193          TCP      60     [TCP ACKed unseen segment] 39083 &gt; https [ACK] Seq=1 Ack=496022

Frame 718: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: Hewlett-_77:98:28 (18:a9:05:77:98:28), Dst: Cisco_ff:fc:f0 (00:08:e3:ff:fc:f0)
Internet Protocol Version 4, Src: 10.168.1.11 (10.168.1.11), Dst: 10.11.78.193 (10.11.78.193)
Transmission Control Protocol, Src Port: 39083 (39083), Dst Port: https (443), Seq: 1, Ack: 496022, Len: 0
    Source port: 39083 (39083)
    Destination port: https (443)
    [Stream index: 4]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 496022    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
    Window size value: 64170
    [Calculated window size: 64170]
    [Window size scaling factor: -1 (unkown)]
    Checksum: 0x6d38 [validation disabled]
    [SEQ/ACK analysis]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-acked" rel="tag" title="see questions tagged &#39;acked&#39;">acked</span> <span class="post-tag tag-link-unseen" rel="tag" title="see questions tagged &#39;unseen&#39;">unseen</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '12, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/50f3c8806b3ff402017d06deb24b752f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gschaarup&#39;s gravatar image" /><p><span>gschaarup</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gschaarup has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Dec '12, 06:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17132" class="comments-container"></div><div id="comment-tools-17132" class="comment-tools"></div><div class="clear"></div><div id="comment-17132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17379"></span>

<div id="answer-container-17379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17379-score" class="post-score" title="current number of votes">3</div><span id="post-17379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First, the ACK from one system is the <em>next expected sequence number</em> from the other system, not a sequence number that has already been seen. The ACK of 496022 in frame 718 is not acknowledging the sequence number of 496022 in frame 713; its saying that the sequence number 496022 is what it expects next. The ACK in frame 718 is acknowledging frame 712, not frame 713. The sequence number of frame 712 is 494642 and there 1380 bytes in the TCP portion of that frame, so frame 712 contains bytes 494642 through 496021, and 496022 should be next. You can see "Next sequence number: 496022" in the Packet Details portion of Frame 712.</p><p>Second, ACKs are cumulative. When 10.68.1.11 sends an ACK of 496022, it's not only saying that it expects sequence number 496022 next, it's also saying that it has received bytes 1 through 496021. So, by transmitting a sequence number of 496022,10.68.1.11 is saying that it has received all data from 10.11.78.193 up through and including frame 712. Somewhere before frame 712 there was a frame that Wireshark didn't see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '13, 05:10</strong> </span></p></div></div><div id="comments-container-17379" class="comments-container"><span id="17381"></span><div id="comment-17381" class="comment"><div id="post-17381-score" class="comment-score"></div><div class="comment-text"><p>Thank you for that clarification.</p></div><div id="comment-17381-info" class="comment-info"><span class="comment-age">(02 Jan '13, 05:29)</span> <span class="comment-user userinfo">gschaarup</span></div></div></div><div id="comment-tools-17379" class="comment-tools"></div><div class="clear"></div><div id="comment-17379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17133"></span>

<div id="answer-container-17133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17133-score" class="post-score" title="current number of votes">0</div><span id="post-17133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could a segment from 10.11.78.193 be missing before frame 712? What was the last ACK number from 10.168.1.11 before frame 712 and what were the frames of 10.11.78.193 since the previous ACK of 10.168.1.11?</p><p>Could you upload the capture file to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and ost the link here for us to check?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '12, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17133" class="comments-container"><span id="17181"></span><div id="comment-17181" class="comment"><div id="post-17181-score" class="comment-score"></div><div class="comment-text"><p>I am sorry but capture wasn´t saved, but why should a missing segment before frame 712 have any influence on the dialog from 713 and onwards ?</p></div><div id="comment-17181-info" class="comment-info"><span class="comment-age">(22 Dec '12, 15:28)</span> <span class="comment-user userinfo">gschaarup</span></div></div><span id="17183"></span><div id="comment-17183" class="comment"><div id="post-17183-score" class="comment-score"></div><div class="comment-text"><p>Consider this:</p><pre><code>a-&gt;b seq 100, len 10, ack 1
a-&gt;b seq 120, len 10, ack 1
a-&gt;b seq 130, len 10, ack 1
b-&gt;a seq 1, ack 140</code></pre><p>clearly b is acking a segment (seq 110-119) that has not been seen by wireshark.</p></div><div id="comment-17183-info" class="comment-info"><span class="comment-age">(22 Dec '12, 15:35)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17376"></span><div id="comment-17376" class="comment"><div id="post-17376-score" class="comment-score"></div><div class="comment-text"><p>But:<br />
</p><p>frame 713 10.11.78.193 -&gt; 10.168.1.11 is seq 496022<br />
frame 718 10.168.1.11 -&gt; 10.11.78.193 is ack 496022</p><p>and here wireshark say "TCP ACKed unseen segment" (why unseen, when the packet (seq=496022) has been seen in frame 713 ?)</p></div><div id="comment-17376-info" class="comment-info"><span class="comment-age">(01 Jan '13, 22:22)</span> <span class="comment-user userinfo">gschaarup</span></div></div><span id="17377"></span><div id="comment-17377" class="comment"><div id="post-17377-score" class="comment-score"></div><div class="comment-text"><p>Wireshark might indeed be wrong here. But I tried to say that that depends on the packets before frame 712. Are you able to share the pcap file of the whole TCP stream?</p><p>You could upload it to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and paste the link to it in a comment.</p></div><div id="comment-17377-info" class="comment-info"><span class="comment-age">(02 Jan '13, 00:49)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-17133" class="comment-tools"></div><div class="clear"></div><div id="comment-17133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "TCP Dup ACK and a TCP retransmission _large packet size"
description = '''I do not understand why there is a DUP ACK and a TCP retransmission was intiated. i am using cisco ASA as a ptoxy for TCP connication, when i set the MTU to 1500 connection works with out any problem, but when i set the MTU to larger than 1500 i see a DUP ACK and a TCP retransmission. is it becouse ...'''
date = "2015-04-26T05:31:00Z"
lastmod = "2015-04-26T13:36:00Z"
weight = 41852
keywords = [ "tcp_retransmission", "tcp" ]
aliases = [ "/questions/41852" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dup ACK and a TCP retransmission \_large packet size](/questions/41852/tcp-dup-ack-and-a-tcp-retransmission-_large-packet-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41852-score" class="post-score" title="current number of votes">0</div><span id="post-41852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I do not understand why there is a DUP ACK and a TCP retransmission was intiated. i am using cisco ASA as a ptoxy for TCP connication, when i set the MTU to 1500 connection works with out any problem, but when i set the MTU to larger than 1500 i see a DUP ACK and a TCP retransmission. is it becouse the large MTU ?</p><pre><code>1055 &gt; x.x.x.x 10.1.23.25 TCP 60 22345→80 [ACK] Seq=1 Ack=171121 Win=64240 Len=0
1057 &gt; x.x.x.x 10.1.23.25 TCP 60 22345→80 [ACK] Seq=1 Ack=173881 Win=64240 Len=0
1060 &gt; x.x.x.x 10.1.23.25 TCP 60 22345→80 [ACK] Seq=1 Ack=176641 Win=63860 Len=0
1061 &gt; x.x.x.x 10.1.23.25 TCP 60 [TCP Dup ACK 1060#1] 22345→80 [ACK] Seq=1 Ack=176641 Win=63860 Len=0
1063 &gt;x.x.x.x 10.1.23.25 TCP 60 22345→80 [ACK] Seq=1 Ack=179401 Win=64240 Len=0
1064 &gt; x.x.x.x 10.1.23.25 TCP 66 [TCP Dup ACK 1063#1] 22345→80 [ACK] Seq=1 Ack=179401 Win=64240 Len=0 SLE=180781 SRE=182161
1065 &gt; 10.1.23.25 x.x.x.x TCP 4194 80→22345 [ACK] Seq=224941 Ack=1 Win=6640 Len=4140[Packet size limited during capture]
1067 &gt; x.x.x.x 10.1.23.25 TCP 74 [TCP Dup ACK 1063#2] 22345→80 [ACK] Seq=1 Ack=179401 Win=64240 Len=0 SLE=180781 SRE=182161 SLE=184921 SRE=186301
1068 &gt; 10.1.23.25 x.x.x.x TCP 1434 [TCP Fast Retransmission] 80→22345 [ACK] Seq=179401 Ack=1 Win=6640 Len=1380[Packet size limited during capture]
1069 &gt; x.x.x.x 10.1.23.25 TCP 74 [TCP Dup ACK 1063#3] 22345→80 [ACK] Seq=1 Ack=179401 Win=64240 Len=0 SLE=184921 SRE=186301 SLE=189061 SRE=190441
1070 &gt; 10.1.23.25 x.x.x.x TCP 1434 [TCP Retransmission] 80→22345 [ACK] Seq=182161 Ack=1 Win=6640 Len=1380[Packet size limited during capture]
1117 &gt; x.x.x.x 10.1.23.25 TCP 74 [TCP Dup ACK 1063#4] 22345→80 [ACK] Seq=1 Ack=179401 Win=64240 Len=0 SLE=189061 SRE=190441 SLE=193201 SRE=194581</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '15, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/03882972d96b7e76ef905f73a602b4af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAM_R&#39;s gravatar image" /><p><span>RAM_R</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAM_R has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '15, 06:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41852" class="comments-container"></div><div id="comment-tools-41852" class="comment-tools"></div><div class="clear"></div><div id="comment-41852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41855"></span>

<div id="answer-container-41855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41855-score" class="post-score" title="current number of votes">0</div><span id="post-41855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unless your devices all run with Jumbo frame support enabled you cannot set an MTU greater than 1500.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41855" class="comments-container"><span id="41856"></span><div id="comment-41856" class="comment"><div id="post-41856-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thank you for your answer.</p><p>actually, Jumbo frame support is enabled, and all the interfaces have the same MTU size equal to 9198.</p><p>also, from the capture I can see the scaling widows is unknown. but in the TCP hand shack is being negotiated</p><p>1624 3.175962 x.x.x.x 10.1.244.25 TCP 74 [TCP Dup ACK 1620#1] 22345→80 [ACK] Seq=1 Ack=186301 Win=63860 Len=0 SLE=193201 SRE=229081 SLE=189061 SRE=190441</p><p>Window size value: 63860</p><p>Calculated window size: 63860</p><p>Window size scaling factor: -1 (unknown)</p></div><div id="comment-41856-info" class="comment-info"><span class="comment-age">(26 Apr '15, 06:48)</span> <span class="comment-user userinfo">RAM_R</span></div></div><span id="41857"></span><div id="comment-41857" class="comment"><div id="post-41857-score" class="comment-score"></div><div class="comment-text"><p>Scaling factor -1 happens if don't have captured the tcp handshake.</p></div><div id="comment-41857-info" class="comment-info"><span class="comment-age">(26 Apr '15, 07:25)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="41860"></span><div id="comment-41860" class="comment"><div id="post-41860-score" class="comment-score"></div><div class="comment-text"><p>yes, I cannot see the TCP handchack for this in the capture. is it possible that the reason for this behavior is the buffer limits.</p></div><div id="comment-41860-info" class="comment-info"><span class="comment-age">(26 Apr '15, 08:02)</span> <span class="comment-user userinfo">RAM_R</span></div></div></div><div id="comment-tools-41855" class="comment-tools"></div><div class="clear"></div><div id="comment-41855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41865"></span>

<div id="answer-container-41865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41865-score" class="post-score" title="current number of votes">0</div><span id="post-41865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"I do not understand why there is a DUP ACK and a TCP retransmission was intiated."<br />
</p><blockquote><p>Because the client is reporting gaps using the TCP SACK option</p></blockquote><p>"i am using cisco ASA as a ptoxy for TCP connication, when i set the MTU to 1500 connection works with out any problem, but when i set the MTU to larger than 1500 i see a DUP ACK and a TCP retransmission. is it becouse the large MTU ?"<br />
</p><blockquote><p>Obviously yes ;-)</p></blockquote><p>The negotiated MSS is 1380 bytes: The client ACKs 2*1380 bytes and the gap reports and re-tranmsissions are also for 1380 bytes segments (ASA adjusts the negotiated MSS values in the SYN packets)</p><p>"and all the interfaces have the same MTU size equal to 9198"<br />
</p><blockquote><p>the maximum size for JumboFrames is 9000 bytes</p></blockquote><p>TCP segmentation offload (TSO or <a href="http://www.peerwisdom.org/2013/04/03/large-send-offload-and-network-performance/">LargeSendOffload</a>) seems to be enabled at the sender and defining a too large MTU size might confuse this algorithm.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '15, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-41865" class="comments-container"></div><div id="comment-tools-41865" class="comment-tools"></div><div class="clear"></div><div id="comment-41865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


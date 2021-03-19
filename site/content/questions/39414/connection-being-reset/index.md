+++
type = "question"
title = "Connection being reset"
description = '''I have a device on my network trying to connect to a remote server but is failing to do so. I have taken the device off-site and it will connect, so I believe I have an issue with my firewall but can&#x27;t pin point my issue. I am seeing a lot of TCP Retransmissions and TCP Dup Acks in my capture. https...'''
date = "2015-01-26T13:50:00Z"
lastmod = "2015-01-26T16:22:00Z"
weight = 39414
keywords = [ "connection_reset", "dup-ack", "retransmissions" ]
aliases = [ "/questions/39414" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Connection being reset](/questions/39414/connection-being-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39414-score" class="post-score" title="current number of votes">0</div><span id="post-39414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device on my network trying to connect to a remote server but is failing to do so. I have taken the device off-site and it will connect, so I believe I have an issue with my firewall but can't pin point my issue. I am seeing a lot of TCP Retransmissions and TCP Dup Acks in my capture. <a href="https://www.dropbox.com/s/srv5tlg1jy93bbz/egress.pcap?dl=0">https://www.dropbox.com/s/srv5tlg1jy93bbz/egress.pcap?dl=0</a><br />
</p><p>This device connected properly before but now is unable to. Any help would be appreciated.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connection_reset" rel="tag" title="see questions tagged &#39;connection_reset&#39;">connection_reset</span> <span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '15, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/fcc2daee8c32d00914f9d70c14148cff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Speaker&#39;s gravatar image" /><p><span>Speaker</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Speaker has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39414" class="comments-container"></div><div id="comment-tools-39414" class="comment-tools"></div><div class="clear"></div><div id="comment-39414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39417"></span>

<div id="answer-container-39417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39417-score" class="post-score" title="current number of votes">1</div><span id="post-39417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your capture file the content of the TCP session is not SSL, what kind of protocol is it? Do you have a NextGen firewall that does protocol inspection? Then most likely it is blocking the packets from your device as it is not SSL.</p><p>You will need to add a new outgoing rule for your device where you disable protocol inspection or better yet, make it inspect the traffic as the protocol that it is using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '15, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39417" class="comments-container"></div><div id="comment-tools-39417" class="comment-tools"></div><div class="clear"></div><div id="comment-39417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39418"></span>

<div id="answer-container-39418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39418-score" class="post-score" title="current number of votes">0</div><span id="post-39418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like 98.100.152.162 is the client (on your network/?/) and 23.99.129.46 is the off-site server.<br />
</p><p>Assuming that is the case, it looks like this capture may have been taken from some intermediary device, since the TTL for packets from 98.100.152.162 is 62.<br />
</p><p>First thing to note, is that it looks like the incoming packets from 23.99.129.46 are not being passed to the actual client.<br />
</p><p>Note the pattern that begins with frame#4</p><p>frame#4 98.100.152.162 &gt;&gt; 23.99.129.46 Seq=1106885107 Ack=496659091 Len=16</p><p>frame#5 23.99.129.46 &gt;&gt; 98.100.152.162 Seq=496659091 Ack=1106885123 Len=0 (ACK for segment in frame #4)</p><p>frame #6 23.99.129.46 &gt;&gt; 98.100.152.162 Seq=496659091 Ack=1106885123 Len=28 (expecting ACK# 496659119)</p><p>frame #7-10 [Server Retransmission of frame #6]</p><p>frame #11 98.100.152.162 &gt;&gt; 23.99.129.46<br />
Seq=1106885123 Ack=496659091 Len=16<br />
Note that the ACK# is no different than frame#4 (also note the 2.3 sec delta between frame #4 and this frame). This implies that the client has not received any server frames since frame #5. The data is not readable, but it is possible that this is an application keepalive from the server (hence the 2+ sec delay and sequence incrementation).<br />
</p><p>frame #12 23.99.129.46 &gt;&gt; 98.100.152.162<br />
Seq=496659119 Ack=1106885139 Len=0 (ACK for segment in frame #11)</p><p>frame #13 98.100.152.162 &gt;&gt; 23.99.129.46 Seq=1106885123 Ack=496659091 Len=16 (Retransmission of frame #11 ~230ms later (looks like an RTO)) This suggests, again, that server segments are not being forwarded to the client.</p><p>frame #14 23.99.129.46 &gt;&gt; 98.100.152.162 Seq=496659119 Ack=1106885139 Len=0 (ACK for frame #11 with SACK options) SLE=1106885123 SRE=1106885139 (Suggests that server never saw frame #4 (missing segment )</p><p>frame #15 98.100.152.162 &gt;&gt; 23.99.129.46 Seq=1106885123 Ack=496659091 Len=16 (Retransmission of frame #11 - Already ACK'd twice by the server (looks like another RTO)</p><p>It appears that RTO driven retransmissions of this frame continue in frames 18, 20, 23, 26, and 29. Each time, the server continues to ACK the segment, with the later segments also including SACK options to indicate that the server never saw frame #4.</p><p>At first glance, it appears that a device is not forwarding the traffic from the server to the client.<br />
</p><p>(didn't have time to dig out the details of why the RST is occurring, exaclty, but I hope this helps)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '15, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p><span>Qwert</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-39418" class="comments-container"></div><div id="comment-tools-39418" class="comment-tools"></div><div class="clear"></div><div id="comment-39418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


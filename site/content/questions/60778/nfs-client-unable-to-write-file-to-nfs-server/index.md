+++
type = "question"
title = "NFS client unable to write file to NFS server"
description = '''NFS client is unable to copy file to NFS server. The NFS client is 10.206.5.158. The NFS server is 10.206.0.200. When the copy is attempted it appears that the session goes in to a cycle of TCP retransmissions. The client appears to transmit multiple packets and the server receives a single large pa...'''
date = "2017-04-12T12:24:00Z"
lastmod = "2017-04-13T12:46:00Z"
weight = 60778
keywords = [ "nfsassurances", "civil" ]
aliases = [ "/questions/60778" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [NFS client unable to write file to NFS server](/questions/60778/nfs-client-unable-to-write-file-to-nfs-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60778-score" class="post-score" title="current number of votes">0</div><span id="post-60778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>NFS client is unable to copy file to NFS server. The NFS client is 10.206.5.158. The NFS server is 10.206.0.200.</p><p>When the copy is attempted it appears that the session goes in to a cycle of TCP retransmissions. The client appears to transmit multiple packets and the server receives a single large packet. The MTUs in the path have been checked and all appear to be 1500.</p><p>Can someone take a look and see if they can see the issue in the traces.</p><p><a href="https://www.cloudshark.org/captures/eb5d9738a5c7">Client capture</a></p><p><a href="https://www.cloudshark.org/captures/9c06b5a0a59a">Server capture</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfsassurances" rel="tag" title="see questions tagged &#39;nfsassurances&#39;">nfsassurances</span> <span class="post-tag tag-link-civil" rel="tag" title="see questions tagged &#39;civil&#39;">civil</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '17, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/847dbd6e288ab8e85e34fa7a11f148e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SloDog&#39;s gravatar image" /><p><span>SloDog</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SloDog has no accepted answers">0%</span></p></div></div><div id="comments-container-60778" class="comments-container"></div><div id="comment-tools-60778" class="comment-tools"></div><div class="clear"></div><div id="comment-60778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60787"></span>

<div id="answer-container-60787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60787-score" class="post-score" title="current number of votes">0</div><span id="post-60787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the the initial transmits arriving at the server still have the tcp.checksum of 0 which indicates that tcp checksum offload (TCO) is enabled at the client.</p><p>If the client is AIX (which I guess it is ) then disabling the offload functions can be done using</p><p>chdev -l ent1 -a large_send=no -a chksum_offload=no -P shutdown -Fr</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-60787" class="comments-container"><span id="60798"></span><div id="comment-60798" class="comment"><div id="post-60798-score" class="comment-score"></div><div class="comment-text"><p>I would disable offloading or updating the driver, too.</p></div><div id="comment-60798-info" class="comment-info"><span class="comment-age">(13 Apr '17, 02:16)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="60809"></span><div id="comment-60809" class="comment"><div id="post-60809-score" class="comment-score"></div><div class="comment-text"><p>What you. I have my systems team checking the setting.</p></div><div id="comment-60809-info" class="comment-info"><span class="comment-age">(13 Apr '17, 09:55)</span> <span class="comment-user userinfo">SloDog</span></div></div><span id="60810"></span><div id="comment-60810" class="comment"><div id="post-60810-score" class="comment-score"></div><div class="comment-text"><p>Not what you. Thank you.</p></div><div id="comment-60810-info" class="comment-info"><span class="comment-age">(13 Apr '17, 09:55)</span> <span class="comment-user userinfo">SloDog</span></div></div><span id="60816"></span><div id="comment-60816" class="comment"><div id="post-60816-score" class="comment-score"></div><div class="comment-text"><p>All offload parameters have been set to off on both ends. The same behavior is be observed. Anyone have any additional ideas?</p><p>Just to confirm Matthias assumption. The server is Linux, the client is AIX.</p></div><div id="comment-60816-info" class="comment-info"><span class="comment-age">(13 Apr '17, 12:46)</span> <span class="comment-user userinfo">SloDog</span></div></div></div><div id="comment-tools-60787" class="comment-tools"></div><div class="clear"></div><div id="comment-60787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60797"></span>

<div id="answer-container-60797" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60797-score" class="post-score" title="current number of votes">0</div><span id="post-60797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can tell you what is happening, but not exactly why.</p><p>This description is for the client side capture, but the server side is very similar.</p><p>There are 2 TCP connections that are re-used over and over. Each time, there is a 3-way handshake, data transfer then Reset. This is repeated on the other connection (tuple) then again on the first connection. This bouncing between the two continues 11 times.</p><p>The data transfers are interesting in that there are always just 3 packets every 1.5 seconds. The pattern is that the first two are retransmissions of earlier data plus one new data packet.</p><p>This pattern means that every data packet is transmitted three times (taking 4.5 seconds) and is only acknowledged after the third retransmission.</p><p>This pattern can be seen in this zoom-in on the TCP Stream chart.</p><p>After an initial burst of some small (occur once each) and then 5 large (retransmitted at least 3 times each) we settle into the pattern of three's. The blue horizontal line passes through three packets and the ACK line follows the third packets each time.</p><p>Why would the receiver only ACK the third ones (when we see the first two in the server-side trace)?</p><p>In the server trace, the pattern is slightly different. Each 1.5 seconds there are 2 packets, the first is size 1436 (later 1448) and the second double at 2872 (later 2896). The server perhaps is not accepting these double-sized packets and hence only ACKing the first smaller ones.</p><p>The reason for this very likely the invalid checksum for the large ones and the good checksum for the 1448 ones. This explains why the receiver is ignoring the large packets.</p><p>The difficult part for you is now to determine what is it in the receiver (server) that is deciding to combine the two received 1436 (or 1448) packets into a single 2872 (or 2896) packet with an incorrect checksum?</p><p>This is the likely "root cause" of your problem.</p><p>Why is the sender transmitting just 3 packets every 1.5 seconds? My guess is that the sender has a retransmission timeout of 1.5 seconds. It is observing that it gets an ACK only after retransmitting each packet twice. It therefore perceives that this is an extremely "congested" network and keeps its transmit window very small (just 3 packets).</p><p>Bear in mind that it sees an ACK to just a single packet, even though it has sent 3 packets in each round trip.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/NFSclient.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p><span>Philst</span><br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '17, 23:49</strong> </span></p></div></div><div id="comments-container-60797" class="comments-container"><span id="60811"></span><div id="comment-60811" class="comment"><div id="post-60811-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This confirms what we were seeing.</p></div><div id="comment-60811-info" class="comment-info"><span class="comment-age">(13 Apr '17, 09:55)</span> <span class="comment-user userinfo">SloDog</span></div></div></div><div id="comment-tools-60797" class="comment-tools"></div><div class="clear"></div><div id="comment-60797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


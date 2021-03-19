+++
type = "question"
title = "Bytes in Flight more than the size of tcp window."
description = '''I have a situation where the server is Mac OS X and client is windows 7. The dump is taken on windows machine. I see that the negotiated window size is 32k (see syn packets) on both windows and mac but the bytes in flight are much more than that. Same is reported by cloudshark&#x27;s graphs of data/time....'''
date = "2012-11-20T03:38:00Z"
lastmod = "2012-11-20T05:11:00Z"
weight = 16103
keywords = [ "windows7", "tcp-bytes-in-flight" ]
aliases = [ "/questions/16103" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Bytes in Flight more than the size of tcp window.](/questions/16103/bytes-in-flight-more-than-the-size-of-tcp-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16103-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a situation where the server is Mac OS X and client is windows 7. The <a href="http://www.cloudshark.org/captures/19827a7efd41">dump</a> is taken on windows machine. I see that the negotiated window size is 32k (see syn packets) on both windows and mac but the bytes in flight are much more than that. Same is reported by cloudshark's graphs of data/time. In this case the tcp send and receive buffers were set at default on both windows and mac.</p><p>I took <a href="http://www.cloudshark.org/captures/726779d098c0">another dump</a> after increasing the send and recv buffers to 128k on mac to see if the announcement changes during the connection establishment, which didn't happen and still a window of 32k was announced but the bytes in flight and cloudshark's graphs reported an increase in data.</p><p>The latency was 500ms between both the connections.</p><p>Why is this announcement just 32k? Is it normal (or even possible) to have more bytes in flight than the tcp window?</p></div><div id="question-tags" class="tags-container tags">windows7 tcp-bytes-in-flight</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/2df84c5f3698faf841410ada02c8e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditya%20Patawari&#39;s gravatar image" /><p>Aditya Patawari<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditya Patawari has no accepted answers">0%</span></p></div></div><div id="comments-container-16103" class="comments-container"></div><div id="comment-tools-16103" class="comment-tools"></div><div class="clear"></div><div id="comment-16103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16111"></span>

<div id="answer-container-16111" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16111-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the trace you provided I don't see a chance that those packets are what really happens on the wire.</p><p>Both OS X and Windows 7 in every way use Window Scaling, advertise their MSS and in most cases provide SACK which are always seen inside TCP options during the handshake. Since in the trace you uploaded both SYN packets are free of options, I would not further investigate the issue, due to the fact that those packets cannot be captured from a real network transmission.</p><p>Your observation is true anyways, a TCP sender must not send more unacknowledged data than the advertised recieve window allows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16111" class="comments-container"></div><div id="comment-tools-16111" class="comment-tools"></div><div class="clear"></div><div id="comment-16111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16106"></span>

<div id="answer-container-16106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16106-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Aditya,</p><p>Are these the original pcap-files or have they been altered/anonymized in any way? There are no TCP Options set in the handshake for instance, which is odd considering you're using OS X and Windows 7 :-)</p><p>You're right, if a receiver announces a windows size of 32k, the sender is not allowed to send more than 32k of data before receiving an acknowledgement.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/c23b8846cec43a35da426aa0657605a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="holmahenkel&#39;s gravatar image" /><p>holmahenkel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="holmahenkel has no accepted answers">0%</span></p></div></div><div id="comments-container-16106" class="comments-container"><span id="16107"></span><div id="comment-16107" class="comment"><div id="post-16107-score" class="comment-score"></div><div class="comment-text"><p>No. They are not altered in anyway. Is there a possibility that windows tcpdump didn't capture the packets properly?</p></div><div id="comment-16107-info" class="comment-info"><span class="comment-age">(20 Nov '12, 04:33)</span> Aditya Patawari</div></div><span id="16126"></span><div id="comment-16126" class="comment"><div id="post-16126-score" class="comment-score">2</div><div class="comment-text"><p>not altered in any way?</p><p>So, the MAC addresses, with the ASCII representation <strong>LOCAL</strong> (4c:4f:43:41:4c:20) and <strong>REMOTE</strong> (52:45:4d:4f:54:45) and the IP address 0.0.0.0 are just incidental?</p></div><div id="comment-16126-info" class="comment-info"><span class="comment-age">(20 Nov '12, 11:07)</span> Kurt Knochner ♦</div></div><span id="16159"></span><div id="comment-16159" class="comment"><div id="post-16159-score" class="comment-score"></div><div class="comment-text"><p>Trust me, it hasn't been touched. I think that address 0.0.0.0 is because it is listening on all the interfaces or maybe because tcpdump is behaving differently on windows.</p></div><div id="comment-16159-info" class="comment-info"><span class="comment-age">(21 Nov '12, 06:17)</span> Aditya Patawari</div></div><span id="16160"></span><div id="comment-16160" class="comment"><div id="post-16160-score" class="comment-score"></div><div class="comment-text"><p>Pretty sure that it is a bogus trace. IP 0.0.0.0 is never used in unicast communication; only DHCP negotiations using broadcast frames have it because the client node has no IP yet. My bet is, you're using a software network simulator that allows to capture, leading to bogus stuff in the headers - which means the simulator doesn't do it's job too well.</p><p>The "listening on 0.0.0.0" is a local system thing, and has nothing to do with IPs that are actually used on "the wire" in directional communications.</p></div><div id="comment-16160-info" class="comment-info"><span class="comment-age">(21 Nov '12, 06:46)</span> Jasper ♦♦</div></div><span id="16162"></span><div id="comment-16162" class="comment"><div id="post-16162-score" class="comment-score"></div><div class="comment-text"><p>It is not a bogus trace. I would have had no issues in accepting any alteration. People are not killed for modifying the traces for anonymity. I'll make sure that next time I take some screenshots while taking the dump.</p><p>Anyway, I understand from Landi's answer that the trace is more or less useless so I would not spend my time on this.</p></div><div id="comment-16162-info" class="comment-info"><span class="comment-age">(21 Nov '12, 07:29)</span> Aditya Patawari</div></div><span id="16164"></span><div id="comment-16164" class="comment not_top_scorer"><div id="post-16164-score" class="comment-score"></div><div class="comment-text"><p>Sorry if my comment sounded offensive, it wasn't meant to be. It is just that a trace with addresses like that can't be captured under normal circumstances. I think it is wise not to spend any more time on it.</p></div><div id="comment-16164-info" class="comment-info"><span class="comment-age">(21 Nov '12, 08:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16106" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Server sends tons of SYN ACK packets in answer to a single SYN packet"
description = '''Hi. looking at suspicious traffic I found that a lab Windows Domain Controller with DNS enabled was sending, in a single second, over 100 SYN,ACK packets in response to a single SYN packet. The SYN packet was sent by a workstation joined to the server&#x27;s domain.  The SYN,ACK packet&#x27;s data part cannot...'''
date = "2014-01-03T20:54:00Z"
lastmod = "2014-01-03T20:54:00Z"
weight = 28561
keywords = [ "flood", "53", "dns", "tcp" ]
aliases = [ "/questions/28561" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server sends tons of SYN ACK packets in answer to a single SYN packet](/questions/28561/server-sends-tons-of-syn-ack-packets-in-answer-to-a-single-syn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28561-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. looking at suspicious traffic I found that a lab Windows Domain Controller with DNS enabled was sending, in a single second, over 100 SYN,ACK packets in response to a single SYN packet. The SYN packet was sent by a workstation joined to the server's domain.</p><p>The SYN,ACK packet's data part cannot be read in clear text, but It looks like there are only two variations of this packet. A quick inspection shows that variation_1 and variation_2 are being sent in a round-robin fashion. In all SYN,ACK packets the destination port is the same (59092), Seq=0, Ack=1, Win=8192, Len=0. This is not a covert channel, unless using some form of morse code. And I have a hard time believing that a lab DC would DoS a workstation in this fashion.</p><p>Any hint would be appreciated.</p></div><div id="question-tags" class="tags-container tags">flood 53 dns tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '14, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/03ad002cc5653364d596627b4e6143b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcus&#39;s gravatar image" /><p>Marcus<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcus has no accepted answers">0%</span></p></div></div><div id="comments-container-28561" class="comments-container"><span id="28566"></span><div id="comment-28566" class="comment"><div id="post-28566-score" class="comment-score"></div><div class="comment-text"><p>can you provide a trace? If the data is sensitive you could use TraceWrangler to sanitize it before posting it on CloudShark.</p></div><div id="comment-28566-info" class="comment-info"><span class="comment-age">(04 Jan '14, 06:35)</span> Jasper ♦♦</div></div><span id="28582"></span><div id="comment-28582" class="comment"><div id="post-28582-score" class="comment-score"></div><div class="comment-text"><p>"The SYN,ACK packet's data part cannot be read in clear text ... In all SYN,ACK packets the destination port is the same (59092), Seq=0, Ack=1, Win=8192, Len=0 ."</p><p>With a len=0 how can there be data with a syn_ack packet? Is the ip.ttl always the same?</p></div><div id="comment-28582-info" class="comment-info"><span class="comment-age">(05 Jan '14, 04:55)</span> mrEEde</div></div><span id="28831"></span><div id="comment-28831" class="comment"><div id="post-28831-score" class="comment-score"></div><div class="comment-text"><blockquote><p>variation_1 and variation_2 are being sent in a round-robin fashion.</p></blockquote><p>do you mind to tell us the difference between the two variations?</p><p>BTW: if you are no longer interested in solving/discussing the problem, we might want to close the question.</p></div><div id="comment-28831-info" class="comment-info"><span class="comment-age">(12 Jan '14, 14:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28561" class="comment-tools"></div><div class="clear"></div><div id="comment-28561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


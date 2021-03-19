+++
type = "question"
title = "LAN slowdown"
description = '''Hello, may any expert can help me please? My LAN runs very slow and I am trying to find out why. Please see the capture I made with Wireshark (see below the link to download the file), where it seems there are wrong or repeated packets or lost packets. I know the cable is fine, as sometimes I reache...'''
date = "2013-03-31T13:26:00Z"
lastmod = "2013-03-31T14:21:00Z"
weight = 19975
keywords = [ "dup-ack", "duplicate", "slow", "lost" ]
aliases = [ "/questions/19975" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [LAN slowdown](/questions/19975/lan-slowdown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19975-score" class="post-score" title="current number of votes">0</div><span id="post-19975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, may any expert can help me please?</p><p>My LAN runs very slow and I am trying to find out why. Please see the capture I made with Wireshark (see below the link to download the file), where it seems there are wrong or repeated packets or lost packets.</p><p>I know the cable is fine, as sometimes I reached high speeds, I believe it is something with the router, the terminals, or any other thing.</p><p>Thanks a lot,</p><p>Jesus</p><p><a href="https://www.dropbox.com/s/f9my2b5q6192ula/capture%201">https://www.dropbox.com/s/f9my2b5q6192ula/capture%201</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '13, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/56f1b8ef43d87c0e9ca2abb1fb7946ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesus&#39;s gravatar image" /><p><span>Jesus</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesus has no accepted answers">0%</span></p></div></div><div id="comments-container-19975" class="comments-container"></div><div id="comment-tools-19975" class="comment-tools"></div><div class="clear"></div><div id="comment-19975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19976"></span>

<div id="answer-container-19976" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19976-score" class="post-score" title="current number of votes">1</div><span id="post-19976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jesus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From a quick look I can see nothing special going wrong. You have a couple of lost packets with retransmissions in there, but the retransmission resolving the packet loss comes in quite fast within one RTT after the loss had been reported - it doesn't get any better than that. And that you have packet loss to the outside world happens in every network, so unless there are tons of lost packets (which there isn't, in your case) there's nothing really bad going on.</p><p>The packet loss will certainly lead to slow results on that speed page you're visiting, but since that page is 60ms away from your testing PC it's not ideal to test your connection speed anyway. There's just too much distance for accidental packet loss to happen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '13, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19976" class="comments-container"></div><div id="comment-tools-19976" class="comment-tools"></div><div class="clear"></div><div id="comment-19976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


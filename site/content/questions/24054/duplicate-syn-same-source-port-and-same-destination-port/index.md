+++
type = "question"
title = "Duplicate SYN, same source port and same destination port"
description = '''Hi, I am looking at a trace to monitor a TCP/IP connection over GPRS and I am noticing that I see two consecutive SYN messages (with a difference of a couple of seconds) everytime there is a connection attempt. I notice that in these 2 SYN messages the source port is always the same, and there is no...'''
date = "2013-08-26T04:38:00Z"
lastmod = "2013-08-26T05:59:00Z"
weight = 24054
keywords = [ "duplicate", "syn" ]
aliases = [ "/questions/24054" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate SYN, same source port and same destination port](/questions/24054/duplicate-syn-same-source-port-and-same-destination-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24054-score" class="post-score" title="current number of votes">0</div><span id="post-24054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am looking at a trace to monitor a TCP/IP connection over GPRS and I am noticing that I see two consecutive SYN messages (with a difference of a couple of seconds) everytime there is a connection attempt. I notice that in these 2 SYN messages the source port is always the same, and there is nothing wrong at checksum level. I don't think this is being done at application level. Can you help me to understand this behavior? I can post here the 2 frames if it helps.</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/15062dd097a6aba52774abb26c6e3ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cpzao&#39;s gravatar image" /><p><span>cpzao</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cpzao has no accepted answers">0%</span></p></div></div><div id="comments-container-24054" class="comments-container"><span id="24055"></span><div id="comment-24055" class="comment"><div id="post-24055-score" class="comment-score"></div><div class="comment-text"><p>Could this be related to routing issues?</p></div><div id="comment-24055-info" class="comment-info"><span class="comment-age">(26 Aug '13, 05:06)</span> <span class="comment-user userinfo">cpzao</span></div></div></div><div id="comment-tools-24054" class="comment-tools"></div><div class="clear"></div><div id="comment-24054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24056"></span>

<div id="answer-container-24056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24056-score" class="post-score" title="current number of votes">0</div><span id="post-24056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I see two consecutive SYN messages (<strong>with a difference of a couple of seconds</strong>) everytime there is a connection attempt</p></blockquote><p>That's (most certainly) the TCP retry algorithm if there is no answer to the first SYN packet.</p><p>Typical reasons for a missing SYN-ACK:</p><ul><li>A failure in the server software (TCP stack or application), where it drops the first SYN. This is rather unusual.</li><li>Overload on the server, which leads to a drop of the first SYN packet. This happens from time to time.</li><li>A firewall and/or a load balancer either blocks or drops the first SYN and/or the SYN-ACK packet. This is a rather common problem.</li><li>The SYN-ACK does not get through to the client, due to routing problems (backward route not correct). This happens rather seldom, and in your case the seconds SYN-ACK gets through, so a routing problem is either not involved or caused by a problem with dynamic routing protocols (works, does not work, works, does not, etc.).</li></ul><p>The best way to figure out what's going on is to capture near (or on) the client <strong>and</strong> the server and then compare the capture files to figure out which packet (SYN or SYN-ACK) get lost at what point in the path.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24056" class="comments-container"></div><div id="comment-tools-24056" class="comment-tools"></div><div class="clear"></div><div id="comment-24056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


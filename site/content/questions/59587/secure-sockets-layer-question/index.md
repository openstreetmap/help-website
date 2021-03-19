+++
type = "question"
title = "Secure Sockets Layer Question"
description = '''Hello, I am analyzing a stream between a client and server in where the server is SaaS. There has been some lengthy lag time with the application and I have been tracking it down where I can from our end. In this particular stream things are clicking back and forth at a good pace then our client mac...'''
date = "2017-02-21T10:44:00Z"
lastmod = "2017-03-21T00:06:00Z"
weight = 59587
keywords = [ "layer", "secure", "noobquestion", "sockets" ]
aliases = [ "/questions/59587" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Secure Sockets Layer Question](/questions/59587/secure-sockets-layer-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59587-score" class="post-score" title="current number of votes">0</div><span id="post-59587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am analyzing a stream between a client and server in where the server is SaaS. There has been some lengthy lag time with the application and I have been tracking it down where I can from our end. In this particular stream things are clicking back and forth at a good pace then our client machine sends an ACK packet then 28.365017 whole seconds later our client sends some kind of data to the server WS shows me it's secure sockets layer with no info in the info column. Is there anyway to figure out what caused this delay? This seems to be the pattern when I'm looking at other streams where things clip along then it takes our client 30 seconds plus to send something to the server.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-secure" rel="tag" title="see questions tagged &#39;secure&#39;">secure</span> <span class="post-tag tag-link-noobquestion" rel="tag" title="see questions tagged &#39;noobquestion&#39;">noobquestion</span> <span class="post-tag tag-link-sockets" rel="tag" title="see questions tagged &#39;sockets&#39;">sockets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '17, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p><span>rock90</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-59587" class="comments-container"></div><div id="comment-tools-59587" class="comment-tools"></div><div class="clear"></div><div id="comment-59587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60213"></span>

<div id="answer-container-60213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60213-score" class="post-score" title="current number of votes">0</div><span id="post-60213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look in your sniffer data for [TCP Window Full] or [Zero Window] packets. It might be that your client resources are over utilized.</p><p>Another possible reason for taking a long time to reply might be security software (Antivirus, IPS, etc.) which takes a while to scan certain packets prior to allowing them through to be processed.</p><p>For either/both of the above, you might try looking at Microsoft's PerfMon statistics to see if there is anything (certain process(s)) with a high CPU utilization or perhaps if you're out of RAM, your machine might be disk swapping.</p><p>Cheers,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-60213" class="comments-container"></div><div id="comment-tools-60213" class="comment-tools"></div><div class="clear"></div><div id="comment-60213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


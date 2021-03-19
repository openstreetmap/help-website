+++
type = "question"
title = "dns resolution latency"
description = '''I am troubleshooting a slow performance issue and I think the DNS resolution may be the cause. But I need to prove that. I am just wondering if I can use Wireshark to get the latency for the DNS resolution. I have a internal DNS server that does the name resolution. My knowledge is very limited on D...'''
date = "2015-02-09T15:53:00Z"
lastmod = "2015-02-09T16:01:00Z"
weight = 39727
keywords = [ "networking", "resolution", "dns" ]
aliases = [ "/questions/39727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dns resolution latency](/questions/39727/dns-resolution-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39727-score" class="post-score" title="current number of votes">0</div><span id="post-39727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting a slow performance issue and I think the DNS resolution may be the cause. But I need to prove that. I am just wondering if I can use Wireshark to get the latency for the DNS resolution. I have a internal DNS server that does the name resolution. My knowledge is very limited on DNS and server but I appreciate any tips I can get to get me going. Thank you very much in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '15, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/b68ecd02e11309f135e5caf5e144f2a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaja&#39;s gravatar image" /><p><span>jaja</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaja has no accepted answers">0%</span></p></div></div><div id="comments-container-39727" class="comments-container"></div><div id="comment-tools-39727" class="comment-tools"></div><div class="clear"></div><div id="comment-39727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39730"></span>

<div id="answer-container-39730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39730-score" class="post-score" title="current number of votes">1</div><span id="post-39730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can find the delta between dns request and response in the field <strong>dns.time</strong>, see screenshot.</p><p><a href="http://i.imgur.com/0iAMyfw.png">http://i.imgur.com/0iAMyfw.png</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39730" class="comments-container"></div><div id="comment-tools-39730" class="comment-tools"></div><div class="clear"></div><div id="comment-39730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


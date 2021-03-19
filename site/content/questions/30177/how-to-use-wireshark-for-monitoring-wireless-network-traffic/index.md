+++
type = "question"
title = "How to use wireshark for monitoring Wireless network traffic?"
description = '''Hello, I have atm. 1 Router, and multiple laptops/phones on the router, Is it possible to figure out who is taking all the bandwidth, with wireshark? G.'''
date = "2014-02-25T06:24:00Z"
lastmod = "2014-03-02T09:04:00Z"
weight = 30177
keywords = [ "traffic", "monitoring", "wireshark" ]
aliases = [ "/questions/30177" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use wireshark for monitoring Wireless network traffic?](/questions/30177/how-to-use-wireshark-for-monitoring-wireless-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30177-score" class="post-score" title="current number of votes">0</div><span id="post-30177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have atm. 1 Router, and multiple laptops/phones on the router, Is it possible to figure out who is taking all the bandwidth, with wireshark?</p><p>G.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '14, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/d4ee95aceba90adcb56692016a4363c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GuKnowMe&#39;s gravatar image" /><p><span>GuKnowMe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GuKnowMe has no accepted answers">0%</span></p></div></div><div id="comments-container-30177" class="comments-container"></div><div id="comment-tools-30177" class="comment-tools"></div><div class="clear"></div><div id="comment-30177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30327"></span>

<div id="answer-container-30327" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30327-score" class="post-score" title="current number of votes">0</div><span id="post-30327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to figure out who is taking all the bandwidth, with wireshark?</p></blockquote><p>Sure.</p><p>Please <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">capture the whole wireless traffic</a>, then take a look at the statistics in Wireshark.</p><blockquote><p>Statistics -&gt; Conversations -&gt; IP Tab (or TCP Tab)</p></blockquote><p>Click on the <strong>bytes</strong> column. The system with the most transmitted frames is (most likely) the one you are looking for.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30327" class="comments-container"></div><div id="comment-tools-30327" class="comment-tools"></div><div class="clear"></div><div id="comment-30327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


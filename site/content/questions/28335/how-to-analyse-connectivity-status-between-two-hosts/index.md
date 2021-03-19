+++
type = "question"
title = "How to Analyse Connectivity status between Two Hosts."
description = '''Hi Forum, I want to analyse the connectivity between two hosts. Collected pcap trace for the same. Now need to check whether connection has been established or not. Can someone help how do i track this? Thank you, Br: Srinivas Vandanapu.'''
date = "2013-12-22T22:49:00Z"
lastmod = "2013-12-23T11:32:00Z"
weight = 28335
keywords = [ "connectivity" ]
aliases = [ "/questions/28335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Analyse Connectivity status between Two Hosts.](/questions/28335/how-to-analyse-connectivity-status-between-two-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28335-score" class="post-score" title="current number of votes">0</div><span id="post-28335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum, I want to analyse the connectivity between two hosts. Collected pcap trace for the same. Now need to check whether connection has been established or not.</p><p>Can someone help how do i track this?</p><p>Thank you, Br: Srinivas Vandanapu.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connectivity" rel="tag" title="see questions tagged &#39;connectivity&#39;">connectivity</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '13, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/5a71a2924b06b6e80dae4f1a541bc787?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vandanap&#39;s gravatar image" /><p><span>vandanap</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vandanap has no accepted answers">0%</span></p></div></div><div id="comments-container-28335" class="comments-container"></div><div id="comment-tools-28335" class="comment-tools"></div><div class="clear"></div><div id="comment-28335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28346"></span>

<div id="answer-container-28346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28346-score" class="post-score" title="current number of votes">1</div><span id="post-28346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now need to check whether connection has been established or not.</p></blockquote><p>well, just view the 'conversations' and if the two systems are talking to each other, you should see some traffic</p><blockquote><p>Statistics -&gt; Conversations -&gt; IPv4 [or TCP or UDP tab]</p></blockquote><p>Look for the two IP addresses in one line.</p><p>Another option: use a display filter</p><blockquote><p>ip.addr eq x.x.x.x and ip.addr eq y.y.y.y</p></blockquote><p>Where x.x.x.x and y.y.y.y are the IP addresses of the two hosts. If you see any frames, after you apply the filter, there is communication between the two.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28346" class="comments-container"></div><div id="comment-tools-28346" class="comment-tools"></div><div class="clear"></div><div id="comment-28346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


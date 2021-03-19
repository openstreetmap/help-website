+++
type = "question"
title = "all traffic except the list of mac address"
description = '''hello how i can write right caputre filter to pick all the traffic except the follow mac addresses?'''
date = "2017-10-24T02:11:00Z"
lastmod = "2017-10-24T04:51:00Z"
weight = 64141
keywords = [ "capture-filter", "mac-address" ]
aliases = [ "/questions/64141" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [all traffic except the list of mac address](/questions/64141/all-traffic-except-the-list-of-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64141-score" class="post-score" title="current number of votes">0</div><span id="post-64141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><p>how i can write right caputre filter to pick all the traffic except the follow mac addresses?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/cfbaa9b6a683a5635d9225852395b656?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scanman&#39;s gravatar image" /><p><span>scanman</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scanman has no accepted answers">0%</span></p></div></div><div id="comments-container-64141" class="comments-container"></div><div id="comment-tools-64141" class="comment-tools"></div><div class="clear"></div><div id="comment-64141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64149"></span>

<div id="answer-container-64149" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64149-score" class="post-score" title="current number of votes">1</div><span id="post-64149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scanman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture filter for a MAC address is in the form of <code>ether host xx:xx:xx:xx:xx:xx</code> where x is a hexadecimal digit.</p><p>To combine multiple addresses and then exclude them, firstly "or" them together and then negate the entire list, e.g.</p><pre><code>!(ether host 12:34:56:78:9A:BC or aa:bb:cc:dd:ee:ff or ff:ff:ff:ff:ff:ff)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64149" class="comments-container"></div><div id="comment-tools-64149" class="comment-tools"></div><div class="clear"></div><div id="comment-64149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64146"></span>

<div id="answer-container-64146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64146-score" class="post-score" title="current number of votes">0</div><span id="post-64146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on your exact requirements it would be something like this:</p><pre><code>not ether host 00:01:02:03:04:05 and not ether host 00:06:07:08:09:0A</code></pre><p>but you can check the <a href="https://wiki.wireshark.org/CaptureFilters">Wiki</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-64146" class="comments-container"><span id="64150"></span><div id="comment-64150" class="comment"><div id="post-64150-score" class="comment-score"></div><div class="comment-text"><p>thank you alot )</p></div><div id="comment-64150-info" class="comment-info"><span class="comment-age">(24 Oct '17, 04:51)</span> <span class="comment-user userinfo">scanman</span></div></div></div><div id="comment-tools-64146" class="comment-tools"></div><div class="clear"></div><div id="comment-64146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Linux access to interfaces"
description = '''As I understand it only one process can access a network interface at any given time. Does this mean running wireshark and a packet generator on the same interface will half productivity?'''
date = "2012-10-11T00:00:00Z"
lastmod = "2012-10-11T01:44:00Z"
weight = 14913
keywords = [ "linux" ]
aliases = [ "/questions/14913" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Linux access to interfaces](/questions/14913/linux-access-to-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14913-score" class="post-score" title="current number of votes">0</div><span id="post-14913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I understand it only one process can access a network interface at any given time. Does this mean running wireshark and a packet generator on the same interface will half productivity?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/60074dc48073fb4204f469af5ca2b439?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Urumiko&#39;s gravatar image" /><p><span>Urumiko</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Urumiko has no accepted answers">0%</span></p></div></div><div id="comments-container-14913" class="comments-container"></div><div id="comment-tools-14913" class="comment-tools"></div><div class="clear"></div><div id="comment-14913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14917"></span>

<div id="answer-container-14917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14917-score" class="post-score" title="current number of votes">0</div><span id="post-14917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>As I understand it only one process can access a network interface at any given time.</p></blockquote><p>I'm not aware of such a limitation, at least not for Linux. You can start as many instances of Wireshark and packet generators as you like and they will all have access to the same interface.</p><blockquote><p>Does this mean running wireshark and a packet generator on the same interface will half productivity?</p></blockquote><p>well, it depends on how you define "productivity". Wireshark is a passive packet sniffer, so it will not consume any bandwidth. It will however consume system resources (cpu, ram). And in that respect, it will reduce the overall "productivity" of the system.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '12, 03:42</strong> </span></p></div></div><div id="comments-container-14917" class="comments-container"></div><div id="comment-tools-14917" class="comment-tools"></div><div class="clear"></div><div id="comment-14917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


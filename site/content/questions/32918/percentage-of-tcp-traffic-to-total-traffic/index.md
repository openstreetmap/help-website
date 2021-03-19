+++
type = "question"
title = "Percentage of TCP traffic to Total Traffic"
description = '''Hey everyone, Im trying to figure out a way to get the percentage of TCP traffic to total traffic from a capture. Ive been trying to do it with tcpdump or tcpstat or wireshark but I`m at a loss with how to do it.'''
date = "2014-05-19T12:59:00Z"
lastmod = "2014-05-19T14:51:00Z"
weight = 32918
keywords = [ "tcpstat", "tcpdump", "tcp" ]
aliases = [ "/questions/32918" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Percentage of TCP traffic to Total Traffic](/questions/32918/percentage-of-tcp-traffic-to-total-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32918-score" class="post-score" title="current number of votes">0</div><span id="post-32918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey everyone, I<code>m trying to figure out a way to get the percentage of TCP traffic to total traffic from a capture. I</code>ve been trying to do it with tcpdump or tcpstat or wireshark but I`m at a loss with how to do it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpstat" rel="tag" title="see questions tagged &#39;tcpstat&#39;">tcpstat</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/4050703abce32485097940e68bbc0393?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heizenberg&#39;s gravatar image" /><p><span>Heizenberg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heizenberg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '14, 12:59</strong> </span></p></div></div><div id="comments-container-32918" class="comments-container"></div><div id="comment-tools-32918" class="comment-tools"></div><div class="clear"></div><div id="comment-32918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32919"></span>

<div id="answer-container-32919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32919-score" class="post-score" title="current number of votes">1</div><span id="post-32919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Load the capture file in Wireshark and apply "tcp" as a display filter. Look in the status bar, and Wireshark will show the number of displayed packets, and also the displayed packets as a percentage of the total number of packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-32919" class="comments-container"></div><div id="comment-tools-32919" class="comment-tools"></div><div class="clear"></div><div id="comment-32919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32921"></span>

<div id="answer-container-32921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32921-score" class="post-score" title="current number of votes">0</div><span id="post-32921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at this</p><blockquote><p>Statistics -&gt; Protocol Hierarchy</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32921" class="comments-container"></div><div id="comment-tools-32921" class="comment-tools"></div><div class="clear"></div><div id="comment-32921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


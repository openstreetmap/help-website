+++
type = "question"
title = "Radius load(*) graph with in wireshark"
description = '''Hi, I want to ask question related to radius. Is there any way to use the LOAD(*) graphs for RADIUS? Is there any mechanism to generate stats that say : A nos. of transactions were completed between 0-10ms B nos. of transactions were completed between 11-20ms C nos. of transactions were completed be...'''
date = "2011-02-24T08:16:00Z"
lastmod = "2011-02-25T00:50:00Z"
weight = 2553
keywords = [ "performance" ]
aliases = [ "/questions/2553" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Radius load(\*) graph with in wireshark](/questions/2553/radius-load-graph-with-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2553-score" class="post-score" title="current number of votes">0</div><span id="post-2553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to ask question related to radius.</p><p>Is there any way to use the LOAD(*) graphs for RADIUS?</p><p>Is there any mechanism to generate stats that say :</p><p>A nos. of transactions were completed between 0-10ms</p><p>B nos. of transactions were completed between 11-20ms</p><p>C nos. of transactions were completed between 21-30ms</p><p>D nos. of transactions were completed between 31-40ms</p><p>E nos. of transactions were completed after 40ms</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '11, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '11, 08:18</strong> </span></p></div></div><div id="comments-container-2553" class="comments-container"></div><div id="comment-tools-2553" class="comment-tools"></div><div class="clear"></div><div id="comment-2553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2556"></span>

<div id="answer-container-2556" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2556-score" class="post-score" title="current number of votes">1</div><span id="post-2556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vijay Gharge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, but you will have to use <code>COUNT(*)</code> and use the appropriate filters:</p><pre><code>radius.time&lt;=0.010
radius.time&gt;0.010 and radius.time&lt;=0.020
radius.time&gt;0.020 and radius.time&lt;=0.030
radius.time&gt;0.030 and radius.time&lt;=0.040
radius.time&gt;0.040</code></pre><p><img src="http://www.euronet.nl/~sake/files/radius-io-graph.png" alt="io-graph" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '11, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-2556" class="comments-container"><span id="2563"></span><div id="comment-2563" class="comment"><div id="post-2563-score" class="comment-score"></div><div class="comment-text"><p>Wow! Let me try this...This is simply awesome...</p></div><div id="comment-2563-info" class="comment-info"><span class="comment-age">(25 Feb '11, 00:50)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div></div><div id="comment-tools-2556" class="comment-tools"></div><div class="clear"></div><div id="comment-2556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


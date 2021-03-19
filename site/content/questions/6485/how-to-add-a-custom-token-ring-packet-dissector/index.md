+++
type = "question"
title = "How to add a custom token-ring packet dissector"
description = '''I want build a dissector, the packet first 32 bytes is: 0000: 55 55 00 26 db 00 11 00 00 00 07 00 22 00 00 00  0010: 08 51 00 00 26 02 00 45 00 01 ee 00 00 00 00 40  when i used follow code, it can work for ethernet packet, but not work for this packet. heur_dissector_add(&quot;eth&quot;, dissect_myprotocol, ...'''
date = "2011-09-22T00:21:00Z"
lastmod = "2011-09-22T06:13:00Z"
weight = 6485
keywords = [ "dissector", "token-ring" ]
aliases = [ "/questions/6485" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add a custom token-ring packet dissector](/questions/6485/how-to-add-a-custom-token-ring-packet-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6485-score" class="post-score" title="current number of votes">0</div><span id="post-6485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want build a dissector, the packet first 32 bytes is:</p><pre><code>0000: 55 55 00 26 db 00 11 00 00 00 07 00 22 00 00 00 
0010: 08 51 00 00 26 02 00 45 00 01 ee 00 00 00 00 40</code></pre>when i used follow code, it can work for ethernet packet, but not work for this packet.<p><code>heur_dissector_add("eth", dissect_myprotocol, proto_myprotocol);</code></p><p>I want used like this, but it wrong:</p><p><code>heur_dissector_add("tr", dissect_myprotocol, proto_myprotocol);</code></p><p>Some body can tell me which parent id should i use?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-token-ring" rel="tag" title="see questions tagged &#39;token-ring&#39;">token-ring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '11, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/cd5101a4558bd6a4d8a07727e61c0274?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhoushuming&#39;s gravatar image" /><p><span>zhoushuming</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhoushuming has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Sep '11, 06:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6485" class="comments-container"></div><div id="comment-tools-6485" class="comment-tools"></div><div class="clear"></div><div id="comment-6485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6489"></span>

<div id="answer-container-6489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6489-score" class="post-score" title="current number of votes">0</div><span id="post-6489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no heuristic subdissector table defined for <code>tr</code>, as opposed to <code>eth</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '11, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6489" class="comments-container"></div><div id="comment-tools-6489" class="comment-tools"></div><div class="clear"></div><div id="comment-6489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


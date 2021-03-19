+++
type = "question"
title = "Capture only TZSP"
description = '''I want to capture a remote stream from a router. Normally I just capture everything and later deal with it, but there will be a ton of data, so might as well capture the minimum than I can. What filter would I enter to capture only TZSP? Just entering tzsp in the filter field isn&#x27;t valid syntax.'''
date = "2013-12-12T06:45:00Z"
lastmod = "2013-12-13T08:16:00Z"
weight = 28053
keywords = [ "tzsp" ]
aliases = [ "/questions/28053" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture only TZSP](/questions/28053/capture-only-tzsp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28053-score" class="post-score" title="current number of votes">0</div><span id="post-28053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture a remote stream from a router. Normally I just capture everything and later deal with it, but there will be a ton of data, so might as well capture the minimum than I can.</p><p>What filter would I enter to capture only TZSP? Just entering tzsp in the filter field isn't valid syntax.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tzsp" rel="tag" title="see questions tagged &#39;tzsp&#39;">tzsp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/bb323a2d0e0857331597629c9386d207?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHammett&#39;s gravatar image" /><p><span>MHammett</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHammett has no accepted answers">0%</span></p></div></div><div id="comments-container-28053" class="comments-container"></div><div id="comment-tools-28053" class="comment-tools"></div><div class="clear"></div><div id="comment-28053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28079"></span>

<div id="answer-container-28079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28079-score" class="post-score" title="current number of votes">0</div><span id="post-28079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try:</p><pre><code>udp port 37008</code></pre><p>Ref (line 44): <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-tzsp.c?revision=53911&amp;view=markup">http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-tzsp.c?revision=53911&amp;view=markup</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-28079" class="comments-container"></div><div id="comment-tools-28079" class="comment-tools"></div><div class="clear"></div><div id="comment-28079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


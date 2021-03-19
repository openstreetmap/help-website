+++
type = "question"
title = "Unsupported Display Filter Reference for Modbus in latest Wireshark versions"
description = '''Looking at the Display Filter Reference for Modbus/TCP  I noticed that most of the fields are not supported in the newer Wireshark versions. I wonder why, and I&#x27;ll be more than happy to understand how can I still use these fields Many Thanks in advance, A.K.'''
date = "2015-07-25T05:35:00Z"
lastmod = "2015-07-25T08:00:00Z"
weight = 44467
keywords = [ "filter", "display", "reference" ]
aliases = [ "/questions/44467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unsupported Display Filter Reference for Modbus in latest Wireshark versions](/questions/44467/unsupported-display-filter-reference-for-modbus-in-latest-wireshark-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44467-score" class="post-score" title="current number of votes">0</div><span id="post-44467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking at the Display Filter Reference for Modbus/TCP I noticed that most of the fields are not supported in the newer Wireshark versions. I wonder why, and I'll be more than happy to understand how can I still use these fields</p><p>Many Thanks in advance,</p><p>A.K.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-reference" rel="tag" title="see questions tagged &#39;reference&#39;">reference</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '15, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/d37bb6cf106fdfe0050c1e02fc6fa7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ABK&#39;s gravatar image" /><p><span>ABK</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ABK has no accepted answers">0%</span></p></div></div><div id="comments-container-44467" class="comments-container"><span id="44468"></span><div id="comment-44468" class="comment"><div id="post-44468-score" class="comment-score"></div><div class="comment-text"><p>Which specific filters are no longer supported? (i.e., can you provide some of their filter names?)</p></div><div id="comment-44468-info" class="comment-info"><span class="comment-age">(25 Jul '15, 07:05)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-44467" class="comment-tools"></div><div class="clear"></div><div id="comment-44467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44469"></span>

<div id="answer-container-44469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44469-score" class="post-score" title="current number of votes">2</div><span id="post-44469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think they're gone - I think they just changed names and which protocol they're listed under.</p><p>I don't know anything about Modbus, but it looks like Wireshark added support for "Modbus RTU", as well as the previous "Modbus/TCP", so the display filter fields were split up: "<code>Modbus/TCP</code>" only lists the TCP-specific ones, "<code>Modbus RTU</code>" lists the RTU-specific ones, and a generic "<code>Modbus</code>" is where most of them are now, since they presumably apply to both TCP and RTU formats.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44469" class="comments-container"><span id="44470"></span><div id="comment-44470" class="comment"><div id="post-44470-score" class="comment-score"></div><div class="comment-text"><p>You are right thanks!! ABK</p></div><div id="comment-44470-info" class="comment-info"><span class="comment-age">(25 Jul '15, 07:32)</span> <span class="comment-user userinfo">ABK</span></div></div><span id="44471"></span><div id="comment-44471" class="comment"><div id="post-44471-score" class="comment-score"></div><div class="comment-text"><p>For reference, Modbus RTU is the binary protocol originally used over serial links that defines the basic data types and functions of Modbus, Modbus TCP is one of the variants of Modbus over IP that adds some header fields but doesn't alter the data types or functions used.</p></div><div id="comment-44471-info" class="comment-info"><span class="comment-age">(25 Jul '15, 08:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-44469" class="comment-tools"></div><div class="clear"></div><div id="comment-44469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


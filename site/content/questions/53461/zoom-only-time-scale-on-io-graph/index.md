+++
type = "question"
title = "Zoom only time scale on I/O Graph"
description = '''I&#x27;m running two versions of Wireshark on my machine. v1.8.14 (because it supports a no longer supported protocol) and v2.0.3 (portable version) I&#x27;m trying to do a timing analysis on packets over the network and finding the I/O Graph function handy. However, I find myself having to simultaneously run...'''
date = "2016-06-15T06:06:00Z"
lastmod = "2016-06-15T10:19:00Z"
weight = 53461
keywords = [ "zooming", "iograph" ]
aliases = [ "/questions/53461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Zoom only time scale on I/O Graph](/questions/53461/zoom-only-time-scale-on-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53461-score" class="post-score" title="current number of votes">0</div><span id="post-53461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running two versions of Wireshark on my machine.</p><p>v1.8.14 (because it supports a no longer supported protocol) and v2.0.3 (portable version)</p><p>I'm trying to do a timing analysis on packets over the network and finding the I/O Graph function handy. However, I find myself having to simultaneously run both versions of Wireshark to get what I need!</p><p>1.8.14 is good for looking at the details. The time scale is stretched and I have to do a lot of scrolling to see all of the data, but it gives me a really good, up close picture. Unfortunately, I can't "zoom out" to see the big picture. Also, it's limited to 100,000 sample points.</p><p>2.0.3 is the opposite. I get a great "high level" picture of the entire capture. It has a built-in zoom feature which seems nice - I can use my mouse wheel to zoom. The only problem is, it zooms the packets/s axis as well as the time! So when I zoom in to get the time scale right, now the packet scale is way off and I have to scroll a long way up to see the points I want!</p><p>Is there a way in 2.0.3 to just zoom the time axis and leave the Packets/s axis alone? Or, less preferably, a way to "zoom out" in 1.8.14?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zooming" rel="tag" title="see questions tagged &#39;zooming&#39;">zooming</span> <span class="post-tag tag-link-iograph" rel="tag" title="see questions tagged &#39;iograph&#39;">iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '16, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/7aa31b10303327434572773aabbc9b2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trashman&#39;s gravatar image" /><p><span>Trashman</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trashman has no accepted answers">0%</span></p></div></div><div id="comments-container-53461" class="comments-container"><span id="53467"></span><div id="comment-53467" class="comment"><div id="post-53467-score" class="comment-score"></div><div class="comment-text"><p>Which protocol is no longer supported in 2.0?</p></div><div id="comment-53467-info" class="comment-info"><span class="comment-age">(15 Jun '16, 08:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53471"></span><div id="comment-53471" class="comment"><div id="post-53471-score" class="comment-score"></div><div class="comment-text"><p>MODBUS over UDP was dropped in 1.10 and later because it is a nonstandard protocol.</p></div><div id="comment-53471-info" class="comment-info"><span class="comment-age">(15 Jun '16, 10:19)</span> <span class="comment-user userinfo">Trashman</span></div></div></div><div id="comment-tools-53461" class="comment-tools"></div><div class="clear"></div><div id="comment-53461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53463"></span>

<div id="answer-container-53463" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53463-score" class="post-score" title="current number of votes">1</div><span id="post-53463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With 2.1.0 (development snapshot of upcoming 2.2) at least I'm capable of selecting a certain piece of the graph and have that zoomed in. That gives me free choice of X and Y axis. Lacking a mouse wheel I can't test further, but do modifier keys (Shift, Ctrl, Alt) have any influence on the axis selected for zoom?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53463" class="comments-container"><span id="53470"></span><div id="comment-53470" class="comment"><div id="post-53470-score" class="comment-score"></div><div class="comment-text"><p>Modifier keys do not make a difference. But, I figured it out. At the bottom, I have to change Mouse: drags to Mouse:zooms, then I can highlight what I need and zoom in to exactly what I want as you described.</p></div><div id="comment-53470-info" class="comment-info"><span class="comment-age">(15 Jun '16, 10:01)</span> <span class="comment-user userinfo">Trashman</span></div></div></div><div id="comment-tools-53463" class="comment-tools"></div><div class="clear"></div><div id="comment-53463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Unaltering filter after following a stream"
description = '''When you try to follow tcp/udp stream on a packet, it pops up a new window with the stream content but it also changes the display filter on the main window (tc.stream eq 100 for instance). Is there a way to make wireshark not change the filter?'''
date = "2012-09-07T00:02:00Z"
lastmod = "2012-09-07T00:15:00Z"
weight = 14104
keywords = [ "filter", "stream" ]
aliases = [ "/questions/14104" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unaltering filter after following a stream](/questions/14104/unaltering-filter-after-following-a-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14104-score" class="post-score" title="current number of votes">0</div><span id="post-14104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When you try to follow tcp/udp stream on a packet, it pops up a new window with the stream content but it also changes the display filter on the main window (tc.stream eq 100 for instance). Is there a way to make wireshark not change the filter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/d0c9495c2b4db2649eec2b9ca8d956c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="l46kok&#39;s gravatar image" /><p><span>l46kok</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="l46kok has no accepted answers">0%</span></p></div></div><div id="comments-container-14104" class="comments-container"></div><div id="comment-tools-14104" class="comment-tools"></div><div class="clear"></div><div id="comment-14104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14105"></span>

<div id="answer-container-14105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14105-score" class="post-score" title="current number of votes">0</div><span id="post-14105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately not. The way "follow..." works is dependent on the fact that the capture file is filtered so that only frames from the same conversation are displayed.</p><p>To change this behavior, the Wireshark source code must be altered...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14105" class="comments-container"></div><div id="comment-tools-14105" class="comment-tools"></div><div class="clear"></div><div id="comment-14105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


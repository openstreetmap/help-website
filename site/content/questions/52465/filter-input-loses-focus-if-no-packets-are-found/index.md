+++
type = "question"
title = "Filter input loses focus if no packets are found"
description = '''Hi! Tested versions:  - 2.0.3 Win64  - Wireshark-win64-2.1.0-3015-g21090ca.exe (2.1.0-3015-g21090ca (v2.1.0rc0-3015-g21090ca from master)) If I capture on LAN with no capture filter and then select a filter in the filter input and no packets are found, the filter input always loses focus after appro...'''
date = "2016-05-12T05:28:00Z"
lastmod = "2016-05-13T01:02:00Z"
weight = 52465
keywords = [ "display-filter" ]
aliases = [ "/questions/52465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter input loses focus if no packets are found](/questions/52465/filter-input-loses-focus-if-no-packets-are-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52465-score" class="post-score" title="current number of votes">0</div><span id="post-52465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>Tested versions: - 2.0.3 Win64 - Wireshark-win64-2.1.0-3015-g21090ca.exe (2.1.0-3015-g21090ca (v2.1.0rc0-3015-g21090ca from master))</p><p>If I capture on LAN with no capture filter and then select a filter in the filter input and no packets are found, the filter input always loses focus after approximately 200 ms if I focus it with a mouse click. Do I do something wrong or is this a bug?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/d24094a18322db85a4a9e6efbc737445?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="njm&#39;s gravatar image" /><p><span>njm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="njm has no accepted answers">0%</span></p></div></div><div id="comments-container-52465" class="comments-container"><span id="52468"></span><div id="comment-52468" class="comment"><div id="post-52468-score" class="comment-score"></div><div class="comment-text"><p>I assume the capture is still going? It sounds as though the packet list/last packet (which is not visible) is getting the focus, which is not okay IMHO.</p><p>What happens if you do stop the capture?</p></div><div id="comment-52468-info" class="comment-info"><span class="comment-age">(12 May '16, 06:38)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52470"></span><div id="comment-52470" class="comment"><div id="post-52470-score" class="comment-score"></div><div class="comment-text"><p><span>@Jaap</span>: Yes, the capture is still going. If I stop the capture and then click into the filter input, the focus stays there.</p></div><div id="comment-52470-info" class="comment-info"><span class="comment-age">(12 May '16, 06:42)</span> <span class="comment-user userinfo">njm</span></div></div></div><div id="comment-tools-52465" class="comment-tools"></div><div class="clear"></div><div id="comment-52465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52484"></span>

<div id="answer-container-52484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52484-score" class="post-score" title="current number of votes">0</div><span id="post-52484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This seems like a bug in the Qt interface. If not already there (haven't checked), you could <a href="https://bugs.wireshark.org/bugzilla/">file a bugreport</a> describing this scenario.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '16, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52484" class="comments-container"><span id="52494"></span><div id="comment-52494" class="comment"><div id="post-52494-score" class="comment-score"></div><div class="comment-text"><p>Found the bug in bugzilla <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12219.">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12219.</a> Sry, I thought checking here would also show tickets.</p></div><div id="comment-52494-info" class="comment-info"><span class="comment-age">(13 May '16, 01:02)</span> <span class="comment-user userinfo">njm</span></div></div></div><div id="comment-tools-52484" class="comment-tools"></div><div class="clear"></div><div id="comment-52484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


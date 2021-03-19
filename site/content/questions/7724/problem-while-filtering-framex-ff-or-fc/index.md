+++
type = "question"
title = "Problem while filtering frame[x] == ff (or fc)"
description = '''I can&#x27;t filter displayed frames where specific byte is equal ff or fc (eq. frame[4] == ff), the filter sequence is not allowed, filter window turns red. Any solution, please?'''
date = "2011-12-01T02:12:00Z"
lastmod = "2016-09-01T08:11:00Z"
weight = 7724
keywords = [ "filter", "frame", "display" ]
aliases = [ "/questions/7724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem while filtering frame\[x\] == ff (or fc)](/questions/7724/problem-while-filtering-framex-ff-or-fc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7724-score" class="post-score" title="current number of votes">0</div><span id="post-7724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't filter displayed frames where specific byte is equal ff or fc (eq. frame[4] == ff), the filter sequence is not allowed, filter window turns red. Any solution, please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '11, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/f2e70b4959be9f6b55fb6eb12e249dd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jenda%20Nespor&#39;s gravatar image" /><p><span>Jenda Nespor</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jenda Nespor has no accepted answers">0%</span></p></div></div><div id="comments-container-7724" class="comments-container"></div><div id="comment-tools-7724" class="comment-tools"></div><div class="clear"></div><div id="comment-7724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7725"></span>

<div id="answer-container-7725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7725-score" class="post-score" title="current number of votes">2</div><span id="post-7725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is because both <code>fc</code> and <code>ff</code> are filters on their own, for "Fibre Channel" and "FOUNDATION Fieldbus", respectively. You should be able to work around it using <code>frame[4] == ff:</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '11, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Sep '16, 06:48</strong> </span></p></div></div><div id="comments-container-7725" class="comments-container"><span id="7726"></span><div id="comment-7726" class="comment"><div id="post-7726-score" class="comment-score"></div><div class="comment-text"><p>Good to know. Still I think this behavior is a little strange to work with; isn't it possible to look at fc and ff as values instead of as filter names?</p></div><div id="comment-7726-info" class="comment-info"><span class="comment-age">(01 Dec '11, 07:56)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="7729"></span><div id="comment-7729" class="comment"><div id="post-7729-score" class="comment-score"></div><div class="comment-text"><p>Well, it's only a problem for single bytes. If you were searching for 2 (or more) bytes, then <code>frame[4:2]==ff:fc</code> would work just fine without the trailing colon.</p><p>But I do agree with you, and I think there is very likely a bug here since the display filter parsing doesn't support display filters on the right-hand side of a comparison operator anyway, at least as far as I'm aware, so it shouldn't be trying to match a filter here. You might want to file a bug report about this.</p></div><div id="comment-7729-info" class="comment-info"><span class="comment-age">(01 Dec '11, 09:03)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="55269"></span><div id="comment-55269" class="comment"><div id="post-55269-score" class="comment-score"></div><div class="comment-text"><p>It's a bit more complex. You talk about a "filter" above but I guess what you exactly had in mind was a filter primitive, like <code>tcp</code> or <code>ip.addr == 1.1.1.1</code>. As any field name may be used alone as a filter primitive (which makes true if that field is present in the frame, regardless what is its value and whether it has a value at all), the preference between interpretation of <code>[a-f][0-9a-f]</code> strings as hexadecimal values or filter primitives would at least have to take into account whether the field bearing the name has a value or not. A display filter <code>wlan.ta == wlan.sa</code> does work and <a href="https://ask.wireshark.org/questions/49145/ap-forward-labeled-as-retransmission/49147">is useful in some cases</a>, so blindly giving priority to the hexadecimal constant over field name interpretation at the right side of comparison operators could cause other issues. But doing it this way would just make the issue better hidden - if I assign to a protocol field which has a value a name like "ab", omitting the protocol name (like some dissectors do), I'll bump into the same wall again.</p></div><div id="comment-55269-info" class="comment-info"><span class="comment-age">(01 Sep '16, 07:19)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55271"></span><div id="comment-55271" class="comment"><div id="post-55271-score" class="comment-score"></div><div class="comment-text"><p><em>You might want to file a bug report about this.</em></p><p>FYI: <a href="https://ask.wireshark.org/users/8/stig">Stig</a> has recently filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12810">bug 12810</a> for this.</p></div><div id="comment-55271-info" class="comment-info"><span class="comment-age">(01 Sep '16, 08:11)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-7725" class="comment-tools"></div><div class="clear"></div><div id="comment-7725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


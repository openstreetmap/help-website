+++
type = "question"
title = "How to filter out all packets to/from a specific process?"
description = '''Hi all, May I know how to filter out all packets to/from a specific process through display filter? thanks!'''
date = "2012-10-15T01:49:00Z"
lastmod = "2012-12-28T04:05:00Z"
weight = 15006
keywords = [ "display-filter" ]
aliases = [ "/questions/15006" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter out all packets to/from a specific process?](/questions/15006/how-to-filter-out-all-packets-tofrom-a-specific-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15006-score" class="post-score" title="current number of votes">0</div><span id="post-15006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>May I know how to filter out all packets to/from a specific process through display filter?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '12, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-15006" class="comments-container"></div><div id="comment-tools-15006" class="comment-tools"></div><div class="clear"></div><div id="comment-15006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15007"></span>

<div id="answer-container-15007" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15007-score" class="post-score" title="current number of votes">0</div><span id="post-15007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not possible with current Wireshark as it has no knowledge of processes. If you know which port(s) a process is using then you can construct a filter with those ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '12, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15007" class="comments-container"><span id="15008"></span><div id="comment-15008" class="comment"><div id="post-15008-score" class="comment-score"></div><div class="comment-text"><p>thank you for quick response. As I saw this feature in Microsoft Network Monitor 3.4 so would like to know the same for wireshark.</p></div><div id="comment-15008-info" class="comment-info"><span class="comment-age">(15 Oct '12, 02:11)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="15009"></span><div id="comment-15009" class="comment"><div id="post-15009-score" class="comment-score"></div><div class="comment-text"><p>You can capture with NM, and then load the capture file in Wireshark.</p><p>There is a feature request for identifying processes(<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">1184</a>), but as it's 6 years old I don't think it'll be happening soon.</p></div><div id="comment-15009-info" class="comment-info"><span class="comment-age">(15 Oct '12, 02:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-15007" class="comment-tools"></div><div class="clear"></div><div id="comment-15007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17305"></span>

<div id="answer-container-17305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17305-score" class="post-score" title="current number of votes">0</div><span id="post-17305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On windows there is an experimental build that implements the idea in bug 1184, as described on the mailing list: <a href="http://www.wireshark.org/lists/wireshark-dev/201212/msg00069.html">http://www.wireshark.org/lists/wireshark-dev/201212/msg00069.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '12, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/559d96d22fbbf916f435cb4eb0d63dd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patraulea&#39;s gravatar image" /><p><span>patraulea</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patraulea has no accepted answers">0%</span></p></div></div><div id="comments-container-17305" class="comments-container"></div><div id="comment-tools-17305" class="comment-tools"></div><div class="clear"></div><div id="comment-17305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


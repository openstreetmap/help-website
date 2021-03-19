+++
type = "question"
title = "Resolving server from DNS?"
description = '''Using Wireshark, how would I able to resolve server from DNS?'''
date = "2015-09-20T04:56:00Z"
lastmod = "2015-09-20T13:19:00Z"
weight = 45968
keywords = [ "dns", "trace", "wireshark" ]
aliases = [ "/questions/45968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Resolving server from DNS?](/questions/45968/resolving-server-from-dns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45968-score" class="post-score" title="current number of votes">0</div><span id="post-45968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark, how would I able to resolve server from DNS?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '15, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/53a2fefbbff54041eee79bd3865dbf10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="airr&#39;s gravatar image" /><p><span>airr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="airr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '15, 00:12</strong> </span></p></div></div><div id="comments-container-45968" class="comments-container"></div><div id="comment-tools-45968" class="comment-tools"></div><div class="clear"></div><div id="comment-45968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45969"></span>

<div id="answer-container-45969" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45969-score" class="post-score" title="current number of votes">2</div><span id="post-45969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="airr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Start a capture on the correct interface using the capture filter "port 53", and then force your computer to lookup up a name, e.g. from a command line use (Windows) <code>nslookup name.to.lookup</code> or (Linux) <code>dig name.to.lookup</code>.</p><p>Your computer might have cached the name so to force a lookup, try a name you haven't visited for a while.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '15, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45969" class="comments-container"><span id="45978"></span><div id="comment-45978" class="comment"><div id="post-45978-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-45978-info" class="comment-info"><span class="comment-age">(20 Sep '15, 13:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-45969" class="comment-tools"></div><div class="clear"></div><div id="comment-45969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "filter for comparing values of two different fields of GTP protocol"
description = '''Hi, Just wanted to know that whether there is a way to build a filter, where values of two fields can be compared. For example: if we want to filter gtp-c packets where gtp.teid_data is equal to gtp.teid_cp Thanks in advance. Ravi'''
date = "2012-11-26T07:43:00Z"
lastmod = "2012-11-26T12:28:00Z"
weight = 16321
keywords = [ "display-filter" ]
aliases = [ "/questions/16321" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [filter for comparing values of two different fields of GTP protocol](/questions/16321/filter-for-comparing-values-of-two-different-fields-of-gtp-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16321-score" class="post-score" title="current number of votes">0</div><span id="post-16321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Just wanted to know that whether there is a way to build a filter, where values of two fields can be compared. For example: if we want to filter gtp-c packets where gtp.teid_data is equal to gtp.teid_cp</p><p>Thanks in advance.</p><p>Ravi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '12, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/3ac62e4a103b118d6c93f65777d77402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAVI_TANDON&#39;s gravatar image" /><p><span>RAVI_TANDON</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAVI_TANDON has no accepted answers">0%</span></p></div></div><div id="comments-container-16321" class="comments-container"></div><div id="comment-tools-16321" class="comment-tools"></div><div class="clear"></div><div id="comment-16321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16336"></span>

<div id="answer-container-16336" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16336-score" class="post-score" title="current number of votes">1</div><span id="post-16336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually you can do this in the current development builds (1.9.0) of Wireshark thanks to <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=43069">r43069</a>. The link has some basic examples.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16336" class="comments-container"><span id="16338"></span><div id="comment-16338" class="comment"><div id="post-16338-score" class="comment-score"></div><div class="comment-text"><p>ok...thanks a lot, will try to use 1.9.0 release</p></div><div id="comment-16338-info" class="comment-info"><span class="comment-age">(26 Nov '12, 12:28)</span> <span class="comment-user userinfo">RAVI_TANDON</span></div></div></div><div id="comment-tools-16336" class="comment-tools"></div><div class="clear"></div><div id="comment-16336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16322"></span>

<div id="answer-container-16322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16322-score" class="post-score" title="current number of votes">0</div><span id="post-16322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that with normal Wireshark filters. They can only match values in a single frame. The one exception to that are things like tcp.expert filters, because they filter on expert symptons that can be caused by interaction between two frames.</p><p>But you might want to use the mate engine to do what you want: <a href="http://wiki.wireshark.org/Mate">http://wiki.wireshark.org/Mate</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16322" class="comments-container"><span id="16323"></span><div id="comment-16323" class="comment"><div id="post-16323-score" class="comment-score"></div><div class="comment-text"><p>Actually, both fields are present in the single frame/packet of gtp-c packets</p></div><div id="comment-16323-info" class="comment-info"><span class="comment-age">(26 Nov '12, 07:55)</span> <span class="comment-user userinfo">RAVI_TANDON</span></div></div><span id="16324"></span><div id="comment-16324" class="comment"><div id="post-16324-score" class="comment-score"></div><div class="comment-text"><p>Okay, I still think it can't be done with the normal filter engine. As far as I know you can only to compare field values to static values, not other field values - at least I can't think of any case where this is possible.</p></div><div id="comment-16324-info" class="comment-info"><span class="comment-age">(26 Nov '12, 08:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-16322" class="comment-tools"></div><div class="clear"></div><div id="comment-16322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


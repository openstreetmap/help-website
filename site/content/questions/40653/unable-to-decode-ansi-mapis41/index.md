+++
type = "question"
title = "Unable to decode ANSI MAP(IS41)"
description = '''trying to capture ANSI MAP i.e IS41 trace on wireshark but its showing till SCCP and that too malformed Please suggest'''
date = "2015-03-18T04:33:00Z"
lastmod = "2015-05-07T07:19:00Z"
weight = 40653
keywords = [ "ansi_map" ]
aliases = [ "/questions/40653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decode ANSI MAP(IS41)](/questions/40653/unable-to-decode-ansi-mapis41)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40653-score" class="post-score" title="current number of votes">0</div><span id="post-40653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>trying to capture ANSI MAP i.e IS41 trace on wireshark but its showing till SCCP and that too malformed Please suggest</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ansi_map" rel="tag" title="see questions tagged &#39;ansi_map&#39;">ansi_map</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '15, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/6b7e62c42828cfd385f7bf6f809393e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rkadvantal&#39;s gravatar image" /><p><span>rkadvantal</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rkadvantal has no accepted answers">0%</span></p></div></div><div id="comments-container-40653" class="comments-container"><span id="42184"></span><div id="comment-42184" class="comment"><div id="post-42184-score" class="comment-score"></div><div class="comment-text"><p>What Dianalab9 said, as well as make sure in the ANSI_MAP protocol preferences you have the correct SSN(s) listed. Wireshark gets to SCCP but for some reason, it is not obvious to it how to decode the layer above SCCP (which is ANSI TCAP in your case)</p></div><div id="comment-42184-info" class="comment-info"><span class="comment-age">(07 May '15, 07:19)</span> <span class="comment-user userinfo">tiger762</span></div></div></div><div id="comment-tools-40653" class="comment-tools"></div><div class="clear"></div><div id="comment-40653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40654"></span>

<div id="answer-container-40654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40654-score" class="post-score" title="current number of votes">0</div><span id="post-40654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you need to choose ANSI under mtp3 in preferences--&gt;protocols</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-40654" class="comments-container"></div><div id="comment-tools-40654" class="comment-tools"></div><div class="clear"></div><div id="comment-40654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


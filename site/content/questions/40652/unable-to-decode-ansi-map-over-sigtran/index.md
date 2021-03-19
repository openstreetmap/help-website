+++
type = "question"
title = "Unable To decode ANSI MAP over SIGTRAN"
description = '''Hi I am trying to send SMS DPTP request for ANSI MAP over SIGTRAN but wireshark showing it till SCCP and that too malformed Please suggest.'''
date = "2015-03-18T04:30:00Z"
lastmod = "2015-05-07T07:17:00Z"
weight = 40652
keywords = [ "sccp" ]
aliases = [ "/questions/40652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable To decode ANSI MAP over SIGTRAN](/questions/40652/unable-to-decode-ansi-map-over-sigtran)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40652-score" class="post-score" title="current number of votes">0</div><span id="post-40652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am trying to send SMS DPTP request for ANSI MAP over SIGTRAN but wireshark showing it till SCCP and that too malformed Please suggest.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '15, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/6b7e62c42828cfd385f7bf6f809393e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rkadvantal&#39;s gravatar image" /><p><span>rkadvantal</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rkadvantal has no accepted answers">0%</span></p></div></div><div id="comments-container-40652" class="comments-container"></div><div id="comment-tools-40652" class="comment-tools"></div><div class="clear"></div><div id="comment-40652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40655"></span>

<div id="answer-container-40655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40655-score" class="post-score" title="current number of votes">0</div><span id="post-40655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Edit-&gt;Preferences-&gt;mtp3 and set it as ANSI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-40655" class="comments-container"><span id="40708"></span><div id="comment-40708" class="comment"><div id="post-40708-score" class="comment-score"></div><div class="comment-text"><p>I tried that but its still same Is it Feasible for you to have a look if i can send you the capture?</p></div><div id="comment-40708-info" class="comment-info"><span class="comment-age">(19 Mar '15, 21:42)</span> <span class="comment-user userinfo">rkadvantal</span></div></div><span id="40714"></span><div id="comment-40714" class="comment"><div id="post-40714-score" class="comment-score"></div><div class="comment-text"><p>sure, no problem</p></div><div id="comment-40714-info" class="comment-info"><span class="comment-age">(20 Mar '15, 01:16)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="42183"></span><div id="comment-42183" class="comment"><div id="post-42183-score" class="comment-score"></div><div class="comment-text"><p>You might need to tell Wireshark what SCCP SubSystem Numbers correspond to ANSI MAP. You might have a non-standard SSN.</p></div><div id="comment-42183-info" class="comment-info"><span class="comment-age">(07 May '15, 07:17)</span> <span class="comment-user userinfo">tiger762</span></div></div></div><div id="comment-tools-40655" class="comment-tools"></div><div class="clear"></div><div id="comment-40655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


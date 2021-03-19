+++
type = "question"
title = "How to know which is the next layer on SCCP -  RANAP or BSSAP (not according SSN)"
description = '''Hi.  When I have only one frame of SCCP - according what can I know which is the next protocol RANAP or BSSAP.  I don&#x27;t want to rely on the SSN because not always I have the CR message. Thanks, Zeev'''
date = "2012-11-07T00:14:00Z"
lastmod = "2013-03-08T14:31:00Z"
weight = 15611
keywords = [ "sccp" ]
aliases = [ "/questions/15611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to know which is the next layer on SCCP - RANAP or BSSAP (not according SSN)](/questions/15611/how-to-know-which-is-the-next-layer-on-sccp-ranap-or-bssap-not-according-ssn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15611-score" class="post-score" title="current number of votes">0</div><span id="post-15611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. When I have only one frame of SCCP - according what can I know which is the next protocol RANAP or BSSAP. I don't want to rely on the SSN because not always I have the CR message. Thanks, Zeev</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 00:14</strong></p><img src="https://secure.gravatar.com/avatar/77c55765ba533d357e966caa97e1ec29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zeev&#39;s gravatar image" /><p><span>zeev</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zeev has no accepted answers">0%</span></p></div></div><div id="comments-container-15611" class="comments-container"></div><div id="comment-tools-15611" class="comment-tools"></div><div class="clear"></div><div id="comment-15611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15666"></span>

<div id="answer-container-15666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15666-score" class="post-score" title="current number of votes">0</div><span id="post-15666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, unless the code has something to "route" on (such as SSN) the code would have to do some kind of heuristic: for example trying to decode as RANAP and if that fails try BSSAP. (This isn't something Wireshark will do currently.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '12, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-15666" class="comments-container"><span id="19299"></span><div id="comment-19299" class="comment"><div id="post-19299-score" class="comment-score"></div><div class="comment-text"><p>How do i know that it failed..? I mean, what if I decoded the hole RANAP bytes as BSSAP without finfing any errors..? Thanks</p></div><div id="comment-19299-info" class="comment-info"><span class="comment-age">(08 Mar '13, 03:19)</span> <span class="comment-user userinfo">Radhwen Khelia</span></div></div><span id="19316"></span><div id="comment-19316" class="comment"><div id="post-19316-score" class="comment-score"></div><div class="comment-text"><p>In fact I answered this from the perspective of how <em>Wireshark</em> would know. Anyway, if both decodes succeed, you're right, you (and Wireshark) can't really know.</p><p>Keep in mind that "succeed" does not necessarily mean "no errors." You might also have to check the values: some decoded values might be technically legal but make no sense.</p></div><div id="comment-19316-info" class="comment-info"><span class="comment-age">(08 Mar '13, 14:31)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-15666" class="comment-tools"></div><div class="clear"></div><div id="comment-15666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


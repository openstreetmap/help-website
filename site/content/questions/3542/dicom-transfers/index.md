+++
type = "question"
title = "Dicom transfers"
description = '''A lot of dicom transfers happen on tcp ports other than port 104. Is there a way to change this port within the dicom expression filter, or copy the filter and change the port that the expression looks at.'''
date = "2011-04-17T20:55:00Z"
lastmod = "2011-04-17T22:14:00Z"
weight = 3542
keywords = [ "dicom" ]
aliases = [ "/questions/3542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dicom transfers](/questions/3542/dicom-transfers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3542-score" class="post-score" title="current number of votes">1</div><span id="post-3542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A lot of dicom transfers happen on tcp ports other than port 104. Is there a way to change this port within the dicom expression filter, or copy the filter and change the port that the expression looks at.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dicom" rel="tag" title="see questions tagged &#39;dicom&#39;">dicom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '11, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/71385ae66f4253c5874d504ee879886b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vern&#39;s gravatar image" /><p><span>Vern</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vern has no accepted answers">0%</span></p></div></div><div id="comments-container-3542" class="comments-container"></div><div id="comment-tools-3542" class="comment-tools"></div><div class="clear"></div><div id="comment-3542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3545"></span>

<div id="answer-container-3545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3545-score" class="post-score" title="current number of votes">2</div><span id="post-3545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The filter is irrelevant to the port for DICOM. A filter does a lot less than some people appear to think it does - it just lets you test whether, in a particular packet, a given field is present, or lets you test the value of the field. It does not let you change the way a packet is dissected, or change what particular ports are dissected as.</p><p>To change the port or ports that are dissected as DICOM, change the DICOM "DICOM Ports" preference or the DICOM "Search on any TCP port" preference. To change the preferences for DICOM, select "Preferences" from the "Edit" menu, open up the "Protocols" list, and select "DICOM" from the list of protocols. The "DICOM Ports" preference can be set to a single port number, a port range (two port numbers with a hyphen between them, specifying all port numbers starting with the first and ending with the second, or a comma-separated list of port numbers or port ranges. If you turn on the "Search on any TCP port" preference, Wireshark will attempt to recognize DICOM packets on any TCP port; it may fail to recognize them, or it may mistakenly think some non-DICOM packet are DICOM packets (computers aren't necessarily very smart at doing that kind of packet recognition).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '11, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3545" class="comments-container"></div><div id="comment-tools-3545" class="comment-tools"></div><div class="clear"></div><div id="comment-3545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


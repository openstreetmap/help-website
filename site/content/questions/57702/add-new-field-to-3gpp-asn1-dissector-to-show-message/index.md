+++
type = "question"
title = "Add new field to 3GPP ASN1 dissector to show message"
description = '''Hi Some dissectors for 3GPP ASN1 protocols, such as S1AP, will show the name of the decoded message in a dedicated field (s1ap.procedureCode: id-UEContextReleaseRequest (18), and others will not such as LTE RRC. I was wondering if you find it useful to add a field &quot;message&quot; to each 3GPP ASN1 protoco...'''
date = "2016-11-29T05:25:00Z"
lastmod = "2016-11-30T02:44:00Z"
weight = 57702
keywords = [ "dissector", "asn1" ]
aliases = [ "/questions/57702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add new field to 3GPP ASN1 dissector to show message](/questions/57702/add-new-field-to-3gpp-asn1-dissector-to-show-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57702-score" class="post-score" title="current number of votes">0</div><span id="post-57702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Some dissectors for 3GPP ASN1 protocols, such as S1AP, will show the name of the decoded message in a dedicated field (s1ap.procedureCode: id-UEContextReleaseRequest (18), and others will not such as LTE RRC.</p><p>I was wondering if you find it useful to add a field "message" to each 3GPP ASN1 protocol to show the text decoded message name: - s1ap.message = "UEContextReleaseRequest" - lte-rrc.message = "rrcConnectionReconfigurationComplete"</p><p>Even if this additional field is not part of ASN1 grammar of the protocol, it is useful information and simplifies analysis of decode results.</p><p>Thanks for sharing your thought.</p><p>Cyril Deubel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '16, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/7886738a3edf22de214c2e2a1b67f1fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CyrilDeubel&#39;s gravatar image" /><p><span>CyrilDeubel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CyrilDeubel has no accepted answers">0%</span></p></div></div><div id="comments-container-57702" class="comments-container"></div><div id="comment-tools-57702" class="comment-tools"></div><div class="clear"></div><div id="comment-57702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57715"></span>

<div id="answer-container-57715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57715-score" class="post-score" title="current number of votes">0</div><span id="post-57715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should file this as an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '16, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57715" class="comments-container"><span id="57723"></span><div id="comment-57723" class="comment"><div id="post-57723-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy</p><p>Thanks for the suggestion. I'll do that, and even try to propos an implementation for one of the protocols</p></div><div id="comment-57723-info" class="comment-info"><span class="comment-age">(30 Nov '16, 01:49)</span> <span class="comment-user userinfo">CyrilDeubel</span></div></div><span id="57724"></span><div id="comment-57724" class="comment"><div id="post-57724-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-57724-info" class="comment-info"><span class="comment-age">(30 Nov '16, 02:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57715" class="comment-tools"></div><div class="clear"></div><div id="comment-57715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


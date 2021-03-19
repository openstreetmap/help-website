+++
type = "question"
title = "dissection of a protocol"
description = '''Good morning everyone, i want to dissect a protocol encapsulated in UDP. so i don&#x27;t know if i should create a plugin or add a new dissector in wireshark. because i have already create a plugin for this protcole , but when this one is not encapsulated under UDP.  can anyone tell me if i should create...'''
date = "2013-08-07T02:16:00Z"
lastmod = "2013-08-09T07:45:00Z"
weight = 23605
keywords = [ "plugin" ]
aliases = [ "/questions/23605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dissection of a protocol](/questions/23605/dissection-of-a-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23605-score" class="post-score" title="current number of votes">0</div><span id="post-23605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning everyone,</p><p>i want to dissect a protocol encapsulated in UDP.</p><p>so i don't know if i should create a plugin or add a new dissector in wireshark.</p><p>because i have already create a plugin for this protcole , but when this one is not encapsulated under UDP.</p><p>can anyone tell me if i should create a new plugin or a new dissctor , or just modify my plugin</p><p>thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/9fbe9f669a6d14e31178d8193125c39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruz&#39;s gravatar image" /><p><span>cruz</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruz has no accepted answers">0%</span></p></div></div><div id="comments-container-23605" class="comments-container"></div><div id="comment-tools-23605" class="comment-tools"></div><div class="clear"></div><div id="comment-23605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23607"></span>

<div id="answer-container-23607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23607-score" class="post-score" title="current number of votes">2</div><span id="post-23607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your plugin can register with the udp dissector for a particular port using <code>dissector_add_uint("udp.port", A_PORT_NUMBER, your_dissector_handle)</code> or can register as a heuristic dissector using <code>heur_dissector_add("udp", your_dissector_udp_function, your_dissector_ protoregistration_value)</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '13, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23607" class="comments-container"><span id="23610"></span><div id="comment-23610" class="comment"><div id="post-23610-score" class="comment-score"></div><div class="comment-text"><p>Just to clarify (I think) what Graham is saying: it probably makes more sense to just modify your existing plugin/dissector rather than building a new one.</p></div><div id="comment-23610-info" class="comment-info"><span class="comment-age">(07 Aug '13, 06:54)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="23679"></span><div id="comment-23679" class="comment"><div id="post-23679-score" class="comment-score"></div><div class="comment-text"><p>Thank's for your answer;</p></div><div id="comment-23679-info" class="comment-info"><span class="comment-age">(09 Aug '13, 07:42)</span> <span class="comment-user userinfo">cruz</span></div></div><span id="23680"></span><div id="comment-23680" class="comment"><div id="post-23680-score" class="comment-score"></div><div class="comment-text"><p>If the answer answers your question, please be sure to "accept" it by clicking the check box. See the FAQ for more details.</p></div><div id="comment-23680-info" class="comment-info"><span class="comment-age">(09 Aug '13, 07:45)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-23607" class="comment-tools"></div><div class="clear"></div><div id="comment-23607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Prose Authorized IE not displaying in S1AP message and Update LocationAnswer message in Wireshark"
description = '''Hi, I want to see the Prose Authorized IE information in Wireshark logs for S1AP message Initial COntext Setup Request and also in diameter message Update Location Answer.  Currently am seeing the IE as &quot;unknown&quot; in S1AP Initial Context Setup Request message and For Update Location Answer and gettin...'''
date = "2016-01-05T22:14:00Z"
lastmod = "2016-01-07T20:45:00Z"
weight = 48894
keywords = [ "prose", "authorized" ]
aliases = [ "/questions/48894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Prose Authorized IE not displaying in S1AP message and Update LocationAnswer message in Wireshark](/questions/48894/prose-authorized-ie-not-displaying-in-s1ap-message-and-update-locationanswer-message-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48894-score" class="post-score" title="current number of votes">0</div><span id="post-48894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to see the Prose Authorized IE information in Wireshark logs for S1AP message Initial COntext Setup Request and also in diameter message Update Location Answer.</p><p>Currently am seeing the IE as "unknown" in S1AP Initial Context Setup Request message</p><p>and For Update Location Answer and getting as "Unknown AVP 3701 (vendor 3GPP).</p><p>These IE information are there according to 3GPP Rel-12 specifications. I am using the latest wireshark build Version 2.1.0-1334-g4762828 (v2.1.0rc0-1334-g4762828 from master).</p><p>Can you please let me know is this a known issue or when the fix might be available?</p><p>Br, Rajeev</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prose" rel="tag" title="see questions tagged &#39;prose&#39;">prose</span> <span class="post-tag tag-link-authorized" rel="tag" title="see questions tagged &#39;authorized&#39;">authorized</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '16, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/4e676b8c405e5833924c3721e2f7dcc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MME&#39;s gravatar image" /><p><span>MME</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MME has no accepted answers">0%</span></p></div></div><div id="comments-container-48894" class="comments-container"></div><div id="comment-tools-48894" class="comment-tools"></div><div class="clear"></div><div id="comment-48894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48908"></span>

<div id="answer-container-48908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48908-score" class="post-score" title="current number of votes">1</div><span id="post-48908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The S1AP dissector is based on V12.2.0 (2014-06). I'll update it and also look at the diameter.xml files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '16, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-48908" class="comments-container"><span id="48934"></span><div id="comment-48934" class="comment"><div id="post-48934-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer.</p><p>Can you please let me know by when this might be available?</p></div><div id="comment-48934-info" class="comment-info"><span class="comment-age">(06 Jan '16, 21:15)</span> <span class="comment-user userinfo">MME</span></div></div><span id="48935"></span><div id="comment-48935" class="comment"><div id="post-48935-score" class="comment-score"></div><div class="comment-text"><p>The S1AP update was committed yesterday.</p></div><div id="comment-48935-info" class="comment-info"><span class="comment-age">(06 Jan '16, 21:22)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="48936"></span><div id="comment-48936" class="comment"><div id="post-48936-score" class="comment-score"></div><div class="comment-text"><p>Appreciated quick response. Any update on S6a diameter interface?</p><p>diameter side am getting as Unknown AVP.</p></div><div id="comment-48936-info" class="comment-info"><span class="comment-age">(06 Jan '16, 22:28)</span> <span class="comment-user userinfo">MME</span></div></div><span id="48941"></span><div id="comment-48941" class="comment"><div id="post-48941-score" class="comment-score"></div><div class="comment-text"><p>Diameter updates added in</p><p><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=f3ae6c9c5cac0811f465bc08e1adbb0b37e85a7f">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=f3ae6c9c5cac0811f465bc08e1adbb0b37e85a7f</a></p></div><div id="comment-48941-info" class="comment-info"><span class="comment-age">(07 Jan '16, 04:40)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="48963"></span><div id="comment-48963" class="comment"><div id="post-48963-score" class="comment-score"></div><div class="comment-text"><p>Thanks its working now</p></div><div id="comment-48963-info" class="comment-info"><span class="comment-age">(07 Jan '16, 20:45)</span> <span class="comment-user userinfo">MME</span></div></div></div><div id="comment-tools-48908" class="comment-tools"></div><div class="clear"></div><div id="comment-48908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


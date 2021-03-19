+++
type = "question"
title = "ws 1.12 unresolved external for get_plugin_dir"
description = '''I&#x27;m getting the following build error when trying to create my plugin packet-gena.obj : error LNK2019: unresolved external symbol __imp__get_plugin_dir referenced in function _proto_register_gena  filesystem.h was moved to the wsutil for 1.12 according to the changelog. I can also see from the maili...'''
date = "2014-08-12T13:01:00Z"
lastmod = "2014-08-12T14:28:00Z"
weight = 35441
keywords = [ "dissector" ]
aliases = [ "/questions/35441" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ws 1.12 unresolved external for get\_plugin\_dir](/questions/35441/ws-112-unresolved-external-for-get_plugin_dir)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35441-score" class="post-score" title="current number of votes">0</div><span id="post-35441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting the following build error when trying to create my plugin</p><pre><code>packet-gena.obj : error LNK2019: unresolved external symbol __imp__get_plugin_dir referenced in function _proto_register_gena</code></pre><p>filesystem.h was moved to the wsutil for 1.12 according to the changelog. I can also see from the mailing list it was moved because it was more of an appropriate place. The reasons was something along the lines of filesystem is used by the system and not just dissectors. I can see by using grep that mate and wimaxasncp have an include for it. So it looks like I should still be able to link to the code.<br />
</p><p>What should I be looking at to troubleshoot this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '14, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div></div><div id="comments-container-35441" class="comments-container"></div><div id="comment-tools-35441" class="comment-tools"></div><div class="clear"></div><div id="comment-35441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35443"></span>

<div id="answer-container-35443" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35443-score" class="post-score" title="current number of votes">1</div><span id="post-35443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ensure to modify your makefile (Makefile.nmake as you seem to be running on Windows) so as to link with libwsutil.lib.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '14, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35443" class="comments-container"><span id="35444"></span><div id="comment-35444" class="comment"><div id="post-35444-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That worked.</p></div><div id="comment-35444-info" class="comment-info"><span class="comment-age">(12 Aug '14, 14:28)</span> <span class="comment-user userinfo">tlann</span></div></div></div><div id="comment-tools-35443" class="comment-tools"></div><div class="clear"></div><div id="comment-35443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


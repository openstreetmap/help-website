+++
type = "question"
title = "Custom Dissector - Duplicate Protocol found:"
description = '''I continuously am forced to delete the below from ...&#92;wireshark&#92;epan&#92;dissectors&#92;register.c Is there another way to swat this fly from my face? /-----------------------------------------------------------------------------------------/ {extern void proto_register_bppcp (void); if(cb) (*cb)(RA_REGISTE...'''
date = "2013-01-07T14:20:00Z"
lastmod = "2013-01-07T20:36:00Z"
weight = 17535
keywords = [ "duplicate", "dissector", "register.c" ]
aliases = [ "/questions/17535" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Custom Dissector - Duplicate Protocol found:](/questions/17535/custom-dissector-duplicate-protocol-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17535-score" class="post-score" title="current number of votes">0</div><span id="post-17535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I continuously am forced to delete the below from ...\wireshark\epan\dissectors\register.c Is there another way to swat this fly from my face?</p><p>/<em>-----------------------------------------------------------------------------------------</em>/ {extern void proto_register_bppcp (void); if(cb) (*cb)(RA_REGISTER, "proto_register_bppcp", client_data); proto_register_bppcp ();}</p><p>&amp;,</p><p>{extern void proto_reg_handoff_bppcp (void); if(cb) (*cb)(RA_HANDOFF, "proto_reg_handoff_bppcp", client_data); proto_reg_handoff_bppcp ();}</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-register.c" rel="tag" title="see questions tagged &#39;register.c&#39;">register.c</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '13, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p><span>jballard1979</span><br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span></p></div></div><div id="comments-container-17535" class="comments-container"></div><div id="comment-tools-17535" class="comment-tools"></div><div class="clear"></div><div id="comment-17535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17540"></span>

<div id="answer-container-17540" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17540-score" class="post-score" title="current number of votes">1</div><span id="post-17540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jballard1979 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Remove <strong>epan/dissectors/register-cache.pkl</strong>,</p><p>then build again using <strong>make -C epan</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17540" class="comments-container"><span id="17544"></span><div id="comment-17544" class="comment"><div id="post-17544-score" class="comment-score"></div><div class="comment-text"><p>How do I use the make -C epan command using win?</p></div><div id="comment-17544-info" class="comment-info"><span class="comment-age">(07 Jan '13, 20:36)</span> <span class="comment-user userinfo">jballard1979</span></div></div></div><div id="comment-tools-17540" class="comment-tools"></div><div class="clear"></div><div id="comment-17540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


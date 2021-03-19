+++
type = "question"
title = "How to decode CORBA over SSL?"
description = '''Hello! I&#x27;m trying to analyse CORBA traffic encrypted with SSL. I&#x27;ve clicked on the &quot;RSA keys list&quot; Edit button, opened the dialog to add a new entry, but when I try to set the protocol to GIOP, I get this error message: error in column &#x27;Protocol&#x27;: Could not find dissector for: &#x27;GIOP&#x27; What protocol s...'''
date = "2011-12-06T06:44:00Z"
lastmod = "2011-12-13T05:06:00Z"
weight = 7800
keywords = [ "ssl", "corba", "giop" ]
aliases = [ "/questions/7800" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to decode CORBA over SSL?](/questions/7800/how-to-decode-corba-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7800-score" class="post-score" title="current number of votes">0</div><span id="post-7800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I'm trying to analyse CORBA traffic encrypted with SSL. I've clicked on the "RSA keys list" Edit button, opened the dialog to add a new entry, but when I try to set the protocol to GIOP, I get this error message:</p><p>error in column 'Protocol': Could not find dissector for: 'GIOP'</p><p>What protocol shall I use for CORBA? I can see clear text CORBA communication, so Wireshark can definitely decode the GIOP protocol.</p><p>By the way, this is on Windows with Wireshark 1.6.4.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-corba" rel="tag" title="see questions tagged &#39;corba&#39;">corba</span> <span class="post-tag tag-link-giop" rel="tag" title="see questions tagged &#39;giop&#39;">giop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '11, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/64394e237dbbb31608f6491ff2f141e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NAR&#39;s gravatar image" /><p><span>NAR</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NAR has no accepted answers">0%</span></p></div></div><div id="comments-container-7800" class="comments-container"></div><div id="comment-tools-7800" class="comment-tools"></div><div class="clear"></div><div id="comment-7800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7804"></span>

<div id="answer-container-7804" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7804-score" class="post-score" title="current number of votes">1</div><span id="post-7804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NAR has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, It is not possible currently a patch is needed Index: epan/dissectors/packet-giop.c =================================================================== --- epan/dissectors/packet-giop.c (revision 1075) +++ epan/dissectors/packet-giop.c (working copy) @@ -4493,7 +4493,9 @@ proto_register_field_array (proto_giop, hf, array_length (hf)); proto_register_subtree_array (ett, array_length (ett));</p><ul><li>register_dissector("giop", dissect_giop_tcp, proto_gtp);</li></ul><p>+ / <em>register init routine</em> /</p><p>register_init_routine( &amp;giop_init); / <em>any init stuff</em> /</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '11, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7804" class="comments-container"><span id="7806"></span><div id="comment-7806" class="comment"><div id="post-7806-score" class="comment-score"></div><div class="comment-text"><p>You can try a development build (see Wirsharks home page) with revision 40107 or higer the build should finish in a couple of hours.</p></div><div id="comment-7806-info" class="comment-info"><span class="comment-age">(06 Dec '11, 11:35)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="7944"></span><div id="comment-7944" class="comment"><div id="post-7944-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I could add GIOP in the 40110 build.</p></div><div id="comment-7944-info" class="comment-info"><span class="comment-age">(13 Dec '11, 05:06)</span> <span class="comment-user userinfo">NAR</span></div></div></div><div id="comment-tools-7804" class="comment-tools"></div><div class="clear"></div><div id="comment-7804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Getting user input for dissection"
description = '''Hi, In wireshark is there any way I can get input from user at run time and use that information to dissect packet information. The user information will be basically used to assign names to dissected fields.'''
date = "2012-02-29T19:04:00Z"
lastmod = "2012-03-01T02:23:00Z"
weight = 9284
keywords = [ "development" ]
aliases = [ "/questions/9284" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting user input for dissection](/questions/9284/getting-user-input-for-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In wireshark is there any way I can get input from user at run time and use that information to dissect packet information. The user information will be basically used to assign names to dissected fields.</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '12, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p>ashish_goel<br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div></div><div id="comments-container-9284" class="comments-container"></div><div id="comment-tools-9284" class="comment-tools"></div><div class="clear"></div><div id="comment-9284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9288"></span>

<div id="answer-container-9288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9288-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to look into UAT's, see <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/uat.h">epan/uat.h</a>. These can be used in dissector preferences, they're used for example by the HTTP dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9288" class="comments-container"><span id="9314"></span><div id="comment-9314" class="comment"><div id="post-9314-score" class="comment-score"></div><div class="comment-text"><p>thanks jaap for your reply.. But where in the user submits the input and how this information gets available to dissect_XXX() function of the dissector.</p></div><div id="comment-9314-info" class="comment-info"><span class="comment-age">(02 Mar '12, 10:28)</span> ashish_goel</div></div><span id="12094"></span><div id="comment-12094" class="comment"><div id="post-12094-score" class="comment-score"></div><div class="comment-text"><p>Hi!I'm encounter the same trouble . Did you resolve you problem？ waiting for your reply.Thanks!</p></div><div id="comment-12094-info" class="comment-info"><span class="comment-age">(20 Jun '12, 19:09)</span> smilezuzu</div></div><span id="12100"></span><div id="comment-12100" class="comment"><div id="post-12100-score" class="comment-score"></div><div class="comment-text"><p>Please look at <a href="http://anonsvn.wireshark.org/wireshark/trunk-1.6/epan/dissectors/packet-http.c">the HTTP dissector</a>. Look for header_name and header_desc, and UAT.</p></div><div id="comment-12100-info" class="comment-info"><span class="comment-age">(21 Jun '12, 01:18)</span> Jaap ♦</div></div></div><div id="comment-tools-9288" class="comment-tools"></div><div class="clear"></div><div id="comment-9288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


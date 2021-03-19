+++
type = "question"
title = "help with V.150.1 capture"
description = '''What wireshark version contains the ability to capture V.150.1 information like the SSE and SPRT protocols?'''
date = "2012-05-07T13:02:00Z"
lastmod = "2012-05-07T15:54:00Z"
weight = 10745
keywords = [ "v.150" ]
aliases = [ "/questions/10745" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [help with V.150.1 capture](/questions/10745/help-with-v1501-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10745-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What wireshark version contains the ability to capture V.150.1 information like the SSE and SPRT protocols?</p></div><div id="question-tags" class="tags-container tags">v.150</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/2802c7ad0e8364bc71e4699c4984e1f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dgibson&#39;s gravatar image" /><p>dgibson<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dgibson has no accepted answers">0%</span></p></div></div><div id="comments-container-10745" class="comments-container"></div><div id="comment-tools-10745" class="comment-tools"></div><div class="clear"></div><div id="comment-10745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10754"></span>

<div id="answer-container-10754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10754-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>by looking at the code of wireshark 1.7.1, I conclude that there is no support vo V.150.1 (V.MOIP). However, you can allways write your own dissector for that protocol.</p><p><a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a></p><p>EDIT: There is an old entry on the Ethereal mailing list.</p><p><a href="http://www.ethereal.com/lists/ethereal-users/200510/msg00211.html">http://www.ethereal.com/lists/ethereal-users/200510/msg00211.html</a></p><p>Someone mentions, that Michal Lum might have written a dissector for SPRT. Try to contact him. Search google or the wireshark AUTHORS file for his e-mail address.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '12, 16:03</p></div></div><div id="comments-container-10754" class="comments-container"><span id="10762"></span><div id="comment-10762" class="comment"><div id="post-10762-score" class="comment-score">1</div><div class="comment-text"><p>Some one could complete <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3507">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3507</a> or <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2909">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2909</a></p></div><div id="comment-10762-info" class="comment-info"><span class="comment-age">(07 May '12, 21:40)</span> Anders ♦</div></div><span id="10771"></span><div id="comment-10771" class="comment"><div id="post-10771-score" class="comment-score"></div><div class="comment-text"><p>good hint!</p></div><div id="comment-10771-info" class="comment-info"><span class="comment-age">(08 May '12, 02:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10754" class="comment-tools"></div><div class="clear"></div><div id="comment-10754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "How to do repetive tasks."
description = '''I have sample SS7 traces...and my aim is to find tcap abort send in response of alertSC to achieve same following is the procedure i follow. 1.Apply filter gsm_old.localValue == 64 this will filter out all alertSC packet. 2.Get tcap id from TCAP layer. 3.Apply filter tcap.tid == &amp;lt;id&amp;gt; 4.Check i...'''
date = "2012-07-26T03:16:00Z"
lastmod = "2012-07-26T05:10:00Z"
weight = 13013
keywords = [ "tcap" ]
aliases = [ "/questions/13013" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to do repetive tasks.](/questions/13013/how-to-do-repetive-tasks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have sample SS7 traces...and my aim is to find tcap abort send in response of alertSC to achieve same following is the procedure i follow.</p><p>1.Apply filter gsm_old.localValue == 64 this will filter out all alertSC packet. 2.Get tcap id from TCAP layer. 3.Apply filter tcap.tid == &lt;id&gt; 4.Check if this is abort packet or not.</p><p>Now my problem is there are n huge number of alertSC packets and i cant keep on doing this for every packet, is there any way to sort out the problem</p><p>With Regards Avinash Jha</p></div><div id="question-tags" class="tags-container tags">tcap</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/ea81afbd71dc63ea6a6506203bc83c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creative&#39;s gravatar image" /><p>creative<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creative has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 03:25</p></div></div><div id="comments-container-13013" class="comments-container"></div><div id="comment-tools-13013" class="comment-tools"></div><div class="clear"></div><div id="comment-13013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13016"></span>

<div id="answer-container-13016" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13016-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's a thing called <a href="http://wiki.wireshark.org/Mate">MATE</a> build into Wireshark. That may be of help here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13016" class="comments-container"></div><div id="comment-tools-13016" class="comment-tools"></div><div class="clear"></div><div id="comment-13016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


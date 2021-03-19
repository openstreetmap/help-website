+++
type = "question"
title = "GRE Protocol Type"
description = '''The GRE Protocol Type 0x2000 is used by Cisco gear to encapsulate CDP frames. What would be the easiest way to modify the GRE dissector to interpret the Data within the GRE payload as a CDP frame when the GRE Protocol Type is 0x2000 ?'''
date = "2015-04-18T01:08:00Z"
lastmod = "2015-04-18T10:27:00Z"
weight = 41554
keywords = [ "gre", "sub-dissector", "dissector" ]
aliases = [ "/questions/41554" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GRE Protocol Type](/questions/41554/gre-protocol-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The GRE Protocol Type 0x2000 is used by Cisco gear to encapsulate CDP frames. What would be the easiest way to modify the GRE dissector to interpret the Data within the GRE payload as a CDP frame when the GRE Protocol Type is 0x2000 ?</p></div><div id="question-tags" class="tags-container tags">gre sub-dissector dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '15, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/a851e7336d669669afcff1a356d0216a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w1zard&#39;s gravatar image" /><p>w1zard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w1zard has no accepted answers">0%</span></p></div></div><div id="comments-container-41554" class="comments-container"></div><div id="comment-tools-41554" class="comment-tools"></div><div class="clear"></div><div id="comment-41554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41561"></span>

<div id="answer-container-41561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41561-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, You should make the CDP dissector register in the "gre.proto" dissector table. If you raise a bug and attach a sample trace it <em>should</em> be easy to implement.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '15, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-41561" class="comments-container"></div><div id="comment-tools-41561" class="comment-tools"></div><div class="clear"></div><div id="comment-41561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


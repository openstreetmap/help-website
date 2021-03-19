+++
type = "question"
title = "Radius Duplicate"
description = '''When a Radius request is a duplicate request ? What are criteria to define a duplicate request ?  Same question for response Using wireshark Version 2.2.6 (v2.2.6-0-g32dac6a)'''
date = "2017-05-09T07:54:00Z"
lastmod = "2017-05-09T11:03:00Z"
weight = 61310
keywords = [ "duplicate", "radius" ]
aliases = [ "/questions/61310" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Radius Duplicate](/questions/61310/radius-duplicate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When a Radius request is a duplicate request ? What are criteria to define a duplicate request ? Same question for response Using wireshark Version 2.2.6 (v2.2.6-0-g32dac6a)</p></div><div id="question-tags" class="tags-container tags">duplicate radius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/d77957e8aaacad3b911d13d7a74a0bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alain_m&#39;s gravatar image" /><p>alain_m<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alain_m has no accepted answers">0%</span></p></div></div><div id="comments-container-61310" class="comments-container"></div><div id="comment-tools-61310" class="comment-tools"></div><div class="clear"></div><div id="comment-61310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61312"></span>

<div id="answer-container-61312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61312-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's a request and response tracking mechanism involved that also detects duplicates. From reading the code is seems to check for the radius code, ident and conversation (that is, the connection between server and client), and then it checks the authenticator as well. If these all match then it's marked a duplicate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '17, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61312" class="comments-container"></div><div id="comment-tools-61312" class="comment-tools"></div><div class="clear"></div><div id="comment-61312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


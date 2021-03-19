+++
type = "question"
title = "FCoE code"
description = '''Need help in finding the code for FCoE support in wireshark.'''
date = "2011-04-25T23:03:00Z"
lastmod = "2011-04-25T23:22:00Z"
weight = 3713
keywords = [ "fcoe" ]
aliases = [ "/questions/3713" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [FCoE code](/questions/3713/fcoe-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need help in finding the code for FCoE support in wireshark.</p></div><div id="question-tags" class="tags-container tags">fcoe</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '11, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/acb9eb1bd5942bf119cbf15828fa66bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="searching&#39;s gravatar image" /><p>searching<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="searching has no accepted answers">0%</span></p></div></div><div id="comments-container-3713" class="comments-container"></div><div id="comment-tools-3713" class="comment-tools"></div><div class="clear"></div><div id="comment-3713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3714"></span>

<div id="answer-container-3714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3714-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can find the FCoE dissector code in:</p><pre><code>epan/dissectors/packet-fcoe.c</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '11, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3714" class="comments-container"><span id="3717"></span><div id="comment-3717" class="comment"><div id="post-3717-score" class="comment-score"></div><div class="comment-text"><p>Thanks.....</p></div><div id="comment-3717-info" class="comment-info"><span class="comment-age">(25 Apr '11, 23:48)</span> searching</div></div></div><div id="comment-tools-3714" class="comment-tools"></div><div class="clear"></div><div id="comment-3714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3715"></span>

<div id="answer-container-3715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3715-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-fcoe.c">Here you go</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '11, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3715" class="comments-container"></div><div id="comment-tools-3715" class="comment-tools"></div><div class="clear"></div><div id="comment-3715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


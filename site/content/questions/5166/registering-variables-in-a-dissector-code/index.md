+++
type = "question"
title = "Registering variables in a dissector code??"
description = '''I have a field in my protocol like this: IP (which is a set of 32 IP addresses). So should I use an array to display the 32 IP addresses or something else? If I use the array, how do I register my array in the dissector&#x27;s proto_register function?? Please help..!!'''
date = "2011-07-21T23:41:00Z"
lastmod = "2011-07-22T04:36:00Z"
weight = 5166
keywords = [ "array", "dissector" ]
aliases = [ "/questions/5166" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Registering variables in a dissector code??](/questions/5166/registering-variables-in-a-dissector-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5166-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a field in my protocol like this:</p><p>IP (which is a set of 32 IP addresses). So should I use an array to display the 32 IP addresses or something else?</p><p>If I use the array, how do I register my array in the dissector's proto_register function??</p><p>Please help..!!</p></div><div id="question-tags" class="tags-container tags">array dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '11, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-5166" class="comments-container"></div><div id="comment-tools-5166" class="comment-tools"></div><div class="clear"></div><div id="comment-5166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5174"></span>

<div id="answer-container-5174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5174-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Define one field with FT_IPv4, then reuse that for all items in the sequence of your protocol message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '11, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5174" class="comments-container"></div><div id="comment-tools-5174" class="comment-tools"></div><div class="clear"></div><div id="comment-5174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


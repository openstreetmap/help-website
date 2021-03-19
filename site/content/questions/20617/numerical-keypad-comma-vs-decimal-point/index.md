+++
type = "question"
title = "Numerical Keypad comma vs. decimal point"
description = '''When I try to use the numpad (numerical keypad) and hit the decimal point key Wireshark gives me a comma instead of a dot. While I agree that, that is the default for my country, it isn&#x27;t how I have Windows setup. Excel and the built in Windows 7 calculator both re-act &quot;correctly&quot; and use a dot inst...'''
date = "2013-04-19T00:59:00Z"
lastmod = "2013-04-20T05:51:00Z"
weight = 20617
keywords = [ "numpad", "input" ]
aliases = [ "/questions/20617" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Numerical Keypad comma vs. decimal point](/questions/20617/numerical-keypad-comma-vs-decimal-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20617-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to use the numpad (numerical keypad) and hit the decimal point key Wireshark gives me a comma instead of a dot. While I agree that, that is the default for my country, it isn't how I have Windows setup. Excel and the built in Windows 7 calculator both re-act "correctly" and use a dot instead of a comma when I use the "." key on the numpad, but Wireshark seems to be getting its cue from someplace else, and it is using a comma.<br />
</p><p>Does anyone have any idea concerning how I might change this, so that I can type IP addresses using just my numpad?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">numpad input</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '13, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/47965d24c12a3b87affd58ad6f581187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oldenough&#39;s gravatar image" /><p>oldenough<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oldenough has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '13, 08:02</p></div></div><div id="comments-container-20617" class="comments-container"></div><div id="comment-tools-20617" class="comment-tools"></div><div class="clear"></div><div id="comment-20617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20656"></span>

<div id="answer-container-20656" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20656-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After googling a bit, I believe that is a "known problem" of GTK (Other tools seem to have similar problems). Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '13, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20656" class="comments-container"><span id="20660"></span><div id="comment-20660" class="comment"><div id="post-20660-score" class="comment-score"></div><div class="comment-text"><p>After thinking about it some more today--and poking around inside Windows--this is pretty much the conclusion I had arrived at as well, but I am new to Wireshark and wanted some confirmation from the community before I filed a bug report. I will do so now.<br />
</p><p>Thank you for your time and assistance. :)</p></div><div id="comment-20660-info" class="comment-info"><span class="comment-age">(20 Apr '13, 10:21)</span> oldenough</div></div></div><div id="comment-tools-20656" class="comment-tools"></div><div class="clear"></div><div id="comment-20656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


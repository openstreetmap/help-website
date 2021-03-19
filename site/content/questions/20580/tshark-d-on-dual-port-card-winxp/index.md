+++
type = "question"
title = "tshark -D on dual port card (WinXP)"
description = '''On a WInXP computer, I need to programatically read the results of tshark -D and identify the port I want to use based on the description. Unfortunately the board is is a dual port card, so the second port is identified with (Intel(R)... #2), but tshark does not display the #2. Any suggestions, or i...'''
date = "2013-04-18T08:56:00Z"
lastmod = "2013-04-18T10:49:00Z"
weight = 20580
keywords = [ "tshark", "winxp" ]
aliases = [ "/questions/20580" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark -D on dual port card (WinXP)](/questions/20580/tshark-d-on-dual-port-card-winxp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20580-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On a WInXP computer, I need to programatically read the results of tshark -D and identify the port I want to use based on the description. Unfortunately the board is is a dual port card, so the second port is identified with (Intel(R)... #2), but tshark does not display the #2. Any suggestions, or is this a change request.</p></div><div id="question-tags" class="tags-container tags">tshark winxp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/07b58b8569b028b7ddcff3c3ad8983d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mictalley&#39;s gravatar image" /><p>mictalley<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mictalley has no accepted answers">0%</span></p></div></div><div id="comments-container-20580" class="comments-container"></div><div id="comment-tools-20580" class="comment-tools"></div><div class="clear"></div><div id="comment-20580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20585"></span>

<div id="answer-container-20585" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20585-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I mentioned in the answer to the following question, you can use <code>dumpcap -D -M</code></p><blockquote><p><a href="http://ask.wireshark.org/questions/20545/right-interface-to-use-with-tshark-under-windows">http://ask.wireshark.org/questions/20545/right-interface-to-use-with-tshark-under-windows</a></p></blockquote><p>Then use the IP address of the interface to identify the second port of the nic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '13, 10:53</p></div></div><div id="comments-container-20585" class="comments-container"><span id="20591"></span><div id="comment-20591" class="comment"><div id="post-20591-score" class="comment-score"></div><div class="comment-text"><p>Thanks, works great - and this is better than the card description since the computer will have a fixed IP regardless of which manufacturer's card is installed.</p></div><div id="comment-20591-info" class="comment-info"><span class="comment-age">(18 Apr '13, 13:34)</span> mictalley</div></div></div><div id="comment-tools-20585" class="comment-tools"></div><div class="clear"></div><div id="comment-20585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


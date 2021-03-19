+++
type = "question"
title = "Making a Dissector that Changes with Packet Component"
description = '''I am a bit new at writing dissectors for Wireshark and trying to find a way to create a different tree that occurs if I get a certain message in the header of each packet as well as the number of bytes in the packet according to another part of the header. How would I go about changing how each mess...'''
date = "2014-07-03T08:00:00Z"
lastmod = "2014-07-03T08:02:00Z"
weight = 34385
keywords = [ "dissector" ]
aliases = [ "/questions/34385" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Making a Dissector that Changes with Packet Component](/questions/34385/making-a-dissector-that-changes-with-packet-component)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34385-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a bit new at writing dissectors for Wireshark and trying to find a way to create a different tree that occurs if I get a certain message in the header of each packet as well as the number of bytes in the packet according to another part of the header. How would I go about changing how each message is dissected based upon the message type that I receive in the header file?</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/c8e5eace6d27629d342dd0bed8f33ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raiku11&#39;s gravatar image" /><p>raiku11<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raiku11 has no accepted answers">0%</span></p></div></div><div id="comments-container-34385" class="comments-container"></div><div id="comment-tools-34385" class="comment-tools"></div><div class="clear"></div><div id="comment-34385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34386"></span>

<div id="answer-container-34386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34386-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Either create a switch statement that dissects according to the message type, or create sub-dissectors for each message type and again call them depending on the message type value.</p><p>The switch is usually enough for simple cases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '14, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34386" class="comments-container"></div><div id="comment-tools-34386" class="comment-tools"></div><div class="clear"></div><div id="comment-34386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


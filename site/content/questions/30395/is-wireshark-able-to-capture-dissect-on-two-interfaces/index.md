+++
type = "question"
title = "Is wireshark able to capture / dissect on two interfaces?"
description = '''Hi, i&#x27;m looking for solution, but i was not able to build a capable test case. Is wireshark able to capture and dissect packets in the following scenario: eth0 - this interface receives the &quot;outgoing&quot; packets  eth1 - this interface receives the &quot;incoming&quot; packets basically they build up to one tcp s...'''
date = "2014-03-04T07:16:00Z"
lastmod = "2014-03-04T07:43:00Z"
weight = 30395
keywords = [ "multiple-interfaces", "tcp" ]
aliases = [ "/questions/30395" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is wireshark able to capture / dissect on two interfaces?](/questions/30395/is-wireshark-able-to-capture-dissect-on-two-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30395-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i'm looking for solution, but i was not able to build a capable test case. Is wireshark able to capture and dissect packets in the following scenario: eth0 - this interface receives the "outgoing" packets eth1 - this interface receives the "incoming" packets</p><p>basically they build up to one tcp stream, but the "replies" are always separated from the "requests". Both eth0 and eth1 are monitoring ports.</p><p>Is wireshark able to capture and process the tcp-stream properly? Thanks</p></div><div id="question-tags" class="tags-container tags">multiple-interfaces tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/888cd05f58a56cb8dadc4adcf8d160a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lachupe&#39;s gravatar image" /><p>Lachupe<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lachupe has no accepted answers">0%</span></p></div></div><div id="comments-container-30395" class="comments-container"></div><div id="comment-tools-30395" class="comment-tools"></div><div class="clear"></div><div id="comment-30395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30397"></span>

<div id="answer-container-30397" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30397-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, since Wireshark 1.8 you can capture on more than one interface, if you choose PCAPng as capture format. Each interface will be included in the capture file and each packet has an index to the interface it was captured on. You can see that index in the top section of the dissected packets. The TCP expert does not handle multiple interfaces independently, so if you capture as you've descriped it will just consider packets coming in on both interface as one tcp stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30397" class="comments-container"><span id="30398"></span><div id="comment-30398" class="comment"><div id="post-30398-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-30398-info" class="comment-info"><span class="comment-age">(04 Mar '14, 07:49)</span> Lachupe</div></div></div><div id="comment-tools-30397" class="comment-tools"></div><div class="clear"></div><div id="comment-30397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


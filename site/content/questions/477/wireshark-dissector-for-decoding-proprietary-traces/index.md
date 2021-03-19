+++
type = "question"
title = "Wireshark dissector for decoding proprietary traces"
description = '''I have proprietary trace points throughout my code that are captured to a file. I&#x27;d like to build a Wireshark dissector to decode these traces. I worry that these traces are not wire packets. They contain an id, timestamp, size and then some additional bytes in a binary stream format. I currently ha...'''
date = "2010-10-11T13:35:00Z"
lastmod = "2010-10-11T14:38:00Z"
weight = 477
keywords = [ "binary", "dissector", "proprietary", "stream" ]
aliases = [ "/questions/477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark dissector for decoding proprietary traces](/questions/477/wireshark-dissector-for-decoding-proprietary-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-477-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have proprietary trace points throughout my code that are captured to a file. I'd like to build a Wireshark dissector to decode these traces. I worry that these traces are not wire packets. They contain an id, timestamp, size and then some additional bytes in a binary stream format. I currently have created a crude decoder for these traces but I'd rather use Wireshark and some of its features. Does this seem like a good idea or is Wireshark better suited for wire packets?</p></div><div id="question-tags" class="tags-container tags">binary dissector proprietary stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '10, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/b4da07c0f67b732517df5a4283b86f7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cliffconklin&#39;s gravatar image" /><p>cliffconklin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cliffconklin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 19:15</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-477" class="comments-container"></div><div id="comment-tools-477" class="comment-tools"></div><div class="clear"></div><div id="comment-477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="478"></span>

<div id="answer-container-478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-478-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Any 'framed' transport can be processed in a dissector. That's how 'wire' protocols work, but also 'streaming media', like MPEG and even JPEG files work. Wireshark contains dissectors for all these.</p><p>What you can do is write out PCAP format files (see <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">Wiki pcap page</a>) with one of the USER Data Link Types and create a dissector for that DLT.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-478" class="comments-container"></div><div id="comment-tools-478" class="comment-tools"></div><div class="clear"></div><div id="comment-478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


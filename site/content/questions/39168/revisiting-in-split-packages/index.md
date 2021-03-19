+++
type = "question"
title = "Revisiting in split packages"
description = '''Hi, I was wondering about functions for TCP packets (like tcp_dissect_pdus) that need to deal with fragmented packages. When I had to write a similar thing it completely broke down because of the way packets are revisited after the first pass through; specifically when some packets had to be looked ...'''
date = "2015-01-15T09:54:00Z"
lastmod = "2015-01-15T10:20:00Z"
weight = 39168
keywords = [ "tcp_dissect_pdus", "fragmentation", "tcp" ]
aliases = [ "/questions/39168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Revisiting in split packages](/questions/39168/revisiting-in-split-packages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was wondering about functions for TCP packets (like tcp_dissect_pdus) that need to deal with fragmented packages.</p><p>When I had to write a similar thing it completely broke down because of the way packets are revisited after the first pass through; specifically when some packets had to be looked at in the right order for the reassembly to work.</p><p>What's the fix for this? Some pre-made func.s clearly know how to deal with this.</p></div><div id="question-tags" class="tags-container tags">tcp_dissect_pdus fragmentation tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/ca562b18c08fc77caf70657719e1629f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicole_identity&#39;s gravatar image" /><p>nicole_identity<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicole_identity has no accepted answers">0%</span></p></div></div><div id="comments-container-39168" class="comments-container"><span id="39171"></span><div id="comment-39171" class="comment"><div id="post-39171-score" class="comment-score"></div><div class="comment-text"><p>It seemed to me that when I had my dissector ignore packets flagged as visited then any results from the original dissection were deleted and those packets came out undissected.</p><p>By displaying as the dissection occurred I got something like this happening without the flag check:</p><p>Packet A goes in, it's half #1</p><p>some other packets are processed, but they are all normal packets so no problems</p><p>Packet B goes in, it's half #2</p><p>Packet A is combined with packet B and all goes well</p><p>Some other packets are revisited and at some point...</p><p>The packets that were fragmented get looked at again (unnecessarily, it seems, since the recombination worked the first time around)</p><p>Somehow there ends up being a time where the packets are being looked at in inappropriate ways. For example, B being looked at before A and sending out a messaged missing the first half.</p><p>Wrong results since the last time A and B were looked at it wasn't done in the right order (even though the first time around was fine)</p><p>And then I got something like this with the flag check:</p><p>Packet A goes in, it's half #1</p><p>some other packets are processed, but they are all normal packets so no problems</p><p>Packet B goes in, it's half #2</p><p>Packet A is combined with packet B and all goes well</p><p>Packets come back but the dissector ignores them</p><p>In the end all packets appear black because the data gathered the first time through has been erased</p><p>I'll try to word this better in a moment...</p></div><div id="comment-39171-info" class="comment-info"><span class="comment-age">(15 Jan '15, 10:46)</span> nicole_identity</div></div></div><div id="comment-tools-39168" class="comment-tools"></div><div class="clear"></div><div id="comment-39168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39169"></span>

<div id="answer-container-39169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39169-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dissectors can use the pinfo-&gt;fd-&gt;flags.visited flag to determine if this is the first time the dissector has seen the frame.</p><p>Can you add some more detail to your issue, i.e. exactly what didn't work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39169" class="comments-container"><span id="39172"></span><div id="comment-39172" class="comment"><div id="post-39172-score" class="comment-score"></div><div class="comment-text"><p>I'm attempting to add more info.</p></div><div id="comment-39172-info" class="comment-info"><span class="comment-age">(15 Jan '15, 10:49)</span> nicole_identity</div></div></div><div id="comment-tools-39169" class="comment-tools"></div><div class="clear"></div><div id="comment-39169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


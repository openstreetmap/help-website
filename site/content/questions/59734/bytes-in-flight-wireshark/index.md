+++
type = "question"
title = "Bytes in flight - wireshark"
description = '''Is there a field for a &quot;bytes in flight&quot; in Wireshark? How do we calculate or add a field for bytes in flight for each packet on Wireshark?'''
date = "2017-02-28T08:53:00Z"
lastmod = "2017-02-28T09:17:00Z"
weight = 59734
keywords = [ "tcp-bytes-in-flight", "congestion", "wireshark" ]
aliases = [ "/questions/59734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in flight - wireshark](/questions/59734/bytes-in-flight-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a field for a "bytes in flight" in Wireshark? How do we calculate or add a field for bytes in flight for each packet on Wireshark?</p></div><div id="question-tags" class="tags-container tags">tcp-bytes-in-flight congestion wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div></div><div id="comments-container-59734" class="comments-container"></div><div id="comment-tools-59734" class="comment-tools"></div><div class="clear"></div><div id="comment-59734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59737"></span>

<div id="answer-container-59737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59737-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the field is named <code>tcp.analysis.bytes_in_flight</code>.</p><p>The easy way to display this is to open a capture file, select a TCP packet other than one of the three initial handshake packets, expand the TCP details in the packet details pane, expand the SEQ/ACK Analysis item and then right click the [Bytes in flight: xxx] item and select "Apply As Column" from the context menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '17, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '17, 09:25</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-59737" class="comments-container"><span id="59739"></span><div id="comment-59739" class="comment"><div id="post-59739-score" class="comment-score"></div><div class="comment-text"><p>The protocol preference "Analyze TCP sequence numbers" should be enabled to use "bytes_in_flight".</p></div><div id="comment-59739-info" class="comment-info"><span class="comment-age">(28 Feb '17, 09:20)</span> Uli</div></div><span id="59740"></span><div id="comment-59740" class="comment"><div id="post-59740-score" class="comment-score"></div><div class="comment-text"><p>@Uli,</p><p>Good spot, the TCP preference "Track number of bytes in flight" also needs to be enabled.</p></div><div id="comment-59740-info" class="comment-info"><span class="comment-age">(28 Feb '17, 10:32)</span> grahamb ♦</div></div></div><div id="comment-tools-59737" class="comment-tools"></div><div class="clear"></div><div id="comment-59737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


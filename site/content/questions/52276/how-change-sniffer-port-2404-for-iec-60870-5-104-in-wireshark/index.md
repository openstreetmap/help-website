+++
type = "question"
title = "How change sniffer port 2404  for IEC 60870-5-104 in Wireshark?"
description = '''How change sniffer port 2404 for IEC 60870-5-104 in Wireshark? I need 5868 port.'''
date = "2016-05-06T01:42:00Z"
lastmod = "2016-05-06T02:08:00Z"
weight = 52276
keywords = [ "60870-5-104", "iec" ]
aliases = [ "/questions/52276" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How change sniffer port 2404 for IEC 60870-5-104 in Wireshark?](/questions/52276/how-change-sniffer-port-2404-for-iec-60870-5-104-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52276-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How change sniffer port 2404 for IEC 60870-5-104 in Wireshark? I need 5868 port.</p></div><div id="question-tags" class="tags-container tags">60870-5-104 iec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '16, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/1a04b4006aba7ecb78d3a5d9dc5b8e48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Max123&#39;s gravatar image" /><p>Max123<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Max123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 May '16, 02:08</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-52276" class="comments-container"></div><div id="comment-tools-52276" class="comment-tools"></div><div class="clear"></div><div id="comment-52276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52277"></span>

<div id="answer-container-52277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52277-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's hard coded into the dissector, in order to:</p><ul><li>Dissect TCP payloads</li><li>Make distinction between source and destination</li></ul><p>but you can use "decode as..." on the TCP payload and select 104apci to get the first item done. Yet src/dst distinction will fail, decoding 'dst' always (which is an understandable bug in the dissector).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '16, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52277" class="comments-container"><span id="52279"></span><div id="comment-52279" class="comment"><div id="post-52279-score" class="comment-score"></div><div class="comment-text"><p>If you can live without live capture, you may approach the problem from the other end and use <a href="https://www.tracewrangler.com/">TraceWrangler</a> to pre-process your captures (replace the tcp/5868 port with tcp/2404 in all packets).</p></div><div id="comment-52279-info" class="comment-info"><span class="comment-age">(06 May '16, 03:20)</span> sindy</div></div><span id="52450"></span><div id="comment-52450" class="comment"><div id="post-52450-score" class="comment-score"></div><div class="comment-text"><p>I've created <a href="https://code.wireshark.org/review/#/c/15321/">a change</a> that allows the source port to be set. This shall be available in the latest development builds and eventually in 2.2.x.</p></div><div id="comment-52450-info" class="comment-info"><span class="comment-age">(11 May '16, 14:33)</span> Jaap ♦</div></div></div><div id="comment-tools-52277" class="comment-tools"></div><div class="clear"></div><div id="comment-52277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


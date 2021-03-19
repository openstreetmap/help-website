+++
type = "question"
title = "Network Tap usage with wireshark"
description = '''Tap an 100Mbps ethernet with netoptics tap, the tap has two outputs transmit and receive, I have two network adapter but how can I combine intoa single realtime capture?'''
date = "2011-11-23T18:26:00Z"
lastmod = "2011-11-24T00:33:00Z"
weight = 7591
keywords = [ "usage", "tap" ]
aliases = [ "/questions/7591" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Network Tap usage with wireshark](/questions/7591/network-tap-usage-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tap an 100Mbps ethernet with netoptics tap, the tap has two outputs transmit and receive, I have two network adapter but how can I combine intoa single realtime capture?</p></div><div id="question-tags" class="tags-container tags">usage tap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '11, 18:26</strong></p><img src="https://secure.gravatar.com/avatar/e85fae3bfdff623d2ce6383f75b0f616?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cisoccoip&#39;s gravatar image" /><p>cisoccoip<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cisoccoip has no accepted answers">0%</span></p></div></div><div id="comments-container-7591" class="comments-container"></div><div id="comment-tools-7591" class="comment-tools"></div><div class="clear"></div><div id="comment-7591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7593"></span>

<div id="answer-container-7593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try the development version of Wireshark, which allows multiple capture interface selection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '11, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7593" class="comments-container"></div><div id="comment-tools-7593" class="comment-tools"></div><div class="clear"></div><div id="comment-7593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7598"></span>

<div id="answer-container-7598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7598-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or you can use alternatively a Port Aggregation Tap which aggregates both data streams of a full duplex connection into a single output stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '11, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/eb3a25061d443954e07ccb7ce3e2c238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitu&#39;s gravatar image" /><p>mitu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitu has no accepted answers">0%</span></p></div></div><div id="comments-container-7598" class="comments-container"><span id="7600"></span><div id="comment-7600" class="comment"><div id="post-7600-score" class="comment-score"></div><div class="comment-text"><p>...and here´s some more information:</p><p><a href="http://www.network-taps.eu/products/products_aggregationtaps.php">Link to Aggregation Tap information</a></p><p>... also with application diagrams for each product</p></div><div id="comment-7600-info" class="comment-info"><span class="comment-age">(24 Nov '11, 00:30)</span> mitu</div></div><span id="7602"></span><div id="comment-7602" class="comment"><div id="post-7602-score" class="comment-score"></div><div class="comment-text"><p>True, but keep in mind that link aggregation taps cannot deliver full line rate capture due to limited bandwidth after aggregation. Strange things already happened with those, so I'd always try to get data from the already builtin normal 2-cable tap first, and only if that doesn't work think about using link aggregation.</p><p>Just my 2 cents</p></div><div id="comment-7602-info" class="comment-info"><span class="comment-age">(24 Nov '11, 00:35)</span> Landi</div></div></div><div id="comment-tools-7598" class="comment-tools"></div><div class="clear"></div><div id="comment-7598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7601"></span>

<div id="answer-container-7601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know how the 1.7-dev version handles timing problems when capturing from multiple interfaces, so here is a general slightly offtopic thought about this:</p><p>When capturing off a tap device, you have to be careful about the timings if you capture with a regular 2-port NIC or even worse two capture machines. Normally you would use a specific NIC for capturing data over more than one port in parallel. Those NICs make sure that incoming data from several ports is correctly aggregated and timestamped(!) before delivering it to your analyzer.</p><p>So whatever setup you choose to aggregate/merge/whatever your two incoming connections from the tap, please keep this in mind, and doublecheck your final trace for those timing issues and remember that a "normal" 2-port NIC in most cases also has this issues.</p><p>So maybe you try capturing into seperate files and chronologically merge those later via mergecap as a start. If you have timely diffs in the two traces you can <em>try</em> to adapt to those via editcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '11, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7601" class="comments-container"><span id="7609"></span><div id="comment-7609" class="comment"><div id="post-7609-score" class="comment-score"></div><div class="comment-text"><p>Sure, that’s one of the most problematic parts when capturing with a normal tap (RX and TX separated without using dedicated analyzer cards)… As you all know, you always have to choose between an aggregation device (where you should bear in mind that more than 50% utilization will result in packet loss on the monitoring side) or a normal network tap (problems which were just mentioned above).</p><p>Up to you and or, to be more precisely, up to the requirement itself…</p></div><div id="comment-7609-info" class="comment-info"><span class="comment-age">(24 Nov '11, 07:38)</span> mitu</div></div></div><div id="comment-tools-7601" class="comment-tools"></div><div class="clear"></div><div id="comment-7601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


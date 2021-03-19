+++
type = "question"
title = "TLS SERVER_HELLO truncated?"
description = '''I was trying to retrieve some details on a TLS 1.2 handshake, in detail on the SERVER_HELLO. However it looks like the server sends the SERVER_HELLO message split into three TCP packets:  SERVER_HELLO packate (size 1434, no certificates) [TCP segment of reassembled PDU] (size 1434) [TCP segment of r...'''
date = "2016-11-04T03:31:00Z"
lastmod = "2016-11-04T05:57:00Z"
weight = 56975
keywords = [ "tls", "fragmentation", "dissector", "tcp" ]
aliases = [ "/questions/56975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS SERVER\_HELLO truncated?](/questions/56975/tls-server_hello-truncated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to retrieve some details on a TLS 1.2 handshake, in detail on the SERVER_HELLO.</p><p>However it looks like the server sends the SERVER_HELLO message split into three TCP packets:</p><ul><li>SERVER_HELLO packate (size 1434, no certificates)</li><li>[TCP segment of reassembled PDU] (size 1434)</li><li>[TCP segment of reassembled PDU] (size 1390)</li></ul><p>It looks like this confuses Wireshark that much so that it is only able to apply the TLS SERVER_HELLO dissector on the first packet. Therefore the data of packet 2 and 3 is inaccessible and only displayed as binary/hex data without the possibility to apply a dissector.</p><p>As TCP is a stream oriented protocol, it should not make any difference how many packets are received - how to make Wireshark work this was and see the complete SERVER-HELLO packet?</p></div><div id="question-tags" class="tags-container tags">tls fragmentation dissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/feadc214792e2581c3c750140e3eb2c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wire-Rob&#39;s gravatar image" /><p>Wire-Rob<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wire-Rob has no accepted answers">0%</span></p></div></div><div id="comments-container-56975" class="comments-container"><span id="56976"></span><div id="comment-56976" class="comment"><div id="post-56976-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p><p>Attempting to diagnose an issue from your interpretation of it is somewhat difficult.</p></div><div id="comment-56976-info" class="comment-info"><span class="comment-age">(04 Nov '16, 03:35)</span> grahamb ♦</div></div><span id="56983"></span><div id="comment-56983" class="comment"><div id="post-56983-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: How to change the IP addresses in the capture?</p></div><div id="comment-56983-info" class="comment-info"><span class="comment-age">(04 Nov '16, 08:00)</span> Wire-Rob</div></div><span id="56985"></span><div id="comment-56985" class="comment"><div id="post-56985-score" class="comment-score"></div><div class="comment-text"><p>Use an anonymiser such as <a href="https://www.tracewrangler.com/">TraceWrangler</a>.</p></div><div id="comment-56985-info" class="comment-info"><span class="comment-age">(04 Nov '16, 08:36)</span> grahamb ♦</div></div><span id="57003"></span><div id="comment-57003" class="comment"><div id="post-57003-score" class="comment-score">1</div><div class="comment-text"><p>Are you using a recent Wireshark version? Could it be related to this bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303</a></p></div><div id="comment-57003-info" class="comment-info"><span class="comment-age">(04 Nov '16, 16:47)</span> Lekensteyn</div></div><span id="57011"></span><div id="comment-57011" class="comment"><div id="post-57011-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn: Yes that sounds exactly like the problem I have. The Wireshark version I use is always the most current.</p></div><div id="comment-57011-info" class="comment-info"><span class="comment-age">(05 Nov '16, 04:54)</span> Wire-Rob</div></div></div><div id="comment-tools-56975" class="comment-tools"></div><div class="clear"></div><div id="comment-56975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56981"></span>

<div id="answer-container-56981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you'll need to look at your preference settings. Have a look at Sake's <a href="https://sharkfesteurope.wireshark.org/assets/presentations16eu/07.pdf">SSL presentation</a> given at SharkFest'16 Europe, especially slide 27.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '16, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '16, 11:07</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-56981" class="comments-container"><span id="56982"></span><div id="comment-56982" class="comment"><div id="post-56982-score" class="comment-score"></div><div class="comment-text"><p>I already have all five options as shown in the presentation: <code>ip.defragment: TRUE tcp.check_checksum: FALSE tcp.desegment_tcp_streams: TRUE ssl.desegment_ssl_records: TRUE ssl.desegment_ssl_application_data: TRUE</code></p></div><div id="comment-56982-info" class="comment-info"><span class="comment-age">(04 Nov '16, 07:57)</span> Wire-Rob</div></div></div><div id="comment-tools-56981" class="comment-tools"></div><div class="clear"></div><div id="comment-56981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


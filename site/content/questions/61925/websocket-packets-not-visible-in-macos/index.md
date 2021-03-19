+++
type = "question"
title = "WebSocket packets not visible in macOS"
description = '''WebSocket packets are not visible in Wireshark 2.2.7 in macOS Sierra but when i open the same trace file in Windows or Linux version the packets are there and visible by protocol. Is there any way to enable viewing WebSocket packets in macOS? '''
date = "2017-06-09T22:45:00Z"
lastmod = "2017-06-12T08:36:00Z"
weight = 61925
keywords = [ "websocket", "bug" ]
aliases = [ "/questions/61925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WebSocket packets not visible in macOS](/questions/61925/websocket-packets-not-visible-in-macos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61925-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WebSocket packets are not visible in Wireshark 2.2.7 in macOS Sierra but when i open the same trace file in Windows or Linux version the packets are there and visible by protocol.</p><p>Is there any way to enable viewing WebSocket packets in macOS?</p></div><div id="question-tags" class="tags-container tags">websocket bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/985c1645012b9bdbd9a2d2e9c62d0b5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milosr&#39;s gravatar image" /><p>milosr<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milosr has no accepted answers">0%</span></p></div></div><div id="comments-container-61925" class="comments-container"><span id="61932"></span><div id="comment-61932" class="comment"><div id="post-61932-score" class="comment-score"></div><div class="comment-text"><p>The dissector engine is independent of the OS. Therefore I guess it's more an issue of your preferences.</p><ul><li>Is 'Websocket' enabled ('Analyze' -&gt; 'Enabled Protocols' -&gt; 'WebSocket') on your macOS installation?</li><li>Any customized profile configured?</li></ul></div><div id="comment-61932-info" class="comment-info"><span class="comment-age">(11 Jun '17, 08:45)</span> Uli</div></div><span id="61934"></span><div id="comment-61934" class="comment"><div id="post-61934-score" class="comment-score"></div><div class="comment-text"><p>WebSocket is enabled in 'Enabled Protocols' settings, and I did a clean reinstallation to see if it has to do anything with settings but there are still no WebSocket frames visible.</p></div><div id="comment-61934-info" class="comment-info"><span class="comment-age">(11 Jun '17, 09:03)</span> milosr</div></div><span id="61935"></span><div id="comment-61935" class="comment"><div id="post-61935-score" class="comment-score"></div><div class="comment-text"><p>Can you share the pcap showing this issue?</p></div><div id="comment-61935-info" class="comment-info"><span class="comment-age">(11 Jun '17, 11:08)</span> Uli</div></div><span id="61948"></span><div id="comment-61948" class="comment"><div id="post-61948-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/file/d/0B32hB5O91KYXQVRVZk5KVDFHcTA/view?usp=sharing">https://drive.google.com/file/d/0B32hB5O91KYXQVRVZk5KVDFHcTA/view?usp=sharing</a></p><p>this is an example pcapng</p></div><div id="comment-61948-info" class="comment-info"><span class="comment-age">(12 Jun '17, 05:47)</span> milosr</div></div></div><div id="comment-tools-61925" class="comment-tools"></div><div class="clear"></div><div id="comment-61925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61952"></span>

<div id="answer-container-61952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61952-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just tested it with Wireshark 2.2.7 on macOS 10.12.5. Here WebSocket is dissected without any problem.</p><p>Therefore I still guess it's an issue of your (user) settings. A reinstallation will not remove these.</p><p>For testing you can rename your personal configuration folder (To find the location go to: Wireshark -&gt; About Wireshark -&gt; Folders) and restart Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '17, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61952" class="comments-container"><span id="61972"></span><div id="comment-61972" class="comment"><div id="post-61972-score" class="comment-score"></div><div class="comment-text"><p>I deleted the .wireshark personal folder and restarted Wireshark. It now displays the WebSocket packets.</p><p>Thank you.</p></div><div id="comment-61972-info" class="comment-info"><span class="comment-age">(12 Jun '17, 21:22)</span> milosr</div></div><span id="61975"></span><div id="comment-61975" class="comment"><div id="post-61975-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61975-info" class="comment-info"><span class="comment-age">(13 Jun '17, 00:49)</span> grahamb ♦</div></div></div><div id="comment-tools-61952" class="comment-tools"></div><div class="clear"></div><div id="comment-61952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


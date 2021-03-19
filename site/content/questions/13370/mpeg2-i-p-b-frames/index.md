+++
type = "question"
title = "MPEG2 I, P, B frames"
description = '''Hello, I use VLC to stream MPEG2 video files in MPEG TS container through UDP over LAN. I have captured packets with Wireshark and I want to ask if there is any way to identify which frames are I, P, B? Pcap files link: http://www.sendspace.com/filegroup/cuJsOSzuqIrxbGJOQolg1g'''
date = "2012-08-05T09:36:00Z"
lastmod = "2012-08-05T12:32:00Z"
weight = 13370
keywords = [ "mpeg2", "frame" ]
aliases = [ "/questions/13370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MPEG2 I, P, B frames](/questions/13370/mpeg2-i-p-b-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I use VLC to stream MPEG2 video files in MPEG TS container through UDP over LAN. I have captured packets with Wireshark and I want to ask if there is any way to identify which frames are I, P, B?</p><p>Pcap files link: <a href="http://www.sendspace.com/filegroup/cuJsOSzuqIrxbGJOQolg1g">http://www.sendspace.com/filegroup/cuJsOSzuqIrxbGJOQolg1g</a></p></div><div id="question-tags" class="tags-container tags">mpeg2 frame</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '12, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/ff5ae29c49a446662c934890fa255fb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MiniComa&#39;s gravatar image" /><p>MiniComa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MiniComa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '12, 10:41</p></div></div><div id="comments-container-13370" class="comments-container"><span id="13411"></span><div id="comment-13411" class="comment"><div id="post-13411-score" class="comment-score"></div><div class="comment-text"><p><strong><em>NOTE</em></strong>: for the pcap files link, ignore <strong><em>EVERYTHING</em></strong> that says "download" except for the "Click here to start download from sendspace" link; otherwise, it'll try to download some "download manager" program that probably won't work on anything other than Windows (as it downloads a .exe file) and that you probably don't want even on Windows.</p></div><div id="comment-13411-info" class="comment-info"><span class="comment-age">(06 Aug '12, 20:38)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-13370" class="comment-tools"></div><div class="clear"></div><div id="comment-13370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13372"></span>

<div id="answer-container-13372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13372-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use "Decode as..." on the UDP payload and select M2TP. Then use the appropriate display filter to find what you need. "mpeg-pes.frame_type" may be one of them you're seeking.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '12, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13372" class="comments-container"></div><div id="comment-tools-13372" class="comment-tools"></div><div class="clear"></div><div id="comment-13372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


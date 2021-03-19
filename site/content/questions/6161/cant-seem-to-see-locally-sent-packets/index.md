+++
type = "question"
title = "Can&#x27;t seem to see locally sent packets"
description = '''Hello I am new to WireShark and it seems really good! I have a C# client server application which is sending small packets over TCP using the TCPClient and NetworkStream objects. They are sent to 127.0.0.1 port 3000 When I analyse my main network device, I can&#x27;t seem to see the packets. I know they ...'''
date = "2011-09-07T01:30:00Z"
lastmod = "2012-03-22T13:51:00Z"
weight = 6161
keywords = [ "tcp", "wireshark" ]
aliases = [ "/questions/6161" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can't seem to see locally sent packets](/questions/6161/cant-seem-to-see-locally-sent-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6161-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I am new to WireShark and it seems really good!</p><p>I have a C# client server application which is sending small packets over TCP using the TCPClient and NetworkStream objects.</p><p>They are sent to 127.0.0.1 port 3000</p><p>When I analyse my main network device, I can't seem to see the packets. I know they are sent because the client and server respond to them.</p><p>I do though seem to get a result, but they are recorded in WireShark as SMB packets. The client and server exchange 3 packets and when I run the application, I get 3 SMB packets recorded on WireShark.</p><p>Do you know what I could be missing, or do you need some more information?</p><p>Thank you all very much for your time and help,</p><p>Richard Hughes</p></div><div id="question-tags" class="tags-container tags">tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/27dc7f4904bee24fb7259207846ba3cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rhughes&#39;s gravatar image" /><p>rhughes<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rhughes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '12, 14:20</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-6161" class="comments-container"></div><div id="comment-tools-6161" class="comment-tools"></div><div class="clear"></div><div id="comment-6161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6163"></span>

<div id="answer-container-6163" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6163-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6163" class="comments-container"><span id="6175"></span><div id="comment-6175" class="comment"><div id="post-6175-score" class="comment-score"></div><div class="comment-text"><p>Cheers, I didn't know about that.</p><p>I'll have to host the server app on a different machine as loopback network adapters on Win7 seem a bit unreliable from what I have read.</p></div><div id="comment-6175-info" class="comment-info"><span class="comment-age">(07 Sep '11, 04:35)</span> rhughes</div></div></div><div id="comment-tools-6163" class="comment-tools"></div><div class="clear"></div><div id="comment-6163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9710"></span>

<div id="answer-container-9710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9710-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can Microsoft Network Monitor capture local traffic? Or does it have he same limitation? If it can do that capture, you could export it for examination in Wirehark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-9710" class="comments-container"></div><div id="comment-tools-9710" class="comment-tools"></div><div class="clear"></div><div id="comment-9710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


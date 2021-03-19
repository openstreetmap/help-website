+++
type = "question"
title = "TCP Segment"
description = '''Hello, I am using Modbus TCP to communicate between 2 computers. On one computer I am using a program call Ignition and on the other is a program that was created in VB6. Now communications mostly work but Ignition sometimes shows Unknown under Quality and sometimes it show good under quality. I fou...'''
date = "2013-09-16T06:52:00Z"
lastmod = "2013-09-16T08:40:00Z"
weight = 24756
keywords = [ "modbus", "reassembly", "tcp" ]
aliases = [ "/questions/24756" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Segment](/questions/24756/tcp-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24756-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using Modbus TCP to communicate between 2 computers. On one computer I am using a program call Ignition and on the other is a program that was created in VB6. Now communications mostly work but Ignition sometimes shows Unknown under Quality and sometimes it show good under quality. I found in wireshark that the first packet the Vb6 sends to Ignition is good but at the end of the packet there is a 00 which wireshark is saying is "A data segment used in reassembly of a low level protocol."<br />
</p><p>Ignition then Queries and when the VB6 responds it does not show it as a Modbus/TCP Protocol but just TCP. For some reason it reassembled the last byte of the first response onto the front end of the Modbus data of this response. As shown below:</p><p>0000 <strong>00</strong> 07 65 00 00 00 09 00 03 06 00 81 00 00 03 58<br />
0010 00<br />
</p><p>Can anyone tell me why it thinks the second response need to be reassembled? Why the first responds last byte show as a TCP Segment data?</p></div><div id="question-tags" class="tags-container tags">modbus reassembly tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/aab5d39b611f672ba67bfc4df3b1b0fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hban&#39;s gravatar image" /><p>hban<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hban has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-24756" class="comments-container"><span id="24764"></span><div id="comment-24764" class="comment"><div id="post-24764-score" class="comment-score"></div><div class="comment-text"><blockquote><p>For some reason it reassembled the last byte of the first response onto the front end of the Modbus data of this response.<br />
Can anyone tell me why it thinks the second response need to be reassembled? Why the first responds last byte show as a TCP Segment data?</p></blockquote><p>I'm not sure if this is a problem related to Wireshark. It sounds like your program logic has a fault. Anyway, can you please post a capture file. We can then test what Wireshark shows and possibly are able to identify the problem.</p><p>You can post the capture file on google docs, dropbox or cloudshark.</p><p>Regards<br />
Kurt</p></div><div id="comment-24764-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:37)</span> Kurt Knochner ♦</div></div><span id="24767"></span><div id="comment-24767" class="comment"><div id="post-24767-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark?</p><p>Can you post the capture somewhere, e.g. <a href="http://cloudshark.org">Cloudshark</a> or Google Drive and share a link to it here?</p></div><div id="comment-24767-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:45)</span> grahamb ♦</div></div><span id="24769"></span><div id="comment-24769" class="comment"><div id="post-24769-score" class="comment-score"></div><div class="comment-text"><p>WireShark 1.10.2</p><p>Here is the Captured file: <a href="http://cloudshark.org/captures/60ecc9dbb7e2?filter=tcp.port%3D%3D502">Cloudshark</a></p></div><div id="comment-24769-info" class="comment-info"><span class="comment-age">(16 Sep '13, 08:08)</span> hban</div></div></div><div id="comment-tools-24756" class="comment-tools"></div><div class="clear"></div><div id="comment-24756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24772"></span>

<div id="answer-container-24772" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24772-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Modbus slave implementation is adding an extra byte of 0x00 to the responses. As TCP is a stream protocol, the dissector reads the expected bytes from the packet for the response and then treats the extra byte as the first byte of a subsequent message and tries to reassemble it.</p><p>You'll need to fix the slave implementation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-24772" class="comments-container"><span id="24778"></span><div id="comment-24778" class="comment"><div id="post-24778-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I was able to find the problem from what you suggested. Vb6 instead of creating a 15 byte array was creating a 16 byte array.</p></div><div id="comment-24778-info" class="comment-info"><span class="comment-age">(16 Sep '13, 10:38)</span> hban</div></div><span id="24803"></span><div id="comment-24803" class="comment"><div id="post-24803-score" class="comment-score"></div><div class="comment-text"><p>@hban if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-24803-info" class="comment-info"><span class="comment-age">(17 Sep '13, 03:48)</span> grahamb ♦</div></div></div><div id="comment-tools-24772" class="comment-tools"></div><div class="clear"></div><div id="comment-24772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


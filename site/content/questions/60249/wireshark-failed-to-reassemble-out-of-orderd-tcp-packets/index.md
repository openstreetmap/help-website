+++
type = "question"
title = "Wireshark failed to reassemble out of orderd TCP packets?"
description = '''I&#x27;m sending a GET request to a server and found the TCP packet contaning HTTP response is returned out of order.   As seen in the screenshot, TCP segments are reassembled to packet number 170. But that not enough to show the HTTP response in wireshark because packet 171 (and maybe the out of ordered...'''
date = "2017-03-22T01:58:00Z"
lastmod = "2017-03-23T05:03:00Z"
weight = 60249
keywords = [ "reassembly", "out-of-order", "tcp" ]
aliases = [ "/questions/60249" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark failed to reassemble out of orderd TCP packets?](/questions/60249/wireshark-failed-to-reassemble-out-of-orderd-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sending a GET request to a server and found the TCP packet contaning HTTP response is returned out of order. <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2017-03-22_at_4.36.19_PM.png" alt="Example" /></p><p>As seen in the screenshot, TCP segments are reassembled to packet number 170. But that not enough to show the HTTP response in wireshark because packet 171 (and <del>maybe</del> the out of ordered packet number 167) are also parts of the response.</p><p>I want to know</p><ol><li>if this is a bug of wireshark or the result is expected?</li><li>I want to reorder packet to make wireshark easier to analysis but It seems not possible to made it in wireshake. Is there a way to reorder the packet?</li></ol><p>Here is the captured packets: <a href="https://drive.google.com/open?id=0B26Ap_w8XFBKeXk4bWRZMTd0ZFU">captured packets</a></p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">reassembly out-of-order tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '17, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/d343af12ddfe8efca0402e070a968656?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ainopara&#39;s gravatar image" /><p>ainopara<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ainopara has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '17, 18:51</p></div></div><div id="comments-container-60249" class="comments-container"><span id="60250"></span><div id="comment-60250" class="comment"><div id="post-60250-score" class="comment-score">1</div><div class="comment-text"><p>I think you have issues further back at packet 167 that implies a TCP segment is missing, unfortunately a screenshot (as usual) doesn't give enough information to determine for certain. Can you post the capture somewhere and provide a link to it?</p></div><div id="comment-60250-info" class="comment-info"><span class="comment-age">(22 Mar '17, 03:23)</span> grahamb ♦</div></div></div><div id="comment-tools-60249" class="comment-tools"></div><div class="clear"></div><div id="comment-60249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60272"></span>

<div id="answer-container-60272" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60272-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the capture I think this could be reassembled. The packet numbers are different in the capture file provided then the image as it only includes this particular TCP stream, but inspecting gives:</p><ul><li>Packet 11 is the last 5 bytes of the response, but the sequence number (8156) indicates some data is missing.</li><li>Packet 12 is the ACK for the data sent up to and including Packet 10.</li><li>Packet 13 is an SACK for the data in packet 11 and it shows the missing data required (ACK to SLE - 1 or 5793 to 8155)</li><li>Packets 14 &amp; 15 are the missing TCP data.</li><li>Packet 16 is an SACK for packet 14 reporting the data in packet 15 is still missing.</li><li>Packet 17 is the ACK for packet 15.</li></ul><p>So it would appear that all the data is available but failed to be reassembled. Worthy of an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, attaching the capture. Might not be easy to fix though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '17, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60272" class="comments-container"><span id="60783"></span><div id="comment-60783" class="comment"><div id="post-60783-score" class="comment-score"></div><div class="comment-text"><p>For future reference, the issue was reported right here: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13517">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13517</a></p></div><div id="comment-60783-info" class="comment-info"><span class="comment-age">(12 Apr '17, 14:01)</span> Lekensteyn</div></div></div><div id="comment-tools-60272" class="comment-tools"></div><div class="clear"></div><div id="comment-60272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


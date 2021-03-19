+++
type = "question"
title = "Wireshark High Speed Data Display"
description = '''Hi, I have a requirement for a tool for continuous monitoring a 1Gbps data stream, that would allow users to also view the captured data simultaneously. I understand that Wireshark would not allow simultaneous high speed data capture and a useful display as the data would be too fast. Does anyone kn...'''
date = "2014-11-17T03:06:00Z"
lastmod = "2014-11-17T03:14:00Z"
weight = 37897
keywords = [ "high", "speed", "display" ]
aliases = [ "/questions/37897" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark High Speed Data Display](/questions/37897/wireshark-high-speed-data-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37897-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a requirement for a tool for continuous monitoring a 1Gbps data stream, that would allow users to also view the captured data simultaneously.</p><p>I understand that Wireshark would not allow simultaneous high speed data capture and a useful display as the data would be too fast.</p><p>Does anyone know of a tool that would allow data to be captured and stored to file and that could also be accessed so that a snapshot of the captured data is viewable in a UI display?</p><p>Thanks awl</p></div><div id="question-tags" class="tags-container tags">high speed display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/b6f0b9cf8fbd07c11186bdeed9f0e3a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awl&#39;s gravatar image" /><p>awl<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awl has no accepted answers">0%</span></p></div></div><div id="comments-container-37897" class="comments-container"></div><div id="comment-tools-37897" class="comment-tools"></div><div class="clear"></div><div id="comment-37897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37899"></span>

<div id="answer-container-37899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is more in the area of "Network Security Monitoring", e.g. with tools like <a href="https://www.bro.org/">Bro</a> which can automatically extract files and other content.</p><p>Anyway, a full speed 1Gbps stream is hard to monitor in realtime, because normal network cards will loose too many packets, and special capture cards cost extra money (and still the amount of data may be coming in too fast to watch it)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37899" class="comments-container"><span id="37941"></span><div id="comment-37941" class="comment"><div id="post-37941-score" class="comment-score"></div><div class="comment-text"><p>I'm assuming a 10Gbe network card with zero packet loss.</p><p>Do you know if Wireshark has the option to stream dissected packets directly to disk instead of to the display for post analysis?</p></div><div id="comment-37941-info" class="comment-info"><span class="comment-age">(18 Nov '14, 02:47)</span> awl</div></div><span id="37943"></span><div id="comment-37943" class="comment"><div id="post-37943-score" class="comment-score"></div><div class="comment-text"><p>Wireshark (or dumpcap, to be exact) always streams directly to disk, with a small memory buffer of course. Wireshark just reopens and reads the file written by dumpcap when you start a capture.</p></div><div id="comment-37943-info" class="comment-info"><span class="comment-age">(18 Nov '14, 03:26)</span> Jasper ♦♦</div></div><span id="37984"></span><div id="comment-37984" class="comment"><div id="post-37984-score" class="comment-score"></div><div class="comment-text"><p>More detail:</p><ul><li>To capture traffic, Wireshark runs a program (part of the Wireshark program suite) called dumpcap, which captures packets, writes them to a file or files, and sends messages back to Wireshark, over a pipe, as packets arrive;</li><li>Wireshark opens the file to which dumpcap is writing, reads those messages from the packet and, if a message says "N more packets have been written to the file", reads N more packets from the file and displays them.</li></ul><p>If you mean "Can I just write the packets to a file <em>without</em> displaying them?", then you can:</p><ul><li>turn off the "Update list of packets in real time" option when capturing with Wireshark - in that case, Wireshark will <em>not</em> read anything from the file until the capture is stopped, and which point it'll read the entire file;</li><li>run dumpcap as a command, or run tcpdump (which, currently, will drop fewer packets, at least on some platforms, when writing to a file) with the <code>-w</code> flag, and then, when the capture finishes, read the resulting file in Wireshark.</li></ul></div><div id="comment-37984-info" class="comment-info"><span class="comment-age">(19 Nov '14, 16:10)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-37899" class="comment-tools"></div><div class="clear"></div><div id="comment-37899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


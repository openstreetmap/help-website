+++
type = "question"
title = "How to disable tmp file in wireshark"
description = '''When starting a capture, all packets arrive in memory, but also in a temp file. The write speed to disk is probably a limiting factor on how fast wireshark can collect the data. I loose packets as soon as traffic exceeds 400Mbps on a 10 gigabit/s network card. I have a Xeon processor at 2.8Ghz and 4...'''
date = "2012-10-25T01:35:00Z"
lastmod = "2012-10-25T02:28:00Z"
weight = 15243
keywords = [ "tmpfile" ]
aliases = [ "/questions/15243" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to disable tmp file in wireshark](/questions/15243/how-to-disable-tmp-file-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15243-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When starting a capture, all packets arrive in memory, but also in a temp file. The write speed to disk is probably a limiting factor on how fast wireshark can collect the data. I loose packets as soon as traffic exceeds 400Mbps on a 10 gigabit/s network card. I have a Xeon processor at 2.8Ghz and 4GByte RAM at 1066Mhz, so I don't think the writing to RAM is the limiting factor. I would like to be able to disable writing to temp file in wireshark, to see if I still loose packets. Is there a way to do it?</p></div><div id="question-tags" class="tags-container tags">tmpfile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '12, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/779e8f2bc06faef62375ce4b04d43590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbla&#39;s gravatar image" /><p>wbla<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbla has no accepted answers">0%</span></p></div></div><div id="comments-container-15243" class="comments-container"></div><div id="comment-tools-15243" class="comment-tools"></div><div class="clear"></div><div id="comment-15243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15245"></span>

<div id="answer-container-15245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15245-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark uses dumpcap to do the capturing. This is done for security purposes, so that the &gt;2 mln lines of code executable does not need to run with elevated privileges. Dumpcap writes to a temporary file and wireshark reads from the file. So no, capturing without the use of a temporary file is not possible by design.</p><p>If you need to capture high speed networks for small amounts of time, you might want to consider using a RAM-disk for the temporary capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '12, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-15245" class="comments-container"></div><div id="comment-tools-15245" class="comment-tools"></div><div class="clear"></div><div id="comment-15245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15244"></span>

<div id="answer-container-15244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15244-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can only try to increase the buffers in the capture setup, but basically Wireshark will always write to disk as soon as it is full. Increasing the buffers can be done by selecting "Capture" -&gt; "Capture Options" -&gt; double click the NIC you use to capture -&gt; Buffer Size.</p><p>From my experience the amount of memory you can enter there depends on how much RAM you have and if it is a 32bit or 64bit OS you're running. If you increase the buffers you will most likely encounter things like the capture stop button behaving differently, because it will not react right away while there are still packets in the buffer. You'll have to observe the status bar to see if packets are still coming in.</p><p>While I do not want to rain on your parade I still think that the PC you have is probably just not fast enough for a 10G capture. 400Mbps means you're writing 50MB/s to disk, and that is the problem in most cases. A single "normal" HDD can write from 40 to lets say 100 MB/s today, with only SSDs going up to maybe 500MB/s. If your 10GBit link is 100% full you'll get 20GBit in total (10GBit RX, 10GBit TX), and that means that you'll need to be able to write about 2200MByte per second. Yes, that is 2,2 GByte/s. This is only possible with expensive PCI-e based SSD cards, and I'm not sure you want to buy one of those :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '12, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15244" class="comments-container"><span id="15246"></span><div id="comment-15246" class="comment"><div id="post-15246-score" class="comment-score"></div><div class="comment-text"><p>Thank you for this info, now it is obvious my disk write speed. I could see it by the fact that when always caturing 10 seconds and using different bitrates as traffic to capture, the filesize was always maximum 1.2 GB or even less for higher bitrates. This means 1.2GB/10 seconds = indeed the max write speed of my disk. I consider now ordering SSD disk and redo my tests.</p></div><div id="comment-15246-info" class="comment-info"><span class="comment-age">(25 Oct '12, 03:27)</span> wbla</div></div></div><div id="comment-tools-15244" class="comment-tools"></div><div class="clear"></div><div id="comment-15244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


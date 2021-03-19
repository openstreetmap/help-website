+++
type = "question"
title = "Aborting Printing Jobs [TCP Previous segment not captured] [TCP Window Full]"
description = '''Hello there, we have some Problems with three Copy/Printing Stations. After sending a Printjob with about 500 Pages, its possible that the sended printjob will abort after 200-400 Pages. Yes, on all three Stations the same. We tried so much, but we can&#x27;t locate it. We changed from Server based Print...'''
date = "2015-06-17T00:04:00Z"
lastmod = "2015-06-17T04:41:00Z"
weight = 43230
keywords = [ "windowfull", "unseen_segment" ]
aliases = [ "/questions/43230" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Aborting Printing Jobs \[TCP Previous segment not captured\] \[TCP Window Full\]](/questions/43230/aborting-printing-jobs-tcp-previous-segment-not-captured-tcp-window-full)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43230-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there, we have some Problems with three Copy/Printing Stations. After sending a Printjob with about 500 Pages, its possible that the sended printjob will abort after 200-400 Pages. Yes, on all three Stations the same. We tried so much, but we can't locate it. We changed from Server based Printing to Client-Driver based Printing with no changes to the error.</p><p>I have a Wireshark Capture, a long one, maybe someone of you can help me. It's to big for CloudShark so i put it to my DropBox Account.</p><p>Link: <a href="https://www.dropbox.com/s/fdfds8wbhc08751/Tepro_00007_20150311115524.pcap?dl=0">https://www.dropbox.com/s/fdfds8wbhc08751/Tepro_00007_20150311115524.pcap?dl=0</a></p><p>I got many errors with:</p><pre><code>1932    254.617130000   192.168.111.222 192.168.111.21  TCP 60  [TCP ACKed unseen segment] 9100→60156 [ACK] Seq=1 Ack=102277 Win=2920 Len=0
1933    254.617301000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Previous segment not captured] 60156→9100 [ACK] Seq=102277 Ack=1 Win=64240 Len=1460
1934    254.617308000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Window Full] 60156→9100 [ACK] Seq=103737 Ack=1 Win=64240 Len=1460
1935    254.677133000   192.168.111.222 192.168.111.21  TCP 60  [TCP ZeroWindow] [TCP ACKed unseen segment] 9100→60156 [ACK] Seq=1 Ack=105197 Win=0 Len=0</code></pre><p>Followed by:</p><pre><code>2066    259.098839000   192.168.111.21  192.168.111.222 TCP 1514    60242→9100 [ACK] Seq=94977 Ack=1 Win=64240 Len=1460
2067    259.137284000   192.168.111.222 192.168.111.21  TCP 60  [TCP ACKed unseen segment] 9100→60242 [ACK] Seq=1 Ack=102277 Win=2920 Len=0
2068    259.137482000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Previous segment not captured] 60242→9100 [ACK] Seq=102277 Ack=1 Win=64240 Len=1460
2069    259.137489000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Window Full] 60242→9100 [ACK] Seq=103737 Ack=1 Win=64240 Len=1460
2070    259.197319000   192.168.111.222 192.168.111.21  TCP 60  [TCP ZeroWindow] [TCP ACKed unseen segment] 9100→60242 [ACK] Seq=1 Ack=105197 Win=0 Len=0
2071    259.307009000   HewlettP_29:f7:1f   Broadcast   ARP 60  Who has 192.168.111.226?  Tell 192.168.111.173
2072    259.499433000   192.168.111.21  192.168.111.222 TCP 60  [TCP ZeroWindowProbe] 60242→9100 [ACK] Seq=105197 Ack=1 Win=64240 Len=1
2073    259.499602000   192.168.111.222 192.168.111.21  TCP 60  [TCP ZeroWindowProbeAck] [TCP ZeroWindow] 9100→60242 [ACK] Seq=1 Ack=105197 Win=0 Len=0</code></pre><p>...and just 150 Packets later the same:</p><pre><code>2216    265.537768000   192.168.111.21  192.168.111.222 TCP 1514    60271→9100 [ACK] Seq=70157 Ack=1 Win=64240 Len=1460
2217    265.537772000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Previous segment not captured] 60271→9100 [ACK] Seq=78917 Ack=1 Win=64240 Len=1460
2218    265.544039000   192.168.111.222 192.168.111.21  TCP 60  [TCP ACKed unseen segment] 9100→60271 [ACK] Seq=1 Ack=84757 Win=18980 Len=0
2219    265.544198000   192.168.111.21  192.168.111.222 TCP 1514    [TCP Previous segment not captured] 60271→9100 [ACK] Seq=84757 Ack=1 Win=64240 Len=1460
2220    265.544201000   192.168.111.21  192.168.111.222 TCP 1514    60271→9100 [ACK] Seq=86217 Ack=1 Win=64240 Len=1460</code></pre></div><div id="question-tags" class="tags-container tags">windowfull unseen_segment</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/461e8c081066983d7451275e6ac1799c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DonSeppo&#39;s gravatar image" /><p>DonSeppo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DonSeppo has no accepted answers">0%</span></p></div></div><div id="comments-container-43230" class="comments-container"></div><div id="comment-tools-43230" class="comment-tools"></div><div class="clear"></div><div id="comment-43230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43241"></span>

<div id="answer-container-43241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43241-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several streams that successfully finished the data transfer (FIN - FIN/ACK), meaning the printer accepted the full data set. The transmitted data is (almost) identical, with just a few differences at the beginning (date/time/job number).</p><p>So, if those print jobs were also aborted after 200-300 pages, I't more likely to be a problem with the printer itself (bad data format, printer internal problems, etc.) than anything on the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43241" class="comments-container"></div><div id="comment-tools-43241" class="comment-tools"></div><div class="clear"></div><div id="comment-43241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


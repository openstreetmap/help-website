+++
type = "question"
title = "My Dropbox gets into loop and cannot sync, and I find lots of &quot;ignored unknown records&quot; in WireShark trace file. Can I find the root cause from the trace?"
description = '''Hi everyone. I have found that sometimes my Dropbox will get into loop and cannot sync when I try to upload a new file. So I try to use wireshark and tcpdump to capture packets at both client and router. I observed that the Dropbox client may first open a TLS connection for transmission. But after a...'''
date = "2014-06-22T19:23:00Z"
lastmod = "2014-06-22T22:48:00Z"
weight = 34047
keywords = [ "tls", "dropbox", "retransmissions" ]
aliases = [ "/questions/34047" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [My Dropbox gets into loop and cannot sync, and I find lots of "ignored unknown records" in WireShark trace file. Can I find the root cause from the trace?](/questions/34047/my-dropbox-gets-into-loop-and-cannot-sync-and-i-find-lots-of-ignored-unknown-records-in-wireshark-trace-file-can-i-find-the-root-cause-from-the-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone.</p><p>I have found that sometimes my Dropbox will get into loop and cannot sync when I try to upload a new file. So I try to use wireshark and tcpdump to capture packets at both client and router.</p><p>I observed that the Dropbox client may first open a TLS connection for transmission. But after a period this connection was terminated and the client opens a new connection again. However the new connection is closed again after several mins and the client again opens a new connection. That seems like a "transmission loop". So I could not sync my file to server.</p><p>Moreover, I could see lots of TCP retransmission and Dup ACK in my trace file so I could infer that there exists packet loss in the Internet. I hope to reveal what leads to the disconnection of data flow? Is there a timer to manage these sync flows? Why there are so many Ignored unknown records? Would these Ignored unknown records be the root cause of TLS disconnection?</p><p>The data flows I observed were: 1. 50.17.223.173(dstIP)-6759(srcPort), 2. 50.16.184.5(dstIP)-6772(srcPort),(re-transmission) 3. 23.23.227.100(dstIP)-6807(srcPort).(re-transmission)</p><p>And here are the trace files: 1. trace at client: <a href="https://www.dropbox.com/s/s1whav7v32k3ljq/trace-client.pcap">https://www.dropbox.com/s/s1whav7v32k3ljq/trace-client.pcap</a> 2. trace at router: <a href="https://www.dropbox.com/s/t595gtfp3sx9sjh/trace-router.pcap">https://www.dropbox.com/s/t595gtfp3sx9sjh/trace-router.pcap</a></p><p>Any one could help me? Thank you very much!!!!</p></div><div id="question-tags" class="tags-container tags">tls dropbox retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '14, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/44959625f5849a8c85cdf05ca9802478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lzq8272587&#39;s gravatar image" /><p>lzq8272587<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lzq8272587 has no accepted answers">0%</span></p></div></div><div id="comments-container-34047" class="comments-container"></div><div id="comment-tools-34047" class="comment-tools"></div><div class="clear"></div><div id="comment-34047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34049"></span>

<div id="answer-container-34049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34049-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>At least one "Ignored Unknown Record" was part of an out-of-order transmission, so that might just be an artifact of Wireshark's TCP dissection code not fully handling out-of-order packet (if segment N has the beginning of a TLS record, and segment N+1 has a continuation of that record, and segment N+1 is received before segment N, Wireshark won't reassemble them). I wouldn't worry about those.</p><p>However, you do seem to be getting a lot of out-of-order packets and retransmissions, so there might be an issue with your network connection causing packets to be lost; TCP tries to recover from that by the sender "timing out" if there's no acknowledgment from the receiver and re-sending the timed-out data, but even that can't help if the network is <em>really</em> lossy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34049" class="comments-container"><span id="34050"></span><div id="comment-34050" class="comment"><div id="post-34050-score" class="comment-score"></div><div class="comment-text"><p>Hi, Harris. Thank you very much for your comment!</p><p>So the "Ignored Unknown Record" was caused by the out-of-order transmission? In my case,I tried to upload a file, and I captured the packets at the client. I still observed the "Ignored Unknown Record" in client trace. Does it mean the TCP packet is out of order when uploading at the client side?</p><p>I could understand the receiver gets a out-of-order packet. I'm not sure the packets will out-of-order before sending.</p></div><div id="comment-34050-info" class="comment-info"><span class="comment-age">(22 Jun '14, 19:46)</span> lzq8272587</div></div></div><div id="comment-tools-34049" class="comment-tools"></div><div class="clear"></div><div id="comment-34049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34051"></span>

<div id="answer-container-34051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34051-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The packet loss is <strong>not in the internet</strong>, it is between the client and the router in the outbound direction.</p><p>I would check the device at [192.168.150.1|192.168.2.165]</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_220.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-34051" class="comments-container"><span id="34052"></span><div id="comment-34052" class="comment"><div id="post-34052-score" class="comment-score"></div><div class="comment-text"><p>Hi, mrEEde:</p><p>Thank you very much for your answer.</p><p>So the packet loss is between the link between my client and router. I still have a question: why there are so many packets with "Ignored Unknown Record" in the client trace file? Is that caused by the packet loss?</p><p>I hope to analyze the trace file and find whether it is the packet loss that leads to disconnection.</p><p>BTW, how can I set the ip-id column like you?</p><p>Thanks!</p></div><div id="comment-34052-info" class="comment-info"><span class="comment-age">(22 Jun '14, 23:34)</span> lzq8272587</div></div><span id="34053"></span><div id="comment-34053" class="comment"><div id="post-34053-score" class="comment-score"></div><div class="comment-text"><p>Adding the column is easy: Select any field from the packet detail pane and right-click -&gt; Apply as Column</p></div><div id="comment-34053-info" class="comment-info"><span class="comment-age">(23 Jun '14, 00:04)</span> mrEEde</div></div><span id="34054"></span><div id="comment-34054" class="comment"><div id="post-34054-score" class="comment-score"></div><div class="comment-text"><p>If segments are seen that are missing the previous SSL record header, wireshark will not be able to reassemble those and flag them as Ignored... So this symptom is a result of lost packets</p></div><div id="comment-34054-info" class="comment-info"><span class="comment-age">(23 Jun '14, 00:06)</span> mrEEde</div></div></div><div id="comment-tools-34051" class="comment-tools"></div><div class="clear"></div><div id="comment-34051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Ack Packet With No SEQ/ACK Analysis"
description = '''Hi everyone, i am tracing some packets in wireshark and i have this problem that i found a packet that is an ack packet as the LEN = 0 and the only flag set is ack flag = 1, now usually while tracing i open an ack packet and in the TCP i select [Seq/Ack analysis] which tells me which packet this ack...'''
date = "2015-06-03T04:12:00Z"
lastmod = "2015-06-03T22:05:00Z"
weight = 42840
keywords = [ "ack", "tcp", "trace", "wireshark" ]
aliases = [ "/questions/42840" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ack Packet With No SEQ/ACK Analysis](/questions/42840/ack-packet-with-no-seqack-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42840-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, i am tracing some packets in wireshark and i have this problem that i found a packet that is an ack packet as the LEN = 0 and the only flag set is ack flag = 1, now usually while tracing i open an ack packet and in the TCP i select [Seq/Ack analysis] which tells me which packet this ack is for , now i did not find this [seq/ack analysis] and so i don't know what packet it is acknowledging even i tried to find the packet manually by calculating (seq no. + len) but i did not find it ...any help ?</p></div><div id="question-tags" class="tags-container tags">ack tcp trace wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jun '15, 04:21</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42840" class="comments-container"><span id="42852"></span><div id="comment-42852" class="comment"><div id="post-42852-score" class="comment-score"></div><div class="comment-text"><p>well, it's near to impossible to do "virtual" packet troubleshooting based on some problem descriptions ;-)</p><p>Can you please upload a small capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here?</p></div><div id="comment-42852-info" class="comment-info"><span class="comment-age">(03 Jun '15, 08:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42840" class="comment-tools"></div><div class="clear"></div><div id="comment-42840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42869"></span>

<div id="answer-container-42869" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42869-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your approach doesn't work when TCP Segmentation Offload is enabled. At a trace at the sender you see (too) large segments are leaving the host and acknowledgements are arriving that acknowledge bytes in the middle of the sent segment.<br />
In the scenario below the first ack does not have tcp.analysis.acks_frame set. So your logic only works for ACKs that match the display filter<br />
<code>tcp.len==0 and tcp[13]==10 and tcp.analysis.acks_frame</code> <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-237.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-42869" class="comments-container"><span id="43542"></span><div id="comment-43542" class="comment"><div id="post-43542-score" class="comment-score"></div><div class="comment-text"><p>so if the packet is not divided into segments i will not get this type of ack right?so how do i disable segmentation?</p></div><div id="comment-43542-info" class="comment-info"><span class="comment-age">(25 Jun '15, 06:45)</span> yas1234</div></div><span id="43544"></span><div id="comment-43544" class="comment"><div id="post-43544-score" class="comment-score"></div><div class="comment-text"><p>Depends on your operating system... <a href="http://lmgtfy.com/?q=disable+tcp+segmentation+offload">http://lmgtfy.com/?q=disable+tcp+segmentation+offload</a></p></div><div id="comment-43544-info" class="comment-info"><span class="comment-age">(25 Jun '15, 07:04)</span> mrEEde</div></div><span id="43546"></span><div id="comment-43546" class="comment"><div id="post-43546-score" class="comment-score"></div><div class="comment-text"><p>PERFECT THANK U!</p></div><div id="comment-43546-info" class="comment-info"><span class="comment-age">(25 Jun '15, 08:06)</span> yas1234</div></div><span id="43554"></span><div id="comment-43554" class="comment"><div id="post-43554-score" class="comment-score"></div><div class="comment-text"><p>If this answers your question can you please 'accept' the answer by clicking the checkmark. Thanks Matthias</p></div><div id="comment-43554-info" class="comment-info"><span class="comment-age">(25 Jun '15, 10:40)</span> mrEEde</div></div><span id="43558"></span><div id="comment-43558" class="comment"><div id="post-43558-score" class="comment-score"></div><div class="comment-text"><p>i have a small more question, now if i disable the tso ..is it a Must to disable the TX also or not? ..and what is best ? i googled that but seems like always when the tso is off the tx is off also and i do not really get what tx do .</p></div><div id="comment-43558-info" class="comment-info"><span class="comment-age">(25 Jun '15, 11:12)</span> yas1234</div></div><span id="43570"></span><div id="comment-43570" class="comment not_top_scorer"><div id="post-43570-score" class="comment-score"></div><div class="comment-text"><p>I don't know what TX means in this context but TSO has its purpose - to save CPU cycles on the Operating Systems - and many manufacturers have taken a lot of effort to make it work. The drawback is that trace analysis is a little more tricky. So if your main goal is to diagnose traffic then you may/must disable it. If your purpose is to run on an efficient TCPIP stack you leave it enabled... ;-)</p></div><div id="comment-43570-info" class="comment-info"><span class="comment-age">(25 Jun '15, 14:50)</span> mrEEde</div></div><span id="43582"></span><div id="comment-43582" class="comment not_top_scorer"><div id="post-43582-score" class="comment-score"></div><div class="comment-text"><p>actually i need to disable it but the problem now when i disabled it still my captures at the sender are not the same at the receiver, the sender is sending chunks of data and the receiver collects them into one packet then acknowledges it ,,i don't want that i want them both to match ...any help ? i attached the 2 captures <a href="https://www.dropbox.com/s/fu8zonho9wiqp9t/caps.zip?dl=0">https://www.dropbox.com/s/fu8zonho9wiqp9t/caps.zip?dl=0</a></p></div><div id="comment-43582-info" class="comment-info"><span class="comment-age">(26 Jun '15, 02:39)</span> yas1234</div></div><span id="43583"></span><div id="comment-43583" class="comment not_top_scorer"><div id="post-43583-score" class="comment-score"></div><div class="comment-text"><p>It looks like that you should try this command if you use Win2012 R2 or Win 8 netsh int tcp set global rsc=disabled Other wise you can provide the out put of the cmd: netsh int tcp show global</p></div><div id="comment-43583-info" class="comment-info"><span class="comment-age">(26 Jun '15, 03:42)</span> Christian_R</div></div><span id="43585"></span><div id="comment-43585" class="comment not_top_scorer"><div id="post-43585-score" class="comment-score"></div><div class="comment-text"><p>USING linux</p></div><div id="comment-43585-info" class="comment-info"><span class="comment-age">(26 Jun '15, 04:29)</span> yas1234</div></div><span id="43587"></span><div id="comment-43587" class="comment not_top_scorer"><div id="post-43587-score" class="comment-score"></div><div class="comment-text"><p>ethtool -K ethY lro off.<br />
where ethy is your int</p></div><div id="comment-43587-info" class="comment-info"><span class="comment-age">(26 Jun '15, 05:03)</span> Christian_R</div></div></div><div id="comment-tools-42869" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-42869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


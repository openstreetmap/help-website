+++
type = "question"
title = "Lots of retransmissions and out of order frames"
description = '''I have taken a sniffer trace today of an entry point to a NetApp SAN. Within the trace, we see an extreme amount of Out of Order frames as well as TCP retransmissions.  Since there are multiple devices talking to the SAN, how should I approach this to determine why the retrans and OOO frames are occ...'''
date = "2010-10-20T11:21:00Z"
lastmod = "2010-10-20T13:54:00Z"
weight = 562
keywords = [ "retransmissions" ]
aliases = [ "/questions/562" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Lots of retransmissions and out of order frames](/questions/562/lots-of-retransmissions-and-out-of-order-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have taken a sniffer trace today of an entry point to a NetApp SAN. Within the trace, we see an extreme amount of Out of Order frames as well as TCP retransmissions.<br />
</p><p>Since there are multiple devices talking to the SAN, how should I approach this to determine why the retrans and OOO frames are occuring?</p><p>Thank you KMNRuser</p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/9e96b23e3495316e470ba9b487b82a73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmnruser&#39;s gravatar image" /><p>kmnruser<br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmnruser has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-562" class="comments-container"></div><div id="comment-tools-562" class="comment-tools"></div><div class="clear"></div><div id="comment-562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="568"></span>

<div id="answer-container-568" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-568-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, if you're capturing a SAN (and a professional device like a NetApp solution, as opposed to low end SOHO boxes) chance are, that there were less retransmissions than you think, because your capture might have dropped lots of frames for performance reasons. In fact if you don't have a real monster as your sniffing device you will most certainly have a lot of drop outs. Those are frames that the capture device could not record because it couldn't write them fast enough before the next came in.</p><p>Wireshark looks at sequence numbers to determine out-of-orders and retransmissions, so if you have lots of drops you will get lots of those messages. A good way to determine if there really was packet loss or just a dropped packet is to look at acknowledges. If you see that a packet was not seen by Wireshark but an acknowledge for it arrives within the RTT of the connection you probably experienced a dropped packet.</p><p>If you have real retransmissions and out-of-orders you should try to determine in which direction they occur - are the packets lost on their way to the SAN or to the client? Does it affect one communication or many? What communications have the highest count of lost packets (easy to determine: filter on <em>tcp.analysis.lost_segment</em>, open <em>Statistics/Conversations</em>, select TCP tab and check "limit to display filter", then sort by packets).</p><p>Ususally (if there are no capture drops) my money is on the typical situation where the SAN attached to a Gigabit (or 10G) Line is transmitting lots of data towards a client on a 100MBit link, resulting in massive congestion of the poor access switch that has to break the 1G/10G line down to 100MBit and gets slammed by the sheer amount of data the SAN fires at it. Meaning: packet loss towards the client, often at a ratio of 60-90%.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-568" class="comments-container"></div><div id="comment-tools-568" class="comment-tools"></div><div class="clear"></div><div id="comment-568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="569"></span>

<div id="answer-container-569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-569-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did this just start happening? Were there any changes made to your network? Are the retransmissions happening with all of the IP addresses communicating with the SAN, or just a few. I would try to isolate where the problem is in terms of a switch or router. That is, are the devices that are serving the storage on the same switch as the SAN, or are there different switches involved?</p><p>It could be something simple, such as a NIC in the SAN not connected at the proper duplex and speed, a bad NIC in the SAN, a bad switch port, bad switch, or a switch that needs to be rebooted. Do you have a diagram of your network so you can start looking for components that are common to the devices that are experiencing the retransmissions?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/92cb33f82f0bb99520a22ac7a9e33ef2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robert%20obrinsky&#39;s gravatar image" /><p>robert obrinsky<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robert obrinsky has no accepted answers">0%</span></p></div></div><div id="comments-container-569" class="comments-container"></div><div id="comment-tools-569" class="comment-tools"></div><div class="clear"></div><div id="comment-569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


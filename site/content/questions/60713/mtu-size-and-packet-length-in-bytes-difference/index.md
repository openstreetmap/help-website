+++
type = "question"
title = "MTU size and packet length in bytes difference"
description = '''What exactly is the difference between TCP packet length in bytes and MTU size?? Is it OK to have to have TCP packet length in bytes higher (for example: 1845) than MTU size (1500) when we see it in Wireshark trace? '''
date = "2017-04-10T15:04:00Z"
lastmod = "2017-04-10T15:25:00Z"
weight = 60713
keywords = [ "congestion", "wireshark", "tcp", "mtu" ]
aliases = [ "/questions/60713" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MTU size and packet length in bytes difference](/questions/60713/mtu-size-and-packet-length-in-bytes-difference)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What exactly is the difference between TCP packet length in bytes and MTU size?? Is it OK to have to have TCP packet length in bytes higher (for example: 1845) than MTU size (1500) when we see it in Wireshark trace?</p></div><div id="question-tags" class="tags-container tags">congestion wireshark tcp mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '17, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div></div><div id="comments-container-60713" class="comments-container"></div><div id="comment-tools-60713" class="comment-tools"></div><div class="clear"></div><div id="comment-60713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60714"></span>

<div id="answer-container-60714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60714-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP length must stay equal or below MTU minus the IP and TCP header size. E.g. if the MTU is 1500, the TCP length should be less or equal to 1460, (MTU 1500 - 20 Bytes IP header - 20 Bytes TCP header).</p><p>If you see packets with higher length (e.g. 1845) it could be a problem, but most likely it's measurement error. See <a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '17, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60714" class="comments-container"><span id="60715"></span><div id="comment-60715" class="comment"><div id="post-60715-score" class="comment-score"></div><div class="comment-text"><p>Jasper, but to keep the TCP packet lengths equal or below MTU size, we have to turn the TCP segmentation feature OFF. However, the problem when we do that is that we can not utilize the maximum bandwidth. For example: the performance for a 1gbps - we get around 370mbps - which i think is so poor. This got me confused.</p></div><div id="comment-60715-info" class="comment-info"><span class="comment-age">(10 Apr '17, 15:23)</span> armodes</div></div><span id="60717"></span><div id="comment-60717" class="comment"><div id="post-60717-score" class="comment-score">1</div><div class="comment-text"><p>No, that's not true. The segmentation feature puts the task of segmenting packets on the card, not the CPU, so if you do a local capture it shows incorrect values. On the wire it's <strong>always correct</strong>. Which is why you need to start capturing with a SPAN port or a TAP. That's the only way to see the real packets.</p></div><div id="comment-60717-info" class="comment-info"><span class="comment-age">(10 Apr '17, 15:26)</span> Jasper ♦♦</div></div><span id="60718"></span><div id="comment-60718" class="comment"><div id="post-60718-score" class="comment-score"></div><div class="comment-text"><p>OK. I am doing all this on a virtual environment and capturing the traffic on the monitor (between the sender and the receiver). I don't have that physical switch in place now, is there any way to do it on a virtual environment?</p></div><div id="comment-60718-info" class="comment-info"><span class="comment-age">(10 Apr '17, 15:33)</span> armodes</div></div><span id="60720"></span><div id="comment-60720" class="comment"><div id="post-60720-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure, maybe if the monitor device is in bridge mode. But speed tests in that kind of environment are generally not very reliable, so if you're trying to prove you can get maximum bandwidth it's usually much better to do it on a physical link.</p></div><div id="comment-60720-info" class="comment-info"><span class="comment-age">(10 Apr '17, 15:38)</span> Jasper ♦♦</div></div></div><div id="comment-tools-60714" class="comment-tools"></div><div class="clear"></div><div id="comment-60714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60716"></span>

<div id="answer-container-60716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60716-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The most common situation where I see TCP length larger than the MTU is when Wireshark is being run on the sending system, TCP Segmentation Offloading is being used, and Wireshark captures the outgoing packets before the NIC card has actually packetized them. If this interferes with the analysis you can either disable the Segmentation Offloading (often not possible), or capture from the network via a SPAN port or a tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '17, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/a446b2537577b08421cfd0c9b544b19e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djdawson&#39;s gravatar image" /><p>djdawson<br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djdawson has one accepted answer">25%</span></p></div></div><div id="comments-container-60716" class="comments-container"></div><div id="comment-tools-60716" class="comment-tools"></div><div class="clear"></div><div id="comment-60716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


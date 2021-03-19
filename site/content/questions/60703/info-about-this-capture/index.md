+++
type = "question"
title = "info about this capture"
description = '''Hello guys, i&#x27;m pretty new to capture analysis and i&#x27;m asking you some help with this capture. I&#x27;m testing a 4g modem that should reach ~40mbps, actually it makes 1. So i tried a few test i noted that: -tcp connection have 1mbps -upd connection makes a lot more so i&#x27;ve started to think to a tcp prob...'''
date = "2017-04-10T06:49:00Z"
lastmod = "2017-04-10T17:58:00Z"
weight = 60703
keywords = [ "packetloss", "congestion-avoidance", "slow-start", "tcp", "wireshark" ]
aliases = [ "/questions/60703" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [info about this capture](/questions/60703/info-about-this-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60703-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys, i'm pretty new to capture analysis and i'm asking you some help with this capture. I'm testing a 4g modem that should reach ~40mbps, actually it makes 1. So i tried a few test i noted that: -tcp connection have 1mbps -upd connection makes a lot more</p><p>so i've started to think to a tcp problem... but i can not understand wich one is the root cause :( I'm attacching 2 capture file tcp/upd</p><p>thx in advance, andre</p><p><a href="http://www.filedropper.com/tcp-sim">http://www.filedropper.com/tcp-sim</a></p></div><div id="question-tags" class="tags-container tags">packetloss congestion-avoidance slow-start tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '17, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/d0de720079c9988c01f4a1204c16df8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ancestrale012&#39;s gravatar image" /><p>ancestrale012<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ancestrale012 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 10 Apr '17, 18:05</p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p>Philst<br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span></p></div></div><div id="comments-container-60703" class="comments-container"></div><div id="comment-tools-60703" class="comment-tools"></div><div class="clear"></div><div id="comment-60703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60724"></span>

<div id="answer-container-60724" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60724-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your reduced throughput rate is due to TCP's "Congestion Avoidance" mechanism. The sender will halve its Transmit Window in response to observed packet losses.</p><p>In your TCP capture (I couldn't find your UDP file), the sender's "Slow Start" ramps up to 74 packets "in flight" after about 700 ms. But then there is a packet loss (packet #109 goes missing after we've seen it in the trace), SACK (#212) and retransmission (#214). Packets #157, #241 and #245 repeat that pattern.</p><p>On seeing that losses happened, the sender halves its Transmit Window to 34 segments per round trip and ramps up this rate linearly (35 next RT, 36 next RT, etc.) This has the effect of halving the overall throughput and increasing it very slowly.</p><p>Just as we've ramped up to 44 S/RT, packet #696 gets lost and the throughput again halves to 22 S/RT.</p><p>We get three more "halvings" - dropping to 10 S/RT due to the loss of #1130. We get to 42 S/RT when #2295 is lost (retrans = #2357) halving again to 21 S/RT. We only ramp up to 31 at the end of the transfer (terminated with a Reset).</p><p>The server's Receive Window is 627,584 bytes for the almost the whole transfer.</p><p>Your problem is that the sender can't fill that receive window because of the frequent Transmit Window reductions. That is, due to the lost packets in the flow (which all occur after the capture point).</p><p>This TCP Stream chart shows the transition from "Slow Start" to "Congestion Avoidance" mode. The yellow packets are the retransmissions of the "lost" packets.</p><p>Note the slope of the packets changing to the reduced rate. If you view the flows later in the trace, you'll be able to see the other "halvings".</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCP-SIM.PNG" alt="alt text" /></p><p>See my answer to <a href="https://ask.wireshark.org/questions/55972/slow-writes-even-slower-reads-spanning-wan-to-netapp">Question #55972</a> for similar behaviour.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '17, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p>Philst<br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '17, 18:03</p></div></div><div id="comments-container-60724" class="comments-container"><span id="60743"></span><div id="comment-60743" class="comment"><div id="post-60743-score" class="comment-score"></div><div class="comment-text"><p>Hello Philst, thx a lot man! you're awsome! it have been a great exaplanation!</p><p>May i just add 1 more question? i would like to understand wich one is the cause of the packet loss, it is possbile?</p><p>thx again! Andrea</p></div><div id="comment-60743-info" class="comment-info"><span class="comment-age">(11 Apr '17, 08:48)</span> ancestrale012</div></div><span id="60746"></span><div id="comment-60746" class="comment"><div id="post-60746-score" class="comment-score"></div><div class="comment-text"><p>@ancestrale012</p><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-60746-info" class="comment-info"><span class="comment-age">(11 Apr '17, 11:04)</span> grahamb ♦</div></div><span id="60754"></span><div id="comment-60754" class="comment"><div id="post-60754-score" class="comment-score"></div><div class="comment-text"><p>Thanks Andrea, there doesn't seem to be any particular pattern to the losses. They occur at the start, middle and end of packet bursts (if they were always at the end of a burst, we might look for router buffer overflows).</p><p>All we can say is that they all happen after the capture point. That is, we see all the packets in the trace, but they must go missing sometime "downstream" because the receiver sends us SACKs indicating that they weren't received.</p><p>We can also say that they only get lost one at a time (not in groups).</p><p>Out of the total 2,754 packets in that connection (includes ACKs) there are 8 missing data packets.</p><p>Unfortunately then, there's no further clue as to where they are going missing.</p><p>The only real way to find the loss point is to take captures at various places along the path and see which traces they are missing from.</p><p>You could also check switch counters to see if they happen to be counted as "dropped" somewhere.</p></div><div id="comment-60754-info" class="comment-info"><span class="comment-age">(11 Apr '17, 18:43)</span> Philst</div></div></div><div id="comment-tools-60724" class="comment-tools"></div><div class="clear"></div><div id="comment-60724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


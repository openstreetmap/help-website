+++
type = "question"
title = "Packet missing issue at peak of network flow in dumpcap."
description = '''Hi all, I have used dumpcap.exe for dumping the VOIP traffic to the disc. And it is showing packet dropped on network as 0 when it stops. But with testing a sip call there i found some packets missed in the dumped files in Wireshark. The dumpcap command used is below, and the ethernet card speed is ...'''
date = "2013-12-25T21:04:00Z"
lastmod = "2013-12-26T00:45:00Z"
weight = 28392
keywords = [ "dumpcap" ]
aliases = [ "/questions/28392" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet missing issue at peak of network flow in dumpcap.](/questions/28392/packet-missing-issue-at-peak-of-network-flow-in-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28392-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have used dumpcap.exe for dumping the VOIP traffic to the disc. And it is showing packet dropped on network as 0 when it stops. But with testing a sip call there i found some packets missed in the dumped files in Wireshark.</p><p>The dumpcap command used is below, and the ethernet card speed is 1Gbps.</p><pre><code>dumpcap.exe -a files:1000000000 -b filesize:3024 -i 1 -B 10240  -P -s 0 -w e:\Packets\h -f &quot;(host xx.xx.xx.xx) &amp;&amp; (tcp||udp)&quot;</code></pre><p>Can someone please help me on this.</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Dec '13, 21:04</strong></p><img src="https://secure.gravatar.com/avatar/215d9378b10901b1233ef89a5d7cd496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binu%20Babu&#39;s gravatar image" /><p>Binu Babu<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binu Babu has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Dec '13, 21:49</p></div></div><div id="comments-container-28392" class="comments-container"><span id="28432"></span><div id="comment-28432" class="comment"><div id="post-28432-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But with testing a sip call there i found some packets missed in the dumped files in Wireshark.</p></blockquote><p>how do you know that there are some packets missing? Do you have a second capture file (taken at a different location) to compare with?</p></div><div id="comment-28432-info" class="comment-info"><span class="comment-age">(27 Dec '13, 04:21)</span> Kurt Knochner ♦</div></div><span id="28433"></span><div id="comment-28433" class="comment"><div id="post-28433-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner yes i have Palladion call monitor interface to compare. There i could find the missed packet with same sip CallID.</p></div><div id="comment-28433-info" class="comment-info"><span class="comment-age">(27 Dec '13, 05:04)</span> Binu Babu</div></div><span id="28437"></span><div id="comment-28437" class="comment"><div id="post-28437-score" class="comment-score"></div><div class="comment-text"><p>O.K. there are several things to consider</p><ul><li>there are really lost frames. As dumpcap does not show them, they must have been lost before dumpcap received the traffic (see answer of @Jasper). Then you need to figure out where the frames got lost. As you did not say where you have taken the capture file, I would suggest to capture at a different location (switch span port) to compare the results. Your capture filter should have reduced the amount of traffic well enough to not overload dumpcap. However I don't know the amount of SIP traffic in your network</li><li>Palladion call monitor is showing the wrong things (SIP calls) or the right things for the wrong time period (wrong time setting somewhere) and thus you believe there should be SIP traffic in the capture file during a certain time interval, whereas there is nothing and Wireshark is right.</li></ul></div><div id="comment-28437-info" class="comment-info"><span class="comment-age">(27 Dec '13, 05:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28392" class="comment-tools"></div><div class="clear"></div><div id="comment-28392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28397"></span>

<div id="answer-container-28397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28397-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet drop can occur before dumpcap even sees the packet. Depending on your capture setup you may have drops on a SPAN port, NIC driver level, OS level and maybe a couple of other places. So if dumpcap says it has zero dropped frames it only means that dumpcap didn't drop any packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Dec '13, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28397" class="comments-container"><span id="28399"></span><div id="comment-28399" class="comment"><div id="post-28399-score" class="comment-score"></div><div class="comment-text"><p>@Jasper thank you for the reply. Is there any way to check where the drop exists ?</p></div><div id="comment-28399-info" class="comment-info"><span class="comment-age">(26 Dec '13, 01:09)</span> Binu Babu</div></div><span id="28400"></span><div id="comment-28400" class="comment"><div id="post-28400-score" class="comment-score"></div><div class="comment-text"><p>It may be possible to see something like this on the switch for the SPAN session (interface statistics), but I don't think it's possible for the others.</p></div><div id="comment-28400-info" class="comment-info"><span class="comment-age">(26 Dec '13, 01:17)</span> Jasper ♦♦</div></div><span id="28444"></span><div id="comment-28444" class="comment"><div id="post-28444-score" class="comment-score"></div><div class="comment-text"><p>-B is set to high.</p><p>-B &lt;buffer size=""&gt; size of kernel buffer in MiB (def: 2MiB)</p><p>filesize:3024 seems very small to me.</p><p>What does top show when capturing?</p></div><div id="comment-28444-info" class="comment-info"><span class="comment-age">(27 Dec '13, 08:23)</span> Anders ♦</div></div><span id="28446"></span><div id="comment-28446" class="comment"><div id="post-28446-score" class="comment-score"></div><div class="comment-text"><p>If the parameter for -B is set too high, the following will happen (dumpcap 1.10.x and 1.11.x).</p><pre><code>dumpcap: Couldn&#39;t set the capture buffer size!
The capture buffer size of 10240MB seems to be too high for your machine, the default of 1MB will be used.</code></pre><p>I see two 'problems'</p><ul><li>A mismatch between the usage text of <code>dumpcap -h</code> (default 2MB) versus the error message (default 1MB)</li><li>dumpcap might have used another buffer size (1 or 2 MB) than the user expected, because he/she did not realize the error message (if there was one on his/her system)</li></ul></div><div id="comment-28446-info" class="comment-info"><span class="comment-age">(27 Dec '13, 08:28)</span> Kurt Knochner ♦</div></div><span id="28612"></span><div id="comment-28612" class="comment"><div id="post-28612-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner : Thank you for the information, i will try with amending the buffer settings.</p></div><div id="comment-28612-info" class="comment-info"><span class="comment-age">(07 Jan '14, 00:07)</span> Binu Babu</div></div></div><div id="comment-tools-28397" class="comment-tools"></div><div class="clear"></div><div id="comment-28397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


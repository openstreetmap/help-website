+++
type = "question"
title = "Why are packets from one TCP stream not being captured on Lenovo, but working on an HP?"
description = '''Hi, When using the same SPAN session OR when installing a hub between a local server and switch, Wireshark does not display packets from one remote server on a Lenovo T400 or an HP Elitebook 8460P, but it does display on a different model HP laptop. The missing packets are only from one remote serve...'''
date = "2012-07-25T05:00:00Z"
lastmod = "2012-07-26T11:14:00Z"
weight = 12984
keywords = [ "lenovo", "missing" ]
aliases = [ "/questions/12984" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Why are packets from one TCP stream not being captured on Lenovo, but working on an HP?](/questions/12984/why-are-packets-from-one-tcp-stream-not-being-captured-on-lenovo-but-working-on-an-hp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, When using the same SPAN session OR when installing a hub between a local server and switch, Wireshark does not display packets from one remote server on a Lenovo T400 or an HP Elitebook 8460P, but it does display on a different model HP laptop. The missing packets are only from one remote server. Packets from different remote servers show in Wireshark.</p><p>The flow is TCP based on server port 5030 (it's a retail point of sale application.)</p><p>We have a NetScout deployment at our data center and are able to confirm that the return packets from the remote server are flowing. We have also run what's called an "Enhanced LAN Trace" on the local server and know the packets are getting to the server.</p><p>Wireshark simply does not display any packets from this one particular remote server on multiple Lenovo T400 laptops (as well the HP Elitebook 8460P).</p><p>There are no filters configured (capture or display.)</p><p>During the TCP 3 way handshake I see the SYN and ACK from the local server, but never the SYN,ACK from the remote server. Wireshark also does not complain of the missing packets for this TCP stream(?)</p><p>I'm not sure where to turn. NIC Drivers? Wireshark configuration?</p><p>I have also tried TSHARK and get the same result.</p><p>Thx!</p></div><div id="question-tags" class="tags-container tags">lenovo missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '12, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/6f841922afda6f17b3116db6bcb00dac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mik%20Willy&#39;s gravatar image" /><p>Mik Willy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mik Willy has no accepted answers">0%</span></p></div></div><div id="comments-container-12984" class="comments-container"></div><div id="comment-tools-12984" class="comment-tools"></div><div class="clear"></div><div id="comment-12984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12995"></span>

<div id="answer-container-12995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12995-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The frames captured by the HP that works, should identify if they are VLAN tagged or not (assuming it does not strip the VLAN header itself).</p><p>Most Lenovos using the Intel LM825XXX series NIC require either a MonitorMode or a MonitorModeEnabled DWORD to be added to the registry and set to a value of 1. Try searching the registry for a "DriverDesc" entry that is set to the NIC. Normally if not set, all this would do is strip off the VLAN header, not drop the packet.</p><p>If you put the Lenovo on some different SPAN, do they see both directions of the expected traffic?</p><p>What firewall are you running, some need to be turned off before you will see all traffic?</p><p>I use a Lenovo T420 on Windows 7 &amp; once the MonitorMode was set to 1 in the registry, everything works fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '12, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p>KeithFrench<br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-12995" class="comments-container"><span id="12997"></span><div id="comment-12997" class="comment"><div id="post-12997-score" class="comment-score"></div><div class="comment-text"><p>good hint!</p><blockquote><p><code>http://www.intel.com/support/network/sb/cs-005897.htm</code><br />
</p></blockquote><p>Maybe the packets are "damaged" (bad crc or something) and the driver drops them without MonitorMode.</p></div><div id="comment-12997-info" class="comment-info"><span class="comment-age">(25 Jul '12, 11:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12995" class="comment-tools"></div><div class="clear"></div><div id="comment-12995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12985"></span>

<div id="answer-container-12985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12985-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and Tshark both use WinPcap to capture the packets, so indeed the results should be the same. As you noticed too.</p><p>One thing that might cause differences is the encapsulation of some packets (vlan tagged or not for instance), but that mostly will only effect which packets are captured when you <strong>do</strong> filter. And you're not filtering.</p><p>There are a lot of pieces of software that can interfere with the capture process in many different ways. VPN clients and personal firewalls are the most notorious ones. Have a look at <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">http://wiki.wireshark.org/CaptureSetup/InterferingSoftware</a> for more details.</p><p>If that does not help, could you please add a comment to your question with more details on the the laptops, the NICs, the NIC driver versions and NIC configuration?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '12, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-12985" class="comments-container"><span id="12986"></span><div id="comment-12986" class="comment"><div id="post-12986-score" class="comment-score"></div><div class="comment-text"><p>Actually, my bet is that the frames ARE VLAN tagged. IBM (and now Lenovo) laptops have a long history of stubbornly ignoring VLAN tagged frames (capture filter or not), no matter what you try to convince the NIC to accept them...</p></div><div id="comment-12986-info" class="comment-info"><span class="comment-age">(25 Jul '12, 05:57)</span> Jasper ♦♦</div></div><span id="12987"></span><div id="comment-12987" class="comment"><div id="post-12987-score" class="comment-score"></div><div class="comment-text"><p>Ah, one learns every day, thank you for the addition @Jasper!</p></div><div id="comment-12987-info" class="comment-info"><span class="comment-age">(25 Jul '12, 06:13)</span> SYN-bit ♦♦</div></div><span id="12994"></span><div id="comment-12994" class="comment"><div id="post-12994-score" class="comment-score"></div><div class="comment-text"><blockquote><p>IBM (and now Lenovo) laptops have a long history of stubbornly ignoring VLAN tagged frames (capture filter or not), no matter what you try to convince the NIC to accept them</p></blockquote><p>Hm.. if the VLAN tagged frames are dropped, the local application would not see the SYN-ACK and thus there would be no ACK.</p><p>I guess it's a kind of interfering software that keeps WinPcap from capturing the packets, especially because it works on one HP Laptop and not on another HP laptop. Possible difference: Software on that laptop (besides NIC driver)</p><p>Forget what I said ;-) He is capturing on a SPAN port not on the server itself.</p></div><div id="comment-12994-info" class="comment-info"><span class="comment-age">(25 Jul '12, 09:20)</span> Kurt Knochner ♦</div></div><span id="13014"></span><div id="comment-13014" class="comment"><div id="post-13014-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback.</p><p>The frames are not VLAN tagged. I did have to modify the MonitorModeEnabled DWORD value to 1 about a year ago to see DOT1Q headers on another issue I was working on. It did work for me.</p><p>I have at least isolated that it's not the hardware. If I boot my T400 under Backtrack Linux and run Wireshark I am able to see the complete conversation (i.e. the SYN, ACK from the remote server.) I now know to focus my effort within Windows 7 and all the apps. I may next run Win7 in safe mode with networking enabled and see what result I get.</p><p>I am running an Intel 82567LM Gigabit Network adapter. The driver is Intel v10.1.14.0 dated 7/20/2011.</p></div><div id="comment-13014-info" class="comment-info"><span class="comment-age">(26 Jul '12, 04:34)</span> Mik Willy</div></div></div><div id="comment-tools-12985" class="comment-tools"></div><div class="clear"></div><div id="comment-12985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13033"></span>

<div id="answer-container-13033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13033-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What happens if you turn your firewall off?</p><p>Another thing, are you sure that you do not have an existing capture or display filter in place that is filtering that direction out?</p><p>From V1.8.0, the capture filters are sort of hidden. You have to double click on an interface in the Capture options, to see the capture filters. This allows different filters to be applied to different NICs when capturing on multiple interfaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p>KeithFrench<br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-13033" class="comments-container"></div><div id="comment-tools-13033" class="comment-tools"></div><div class="clear"></div><div id="comment-13033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


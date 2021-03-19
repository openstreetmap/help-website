+++
type = "question"
title = "Excessive &quot;TCP Out-of-Order&quot; Messages"
description = '''PROBLEM DEFINITION: Conversations between Server1 and Server2 are fraught with &quot;TCP Out-of-Order&quot; messages. Server1 is in VLAN X while Server 2 is in VLAN Y. I run Wireshark from a laptop connected to a switchport upon which SPAN is enabled.  PRLBLEM ENVIRNOMENT:  All three devices (Server1, Server2...'''
date = "2010-10-25T14:13:00Z"
lastmod = "2010-11-10T15:12:00Z"
weight = 632
keywords = [ "messages", "excessive", "out-of-order", "tcp" ]
aliases = [ "/questions/632" ]
osqa_answers = 8
osqa_accepted = false
+++

<div class="headNormal">

# [Excessive "TCP Out-of-Order" Messages](/questions/632/excessive-tcp-out-of-order-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-632-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>PROBLEM DEFINITION:</strong></p><p>Conversations between Server1 and Server2 are fraught with "TCP Out-of-Order" messages. Server1 is in VLAN X while Server 2 is in VLAN Y. I run Wireshark from a laptop connected to a switchport upon which SPAN is enabled.<br />
</p><p><strong>PRLBLEM ENVIRNOMENT:</strong></p><ol><li>All three devices (Server1, Server2, and WireShark laptop) are connected to a Cisco 6509 switch.</li><li>Communications between Server1 and Server2 traverse a firewall services module (FWSM) on the Cisco 6509.</li><li>Server1 is an application server while Server2 is a SQL server.</li></ol><p><strong>OBSERVATIONS:</strong></p><ol><li>When I run Wireshark from Server1 (instead of the laptop), I do not receive the Out-of-Order messages.</li><li>When I move Server 1 into VLAN Y (so that Server1 and Server2 are in the same VLAN/subnet), and then run Wireshark from the laptop, I do not receive the Out-of-Order messages.</li></ol><p>I have upgraded the FWSM on the Cisco 6509 to no avail. Does anyone have any thoughts/suggestions/feedback? I have been troubleshooting this issue for over a week and have ordered the <strong><em>Wireshark Network Analysis</em></strong> book from Amazon to further my research of this issue. Book has not arrived yet and so I'm sending this plea for help!</p></div><div id="question-tags" class="tags-container tags">messages excessive out-of-order tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-632" class="comments-container"></div><div id="comment-tools-632" class="comment-tools"></div><div class="clear"></div><div id="comment-632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

8 Answers:

</div>

</div>

<span id="646"></span>

<div id="answer-container-646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-646-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Until the book gets there...</p><p>(FYI - I always check to see if the packets are truly out-of-order as some Cisco boxes duplicate the packets when spanning is enabled - since you don't see the condition when you move Server 1 to VLAN Y, then we have to assume this is not the issue and they truly are out-of-order. Always good to check though. Honestly, I'd rather see you have a full-duplex tap in front of each of the servers rather than rely on the span information.)</p><p>Your observations seem to indicate that the condition occurs when crossing from one VLAN to another VLAN. Got any load balancing set up along the path(s)? Any packet expediting?</p><p>There's an interesting write-up about troubleshooting FWSM performance at http://isamology.blogspot.com/2010/02/troubleshooting-fwsm-performance.html. Out-of-order packet issues are addressed in that article. My finger would be pointing at the FWSM as it does all sorts of freaky things to TCP traffic (see the Wireshark Tip #47 about 4 NOPS at http://www.wiresharktraining.com/tips-41-60.html.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-646" class="comments-container"></div><div id="comment-tools-646" class="comment-tools"></div><div class="clear"></div><div id="comment-646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="702"></span>

<div id="answer-container-702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-702-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'll second the vote on FWSM doing screwy things with packets. Is the 6500 also routing between the VLANS, or are you doing inter-VLAN routing on another device? Are you SPANning on the trusted or untrusted side of the FWSM? Does Server1 have a super-duper NIC that handles buffering and pre-processing of packets? I agree that a TAP will let you see exactly what's going down the wire. SPANs are red-headed step children from a switch processing priority point of view.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-702" class="comments-container"><span id="743"></span><div id="comment-743" class="comment"><div id="post-743-score" class="comment-score"></div><div class="comment-text"><p>Hey! What's wrong with red-heads? &lt;g&gt; Just kidding. You know no matter how much I scream to use a tap rather than span it doesn't seem to get across... sigh.</p></div><div id="comment-743-info" class="comment-info"><span class="comment-age">(29 Oct '10, 22:55)</span> lchappell ♦</div></div></div><div id="comment-tools-702" class="comment-tools"></div><div class="clear"></div><div id="comment-702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="768"></span>

<div id="answer-container-768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-768-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You didn't tell us how you're actually spanning on the switch. Hopefully, you didn't span the entire VLAN and chose to span the incoming or exiting port (not the bump in the wire vlan for the FW module).<br />
</p><p>The way to tell is by looking at the IP ID field. See if you see duplicate IDs. Are they the same? If so it's nothing more than duplicate packets causing Wireshark grief. You can use "editcap -d origfile newfile" to get rid of duplicates. This assumes that IP, MAC, or VLAN headers are the same.</p><p>When you have a "MASSIVE...." amount of OO packets, it's rarely as bad as it seems. Check for the duplicate IP ID.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '10, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-768" class="comments-container"><span id="2077"></span><div id="comment-2077" class="comment"><div id="post-2077-score" class="comment-score"></div><div class="comment-text"><p>Hello hansangb</p><p>I am having a very similar problem to what is being discussed in this thread, in that some of the traffic off of the client SAN is loaded with OOO frames, as well as Dup Ack's, a few retransmissions here and there.<br />
I dug into a trace a minute ago after reading your response, and what i see repeatedly is an ID field of all zero's on the OOO frames. What does this mean? thx...</p><p>Oh and by the way, the issue is that devices on the SAN are intermittently disconnecting. The SAN configuration has ESX hardware that connects to a SAN to get to its VMDK's and its storage.</p></div><div id="comment-2077-info" class="comment-info"><span class="comment-age">(01 Feb '11, 11:02)</span> kmnruser</div></div></div><div id="comment-tools-768" class="comment-tools"></div><div class="clear"></div><div id="comment-768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="659"></span>

<div id="answer-container-659" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-659-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Laura,</p><p>Thank you very much for your response. I will thoroughly investigate the articles you referenced and aggressively pursue them. I have already implemented the <strong><em>sysoption np completion-unit</em></strong> command has early in my troubleshooting effort.</p><p>In the meantime, I have one follow-up question: how do you explain that the condition does not manifest when I capture packets from Server 1 instead of the laptop connected to a span port? In other words, with everything being the same (each server is in its own VLAN), I simply change the packet collection point from a third party (laptop) to the Server 1 itself. When I do this, I no longer receive the Out-of-Order condition.</p><p>I have lost sleep over this issue and, along the way, I have been inspired to pursue the Wireshark Network Analyst certification as a result. Thank you very much Laura.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-659" class="comments-container"></div><div id="comment-tools-659" class="comment-tools"></div><div class="clear"></div><div id="comment-659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="661"></span>

<div id="answer-container-661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-661-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's what I see in my head (correct me if I am wrong).</p><ul><li>Scenario 1: Capture on Server 1 in VLAN X - no OoOs (Out-of-Orders)</li><li><strong>Scenario 2: Capture on laptop (spanned port) Server 1 in VLAN X - OoOs</strong></li><li>Scenario 3: Capture on laptop (spanned port) Server 1 in VLAN Y - no OoOs</li></ul><p>My experience with port spanning has yielded such crappy results in the past because of poor implementations by the switch vendors, that I just don't trust it. Can you get a tap in there? It would be good to know what's REALLY crossing the network rather than relying on the switch to forward traffic down a switch port.</p><p>What is the main issue though? Are you seeing performance issues? Is the communication slower/faster when you move Server 1 to VLAN Y?</p><p>I can look at a trace if you'd like. Take a deep breath... get some sleep and hang in there!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-661" class="comments-container"></div><div id="comment-tools-661" class="comment-tools"></div><div class="clear"></div><div id="comment-661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="680"></span>

<div id="answer-container-680" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-680-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Laura,</p><p>You are correct on the two scenarios: Scenario 1: Capture on Server 1 in VLAN X - no OoOs (Out-of-Orders) Scenario 2: Capture on laptop (spanned port) Server 1 in VLAN X - OoOs</p><p>Scenario 3 is something I have never pursued. We are trying to resolve a performance issue with the application -- with 30 concurrent users, we experience degradation.</p><p>When I moved Server 1 to VLAN Y, we didn't have enough time to conduct a performance test, just enough time to capture Wireshark packets (it's a production environment).<br />
</p><p>How can I send you my trace file? Would I be able to send it to you by e-mail directly?<br />
</p><p>Thanks Laura.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-680" class="comments-container"><span id="682"></span><div id="comment-682" class="comment"><div id="post-682-score" class="comment-score"></div><div class="comment-text"><p>You can send the trace over to [email protected] and it will get forwarded to me today.</p></div><div id="comment-682-info" class="comment-info"><span class="comment-age">(26 Oct '10, 11:50)</span> lchappell ♦</div></div></div><div id="comment-tools-680" class="comment-tools"></div><div class="clear"></div><div id="comment-680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="741"></span>

<div id="answer-container-741" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-741-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you Laura and GeonJay:</p><p>I spent the last few days getting all the equipment I needed to implement a tap. Instead of "Out-of-Order" messages, I now have "TCP Retransmission" errors instead. This outcome is explained in Chapter 13 <strong><em>Using Wireshark's Expert System</em></strong> (page 277) -- Wireshark sometimes flags a packet as Out of Order when it is a retransmission due to its inablity to relate retransmissions to earlier packets.</p><p>To answer GeonJay's question: Server1 and Server2 are connected to a Cisco 4506 which uplinks to a Cisco 6509, which facilitates inter-VLAN routing and provides FWSM functionality. I tapped into the uplink using a Netscout Multimode Fiberoptic splitter, which required me to install a Fiber NIC card (hard to find!) into my Wireshark computer.</p><p>Laura, I e-mailed you the trace. Unfortunately, I had to filter it due to its size. In the event it doesn't contain the information you seek, please let me know and I will send another trace. I look forward to solving this mystery!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '10, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span></p></div></div><div id="comments-container-741" class="comments-container"><span id="742"></span><div id="comment-742" class="comment"><div id="post-742-score" class="comment-score"></div><div class="comment-text"><p>Ahh... interesting. Ok! I'll go grab the trace file and look at it tomorrow - I will let you know what I can discern/possible next steps soon (most likely over the weekend as I am curious).</p></div><div id="comment-742-info" class="comment-info"><span class="comment-age">(29 Oct '10, 22:53)</span> lchappell ♦</div></div><span id="779"></span><div id="comment-779" class="comment"><div id="post-779-score" class="comment-score"></div><div class="comment-text"><p>WireShark can also misidentify retransmissions as well as OOSs, so be careful.</p><p>So you are using the 6509 as a router on a stick. Both servers connect to the same 4506, which uplinks to the 6509. Is this correct? What's the volume of traffic going across the uplink? Have you checked CPU/mem utilization on both switches? Be careful how you monitor utilization. I would gather a high resolution utilization baseline for both switches (grab an hour of info or so) then run your transaction and see what kind of impact it has.</p><p>I'd also verify that MTUs are set consistently across the tiers.</p></div><div id="comment-779-info" class="comment-info"><span class="comment-age">(02 Nov '10, 06:35)</span> GeonJay</div></div></div><div id="comment-tools-741" class="comment-tools"></div><div class="clear"></div><div id="comment-741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="906"></span>

<div id="answer-container-906" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-906-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Laura,</p><p>I just wanted to drop a note to follow-up to see if you've had a chance to look at the capture file.</p><p>Hello GeonJay, CPU utilization is low, below 10% consistently. Server MTUs are set to default (1500 bytes). I'll verify that the switches are set the same.</p><p>--James</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '10, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span></p></div></div><div id="comments-container-906" class="comments-container"><span id="910"></span><div id="comment-910" class="comment"><div id="post-910-score" class="comment-score"></div><div class="comment-text"><p>James, it's very important to distinguish real pkt loss from fake ones (e.g. caused by overloading the span port, or from winpcap not being able to keep up). In most cases, analysis of the trace file will provide the hints necessary to determine if it's a fake loss or not. This is so common that one of my case studies in Sharkfest had to do with this exact scenario. Feel free to email me the trace if you want and I'll take a look as well. Please use "editcap -s 128 origfile newfile" to truncate the files to just 128 bytes. My email is: hbae at nyc.rr.com</p></div><div id="comment-910-info" class="comment-info"><span class="comment-age">(11 Nov '10, 08:15)</span> hansangb</div></div></div><div id="comment-tools-906" class="comment-tools"></div><div class="clear"></div><div id="comment-906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


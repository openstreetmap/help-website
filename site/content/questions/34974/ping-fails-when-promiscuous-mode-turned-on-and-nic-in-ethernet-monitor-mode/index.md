+++
type = "question"
title = "Ping fails when promiscuous mode turned on and NIC in Ethernet &quot;monitor mode&quot;"
description = '''Hi, I have following configuration PC#1 &amp;lt;----&amp;gt; switch &amp;lt;----&amp;gt; PC#2 I configured switch such that PVID =4 (default port VLAN) for both ports. Also, both ports have VLAN 4 assigned and are tagged ports. Both PC&#x27;s have Intel NICs with monitoring mode enabled and that works. ie, I can capture...'''
date = "2014-07-29T10:21:00Z"
lastmod = "2014-07-29T14:36:00Z"
weight = 34974
keywords = [ "promiscuous-mode", "vlan", "ping", "monitor", "mode" ]
aliases = [ "/questions/34974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ping fails when promiscuous mode turned on and NIC in Ethernet "monitor mode"](/questions/34974/ping-fails-when-promiscuous-mode-turned-on-and-nic-in-ethernet-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34974-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have following configuration</p><p>PC#1 &lt;----&gt; switch &lt;----&gt; PC#2</p><p>I configured switch such that PVID =4 (default port VLAN) for both ports. Also, both ports have VLAN 4 assigned and are tagged ports.</p><p>Both PC's have Intel NICs with monitoring mode enabled and that works. ie, I can capture RX'd frames and see VLAN tag.</p><p>If I use packet generator to send tagged or untagged packets in, I see tagged packet received by other PC as expected.</p><p>However, if I ping between the two PC's, the ping fails when wireshark is capturing. If I stop wireshark capture, pings continue fine. If I turn monitor mode off in same config, then pings work fine while wireshark is running.</p><p>This doesnt make sense to me since I know the frames being passed back/forth must have VLAN tags when pinging without wireshark capturing (since I see tagged frames with packet generator)</p><p>Can you think of any reason why ping would fail between two windows 7 PC's only when wireshark is capturing and NIC is in monitored mode?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">promiscuous-mode vlan ping monitor mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/f93fc158aa5be1d8eb3e76787074122c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avek&#39;s gravatar image" /><p>avek<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '14, 14:17</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34974" class="comments-container"><span id="34976"></span><div id="comment-34976" class="comment"><div id="post-34976-score" class="comment-score"></div><div class="comment-text"><p>So these are Wi-Fi NICs, right? Otherwise, monitor mode, in the sense in which Wireshark uses it, doesn't exist.</p></div><div id="comment-34976-info" class="comment-info"><span class="comment-age">(29 Jul '14, 11:18)</span> Guy Harris ♦♦</div></div><span id="34977"></span><div id="comment-34977" class="comment"><div id="post-34977-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>Sorry I wasnt clear there. These are wired NIC's.</p><p>Two PC's running Windows 7. They both have wired Intel NICs (I217-LM) connected to to switch with CAT 5 cables. Connected at 1G using autoneg.</p><p>Initially, I was using packet generator to send vlan tagged packets and would see the packets arrive untagged at receiving PC. I then read about NIC/drivers stripping the VLAN tag before sending up stack, which was why I did not see the VLAN tags in wireshark on receiving PC. I saw I could enable monitor mode in registry for the Intel NICs, which would prevent the NIC/driver from stripping the VLAN tags. After doing so, I could see the VLAN tagged packets in wireshark when using packet generator - which is great.</p><p>I then decidd to ping between the two PC's, which normally works fine. And it still does, except when I start capture with wireshark (on either PC), then the pings fail.</p><p>If I stop wireshark capture, the pings start right back up.</p><p>Also, if I go back into registry and turn monitor mode off, then pinging is successful even if wireshark is running.</p><p>Somehow, having BOTH monitor mode enabled in NICs (which allows me to see the VLAN tag in RX frames in wireshark) and wireshark in capture mode, the pinging fails. I'm not sure why that would be.</p><p>Thanks!</p></div><div id="comment-34977-info" class="comment-info"><span class="comment-age">(29 Jul '14, 11:29)</span> avek</div></div><span id="34978"></span><div id="comment-34978" class="comment"><div id="post-34978-score" class="comment-score"></div><div class="comment-text"><p>What happens if you capture with promiscuous mode turned off?</p></div><div id="comment-34978-info" class="comment-info"><span class="comment-age">(29 Jul '14, 11:48)</span> Guy Harris ♦♦</div></div><span id="34982"></span><div id="comment-34982" class="comment"><div id="post-34982-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>If I turn promiscuous mode off on the Intel NICs, then pings work fine while wireshark is capturing.</p><p>However, I can no longer see the VLAN tags in captured frames in wireshark (presumably because NIC/driver strips VLAN tags before getting to wireshark). ie, packet generator still sending in tagged frames and switch still enabled.</p><p>Thanks</p></div><div id="comment-34982-info" class="comment-info"><span class="comment-age">(29 Jul '14, 13:57)</span> avek</div></div></div><div id="comment-tools-34974" class="comment-tools"></div><div class="clear"></div><div id="comment-34974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34983"></span>

<div id="answer-container-34983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34983-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.intel.com/support/network/sb/cs-005897.htm">This Intel support page for "monitor mode" on Ethernet adapters</a> says "This change is only for promiscuous mode/sniffing use."; it might be that, in "monitor mode", the driver configures the adapters not to strip VLAN tags or CRCs, and not to drop bad packets, when in promiscuous mode, under the assumption that a network sniffer is running, <em>but</em> that a consequence of doing so might be that the adapters don't work as normal network adapters when you're in promiscuous mode, and that the driver <em>doesn't</em> configure the adapters that way when <em>not</em> in promiscuous mode, so that the adapter works as a normal network adapter <em>but</em> strips VLAN tags.</p><p>I.e., you may be out of luck if you want pings to work and VLAN tags not to be stripped. You might want to ask Intel whether there's any way to get what you want, but the answer might be "no".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '14, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34983" class="comments-container"><span id="34984"></span><div id="comment-34984" class="comment"><div id="post-34984-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>Fair enough. I was wondering the same thing.....perhaps the Intel NIC/driver, with monitor mode enabled, behaves differently whether or not their is a sniffer in the mix. If that's the case, then nothing can be done on wireshark side.</p><p>Thanks for all of the feedback!</p></div><div id="comment-34984-info" class="comment-info"><span class="comment-age">(29 Jul '14, 14:59)</span> avek</div></div></div><div id="comment-tools-34983" class="comment-tools"></div><div class="clear"></div><div id="comment-34983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


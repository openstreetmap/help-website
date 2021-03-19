+++
type = "question"
title = "ICMP ping error"
description = '''Hai, On testing ping replay for my embedded hardware(LPC2378(MAC) + KSZ8091(PHY) ) from my pc ,I am receiving the Ping replies in wireshark with no errors, but my application on PC side(CMD terminal) is showing time out. Also wire shark is marking the response packet as reply for the request.What wo...'''
date = "2016-02-29T04:54:00Z"
lastmod = "2016-02-29T06:30:00Z"
weight = 50571
keywords = [ "ping" ]
aliases = [ "/questions/50571" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP ping error](/questions/50571/icmp-ping-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50571-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hai,</p><p>On testing ping replay for my embedded hardware(LPC2378(MAC) + KSZ8091(PHY) ) from my pc ,I am receiving the Ping replies in wireshark with no errors, but my application on PC side(CMD terminal) is showing time out. Also wire shark is marking the response packet as reply for the request.What would be the reason for that?? I compared the response with a ping response from another PC all the fields seems to be ok .. Please add your comments.<br />
</p><p>Thanks Sreekanth MK</p></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '16, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/56cb43cd1e133d5f5bdd455afcbf3478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gladiator&#39;s gravatar image" /><p>gladiator<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gladiator has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50571" class="comments-container"><span id="50572"></span><div id="comment-50572" class="comment"><div id="post-50572-score" class="comment-score"></div><div class="comment-text"><p>Do you capture using Wireshark on the same PC from which you send the ping requests? Does the capture show that the destination MAC address of the reply is the MAC of the PC? Does the PC have more than one network card (wired or wireless)?</p></div><div id="comment-50572-info" class="comment-info"><span class="comment-age">(29 Feb '16, 05:51)</span> sindy</div></div><span id="50576"></span><div id="comment-50576" class="comment"><div id="post-50576-score" class="comment-score"></div><div class="comment-text"><p>Yes I captured on the same pc that I send ping request. Please see the attached images. left side shows the ping request from pc to hardware and right side shows the response. No, PC has only one wired connection.</p><p>PC IP :10.0.0.12 Hardware IP : 10.0.0.30</p><p>alt text</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Packet_Image_(Section_1)_OvsZlO0.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Packet_Image_(Section_2)_Mg1NEgZ.jpg" alt="alt text" /></p></div><div id="comment-50576-info" class="comment-info"><span class="comment-age">(29 Feb '16, 06:20)</span> gladiator</div></div><span id="50577"></span><div id="comment-50577" class="comment"><div id="post-50577-score" class="comment-score"></div><div class="comment-text"><p>please see the attached images</p></div><div id="comment-50577-info" class="comment-info"><span class="comment-age">(29 Feb '16, 06:21)</span> gladiator</div></div></div><div id="comment-tools-50571" class="comment-tools"></div><div class="clear"></div><div id="comment-50571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50579"></span>

<div id="answer-container-50579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50579-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so the reply is completely fine except one thing, which is the IP checksum. Can you permit IP checksum evaluation and check whether it is correct for both the ping replies from your embedded device and the ping replies from the other PC? Normally, IP (or TCP, or UDP) checksums may be shown as wrong for packets <em>sent</em> by the machine on which you capture if the packet processing is offloaded from the OS network stack to the network card hardware. For <em>received</em> packets, Wireshark should mark the checksum as incorrect only if it really is.</p><p>So if the icmp replies from the other PC have correct checksums while the icmp replies from your embedded devices have them wrong, we have the answer.</p><p>If not, the next step would be to disable Windows firewall (or any 3pty firewall software) on the PC from which you ping and try again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-50579" class="comments-container"><span id="50593"></span><div id="comment-50593" class="comment"><div id="post-50593-score" class="comment-score"></div><div class="comment-text"><p>Hai,</p><p>Thank you for pointing that. Yes that was due to IP header checksum error. I thought that was not necessary as wireshark is showing checksum verification disabled. So added the checksum calculation for IP header, now it is working. :) :) :) . Thanks allot for the help.</p><p>Regards Sreekanth MK</p></div><div id="comment-50593-info" class="comment-info"><span class="comment-age">(29 Feb '16, 20:39)</span> gladiator</div></div><span id="50599"></span><div id="comment-50599" class="comment"><div id="post-50599-score" class="comment-score"></div><div class="comment-text"><p>@gladiator, bear in mind that in the packet dissection tree, you can find two types of information: one that has been part of the frame/packet as it has been captured on the wire, and another one derived from the former by the dissector in order to make your own analysis easier. The latter falls into two categories, inter-packet relationship (like in which frame you can find a request for the response in the current frame, or vice versa, allowing you to filter packets on properties other than "physical" packet fields' values) and "expert info", informing you about conclusions which can be (almost) automatically made based on the captured data contents or about some settings. Expert info provides you with hints allowing you to speed up your own packet analysis.</p><p>In particular, the <code>IP checksum verification disabled</code> is such an expert info added by Wireshark, notifying you that you've switched checksum verification off in protocol preferences. It is <em>not</em> a value of any real field of the IP packet which would be telling the receiving side that it should ignore the IP checksum.</p></div><div id="comment-50599-info" class="comment-info"><span class="comment-age">(01 Mar '16, 03:17)</span> sindy</div></div></div><div id="comment-tools-50579" class="comment-tools"></div><div class="clear"></div><div id="comment-50579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


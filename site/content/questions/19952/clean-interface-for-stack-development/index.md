+++
type = "question"
title = "clean interface for stack development"
description = '''Hi, I&#x27;m porting an embedded TCP-stack.  I&#x27;d like to use wireshark to test my implementation. The problem is that there is a lot of traffic on my notebooks ethernet interface. I cant use filters, because it is possible that the frames that are sent are corrupt so i would not see them. Any idea how I ...'''
date = "2013-03-30T02:31:00Z"
lastmod = "2013-04-02T09:18:00Z"
weight = 19952
keywords = [ "noise" ]
aliases = [ "/questions/19952" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [clean interface for stack development](/questions/19952/clean-interface-for-stack-development)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm porting an embedded TCP-stack. I'd like to use wireshark to test my implementation. The problem is that there is a lot of traffic on my notebooks ethernet interface. I cant use filters, because it is possible that the frames that are sent are corrupt so i would not see them.</p><p>Any idea how I can obtain an interface where the only traffic is the one i want?</p></div><div id="question-tags" class="tags-container tags">noise</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '13, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/4f80ed9a86a92cfc874da902aecaee29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dill&#39;s gravatar image" /><p>Dill<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dill has no accepted answers">0%</span></p></div></div><div id="comments-container-19952" class="comments-container"></div><div id="comment-tools-19952" class="comment-tools"></div><div class="clear"></div><div id="comment-19952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19958"></span>

<div id="answer-container-19958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19958-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Get yourself a decent <a href="http://wiki.wireshark.org/TapReference">tap</a> or <a href="http://wiki.wireshark.org/SwitchReference">switch</a> and configure an mirror port, or get one preconfigured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19958" class="comments-container"><span id="19969"></span><div id="comment-19969" class="comment"><div id="post-19969-score" class="comment-score"></div><div class="comment-text"><p>could you please explain how that would help?</p></div><div id="comment-19969-info" class="comment-info"><span class="comment-age">(31 Mar '13, 02:20)</span> Dill</div></div><span id="19970"></span><div id="comment-19970" class="comment"><div id="post-19970-score" class="comment-score"></div><div class="comment-text"><p>Hook your laptop interface up to the monitor port, hook the device w/ embedded stack onto the mirrored port, hook the uplink to the rest of your network. If you want your laptop interface to be passive, then bring it up sans IP address (Linux), or disable protocol/services (Windows).</p></div><div id="comment-19970-info" class="comment-info"><span class="comment-age">(31 Mar '13, 06:16)</span> Jaap ♦</div></div><span id="19991"></span><div id="comment-19991" class="comment"><div id="post-19991-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help. i'm a little lost with this network stuff.... will i still be able to send test-traffic to the tested device? which services would that be for windows?</p></div><div id="comment-19991-info" class="comment-info"><span class="comment-age">(01 Apr '13, 09:35)</span> Dill</div></div></div><div id="comment-tools-19958" class="comment-tools"></div><div class="clear"></div><div id="comment-19958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20020"></span>

<div id="answer-container-20020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20020-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>NOT</strong> an offence, I'm just a bit confused!!</p><p>You say:</p><blockquote><p>I'm <strong>porting</strong> an embedded TCP-stack.</p></blockquote><p>and then you say:<br />
</p><blockquote><p>i'm a little lost with this network stuff...</p></blockquote><p>Erm ... how do you <strong>port</strong> a TCP stack without decent network knowledge?</p><p>Anyway, maybe I'm misinterpreting the word '<strong>porting</strong>'. Can you please add some information how you <strong>port</strong> that TCP stack and why you have to do it on a system that already has a TCP/IP stack in place (your laptop) instead of using a virtual machine. That information is necessary to understand your problem and why/how those two TCP stacks interact/conflict.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Apr '13, 09:18</p></div></div><div id="comments-container-20020" class="comments-container"><span id="20032"></span><div id="comment-20032" class="comment"><div id="post-20032-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I'm sorry for the confusion. I should have mentioned that I'm porting the stack (LwIP) to a microcontroller. So I just have to develop the PHY and MAC drivers for that platform which does not call for any deeper networking knowledge. But I need some tools to test the stack. I'd like to be able to "speak" to the ported stack without seeing all that noise that all these windows services and programs send out of the eth-interface of my (windows 7) notebook.</p></div><div id="comment-20032-info" class="comment-info"><span class="comment-age">(02 Apr '13, 14:56)</span> Dill</div></div><span id="20042"></span><div id="comment-20042" class="comment"><div id="post-20042-score" class="comment-score"></div><div class="comment-text"><p>O.K. can you please add some information about your network setup. Is it like one of these?</p><pre><code>PC -- switch -- Micro Controller
PC ---- Micro Controller</code></pre><p>If so, how do you test LwIP? By sending/receiving data from the PC to the MicroController?</p></div><div id="comment-20042-info" class="comment-info"><span class="comment-age">(03 Apr '13, 03:07)</span> Kurt Knochner ♦</div></div><span id="20059"></span><div id="comment-20059" class="comment"><div id="post-20059-score" class="comment-score"></div><div class="comment-text"><p>PC --- switch --- microcontroller is the setup right now, but it would be no problem to purchase some new hardware like a linux pc if that helps. Yes Id like to test LwIP by sending data from the notebook using wireshark to monitor. right now I use ping and netcat but for seriuos testing I'll need something else, but that'll be the next problem.</p></div><div id="comment-20059-info" class="comment-info"><span class="comment-age">(03 Apr '13, 08:52)</span> Dill</div></div><span id="20070"></span><div id="comment-20070" class="comment not_top_scorer"><div id="post-20070-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The problem is that there is a lot of traffic on my notebooks ethernet interface.</p></blockquote><p>well, you could filter on the MAC address of the Micro Controller to see just traffic to/from that device.</p><blockquote><p>I cant use filters, because it is possible that the frames that are sent are corrupt so i would not see them.</p></blockquote><p>If the frames are corrupt, the OS (driver) or the NIC (hardware) might drop the frame anyways, so you won't see it in Wireshark. So, filtering on the MAC address of the Micro Controller may be 'good enough'.</p><p>My suggestion: Get a second interface for your system (pccard for a laptop) and disable all Windows protocol on that additional NIC. That way, you won't get 'noise' on the line between this NIC and the Micro Controller.</p><p>If that is not an option, get second PC with an operating system that is not that chatty ;-) (Linux, *BSD)</p></div><div id="comment-20070-info" class="comment-info"><span class="comment-age">(03 Apr '13, 18:23)</span> Kurt Knochner ♦</div></div><span id="20122"></span><div id="comment-20122" class="comment not_top_scorer"><div id="post-20122-score" class="comment-score"></div><div class="comment-text"><p>So, if i put a PCMCIA ethernet card in my laptop and disable all items but IPv4 in this window:</p><p><a href="http://www.home-network-help.com/images/windows-7-network-tcpip.jpg">http://www.home-network-help.com/images/windows-7-network-tcpip.jpg</a></p><p>I'll have a silent interface?</p><p>Thanks for your patience :)</p></div><div id="comment-20122-info" class="comment-info"><span class="comment-age">(05 Apr '13, 15:48)</span> Dill</div></div><span id="20126"></span><div id="comment-20126" class="comment"><div id="post-20126-score" class="comment-score">1</div><div class="comment-text"><p>No, you also need to disable IPv4. Remove ALL check marks to get a silent interface.</p></div><div id="comment-20126-info" class="comment-info"><span class="comment-age">(06 Apr '13, 04:51)</span> Jasper ♦♦</div></div><span id="20132"></span><div id="comment-20132" class="comment"><div id="post-20132-score" class="comment-score">1</div><div class="comment-text"><p>Hint: If you disable IPv4, you will be able to capture traffic, but you won't be able to send/receive any data to the Micro Controller via that interface, at least not with standard system network calls.</p></div><div id="comment-20132-info" class="comment-info"><span class="comment-age">(06 Apr '13, 08:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20020" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-20020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "MAC address lookup says private but appears on my network"
description = '''I&#x27;ve been noticing a few unknown devices keep appearing on my pc under my network - which prompted me to inventory our home network. I downloaded your program and have been trying to learn all I can. I am concerned about two different devices that keep showing up on my pc when I open Windows Explore...'''
date = "2015-12-28T15:44:00Z"
lastmod = "2015-12-29T07:19:00Z"
weight = 48743
keywords = [ "unknown", "mac", "address" ]
aliases = [ "/questions/48743" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MAC address lookup says private but appears on my network](/questions/48743/mac-address-lookup-says-private-but-appears-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48743-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been noticing a few unknown devices keep appearing on my pc under my network - which prompted me to inventory our home network. I downloaded your program and have been trying to learn all I can. I am concerned about two different devices that keep showing up on my pc when I open Windows Explorer and select Network. These devices only show me their MAC address and an assigned name such as Full_Arial. There is no IP address, nor do I see these MAC address on our router. I tried to look up the MAC address from your site and it comes back as private. Can your software help me to determine what these devices are?</p></div><div id="question-tags" class="tags-container tags">unknown mac address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '15, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/1136b15ccfed1ca27f84e6e82361ce24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MissC&#39;s gravatar image" /><p>MissC<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MissC has no accepted answers">0%</span></p></div></div><div id="comments-container-48743" class="comments-container"></div><div id="comment-tools-48743" class="comment-tools"></div><div class="clear"></div><div id="comment-48743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48746"></span>

<div id="answer-container-48746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48746-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark passively shows you the contents of packets it can see on the network interfaces, so unless the devices write something like "I am a refrigerator &lt;vendor&gt; &lt;model&gt;" into the packets they send, Wireshark can only assist your own investigation what those devices are.</p><p>Too much is unknown about your network, so the fact that the home router does cannot see the MACs may be because the devices use some other protocol other than IP, so your PC can detect them using that protocol while your router cannot because it uses only IP and below. Or they may use IP but be connected to some other network interface of your PC than the one which looks towards the router. Finding this out is what you can use Wireshark for - on a freshly rebooted Windows machine, start a Wireshark capture on all available network interfaces first, and then go Windows Explorer -&gt; Network. If you are lucky, the actual detection of network neighbourhood takes place only after you open that window.</p><p>After the ghost devices show up, you would stop the capture and apply a display filter <code>eth.addr == 00:08:15:00:08:15</code> (of course using the MAC address of the ghost device you are trying to identify). This should allow you to identify the protocol and physical interface through which they are connected, because you'll see both as fields of the frames which the display filter selects.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '15, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48746" class="comments-container"></div><div id="comment-tools-48746" class="comment-tools"></div><div class="clear"></div><div id="comment-48746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48747"></span>

<div id="answer-container-48747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48747-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you know the MAC address, you can look it up here:</p><p><a href="https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries">https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries</a></p><p>Under Select a product, choose "ALL MAC"</p><p>Under Search results look, enter the first 3 bytes of the MAC address, for example:</p><p>00-08-15</p><p>From their, you can determine the company that has listed the MAC (in our example, CATS Co., Ltd)</p><p>This above procedure only works for devices that are publicly listed (i.e., MAC addresses that are not locally administered = The address must start with “02” in the most significant byte).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-48747" class="comments-container"></div><div id="comment-tools-48747" class="comment-tools"></div><div class="clear"></div><div id="comment-48747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


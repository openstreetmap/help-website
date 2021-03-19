+++
type = "question"
title = "win7 64bit wireshark 1.6.4 only can capture receive packets"
description = '''win7 64bit wireshark 1.6.4 only can capture receive packets,can&#x27;t capture the packets which the PC sent out,that&#x27;s mean I can&#x27;t see the packets which the src ip is my PC&#x27;s.'''
date = "2011-12-23T00:00:00Z"
lastmod = "2012-07-23T15:28:00Z"
weight = 8100
keywords = [ "64-bit", "1.6.4" ]
aliases = [ "/questions/8100" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [win7 64bit wireshark 1.6.4 only can capture receive packets](/questions/8100/win7-64bit-wireshark-164-only-can-capture-receive-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8100-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>win7 64bit wireshark 1.6.4 only can capture receive packets,can't capture the packets which the PC sent out,that's mean I can't see the packets which the src ip is my PC's.</p></div><div id="question-tags" class="tags-container tags">64-bit 1.6.4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '11, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/d37b7b18f237533a628621e7bc4d0b0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prince_23&#39;s gravatar image" /><p>prince_23<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prince_23 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '11, 07:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8100" class="comments-container"><span id="8116"></span><div id="comment-8116" class="comment"><div id="post-8116-score" class="comment-score"></div><div class="comment-text"><p>On what type of network interface is this happening? Ethernet, Wi-Fi, or something else?</p></div><div id="comment-8116-info" class="comment-info"><span class="comment-age">(23 Dec '11, 11:12)</span> Guy Harris ♦♦</div></div><span id="8128"></span><div id="comment-8128" class="comment"><div id="post-8128-score" class="comment-score"></div><div class="comment-text"><p>Ethernet interface</p></div><div id="comment-8128-info" class="comment-info"><span class="comment-age">(24 Dec '11, 04:57)</span> prince_23</div></div><span id="8131"></span><div id="comment-8131" class="comment"><div id="post-8131-score" class="comment-score"></div><div class="comment-text"><p>Does that happen regardless of whether you're capturing in promiscuous mode or not? As I read the WinPcap code and both <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff557071(v=vs.85).aspx">Microsoft's "Looping back NDIS packets" note</a> and <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff569575(v=vs.85).aspx">Microsoft's documentation on OID_GEN_CURRENT_PACKET_FILTER for NDIS 6.0 and 5.x</a>, WinPcap, for Ethernet (and Token Ring) adapters, should show sent packets to the application using it whether it's capturing in promiscuous mode or not.</p></div><div id="comment-8131-info" class="comment-info"><span class="comment-age">(24 Dec '11, 22:38)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8100" class="comment-tools"></div><div class="clear"></div><div id="comment-8100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12934"></span>

<div id="answer-container-12934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12934-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had this issue, and found the cause to be the Deterministic Network Enhancer driver. Check if you have the "DNE LightWeight Filter" binding in your network adapter properties, and try disabling it to see if this makes a difference (see screenshot below).</p><p>Please note that the Cisco VPN Client requires this driver to be able to connect. So if you are using this and leave the DNE LightWeight Filter disabled, you will probably find that you can't connect to your VPN. My suggestion is to only disable the driver while you are using Wireshark, and then re-enable when you have finished.</p><p>I hope this solves your issue.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Network_adapter_properties.jpg" alt="Network adapter properties screen-shot" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/528e8a116060f308b7119ed67ec668d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nick&#39;s gravatar image" /><p>Nick<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nick has no accepted answers">0%</span></p></img></div></div><div id="comments-container-12934" class="comments-container"><span id="44417"></span><div id="comment-44417" class="comment"><div id="post-44417-score" class="comment-score"></div><div class="comment-text"><p>It worked¡ thank you so much¡</p></div><div id="comment-44417-info" class="comment-info"><span class="comment-age">(23 Jul '15, 12:07)</span> Pablo Andres A</div></div></div><div id="comment-tools-12934" class="comment-tools"></div><div class="clear"></div><div id="comment-12934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


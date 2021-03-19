+++
type = "question"
title = "What is can see and not see"
description = '''When running Wireshark on my computer... I see packets that are broadcasted. I see packets going in and out of this computer 192.168.1.148 I&#x27;m looking for packets going from mt router 192.168.1.10 to another device 192.168.1.204 Specifically, after 192.168.1.204 request who has 192.168.1.10 I see no...'''
date = "2017-03-02T11:17:00Z"
lastmod = "2017-03-02T11:30:00Z"
weight = 59809
keywords = [ "sniffing", "arqa", "packet" ]
aliases = [ "/questions/59809" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is can see and not see](/questions/59809/what-is-can-see-and-not-see)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59809-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When running Wireshark on my computer...</p><p>I see packets that are broadcasted. I see packets going in and out of this computer 192.168.1.148</p><p>I'm looking for packets going from mt router 192.168.1.10 to another device 192.168.1.204 Specifically, after 192.168.1.204 request who has 192.168.1.10 I see no response from 192.168.1.10 reply back with the MAC address.</p><p>so is it missing or maybe I just cannot see it?</p></div><div id="question-tags" class="tags-container tags">sniffing arqa packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '17, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/02928a0228ba76abd87a58c974b3683e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcalcutt&#39;s gravatar image" /><p>dcalcutt<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcalcutt has no accepted answers">0%</span></p></div></div><div id="comments-container-59809" class="comments-container"></div><div id="comment-tools-59809" class="comment-tools"></div><div class="clear"></div><div id="comment-59809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59810"></span>

<div id="answer-container-59810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59810-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely you can't see it because of your capture setup. You might want to visit <a href="https://wiki.wireshark.org/CaptureSetup">https://wiki.wireshark.org/CaptureSetup</a> and also the more specific <em>"Capturing on .."</em> page most relevant to your network, which I'm guessing is very likely either <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet capture setup</a> or <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">WLAN (IEEE 802.11) capture setup</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '17, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59810" class="comments-container"><span id="59996"></span><div id="comment-59996" class="comment"><div id="post-59996-score" class="comment-score"></div><div class="comment-text"><p>Can you be more specific? I've been reading here, but I'm not seeing what I must do.</p><p>I guess I need to make my computer 192.168.1.148 act like my router 192.168.1.10, to see all the packets it is suppose to be receiving and sending.</p><p>I have issues with the router not sending the MAC address back to the device 192.168.1.200 when requesting.</p></div><div id="comment-59996-info" class="comment-info"><span class="comment-age">(10 Mar '17, 16:40)</span> dcalcutt</div></div><span id="60030"></span><div id="comment-60030" class="comment"><div id="post-60030-score" class="comment-score"></div><div class="comment-text"><p>Maybe you could start by describing your current capture setup? Are you trying to capture on an Ethernet connection, in which case, which picture from the Ethernet capture setup page best depicts your capture setup? Without further information, I'm going to assume it's the one titled, "Switched Media - Same Computer", and if so, then you will see the following written below the diagram:</p><ul><li>Advantage: Easy to use</li><li>Disadvantage: <strong>Other traffic not available</strong></li></ul><p>So, you will need to set up your capture environment so that you can capture other traffic not necessarily destined for your computer. The wiki describes several methods you can use to accomplish that.</p></div><div id="comment-60030-info" class="comment-info"><span class="comment-age">(13 Mar '17, 07:34)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-59810" class="comment-tools"></div><div class="clear"></div><div id="comment-59810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


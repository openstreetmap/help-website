+++
type = "question"
title = "Packet Capture Application performances"
description = '''Dear All, I&#x27;m developing a WIndows7 application that get UDP packets from the network interface card. The application needs the amount of droped packets to be low. I&#x27;m experiencing this funny issue: when the application runs alone on the system I experience a UDP packet loss, the same application ru...'''
date = "2014-08-08T05:30:00Z"
lastmod = "2014-08-10T07:14:00Z"
weight = 35327
keywords = [ "nic", "efficiency", "os", "settings" ]
aliases = [ "/questions/35327" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Capture Application performances](/questions/35327/packet-capture-application-performances)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35327-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All, I'm developing a WIndows7 application that get UDP packets from the network interface card. The application needs the amount of droped packets to be low. I'm experiencing this funny issue: when the application runs alone on the system I experience a UDP packet loss, the same application runs without losing any single UDP packet when Wireshark is capturing data on the same NIC. Now I wonder if (it must be) wireshark applies some setting to the NIC or to the OS to improve its packet capture efficiency. If yes, I would appreciate very much if anybody of you could help me in finding this magic setting and replicate it in my application. Thanks alot in advance for your help. MM</p></div><div id="question-tags" class="tags-container tags">nic efficiency os settings</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/3e3017ce150afcd8a315c019d3d3d1f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MMM&#39;s gravatar image" /><p>MMM<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MMM has no accepted answers">0%</span></p></div></div><div id="comments-container-35327" class="comments-container"></div><div id="comment-tools-35327" class="comment-tools"></div><div class="clear"></div><div id="comment-35327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35328"></span>

<div id="answer-container-35328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35328-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark puts the NIC in promiscuous mode, which means that it also accepts packets that are not targeted at the MAC address of the NIC. If your application runs better with promiscuous mode you should check the layer 2 addresses of the UDP packets. Maybe some of them are addressed at a different/wrong MAC address?</p><p>Promiscuous mode should not be used by any normal application, it is only leveraged for packet captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '14, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35328" class="comments-container"><span id="35486"></span><div id="comment-35486" class="comment"><div id="post-35486-score" class="comment-score"></div><div class="comment-text"><p>Hi, thank a lot for your help. Jasper, you got it. From time to time the ethernet destination address of the UDP packet is wrong at the source. Wireshark is Great!! Thanks you everybody. MMM</p></div><div id="comment-35486-info" class="comment-info"><span class="comment-age">(14 Aug '14, 10:15)</span> MMM</div></div></div><div id="comment-tools-35328" class="comment-tools"></div><div class="clear"></div><div id="comment-35328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35374"></span>

<div id="answer-container-35374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35374-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see my answer to a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/11733/wireshark-install-seems-to-improve-performance">http://ask.wireshark.org/questions/11733/wireshark-install-seems-to-improve-performance</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35374" class="comments-container"></div><div id="comment-tools-35374" class="comment-tools"></div><div class="clear"></div><div id="comment-35374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


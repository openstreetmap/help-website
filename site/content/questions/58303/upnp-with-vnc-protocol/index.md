+++
type = "question"
title = "UPNP with VNC protocol"
description = '''Hi All, I am trying to control my Satellite box with my Automation system for that i need IP commands of box. the satellite box has its own app. I have used wireshark to capture the Communication between Mobile app and Box. After two days of head Bank i understand the its uses UPNP to communicate an...'''
date = "2016-12-22T12:15:00Z"
lastmod = "2016-12-22T13:34:00Z"
weight = 58303
keywords = [ "satellite", "vnc", "upnp", "wireshark" ]
aliases = [ "/questions/58303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [UPNP with VNC protocol](/questions/58303/upnp-with-vnc-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am trying to control my Satellite box with my Automation system for that i need IP commands of box.</p><p>the satellite box has its own app. I have used wireshark to capture the Communication between Mobile app and Box. After two days of head Bank i understand the its uses UPNP to communicate and when i send key press commands from mobile app to box the wireshark output shows "VNC" and this is beyond my understanding.</p><p>Can someone please help me out in this. I have uploaded the wireshrk file on Google driver. Please find the link below.Any help will be greatly appreciated.</p><p>Source IP Address(Mobiel App): 192.168.1.134 Satellite Box IP Address: 192.168.1.227</p><p><a href="https://drive.google.com/open?id=0Bz8ehuXLuisYVVh2OU1fOXBvMWs">Wireshark File Attachement</a></p></div><div id="question-tags" class="tags-container tags">satellite vnc upnp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '16, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/4effb6fb15d9ff03aca5e1ad406bac0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cylon147&#39;s gravatar image" /><p>cylon147<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cylon147 has no accepted answers">0%</span></p></div></div><div id="comments-container-58303" class="comments-container"></div><div id="comment-tools-58303" class="comment-tools"></div><div class="clear"></div><div id="comment-58303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58304"></span>

<div id="answer-container-58304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58304-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The traffic on TCP port 5900 is interpreted as VNC since this is the standard port for VNC. If this is not VNC, as you have stated, simply disable the VNC dissector to get back to raw TCP payload data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58304" class="comments-container"><span id="58310"></span><div id="comment-58310" class="comment"><div id="post-58310-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have tried as you have mentioned but frankly speaking it is not making sense to me. Can you please elaborate.</p><p>I have uploaded two file one with VNC enabled and another one is with Disabled.This packets are of Pressing Down button on Mobile App.</p><p>Without VNC</p><p><a href="https://drive.google.com/file/d/0Bz8ehuXLuisYUE5MZGlmckRkV1k/view?usp=sharing">https://drive.google.com/file/d/0Bz8ehuXLuisYUE5MZGlmckRkV1k/view?usp=sharing</a></p><p>With VNC</p><p><a href="https://drive.google.com/file/d/0Bz8ehuXLuisYYTJMM2xjendxVGc/view?usp=sharing">https://drive.google.com/file/d/0Bz8ehuXLuisYYTJMM2xjendxVGc/view?usp=sharing</a></p></div><div id="comment-58310-info" class="comment-info"><span class="comment-age">(22 Dec '16, 23:23)</span> cylon147</div></div><span id="58312"></span><div id="comment-58312" class="comment"><div id="post-58312-score" class="comment-score">1</div><div class="comment-text"><p>The difference is not in the capture of the frames, it's in the interpretation. Therefore it doesn't matter if you have the VNC dissector (or any dissector for that matter) enabled or disabled during capture, the packets are captured nonetheless (with the exception of frames discarded by the capture filter, but that is not applicable here). Its only when presenting the packets to you that the dissector configuration comes into play.</p></div><div id="comment-58312-info" class="comment-info"><span class="comment-age">(23 Dec '16, 01:27)</span> Jaap ♦</div></div><span id="58314"></span><div id="comment-58314" class="comment"><div id="post-58314-score" class="comment-score">1</div><div class="comment-text"><p>On the other hand, inspection of your capture file called Down Button.pcapng has the telltale signs of VNC. When you look in frame 14, it's TCP payload says: "52 46 42 20 30 30 33 2e 30 30 38 0a", which matches perfectly the <a href="https://tools.ietf.org/html/rfc6143#section-7.1.1">Remote Framebuffer Protocol ProtocolVersion Handshake</a>. So contrary to your initial statement, I do think this is VNC.</p></div><div id="comment-58314-info" class="comment-info"><span class="comment-age">(23 Dec '16, 01:36)</span> Jaap ♦</div></div><span id="58315"></span><div id="comment-58315" class="comment"><div id="post-58315-score" class="comment-score"></div><div class="comment-text"><p>can you please chime in for what app is sending to box.</p><p>From my understanding app asked for Description file. Box sends Description file In XML format.</p><p>But i could not find the Down Button Commands that i have sent. There is not indication of anything.</p></div><div id="comment-58315-info" class="comment-info"><span class="comment-age">(23 Dec '16, 01:40)</span> cylon147</div></div><span id="58317"></span><div id="comment-58317" class="comment"><div id="post-58317-score" class="comment-score">1</div><div class="comment-text"><p>A quick look at Down Button.pcapng shows that frame 23 contains a <a href="https://tools.ietf.org/html/rfc6143#section-7.5.4">Remote Framebuffer Protocol KeyEvent</a>, Where key with code E101 goes down and back up.</p><p>In short, you should read up on Remote Framebuffer Protocol and implement that, because that's what's going on. How to do that is out of scope of this Q&amp;A</p></div><div id="comment-58317-info" class="comment-info"><span class="comment-age">(23 Dec '16, 04:21)</span> Jaap ♦</div></div><span id="58320"></span><div id="comment-58320" class="comment not_top_scorer"><div id="post-58320-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot mate. I will read up more.</p></div><div id="comment-58320-info" class="comment-info"><span class="comment-age">(23 Dec '16, 06:21)</span> cylon147</div></div></div><div id="comment-tools-58304" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-58304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


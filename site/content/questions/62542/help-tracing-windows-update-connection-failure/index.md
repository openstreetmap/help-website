+++
type = "question"
title = "Help tracing Windows Update connection failure"
description = '''Recently, I have had problems getting Windows Update and Windows Activation to work. This is a network level problem, not specific to any one machine and affects both servers (WS2012r2) and desktops (Win 10 Pro), both physical &amp;amp; virtual machines. Sometimes, the problem resolves itself if I let t...'''
date = "2017-07-05T11:23:00Z"
lastmod = "2017-07-17T10:03:00Z"
weight = 62542
keywords = [ "windows", "capture" ]
aliases = [ "/questions/62542" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help tracing Windows Update connection failure](/questions/62542/help-tracing-windows-update-connection-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62542-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently, I have had problems getting Windows Update and Windows Activation to work. This is a network level problem, not specific to any one machine and affects both servers (WS2012r2) and desktops (Win 10 Pro), both physical &amp; virtual machines. Sometimes, the problem resolves itself if I let the PC sit for a few days, but usually not - and never for activations.</p><p>I've been through all of the "fix Windows Update/Activation" steps, multiple times with multiple machines without success, so I did a clean install on a test machine with Wireshark installed. I'm not going to post Windows error codes here because I just want to find out what Wireshark can tell me about these failures.</p><p>If anyone can help me understand what I'm looking at in this capture file, I'd be grateful!</p><p><a href="https://www.dropbox.com/s/lgrbafn1r7whpko/output.pcapng?dl=0">capture file</a></p></div><div id="question-tags" class="tags-container tags">windows capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '17, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/48e198282557b606b1f5762276069a41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LoveToFlyGuy&#39;s gravatar image" /><p>LoveToFlyGuy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LoveToFlyGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-62542" class="comments-container"></div><div id="comment-tools-62542" class="comment-tools"></div><div class="clear"></div><div id="comment-62542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62547"></span>

<div id="answer-container-62547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62547-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are looking at countless attempts of the machine to set up a TLS-encrypted connection with the Microsoft update server. As the encryption uses Diffie-Hellman key exchange, there is no way to decipher the payload and even the result of the handshake unless you would use a MITM-attack on it. But it seems that there is actually no payload at all, as after the end of cipher suite negotiation, the client actively closes the TCP session without transferring any TLS payload at all.</p><p>So if we leave aside a bug of the Microsoft upgrade client, the only idea I could have would be that some security element between the machine attempting the upgrade and the Microsoft server (reverse DNS shows that 157.56.96.58 does belong to Microsoft range) tampers with the Diffie-Hellman exchange and the client recognizes it somehow (or the server does and says the negotiation has failed).</p><p>If you can isolate one of the machines from the rest of the network and let it bypass your current security elements (firewalls) when talking to the internet, and if it upgrades successfully this way, you'll know there is something wrong about your firewally.</p><p>Another thing which surprises me is that your machine sends a DNS request, asking for an IP of <code>ctldl.windowsupdate.com</code>, but doesn't wait for a response for a reasonable amount of time, as when the answer arrives in less than two milliseconds, it is already rejected with icmp "destination port unreachable". Normally, DNS responses coming within seconds are still awaited and accepted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jul '17, 13:56</p></div></div><div id="comments-container-62547" class="comments-container"><span id="62592"></span><div id="comment-62592" class="comment"><div id="post-62592-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy!</p><p>That's more-or-less what I thought was going on. Why it's happening is still a mystery, because I have the local (Windows) firewall turned off, and Defender disabled (as much as it can be) with no effect. I've also temporarily set our WAN firewall to not restrict outbound traffic and enabled WAN ping response as a test - again without effect, and there are currently no intermediary firewalls in place.</p><p>You have given me some great avenues to explore!</p></div><div id="comment-62592-info" class="comment-info"><span class="comment-age">(06 Jul '17, 14:09)</span> LoveToFlyGuy</div></div><span id="62599"></span><div id="comment-62599" class="comment"><div id="post-62599-score" class="comment-score"></div><div class="comment-text"><blockquote><p>enabled WAN ping response as a test</p></blockquote><p>This is totally unrelated.</p><blockquote><p>I've also temporarily set our WAN firewall to not restrict outbound traffic</p></blockquote><p>This may or may not help. Some of the security boxes behave funny and interfere with the traffic even if configured not to do so, so when I said "bypass", I really had in mind "bypass", i.e. connect the machine under test in such a way that its communication to the Internet does not go through that security box at all.</p><p>If you have a virtualization environment, just install a new Windows machine which can connect only to internet and nowhere else so that, if conquered by malware, it cannot infect anything else.</p><p>If you only have physical machines, connect one of them somewhere else where network security is provided by another type of security box, or just switch on the security software provided Windows itself and use a mobile connection (Public network setting of Windows networking).</p></div><div id="comment-62599-info" class="comment-info"><span class="comment-age">(07 Jul '17, 00:23)</span> sindy</div></div></div><div id="comment-tools-62547" class="comment-tools"></div><div class="clear"></div><div id="comment-62547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62827"></span>

<div id="answer-container-62827" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the help, sindy.</p><p>I finally tracked the problem to our Meraki firewall incorrectly identifying certain CDN IPs as belonging to malware domains, and silently blocking them. There were no logs showing the blocking, as Meraki apparently doesn't think admins would need that information.</p><p>I only discovered the cause because I was reading release notes prior to deploying a recent Meraki firmware update. That issue was listed as being addressed in the update.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '17, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/48e198282557b606b1f5762276069a41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LoveToFlyGuy&#39;s gravatar image" /><p>LoveToFlyGuy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LoveToFlyGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-62827" class="comments-container"></div><div id="comment-tools-62827" class="comment-tools"></div><div class="clear"></div><div id="comment-62827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


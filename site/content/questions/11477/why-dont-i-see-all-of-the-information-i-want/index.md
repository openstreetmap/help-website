+++
type = "question"
title = "Why don&#x27;t I see all of the information I want?"
description = '''I am testing wireshark for learning purposes. I wanted to try out a tutorial that hacks a facebook account stealing cookie information. I couldn&#x27;t manage to hack my facebook account because wireshark is sending me truncated packets that I can&#x27;t get cookie info out of. This is the topography of the n...'''
date = "2012-05-30T11:53:00Z"
lastmod = "2012-05-30T12:07:00Z"
weight = 11477
keywords = [ "cookie", "http", "capture-setup" ]
aliases = [ "/questions/11477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why don't I see all of the information I want?](/questions/11477/why-dont-i-see-all-of-the-information-i-want)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11477-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am testing wireshark for learning purposes. I wanted to try out a tutorial that hacks a facebook account stealing cookie information. I couldn't manage to hack my facebook account because wireshark is sending me truncated packets that I can't get cookie info out of.<br />
<strong>This is the topography of the network</strong>: my desktop PC is connected to the Internet to a hub (D-LINK router) via LAN (ethernet cable). I have a notebook connected to Internet via Wi-Fi to the same hub (D-LINK router). I access facebook on my notebook on WIN XP OS. I monitor the packets with wireshark on my desktop PC on Ubuntu 12.04 OS. I only get worthless truncated cookie information. Why is that?<br />
My capture interfaces are:</p><ol><li>eth0</li><li>Pseudo device that captures on all interfaces</li><li>USb1</li><li>USB 2</li><li>lo</li></ol><p>I tried to capture on all interfaces (except usb 1, 2) but the same thing. I <strong>can't get cookie information from my notebook</strong>. I only get NBNS, DNS, Browser, IGMP, SSDP protocol type of packets. I get some HTTP but not facebook cookie with 'datr' line. It is just anoying. It seems so easy in the tutorial. Anyone could help me with this?</p></div><div id="question-tags" class="tags-container tags">cookie http capture-setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '12, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/8cd0541da442c4a46922f8876a27a17a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pahunrepublic&#39;s gravatar image" /><p>pahunrepublic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pahunrepublic has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '12, 12:09</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-11477" class="comments-container"></div><div id="comment-tools-11477" class="comment-tools"></div><div class="clear"></div><div id="comment-11477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11478"></span>

<div id="answer-container-11478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11478-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your D-LINK router is probably a <strong><em>switch</em></strong>, not a <strong><em>hub</em></strong> (See the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a> article). As such, you are only going to see broadcast data on your Ubuntu PC. If, by some chance, your router supports spanning/mirroring traffic, then you should set that up. Otherwise, you'll need to actually insert a hub somewhere.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '12, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-11478" class="comments-container"><span id="11489"></span><div id="comment-11489" class="comment"><div id="post-11489-score" class="comment-score"></div><div class="comment-text"><p>So it means I won't get any cookie info with a router or with my network topology.</p></div><div id="comment-11489-info" class="comment-info"><span class="comment-age">(31 May '12, 07:10)</span> pahunrepublic</div></div><span id="11495"></span><div id="comment-11495" class="comment"><div id="post-11495-score" class="comment-score"></div><div class="comment-text"><p>That is correct; as cookie data is sent unicast, only the intermediary and endpoint nodes will see that data. The only exception to that rule is when using a <em>hub</em>, all nodes connected to that hub will receive a copy of the data. Your best bet is probably to ditch the wireless connection and connect via ethernet both the laptop and PC into the same hub, and then connect that hub to the router.</p></div><div id="comment-11495-info" class="comment-info"><span class="comment-age">(31 May '12, 10:23)</span> multipleinte...</div></div><span id="11498"></span><div id="comment-11498" class="comment"><div id="post-11498-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I wanted to try out a tutorial that hacks a facebook account stealing cookie information</p></blockquote><p>I wonder why you want to hack a facebook account?</p></div><div id="comment-11498-info" class="comment-info"><span class="comment-age">(31 May '12, 10:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11478" class="comment-tools"></div><div class="clear"></div><div id="comment-11478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


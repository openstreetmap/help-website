+++
type = "question"
title = "Monitoring Ethernet II frames in Ubuntu; with and without a local network"
description = '''Hi, I&#x27;m trying to send raw &#x27;Ethernet II&#x27; frames from my ethernet interface (eth0) using Ubuntu, to some embedded electronics (I&#x27;m trying to get my head around low level networking). I would like to only use &#x27;Ethernet&#x27; (layer 2), and not use &#x27;IP&#x27; (layer 3) or any higher protocols, to keep things simp...'''
date = "2013-12-10T17:15:00Z"
lastmod = "2013-12-10T17:15:00Z"
weight = 27983
keywords = [ "ethernet", "ubuntu" ]
aliases = [ "/questions/27983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring Ethernet II frames in Ubuntu; with and without a local network](/questions/27983/monitoring-ethernet-ii-frames-in-ubuntu-with-and-without-a-local-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27983-score" class="post-score" title="current number of votes">0</div><span id="post-27983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to send raw 'Ethernet II' frames from my ethernet interface (eth0) using Ubuntu, to some embedded electronics (I'm trying to get my head around low level networking). I would like to only use 'Ethernet' (layer 2), and not use 'IP' (layer 3) or any higher protocols, to keep things simple for the electronics.</p><p>I have found 2 ways of send raw 'Ethernet II' frames using Ubuntu that seem to work: 1. Using <a href="http://packeth.sourceforge.net/packeth/Home.html" title="packeth">packeth</a> 2. Using python (as per the highest voted stack overflow answer <a href="http://stackoverflow.com/questions/1117958/how-do-i-use-raw-socket-in-python">here</a>)</p><p>When I plug my Ubuntu's Ethernet interface (eth0) to my home router's network port using a ethernet cable, I can start a capture using Wireshark on eth0, and correctly view the transmitted 'Ethernet II' frames, when using either of the methods given above). But when I disconnect the Ethernet cable and repeat transmitting an 'Ethernet II' frame I see nothing at all in Wireshark. Why???</p><p>I am just learning networking, so any help appreciated... I'm having trouble working out what the difference between the 2 scenarios should be at the Ethernet Layer??? Connecting eth0 to a local network provides it with an IP address, but I'm not sure why this should affect eth0's ability to transmit... what am I missing here??? I have turned eth0 on using 'ifconfig eth0 on', but that didn't help... What should be needed theoretically for two Ethernet level devices to talk to each other?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '13, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/3cb0285741ef0948ff5c1f7e8a150299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chendy&#39;s gravatar image" /><p><span>Chendy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chendy has no accepted answers">0%</span></p></div></div><div id="comments-container-27983" class="comments-container"></div><div id="comment-tools-27983" class="comment-tools"></div><div class="clear"></div><div id="comment-27983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


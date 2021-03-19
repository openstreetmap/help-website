+++
type = "question"
title = "packet sniffing in wifi network between two device from 3rd device"
description = '''I have my own wpa2 wifi LAN (router, my pc, device1, device2, I know their IP addresses). Now I need to find out how device1 communicates with device2 (for example which command device1 sends to device2 to turn on green color - device2 is smart bulb). So I need to capture their protocol and packet d...'''
date = "2016-01-16T03:56:00Z"
lastmod = "2016-01-16T04:48:00Z"
weight = 49269
keywords = [ "sniffing" ]
aliases = [ "/questions/49269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [packet sniffing in wifi network between two device from 3rd device](/questions/49269/packet-sniffing-in-wifi-network-between-two-device-from-3rd-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49269-score" class="post-score" title="current number of votes">0</div><span id="post-49269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have my own wpa2 wifi LAN (router, my pc, device1, device2, I know their IP addresses). Now I need to find out how device1 communicates with device2 (for example which command device1 sends to device2 to turn on green color - device2 is smart bulb). So I need to capture their protocol and packet data to be able to read "commands" between these two devices, so I can replicate it from my computer (because for this smart bulb is no API available).</p><p>But I don't know how to do it from my pc? I think I need something easy to use. Is there any newbie step by ste tutorial how to do this? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '16, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/5e3070c0e57f558da88f78534e5e0472?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miamia&#39;s gravatar image" /><p><span>miamia</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miamia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jan '16, 03:58</strong> </span></p></div></div><div id="comments-container-49269" class="comments-container"></div><div id="comment-tools-49269" class="comment-tools"></div><div class="clear"></div><div id="comment-49269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49270"></span>

<div id="answer-container-49270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49270-score" class="post-score" title="current number of votes">0</div><span id="post-49270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>Get prepared for reverse engineering the payload of the bulb control messages from a hex dump as it is not very likely that someone else has already analysed the protocol used and prepared a Wireshark dissector for it.</p></li><li><p>If your PC runs Microsoft Windows, find a Mac or a linux PC.</p></li><li><p>If your PC runs something else than Microsoft Windows, follow <a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Turning_on_monitor_mode">these instructions</a> to set up the capture, and <a href="https://wiki.wireshark.org/HowToDecrypt802.11">these instructions</a> to decrypt the WPA2 traffic (beware, the startup of all devices whose communication you want to decrypt must be captured). Or you may prefer to switch off wireless encryption on the AP instead (and reconfigure the device1 and device2) for the time of capturing the communication between device1 and device2; in such case, you may also want to disconnect the AP from internet for the time the wireless encryption is off if you're afraid of someone else using your internet connection.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '16, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49270" class="comments-container"></div><div id="comment-tools-49270" class="comment-tools"></div><div class="clear"></div><div id="comment-49270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


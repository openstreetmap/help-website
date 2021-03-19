+++
type = "question"
title = "AP sending probe request to a spoofed mac address device"
description = '''when I start sniffing my wlan with wireshark, I noticed my AP send probes requests to a Proxim Wireless device who change his 6 last mac address number each time I start a session. Does I have to worry about that? Why a device change his mac address each time I put my wifi adapter in promiscuous mod...'''
date = "2015-03-19T05:49:00Z"
lastmod = "2015-03-24T12:58:00Z"
weight = 40683
keywords = [ "wireless" ]
aliases = [ "/questions/40683" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [AP sending probe request to a spoofed mac address device](/questions/40683/ap-sending-probe-request-to-a-spoofed-mac-address-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40683-score" class="post-score" title="current number of votes">0</div><span id="post-40683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when I start sniffing my wlan with wireshark, I noticed my AP send probes requests to a Proxim Wireless device who change his 6 last mac address number each time I start a session. Does I have to worry about that? Why a device change his mac address each time I put my wifi adapter in promiscuous mode? What can I do to get more information about this device?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/1f23f580c6d3498a8d4573b1f87e93ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ripper&#39;s gravatar image" /><p><span>ripper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ripper has no accepted answers">0%</span></p></div></div><div id="comments-container-40683" class="comments-container"><span id="40726"></span><div id="comment-40726" class="comment"><div id="post-40726-score" class="comment-score"></div><div class="comment-text"><ol><li><p>In your post you mentioned that the AP is sending Probe requests. Usually WiFi adapters (STA) will send probe requests and AP's will respond with Probe Responses. Is the Proxim Wireless device acting as a STA or AP?</p></li><li><p>When you put your adapter in promiscuous mode, the adapter allows all frames to pass through. This means if there are other Proxim Wireless devices in the area, you will also see them in your sniff. Are there other Proxim Wireless devices in your area when performing your packet capture?</p></li></ol></div><div id="comment-40726-info" class="comment-info"><span class="comment-age">(20 Mar '15, 06:31)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="40739"></span><div id="comment-40739" class="comment"><div id="post-40739-score" class="comment-score"></div><div class="comment-text"><ol><li><p>I don't know if the Proxim Wireless is a STA or AP cause I never received probe request from it. This device is not in my network, it's maybe owned by a neighbour. I try to capture with Commview for WiFi and It doesn't appear in node tab.</p></li><li><p>I don't think there are other Proxim Wireless device in my area, I see only one Proxim device when I perform the packet capture. Each time I start wireshark or commview the 6 last mac address numbers are changed. I tested a capture a complete day without restarting wireshark, the Proxim device kept his mac address, next day I restarted 10 times wireshark and got 10 differents mac address from Proxim device. I don't understand why the device change his mac address when I perform a new capture.</p></li></ol></div><div id="comment-40739-info" class="comment-info"><span class="comment-age">(20 Mar '15, 08:53)</span> <span class="comment-user userinfo">ripper</span></div></div><span id="40744"></span><div id="comment-40744" class="comment"><div id="post-40744-score" class="comment-score"></div><div class="comment-text"><p>I assume you are using the same WiFi adapter and driver for both Wireshark and Commview. Is it possible to use another WiFi adapter and driver? This would eliminate the adapter and driver as the source of the problem.</p></div><div id="comment-40744-info" class="comment-info"><span class="comment-age">(20 Mar '15, 10:09)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-40683" class="comment-tools"></div><div class="clear"></div><div id="comment-40683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40761"></span>

<div id="answer-container-40761" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40761-score" class="post-score" title="current number of votes">0</div><span id="post-40761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just noticed that the active node discovery function is enabled in commview for WiFi. This function makes the application send PROBE REQUEST packets periodically. Such packets facilitate the discovery of those APs that do not broadcast their SSID. When I disable the active node discovery, sending probe request from Proxim device disapear in packet capture. I have tested using together, wireshark with another WiFi adapter and commview with active node enabled. Wireshark see proxim device as STA as soon I enable the function and disapear the same way.</p><p>I always wonder if it's a malicious device that could compromise my security network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '15, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/1f23f580c6d3498a8d4573b1f87e93ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ripper&#39;s gravatar image" /><p><span>ripper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ripper has no accepted answers">0%</span></p></div></div><div id="comments-container-40761" class="comments-container"><span id="40814"></span><div id="comment-40814" class="comment"><div id="post-40814-score" class="comment-score"></div><div class="comment-text"><p>Do you have the capture? If you can post that I can look at it and try to provide some insight?</p></div><div id="comment-40814-info" class="comment-info"><span class="comment-age">(24 Mar '15, 12:48)</span> <span class="comment-user userinfo">Ramprasad</span></div></div><span id="40815"></span><div id="comment-40815" class="comment"><div id="post-40815-score" class="comment-score"></div><div class="comment-text"><p>The Proxim device is functioning correctly. The IEEE specification defines 2 types of scanning: Passive and Active. With Active scanning, the station generates Probe Request frames. When you activate the "node discovery" function in the Proxim device, you are switching the device to Active scanning.</p></div><div id="comment-40815-info" class="comment-info"><span class="comment-age">(24 Mar '15, 12:58)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-40761" class="comment-tools"></div><div class="clear"></div><div id="comment-40761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


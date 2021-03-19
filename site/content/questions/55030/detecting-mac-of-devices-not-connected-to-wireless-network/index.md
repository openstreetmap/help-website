+++
type = "question"
title = "Detecting MAC of devices not connected to wireless network"
description = '''Is there a way to use Wireshark to detect MAC id&#x27;s of devices not connected to a wireless network? If so, how would you set it do achieve this goal?'''
date = "2016-08-21T13:12:00Z"
lastmod = "2016-08-21T16:26:00Z"
weight = 55030
keywords = [ "wireless" ]
aliases = [ "/questions/55030" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Detecting MAC of devices not connected to wireless network](/questions/55030/detecting-mac-of-devices-not-connected-to-wireless-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55030-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to use Wireshark to detect MAC id's of devices not connected to a wireless network? If so, how would you set it do achieve this goal?</p></div><div id="question-tags" class="tags-container tags">wireless</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '16, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/3441f742d2548710ea213a5aee8decf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harlev&#39;s gravatar image" /><p>harlev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harlev has no accepted answers">0%</span></p></div></div><div id="comments-container-55030" class="comments-container"><span id="55031"></span><div id="comment-55031" class="comment"><div id="post-55031-score" class="comment-score"></div><div class="comment-text"><p>Not enough information about what you really want.</p><p>If you mean MAC addresses of devices in the same IP subnet which is used on your wireless interface, nothing special is required, just capture the ARP requests (which are broadcast) for long enough time, or to speed it up, use a script to ping each address in the subnet once (which will make your PC send an ARP request and receive an ARP response from each device) and you should catch them all.</p><p>If you mean MAC addresses outside your wireless interface's subnet, there is no way to capture them on your wireless interface, and you'll need to use a wired one to connect to the (V)LAN where these devices are connected, and use the same method as above.</p><p>If you do not have physical access to the LAN hosting the subnet which those devices use, you're out of luck.</p></div><div id="comment-55031-info" class="comment-info"><span class="comment-age">(21 Aug '16, 13:45)</span> sindy</div></div><span id="55032"></span><div id="comment-55032" class="comment"><div id="post-55032-score" class="comment-score"></div><div class="comment-text"><p>Not sure what you really want, but you can likely get MAC addresses of nearby wireless devices if you are able to capture traffic with a wifi interface in monitor+promsicuous mode. You would see those packets if they are nearby (and your interface can decode them) and they are attached to another network, but even if they are not, you might get lucky and see them probe for configured networks. Those probe requests will tell you lots about the devices around you.<br />
</p><p>This last point meets your requirements: observe MAC addresses of wireless devices not connected to any wireless network. I can think of nefarious uses for this: track devices as they move around. Probably what the NSA does.</p><p>Check out www.aircrack-ng.org as well.</p></div><div id="comment-55032-info" class="comment-info"><span class="comment-age">(21 Aug '16, 13:58)</span> Bob Jones</div></div><span id="55034"></span><div id="comment-55034" class="comment"><div id="post-55034-score" class="comment-score"></div><div class="comment-text"><p>Yes, I would like to see devices probe for networks, but all I need is their MAC address. How can I configure Wireshark to do this?</p><p>I was looking at aircrack-ng but was hoping Wireshark could provide more granular information</p></div><div id="comment-55034-info" class="comment-info"><span class="comment-age">(21 Aug '16, 15:02)</span> harlev</div></div></div><div id="comment-tools-55030" class="comment-tools"></div><div class="clear"></div><div id="comment-55030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55036"></span>

<div id="answer-container-55036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55036-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try here to get started capturing wifi packets:</p><p>CaptureSetup/WLAN - The Wireshark Wiki <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>This will definetly be more granular, maybe too much. You can filter for probes when you get to that point.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '16, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-55036" class="comments-container"></div><div id="comment-tools-55036" class="comment-tools"></div><div class="clear"></div><div id="comment-55036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


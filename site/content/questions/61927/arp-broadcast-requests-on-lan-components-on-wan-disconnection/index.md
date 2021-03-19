+++
type = "question"
title = "ARP Broadcast requests on LAN components on WAN Disconnection"
description = '''We have a newly implemented L2/L3 Multipath Network Infrastructure setup (by a third party) at our facilities. We are trying to validate the setup. All the data from Building A is sent to Building C via Building B (Building B is like a datacenter). When we disconnect Building C (stress test by unplu...'''
date = "2017-06-10T20:20:00Z"
lastmod = "2017-06-10T20:20:00Z"
weight = 61927
keywords = [ "arp" ]
aliases = [ "/questions/61927" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ARP Broadcast requests on LAN components on WAN Disconnection](/questions/61927/arp-broadcast-requests-on-lan-components-on-wan-disconnection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61927-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/BroadcastStorm_JyXkJPh.JPG" alt="alt text" />We have a newly implemented L2/L3 Multipath Network Infrastructure setup (by a third party) at our facilities. We are trying to validate the setup. All the data from Building A is sent to Building C via Building B (Building B is like a datacenter). When we disconnect Building C (stress test by unplugging Building C and disrupting the path) all the LAN components on Building A network lose connectivity. We took wireshark logs on a computer on Building A and found that when we lose the connectivity to Building C, there is a ARP broadcast storm querying about the LAN components on Building A (which is weird, as they should all be talking to each other on the local network) There are no responses from any components from the devices.</p><p>I am happy to share the wireshark logs and the network diagram.</p><p>Thank you for your support</p></div><div id="question-tags" class="tags-container tags">arp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '17, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/dacf3d76298e899d598480e0f72c244b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adityanawab&#39;s gravatar image" /><p>adityanawab<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adityanawab has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '17, 16:17</p></div></div><div id="comments-container-61927" class="comments-container"></div><div id="comment-tools-61927" class="comment-tools"></div><div class="clear"></div><div id="comment-61927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


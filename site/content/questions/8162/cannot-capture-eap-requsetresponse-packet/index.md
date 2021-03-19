+++
type = "question"
title = "cannot capture EAP-requset/response packet"
description = '''I usd wireshark1.6.2 in Ubuntu 11.10 to capture wpa2 authentication packet, but in WPA2-PSK or EAP—TLS authentication methods I only capture EPAOL key switch packet and sequent DHCP、TCP packet ,can not capture eap-request/response packet. Why？How can i solve this problem? '''
date = "2011-12-29T04:05:00Z"
lastmod = "2011-12-29T04:12:00Z"
weight = 8162
keywords = [ "eapol" ]
aliases = [ "/questions/8162" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot capture EAP-requset/response packet](/questions/8162/cannot-capture-eap-requsetresponse-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8162-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I usd wireshark1.6.2 in Ubuntu 11.10 to capture wpa2 authentication packet, but in WPA2-PSK or EAP—TLS authentication methods I only capture EPAOL key switch packet and sequent DHCP、TCP packet ,can not capture eap-request/response packet. Why？How can i solve this problem?</p></div><div id="question-tags" class="tags-container tags">eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '11, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/797614c4f43214b057b31b08f158e5f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zqm0209&#39;s gravatar image" /><p>zqm0209<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zqm0209 has no accepted answers">0%</span></p></div></div><div id="comments-container-8162" class="comments-container"><span id="8183"></span><div id="comment-8183" class="comment"><div id="post-8183-score" class="comment-score"></div><div class="comment-text"><p>it is strange.when I first used EAP-TLS authenticate to the WLAN,I catch the eap-request/response packet,here is the packet: http://sharesend.com/3ks99 but when I reconnect the network,I cannot catch the eap-request/responset frame,even I close the free-radius server and use wrong authentication message,the authentication is still success.Here is the packet file in this situation: http://sharesend.com/lwpga</p><p>My authentication server is free-radius2.1.2,AP is DLink DIR-618,USB wrieless Adapter is TP-Link TL-WN821N.</p></div><div id="comment-8183-info" class="comment-info"><span class="comment-age">(02 Jan '12, 05:14)</span> zqm0209</div></div><span id="8184"></span><div id="comment-8184" class="comment"><div id="post-8184-score" class="comment-score">1</div><div class="comment-text"><p>Try just to reboot your AP, that should force the whole EAP process to renew, I guess your AP kind of "remembers" successful EAP authentication</p></div><div id="comment-8184-info" class="comment-info"><span class="comment-age">(02 Jan '12, 05:29)</span> Landi</div></div><span id="8265"></span><div id="comment-8265" class="comment"><div id="post-8265-score" class="comment-score"></div><div class="comment-text"><p>Thanks.You are right,after reboot my ap, I can capture the packet.</p></div><div id="comment-8265-info" class="comment-info"><span class="comment-age">(07 Jan '12, 04:56)</span> zqm0209</div></div></div><div id="comment-tools-8162" class="comment-tools"></div><div class="clear"></div><div id="comment-8162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8163"></span>

<div id="answer-container-8163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8163-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>WPA2-PSK uses 4 EAPoL Key frames to do the authentication and authorization. After the client successfully exchanges those frames with the AP, DHCP assigns an IP address, so what you see there is perfectly the way it works.</p><p>For EAP-TLS please specify more details about your setup</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '11, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-8163" class="comments-container"></div><div id="comment-tools-8163" class="comment-tools"></div><div class="clear"></div><div id="comment-8163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


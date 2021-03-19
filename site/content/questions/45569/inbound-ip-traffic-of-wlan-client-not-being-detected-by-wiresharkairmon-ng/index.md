+++
type = "question"
title = "Inbound IP traffic of WLAN client not being detected by Wireshark/airmon-ng"
description = '''Hi all I want to debug SIP registration issues with a VoIP client app on my smartphone. If I use this VoIP service via the Twinkle VoIP client on my Linux Mint notebook, it works just fine. So there must be something funny going on in the depths of SIP handshaking on my smartphone. I have initially ...'''
date = "2015-09-01T09:13:00Z"
lastmod = "2015-09-01T09:13:00Z"
weight = 45569
keywords = [ "inbound", "smartphone", "airmon", "voip" ]
aliases = [ "/questions/45569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Inbound IP traffic of WLAN client not being detected by Wireshark/airmon-ng](/questions/45569/inbound-ip-traffic-of-wlan-client-not-being-detected-by-wiresharkairmon-ng)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I want to debug SIP registration issues with a VoIP client app on my smartphone. If I use this VoIP service via the Twinkle VoIP client on my Linux Mint notebook, it works just fine. So there must be something funny going on in the depths of SIP handshaking on my smartphone.</p><p>I have initially installed Wireshark 1.6.7 on the notebook; I could sniff the local SIP handshaking with success, seeing both directions of the handshake.</p><p>To debug SIP handshaking on my smartphone, I additionally installed aircrack-ng to sniff my WLAN. I am using airmon-ng as root, which gives me mon0 port on Wireshark. WLAN traffic is successfully decrypted by Wireshark.</p><p>I see now all SIP REGISTER messages from my smartphone to the Internet, but no SIP answers from the registrar server. If I check other IP traffic, it's the same story, I see all packets with origin 192.168.1.x, but not the other way round.</p><p>How come I can only sniff outbound, but no inbound IP traffic?</p><p>Many thanks in advance for your advice!</p></div><div id="question-tags" class="tags-container tags">inbound smartphone airmon voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/40cd74f886bdf77ab6ecdb293f43d10d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yoyo&#39;s gravatar image" /><p>Yoyo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yoyo has no accepted answers">0%</span></p></div></div><div id="comments-container-45569" class="comments-container"><span id="45570"></span><div id="comment-45570" class="comment"><div id="post-45570-score" class="comment-score"></div><div class="comment-text"><p>Do you have any capture or display filters active in Wireshark?</p></div><div id="comment-45570-info" class="comment-info"><span class="comment-age">(01 Sep '15, 10:07)</span> Amato_C</div></div><span id="45574"></span><div id="comment-45574" class="comment"><div id="post-45574-score" class="comment-score"></div><div class="comment-text"><p>No, all filters are deactivated. When I scanned the notebook's own WLAN port, the settings were the same like for the scan of the smartphone/AP WLAN traffic.</p></div><div id="comment-45574-info" class="comment-info"><span class="comment-age">(01 Sep '15, 11:46)</span> Yoyo</div></div></div><div id="comment-tools-45569" class="comment-tools"></div><div class="clear"></div><div id="comment-45569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


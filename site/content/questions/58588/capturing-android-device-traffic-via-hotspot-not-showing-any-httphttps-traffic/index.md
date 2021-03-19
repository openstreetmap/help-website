+++
type = "question"
title = "Capturing Android device traffic via hotspot, not showing any HTTP/HTTPS traffic"
description = ''' Win 7 laptop with wired internet connection Create a hotspot via connectify in routed mode Android device connected to hotspot Wireshark ran on hotspot interface(Microsoft Virtual WiFi Miniport Adapter)  MDNS, DNS, SSDP, NBNS packets are only shown in the capture, even though I was using multiple a...'''
date = "2017-01-07T21:23:00Z"
lastmod = "2017-01-07T21:23:00Z"
weight = 58588
keywords = [ "android", "packet-capture", "ssdp", "hotspot" ]
aliases = [ "/questions/58588" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Android device traffic via hotspot, not showing any HTTP/HTTPS traffic](/questions/58588/capturing-android-device-traffic-via-hotspot-not-showing-any-httphttps-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58588-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ul><li>Win 7 laptop with wired internet connection</li><li>Create a hotspot via connectify in routed mode</li><li>Android device connected to hotspot</li><li>Wireshark ran on hotspot interface(Microsoft Virtual WiFi Miniport Adapter)</li></ul><p><strong>MDNS, DNS, SSDP, NBNS</strong> packets are only shown in the capture, even though I was using multiple apps that send and receive data over HTTP/HTTPS.</p><p>Why is wireshark not showing any HTTP/HTTPS or any other TCP/UDP traffic ?</p><p>What am I missing here....Help much appreciated.</p><p><strong>Edit 1</strong></p><p>Tried connecting win 8 latop to hotspot. Observation:</p><ul><li>Wireshark still not showing any TCP/UDP or HTTP/HTTPS connections.</li><li>Ran wireshark on the win 8 latop(connected to hotspot), it shows TCP/UDP and HTTP/HTTPS connections.</li></ul><p>So issue must be in capturing the traffic on the laptop on which hotpsot is created.</p></div><div id="question-tags" class="tags-container tags">android packet-capture ssdp hotspot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '17, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/9eebaeef6139596ae0e1ddbecb2f5ec4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikhilgeo&#39;s gravatar image" /><p>nikhilgeo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikhilgeo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '17, 11:15</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58588" class="comments-container"><span id="58593"></span><div id="comment-58593" class="comment"><div id="post-58593-score" class="comment-score"></div><div class="comment-text"><p>You may want to give <a href="https://nmap.org/npcap/">npcap</a> a try.</p></div><div id="comment-58593-info" class="comment-info"><span class="comment-age">(08 Jan '17, 04:53)</span> Jaap ♦</div></div></div><div id="comment-tools-58588" class="comment-tools"></div><div class="clear"></div><div id="comment-58588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


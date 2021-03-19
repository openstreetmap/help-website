+++
type = "question"
title = "Entering promiscuous mode kills ethernet connection"
description = '''Hi! I started with a completely new ubuntu installation (ubuntu-14.04.1lts-lubuntu-odroid-u-20140814). My device is connected with ethernet and I plugged in a wlan stick. I am accessing the computer via vnc (of course via ethernet). Using gnome network manager I connect to my wireless network. When ...'''
date = "2014-10-29T07:19:00Z"
lastmod = "2014-10-29T07:39:00Z"
weight = 37439
keywords = [ "ethernet", "promiscuous", "wlan", "ubuntu" ]
aliases = [ "/questions/37439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Entering promiscuous mode kills ethernet connection](/questions/37439/entering-promiscuous-mode-kills-ethernet-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I started with a completely new ubuntu installation (ubuntu-14.04.1lts-lubuntu-odroid-u-20140814). My device is connected with ethernet and I plugged in a wlan stick. I am accessing the computer via vnc (of course via ethernet).</p><p>Using gnome network manager I connect to my wireless network. When I start Wireshark in promiscuous mode odroid's ethernet connection is lost immediately and of course vnc stops working.</p><p>This is what syslog tells me:</p><pre><code>Oct 30 00:38:02 odroid kernel: [ 1851.202209] wlan2: deauthenticating from blabla by local choice (reason=3)
Oct 30 00:36:35 odroid wpa_supplicant[996]: message repeated 2 times: [ wlan2: CTRL-EVENT-SCAN-STARTED ]
Oct 30 00:38:02 odroid wpa_supplicant[996]: wlan2: CTRL-EVENT-DISCONNECTED bssid=blabla reason=3 locally_generated=1
Oct 30 00:38:02 odroid NetworkManager[610]: &lt;warn&gt; Connection disconnected (reason -3)
Oct 30 00:38:02 odroid kernel: [ 1851.282762] cfg80211: Calling CRDA to update world regulatory domain
Oct 30 00:38:02 odroid avahi-daemon[502]: Interface wlan2.IPv6 no longer relevant for mDNS.
Oct 30 00:38:02 odroid avahi-daemon[502]: Leaving mDNS multicast group on interface wlan2.IPv6 with address blabla.
Oct 30 00:38:02 odroid avahi-daemon[502]: Interface wlan2.IPv4 no longer relevant for mDNS.
Oct 30 00:38:02 odroid avahi-daemon[502]: Leaving mDNS multicast group on interface wlan2.IPv4 with address 192.168.2.152.
Oct 30 00:38:02 odroid dhclient: receive_packet failed on wlan2: Network is down
Oct 30 00:38:03 odroid avahi-daemon[502]: Withdrawing address record for blabla on wlan2.
Oct 30 00:38:03 odroid avahi-daemon[502]: Withdrawing address record for 192.168.2.152 on wlan2.
Oct 30 00:38:03 odroid avahi-daemon[502]: Joining mDNS multicast group on interface wlan2.IPv4 with address 192.168.2.152.
Oct 30 00:38:03 odroid avahi-daemon[502]: New relevant interface wlan2.IPv4 for mDNS.
Oct 30 00:38:03 odroid avahi-daemon[502]: Registering new address record for 192.168.2.152 on wlan2.IPv4.
Oct 30 00:38:03 odroid avahi-daemon[502]: Interface wlan2.IPv4 no longer relevant for mDNS.
Oct 30 00:38:03 odroid avahi-daemon[502]: Leaving mDNS multicast group on interface wlan2.IPv4 with address 192.168.2.152.
Oct 30 00:38:03 odroid avahi-daemon[502]: Withdrawing address record for 192.168.2.152 on wlan2.
Oct 30 00:38:03 odroid kernel: [ 1851.636409] device wlan2 entered promiscuous mode
Oct 30 00:38:03 odroid NetworkManager[610]: &lt;info&gt; (wlan2): supplicant interface state: completed -&gt; scanning
Oct 30 00:38:03 odroid avahi-daemon[502]: Joining mDNS multicast group on interface wlan2.IPv4 with address 192.168.2.152.
Oct 30 00:38:03 odroid avahi-daemon[502]: New relevant interface wlan2.IPv4 for mDNS.
Oct 30 00:38:03 odroid avahi-daemon[502]: Registering new address record for 192.168.2.152 on wlan2.IPv4.
Oct 30 00:38:05 odroid ntpd[1712]: Deleting interface #6 wlan2, blabla#123, interface stats: received=0, sent=0, dropped=0, active_time=1800 secs
Oct 30 00:38:05 odroid ntpd[1712]: peers refreshed
Oct 30 00:07:56 odroid whoopsie[774]: message repeated 5 times: [ online]
Oct 30 00:38:23 odroid whoopsie[774]: offline</code></pre><p>What is happening here and how can I prevent it? Thanks for your help!</p></div><div id="question-tags" class="tags-container tags">ethernet promiscuous wlan ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/9271a3d05ddb400f58241f33a113c20c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badudel&#39;s gravatar image" /><p>Badudel<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badudel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Oct '14, 07:21</p></div></div><div id="comments-container-37439" class="comments-container"></div><div id="comment-tools-37439" class="comment-tools"></div><div class="clear"></div><div id="comment-37439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37441"></span>

<div id="answer-container-37441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37441-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As your platform is a SOC (Odroid), the problems could be related to the ethernet chipset, which seems to be something that's bridging USB to Ethernet !?!</p><blockquote><p><a href="http://www.hardkernel.com/main/products/prdt_info.php?g_code=G138745696275&amp;tab_idx=2">http://www.hardkernel.com/main/products/prdt_info.php?g_code=G138745696275&amp;tab_idx=2</a></p></blockquote><pre><code>HSIC Ethernet controller    LAN9730HSIC USB 2.0 to 10/100 Ethernet controller with HP Auto-MDIX from SMSC/Microchip</code></pre><p>So, if you have problems with your WLAN, especially if that's a USB dongle, it could be related to that chip or the driver.</p><p>I guess you will get a better answer in an Odroid forum, as others might have experienced the same problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Oct '14, 07:45</p></div></div><div id="comments-container-37441" class="comments-container"></div><div id="comment-tools-37441" class="comment-tools"></div><div class="clear"></div><div id="comment-37441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


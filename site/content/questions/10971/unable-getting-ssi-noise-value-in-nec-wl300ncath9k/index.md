+++
type = "question"
title = "Unable Getting SSI noise value in NEC WL300NC(ath9k)"
description = '''now. I want get SSI noise value in Radiotap header by wireshark(on ubuntu 10.04 LTS). but I couldn&#x27;t, so it became useless during the weekend..... Then, there are some questions. 1.how to Get SSI noise value in NEC WL300NC(running with ubuntu 10.04 default ath9k)? 2.The conditions which acquire the ...'''
date = "2012-05-14T14:04:00Z"
lastmod = "2012-05-14T14:04:00Z"
weight = 10971
keywords = [ "radiotap" ]
aliases = [ "/questions/10971" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable Getting SSI noise value in NEC WL300NC(ath9k)](/questions/10971/unable-getting-ssi-noise-value-in-nec-wl300ncath9k)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10971-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>now. I want get SSI noise value in Radiotap header by wireshark(on ubuntu 10.04 LTS). but I couldn't, so it became useless during the weekend..... Then, there are some questions.</p><p>1.how to Get SSI noise value in NEC WL300NC(running with ubuntu 10.04 default ath9k)?</p><p>2.The conditions which acquire the value? (Device,DriverModule,Config..?)</p><p>I already succeeded getting other radiotap values(this card can set to monitor mode). I trid update driver-module (compat-wireless2.6),but result doesn’t change.</p><hr /><p>lspci -nn | grep 'Atheros' 0b:00.0 Network controller [0280]: Atheros Communications Inc. AR5008 Wireless Network Adapter [168c:0023] (rev 01)</p><p>lsmod | grep "ath9k" ath9k 68107 0 ath9k_common 2551 1 ath9k ath9k_hw 223661 2 ath9k,ath9k_common ath 8041 2 ath9k,ath9k_hw led_class 2864 1 ath9k mac80211 225587 4 ath9k,ath9k_common,iwl3945,iwlcore cfg80211 144778 6 ath9k,ath9k_common,ath,iwl3945,iwlcore,mac80211</p><p>sudo lshw -C network <em>-network DISABLED description: Wireless interface product: PRO/Wireless 3945ABG [Golan] Network Connection vendor: Intel Corporation physical id: 0 bus info: [email protected]:06:00.0 logical name: wlan0 version: 02 serial: 00:19:d2:aa:bf:## width: 32 bits clock: 33MHz capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless configuration: broadcast=yes driver=iwl3945 driverversion=2.6.32-41-generic-pae firmware=15.32.2.9 latency=0 link=yes multicast=yes wireless=IEEE 802.11abg resources: irq:28 memory:cc000000-cc000fff</em> -network description: Ethernet interface product: PRO/100 VE Network Connection vendor: Intel Corporation physical id: 8 bus info: [email protected]:0a:08.0 logical name: eth0 version: 02 serial: 00:1a:80:08:d9:## size: 100MB/s capacity: 100MB/s width: 32 bits clock: 33MHz capabilities: pm bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd autonegotiation configuration: autonegotiation=on broadcast=yes driver=e100 driverversion=3.5.24-k2-NAPI duplex=full firmware=N/A ip=192.168.1.4 latency=64 link=yes maxlatency=56 mingnt=8 multicast=yes port=MII speed=100MB/s resources: irq:20 memory:d0005000-d0005fff ioport:6000(size=64) *-network description: Wireless interface product: AR5008 Wireless Network Adapter vendor: Atheros Communications Inc. physical id: 2 bus info: [email protected]:0b:00.0 logical name: wlan1 version: 01 serial: 00:0d:02:3b:54:## width: 32 bits clock: 66MHz capabilities: bus_master cap_list ethernet physical wireless configuration: broadcast=yes driver=ath9k driverversion=2.6.32-41-generic-pae firmware=N/A latency=168 link=no multicast=yes wireless=IEEE 802.11abgn resources: irq:16 memory:48000000-4800ffff</p><p>lsb_release -d Description: Ubuntu 10.04.4 LTS</p><p>uname -mr 2.6.32-41-generic-pae i686</p></div><div id="question-tags" class="tags-container tags">radiotap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '12, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/bb3b3c47982b3b6cb9aeb04ab8182963?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdcmtd&#39;s gravatar image" /><p>sdcmtd<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdcmtd has no accepted answers">0%</span></p></div></div><div id="comments-container-10971" class="comments-container"></div><div id="comment-tools-10971" class="comment-tools"></div><div class="clear"></div><div id="comment-10971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "Kali Linux,Wireshark,Monitor mode and others..."
description = '''Hello guys,yesterday I tried to &quot;sniff&quot; some network packets so as to find out passwords from my Laptop and from others devices in my network, At first from my laptop works perfectly,I just had to select the correct interface(eth0,wlan0,any).After that I was about to try do the same thing so as to c...'''
date = "2016-08-28T05:02:00Z"
lastmod = "2016-08-28T07:44:00Z"
weight = 55145
keywords = [ "monitor-mode", "kali-linux", "wireshark" ]
aliases = [ "/questions/55145" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Kali Linux,Wireshark,Monitor mode and others...](/questions/55145/kali-linuxwiresharkmonitor-mode-and-others)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55145-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,yesterday I tried to "sniff" some network packets so as to find out passwords from my Laptop and from others devices in my network, At first from my laptop works perfectly,I just had to select the correct interface(eth0,wlan0,any).After that I was about to try do the same thing so as to catch the password from my phone! But it didn't worked! I choose at first wlan0,after that eth0(because I connect my laptop with ethernet cable as well due to disconnections) and at the end I tried the "any" interface.Nothing! I did a little research and I came accross the "monitor mode".I see what it is and where it is used so I searched how to enable it in my laptop so as I could do my job! I opened a terminal and typed in:</p><pre><code>airmon-ng check kill</code></pre><p>I read that I should kill all processes before enabling monitor mode and if I do not,then I get an message in the terminal I get this output:</p><pre><code>Killing these processes:

  PID Name
  786 wpa_supplicant
  798 dhclient
 2201 avahi-daemon-ch</code></pre><p>Then my wifi isn't working and I could connect to the internet only through ethernet! Then type in the terminal</p><pre><code>airmon-ng start wlan0</code></pre><p>The output I get after typing that command is:</p><pre><code>PHY Interface   Driver      Chipset

phy0    wlan0       rtl8723be   Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter

        (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
        (mac80211 station mode vif disabled for [phy0]wlan0)</code></pre><p>Internet stills working only when laptop is connected with ethernet cable. What's more in Wireshark,in the interface list the "wlan0" is renamed in "wlan0mon". No "Monitor Mode" checkbox appears in Wireshark. I have again Internet access through wifi only when I type in the terminal:</p><pre><code>service network-manager start</code></pre><p>But the wlan0mon interface in Wireshark doesn't see any packets even if I am using my wifi with my laptop and my phone!</p><p>At the end,if I type in terminal:</p><pre><code>airmon-ng stop wlan0mon</code></pre><p>I get output:</p><pre><code>PHY Interface   Driver      Chipset

phy0    wlan0mon    rtl8723be   Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter

You are trying to stop a device that isn&#39;t in monitor mode.
Doing so is a terrible idea, if you really want to do it then you
need to type &#39;iw wlan0mon del&#39; yourself since it is a terrible idea.
Most likely you want to remove an interface called wlan[0-9]mon
If you feel you have reached this warning in error,
please report it.</code></pre><p>My wireless network card is: Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter. I am currently running Kali Linux 2 Rolling Edition. Please HELP! What should I do?? Thanks :)</p></div><div id="question-tags" class="tags-container tags">monitor-mode kali-linux wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/4e26f42417b6c5a52e66bb361c3e6caf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yotta51&#39;s gravatar image" /><p>Yotta51<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yotta51 has no accepted answers">0%</span></p></div></div><div id="comments-container-55145" class="comments-container"><span id="55146"></span><div id="comment-55146" class="comment"><div id="post-55146-score" class="comment-score"></div><div class="comment-text"><p>no one have an answer? :/</p></div><div id="comment-55146-info" class="comment-info"><span class="comment-age">(28 Aug '16, 06:30)</span> Yotta51</div></div></div><div id="comment-tools-55145" class="comment-tools"></div><div class="clear"></div><div id="comment-55145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55147"></span>

<div id="answer-container-55147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't have enough points to move your answer to a comment.</p><p>Since this is related to a specific software product which sin't Wireshark, I suggest you start there:</p><p><a href="http://www.aircrack-ng.org/">http://www.aircrack-ng.org/</a></p><p>They have a forum and I suggest you post there. It's been down for a couple of days but when it returns that will be your best place to learn how to use that software.</p><p>It's possible to put the interface in monitor mode without those scripts so if they are causing you problems perhaps you could try an alternate method.</p><p>Some commands that could be used:</p><ul><li>iwconfig</li><li>iw</li></ul><p>You should expect to lose network connectivity through the WiFi interface when you put it into monitor mode. There are advanced ways to add a virtual interface to the phy, as a prototype:</p><p>iw dev &lt;devname&gt; interface add &lt;name&gt; type &lt;type&gt;</p><p>There is plenty of documentation in the man pages or on google and this could let you use the interface for network access as well as monitor mode. Look out for the Realtek regression with promiscuous mode which cycled through Kali rolling earlier this year. There are plenty of notes on this site about it if you run into it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '16, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-55147" class="comments-container"><span id="55148"></span><div id="comment-55148" class="comment"><div id="post-55148-score" class="comment-score"></div><div class="comment-text"><p>Thank's for the answer! I came across the aircrack-ng forum before and I saw that it didn't worked. I have also tried the iwconfig wlan0 mode monitor command and did not get anything at the wireshark screen that I could use for my purpose. Every answer is useful so if someone could help me more... :)</p></div><div id="comment-55148-info" class="comment-info"><span class="comment-age">(28 Aug '16, 09:33)</span> Yotta51</div></div></div><div id="comment-tools-55147" class="comment-tools"></div><div class="clear"></div><div id="comment-55147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


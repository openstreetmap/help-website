+++
type = "question"
title = "Capture SNR value using tcpdump"
description = '''Hi everyone. Does anybody know how to capture SNR value of a WiFi link using tcpdump? I tried capturing using wireshark by showing the signal and noise but those values never exists during capturing. Thanks'''
date = "2013-04-24T22:15:00Z"
lastmod = "2013-05-08T20:29:00Z"
weight = 20789
keywords = [ "snr" ]
aliases = [ "/questions/20789" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture SNR value using tcpdump](/questions/20789/capture-snr-value-using-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20789-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone. Does anybody know how to capture SNR value of a WiFi link using tcpdump? I tried capturing using wireshark by showing the signal and noise but those values never exists during capturing. Thanks</p></div><div id="question-tags" class="tags-container tags">snr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 22:15</strong></p><img src="https://secure.gravatar.com/avatar/a3291ae3aa2fd3100059945d1afa121c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tyanium&#39;s gravatar image" /><p>Tyanium<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tyanium has no accepted answers">0%</span></p></div></div><div id="comments-container-20789" class="comments-container"><span id="20813"></span><div id="comment-20813" class="comment"><div id="post-20813-score" class="comment-score"></div><div class="comment-text"><p>What version of what OS is this? (For Linux, that means both "what version of the kernel" and "what distribution and what version of that distribution".)</p><p>What does <code>tcpdump -h</code> print?</p></div><div id="comment-20813-info" class="comment-info"><span class="comment-age">(25 Apr '13, 18:59)</span> Guy Harris ♦♦</div></div><span id="21044"></span><div id="comment-21044" class="comment"><div id="post-21044-score" class="comment-score"></div><div class="comment-text"><p>This is what printed after tcpdump -h</p><pre><code>tcpdump version 3.9.8
libpcap version 0.9.8</code></pre><p>Im using fedora release 9 with kernel version 2.6.27.25-78.2.56.fc9.i686</p></div><div id="comment-21044-info" class="comment-info"><span class="comment-age">(08 May '13, 20:00)</span> Tyanium</div></div></div><div id="comment-tools-20789" class="comment-tools"></div><div class="clear"></div><div id="comment-20789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20791"></span>

<div id="answer-container-20791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing WiFi traffic including the 802.11 layer requires a little more preparation, especially on Windows (which may not be the OS in your case since you mentioned tcpdump) where you need to have an AirPCAP USB adapter to do it. See this Wiki page: <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>I'm not sure if TCPdump is capable of capturing the radio layer, but there are tools like <a href="http://www.aircrack-ng.org/doku.php?id=airodump-ng">airodump-ng</a> that could help you out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '13, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20791" class="comments-container"><span id="21047"></span><div id="comment-21047" class="comment"><div id="post-21047-score" class="comment-score"></div><div class="comment-text"><p>tcpdump can capture the radio layer, but, on most OSes, you have to be in monitor mode to do that, and his libpcap and tcpdump are too old to support having tcpdump do it with the <code>-I</code> flag.</p></div><div id="comment-21047-info" class="comment-info"><span class="comment-age">(08 May '13, 20:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-20791" class="comment-tools"></div><div class="clear"></div><div id="comment-20791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21046"></span>

<div id="answer-container-21046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21046-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to put your adapter into monitor mode in order to get the radio information. Try using the <a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">airmon-ng</a> script from <a href="http://www.aircrack-ng.org">aircrack-ng</a>; there might be a Fedora 9 RPM for aircrack-ng.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21046" class="comments-container"><span id="21161"></span><div id="comment-21161" class="comment"><div id="post-21161-score" class="comment-score"></div><div class="comment-text"><p>Now I put my computer in monitor mode already. But when I try to capture packets, this is what happen:</p><pre><code>tcpdump -U -w ./test.cap
tcpdump: WARNING: eth0: no IPv4 address assigned
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes
^C0 packets captured
tcpdump -L -i ath0
tcpdump: bind: Network is down</code></pre><p>My goal is to capture SINR value of a wifi channel. Do u have any idea what's going on? And please guide me to achieve my goal. Thanks</p></div><div id="comment-21161-info" class="comment-info"><span class="comment-age">(15 May '13, 21:21)</span> Tyanium</div></div><span id="21162"></span><div id="comment-21162" class="comment"><div id="post-21162-score" class="comment-score"></div><div class="comment-text"><blockquote><p><code>tcpdump: WARNING: eth0: no IPv4 address assigned</code></p></blockquote><p>So that was capturing on <code>eth0</code>. Is that your Wi-Fi adapter?</p><p>Also:</p><blockquote><p><code>tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 96 bytes</code></p></blockquote><p>Sadly, this is an old version of tcpdump, which defaults (when it supports IPv6) to a snapshot length of 96 bytes. Try doing <code>-s 0</code> as part of your tcpdump argument list, to capture the <em>entire</em> packet (the radiotap header might not fit in 96 bytes).</p></div><div id="comment-21162-info" class="comment-info"><span class="comment-age">(15 May '13, 21:31)</span> Guy Harris ♦♦</div></div><span id="21164"></span><div id="comment-21164" class="comment"><div id="post-21164-score" class="comment-score"></div><div class="comment-text"><p>Thank for your comment. I tried again yet still not working. No packets are captured.</p><p>[[email protected] ~]# tcpdump -s 0 -i ath0 tcpdump: bind: Network is down [[email protected] ~]# tcpdump -s 0 -i wifi0 tcpdump: WARNING: wifi0: no IPv4 address assigned tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on wifi0, link-type IEEE802_11 (802.11), capture size 65535 bytes ^C 0 packets captured 0 packets received by filter 0 packets dropped by kernel</p></div><div id="comment-21164-info" class="comment-info"><span class="comment-age">(15 May '13, 22:22)</span> Tyanium</div></div><span id="21168"></span><div id="comment-21168" class="comment"><div id="post-21168-score" class="comment-score"></div><div class="comment-text"><p>I still don't get it, I put ath0 in monitor mode already but once typing tcpdump using ath0 it won't work</p><p>[[email protected] ~]# iwconfig lo no wireless extensions.</p><p>eth0 no wireless extensions.</p><p>wifi0 no wireless extensions.</p><p>pan0 no wireless extensions.</p><p>ath0 IEEE 802.11g ESSID:"" Nickname:"" Mode:Monitor Channel:0 Access Point: Not-Associated<br />
Bit Rate:0 kb/s Tx-Power:18 dBm Sensitivity=1/1<br />
Retry:off RTS thr:off Fragment thr:off Encryption key:off Power Management:off Link Quality=0/70 Signal level=-98 dBm Noise level=-98 dBm Rx invalid nwid:0 Rx invalid crypt:0 Rx invalid frag:0 Tx excessive retries:0 Invalid misc:0 Missed beacon:0</p><p>[[email protected] ~]# tcpdump -i ath0 -s 0 -w stress.pcap tcpdump: bind: Network is down</p></div><div id="comment-21168-info" class="comment-info"><span class="comment-age">(15 May '13, 23:07)</span> Tyanium</div></div></div><div id="comment-tools-21046" class="comment-tools"></div><div class="clear"></div><div id="comment-21046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


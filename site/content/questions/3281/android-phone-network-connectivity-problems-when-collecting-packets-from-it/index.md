+++
type = "question"
title = "android phone network connectivity problems when collecting packets from it"
description = '''while collecting wifi packets from my mobile phone (from a linux vm running wireshark on my laptop), I noticed, while collecting packets, the phone began having difficulty connecting to various network services (IMAP, Activesync, pings to local network and remote addresses...etc). Once I stopped col...'''
date = "2011-04-01T21:11:00Z"
lastmod = "2011-04-02T13:48:00Z"
weight = 3281
keywords = [ "android", "wireshark", "ubuntu" ]
aliases = [ "/questions/3281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [android phone network connectivity problems when collecting packets from it](/questions/3281/android-phone-network-connectivity-problems-when-collecting-packets-from-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3281-score" class="post-score" title="current number of votes">0</div><span id="post-3281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>while collecting wifi packets from my mobile phone (from a linux vm running wireshark on my laptop), I noticed, while collecting packets, the phone began having difficulty connecting to various network services (IMAP, Activesync, pings to local network and remote addresses...etc). Once I stopped collecting packets, the phone network operations began operating normally. This was repeatable. Any idea what is causing the phone TCP/IP problems while collecting packets via wireshark ?</p><p>Some additional detail: wireshark 1.2.11 Ubuntu 10.10 WPA2 PSK Android IP 192.168.200.112</p><p>wlan1 IEEE 802.11bgn Mode:Monitor Tx-Power=27 dBm<br />
Retry long limit:7 RTS thr:off Fragment thr:off Power Management:off</p><p>My wifi adapter for capturing is a NETGEAR WN111 v2 300Mbps 802.11n Wireless LAN USB 2.0 Adapter</p><p>thanks Tim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '11, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/1f57db2555deb37f42ec181a0dd9d438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Clement&#39;s gravatar image" /><p><span>Tim Clement</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Clement has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '11, 21:17</strong> </span></p></div></div><div id="comments-container-3281" class="comments-container"><span id="3284"></span><div id="comment-3284" class="comment"><div id="post-3284-score" class="comment-score"></div><div class="comment-text"><p>I see a lot of TCP DUP ACK ; TCP Retransmission ; TCP Out-of-order packets when using a display filter of ip.addr==192.168.200.112</p></div><div id="comment-3284-info" class="comment-info"><span class="comment-age">(01 Apr '11, 21:32)</span> <span class="comment-user userinfo">Tim Clement</span></div></div><span id="3292"></span><div id="comment-3292" class="comment"><div id="post-3292-score" class="comment-score"></div><div class="comment-text"><p>further testing ; using wireshark 1.4.4 on my laptop (no vm involved) and using an AirPcap adapter ; there is no affect upon the phone's network connections when capturing packets</p></div><div id="comment-3292-info" class="comment-info"><span class="comment-age">(02 Apr '11, 13:45)</span> <span class="comment-user userinfo">Tim Clement</span></div></div><span id="3294"></span><div id="comment-3294" class="comment"><div id="post-3294-score" class="comment-score"></div><div class="comment-text"><p>The TCP DUP ACK ; TCP Retransmission ; TCP Out-of-order packets don't appear to be related since I still see them</p></div><div id="comment-3294-info" class="comment-info"><span class="comment-age">(02 Apr '11, 13:48)</span> <span class="comment-user userinfo">Tim Clement</span></div></div></div><div id="comment-tools-3281" class="comment-tools"></div><div class="clear"></div><div id="comment-3281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


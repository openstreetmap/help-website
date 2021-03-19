+++
type = "question"
title = "Can&#x27;t capture packets on Wi-Fi"
description = '''Hi, I have a problem capturing packets on my wi-fi device. I have 2 computers - the first one is an access point and it sends a signal to the second computer. The signal is protected with wpa-psk password. Wireshark is installed on the first computer on which I want to see packets from the second co...'''
date = "2013-10-31T13:51:00Z"
lastmod = "2013-11-01T06:58:00Z"
weight = 26603
keywords = [ "capture", "wifi", "packets" ]
aliases = [ "/questions/26603" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't capture packets on Wi-Fi](/questions/26603/cant-capture-packets-on-wi-fi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26603-score" class="post-score" title="current number of votes">0</div><span id="post-26603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a problem capturing packets on my wi-fi device.</p><p>I have 2 computers - the first one is an access point and it sends a signal to the second computer. The signal is protected with wpa-psk password. Wireshark is installed on the first computer on which I want to see packets from the second computer. But I don't see them and I don't know why.</p><p>A step by step description of what I did:</p><ul><li><p>Reinstalled Windows 7 (64-bit). Installed 64-bit Wireshark and that add-on thingy that comes with it. In Wireshark's Interface List there was only Local Area Connection because Windows didn't recognize my USB wi-fi adapter. Downloaded and installed appropriate wi-fi driver and after that Wireshark added Wireless Network Connection to the Interface list. Promiscuous mode was turned on by default.</p></li><li><p>edit -&gt; preferences -&gt; capture -&gt; default interface: wi-fi device</p></li><li><p>protocols -&gt; IEE 802.11: entered both wpa-psk and wpa-pwd keys and checkhed enable decryption</p></li></ul><p>After I click "Start", Wireshark receives packets only for Local Area Connection. There are 0 packets coming for my wi-fi device and I don't know why. I can choose to see Local Area Connection traffic, but it only shows traffic on my computer and I don't want that. Btw, the icon of my Wireless Network Connection in Wireshark is the same as of Local Area Connection (I think it should have an icon of antenna)...</p><p>Additional info:</p><ul><li><p>Wi-fi device: TP-Link TL-WN722N (Atheros chipset), driver downloaded from official website</p></li><li><p>Network adapter: NVIDIA nForce 10/100 Mbps Ethernet</p></li><li><p>I have tried Wireshark on Linux Ubuntu on the same computer and it worked without any problem, but now I deleted Linux and have only Windows left, and I need it for Windows. I am a newbie with Wireshark, so I apologize if this is trivial question, but I tried many things and nothing made it work, so I ask here. Any help appreciated!</p></li></ul><p>ip config (copy/paste):</p><p>Windows IP Configuration</p><p>Wireless LAN adapter Wireless Network Connection:</p><p>Media State . . . . . . . . . . . : Media disconnected Connection-specific DNS Suffix . :</p><p>Ethernet adapter Local Area Connection:</p><p>Connection-specific DNS Suffix . : Link-local IPv6 Address . . . . . : fe80::20df:7d9e:ed40:91ae%11 IPv4 Address. . . . . . . . . . . : 192.168.1.100 Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 192.168.1.1</p><p>Tunnel adapter isatap.{8353D0C0-BDC2-407A-B67D-1C43CE182F41}:</p><p>Media State . . . . . . . . . . . : Media disconnected Connection-specific DNS Suffix . :</p><p>Tunnel adapter Local Area Connection* 9:</p><p>Connection-specific DNS Suffix . : IPv6 Address. . . . . . . . . . . : 2001:0:9d38:6abd:1811:6551:43fd:f38e Link-local IPv6 Address . . . . . : fe80::1811:6551:43fd:f38e%13 Default Gateway . . . . . . . . . : ::</p><p>Tunnel adapter isatap.{170C612B-CC07-4916-9E68-82EFDB3ED1EA}:</p><p>Media State . . . . . . . . . . . : Media disconnected Connection-specific DNS Suffix . :</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '13, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/412b10652e55b9c4d3cc5243b7b58d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myrddin&#39;s gravatar image" /><p><span>myrddin</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myrddin has no accepted answers">0%</span></p></div></div><div id="comments-container-26603" class="comments-container"></div><div id="comment-tools-26603" class="comment-tools"></div><div class="clear"></div><div id="comment-26603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26604"></span>

<div id="answer-container-26604" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26604-score" class="post-score" title="current number of votes">0</div><span id="post-26604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>... Windows ...</p></blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Windows">Wi-Fi capturing doesn't work well on Windows with WinPcap</a>, and Wireshark uses WinPcap to do capturing. You'd need an AirPcap card or need to run Linux or *BSD.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26604" class="comments-container"><span id="26612"></span><div id="comment-26612" class="comment"><div id="post-26612-score" class="comment-score"></div><div class="comment-text"><p>Are you sure it is because of Windows? Because there is a version of Wireshark specifically designed to work under Windows and if it wouldn't work why would they put it on their website. But hey, what do I know...</p></div><div id="comment-26612-info" class="comment-info"><span class="comment-age">(01 Nov '13, 05:41)</span> <span class="comment-user userinfo">myrddin</span></div></div><span id="26614"></span><div id="comment-26614" class="comment"><div id="post-26614-score" class="comment-score"></div><div class="comment-text"><p>Did you look at the link posted by Guy? It explains all the issues.</p></div><div id="comment-26614-info" class="comment-info"><span class="comment-age">(01 Nov '13, 05:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26615"></span><div id="comment-26615" class="comment"><div id="post-26615-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and if it wouldn't work why would they put it on their website</p></blockquote><p>I guess one of those guys who put it on 'their' website <strong>is</strong> <span>@Guy Harris</span> ;-))</p></div><div id="comment-26615-info" class="comment-info"><span class="comment-age">(01 Nov '13, 05:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26618"></span><div id="comment-26618" class="comment"><div id="post-26618-score" class="comment-score"></div><div class="comment-text"><p>Oh OK, I guess he knows his stuff then :)</p><p>So, Linux, we meet again.</p></div><div id="comment-26618-info" class="comment-info"><span class="comment-age">(01 Nov '13, 06:58)</span> <span class="comment-user userinfo">myrddin</span></div></div></div><div id="comment-tools-26604" class="comment-tools"></div><div class="clear"></div><div id="comment-26604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


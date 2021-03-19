+++
type = "question"
title = "Monitor mode problems"
description = '''Hello, I have recently been having trouble with monitor mode on wireshark in Kali Linux. Here&#x27;s what happens: On Wireshark I select the capture interface eth1, I then double-click it and change the mode to monitor, I click ok and go START CAPTURE.  I then get the error message: The capture session c...'''
date = "2013-08-14T03:15:00Z"
lastmod = "2013-08-30T12:48:00Z"
weight = 23769
keywords = [ "error", "monitor", "mode" ]
aliases = [ "/questions/23769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor mode problems](/questions/23769/monitor-mode-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23769-score" class="post-score" title="current number of votes">0</div><span id="post-23769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have recently been having trouble with monitor mode on wireshark in Kali Linux. Here's what happens: On Wireshark I select the capture interface eth1, I then double-click it and change the mode to monitor, I click ok and go START CAPTURE. I then get the error message: The capture session could not be initiated (eth1 SIOCGIWPRIV: Argument list too long) Please check that you have sufficient permissions, and that you have a proper interface or pipe selected. Next when I go to change I back to promiscuous mode the monitor mode checkbox is greyed out so that I cannot un-check it. Any help would be much appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '13, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/91c0ffe139bd5018f5b7a8c58c7c04ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Programmer&#39;s gravatar image" /><p><span>Programmer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Programmer has no accepted answers">0%</span></p></div></div><div id="comments-container-23769" class="comments-container"></div><div id="comment-tools-23769" class="comment-tools"></div><div class="clear"></div><div id="comment-23769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23787"></span>

<div id="answer-container-23787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23787-score" class="post-score" title="current number of votes">0</div><span id="post-23787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The capture session could not be initiated (eth1 SIOCGIWPRIV: Argument list too long)</p></blockquote><p>That's a libpcap issue, in libpcap's somewhat tangled and complicated code required on Linux to turn monitor mode on. I'll look into it; what type of Wi-Fi adapter do you have, and what version of the Linux kernel are you running (what does the command <code>uname -sr</code> print?)?</p><blockquote><p>Any help would be much appreciated.</p></blockquote><p>Workaround: try using the <a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">airmon-ng</a> script from aircrack-ng (which I strongly suspect is part of Kali Linux, given Kali Linux's purpose) to turn monitor mode on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 20:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23787" class="comments-container"><span id="23790"></span><div id="comment-23790" class="comment"><div id="post-23790-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the fast response, uname sr prints:Linux 3.7-trunk-686-pae I have a wireless connection to a bt home hub. The command airmon-ng start eth1 prints this: Found 3 processes that could cause trouble. If airodump-ng, aireplay-ng or airtun-ng stops working after a short period of time, you may want to kill (some of) them! -e PID Name 2117 NetworkManager 2215 wpa_supplicant 2333 dhclient Process with PID 2333 (dhclient) is running on interface eth1</p><p>Interface Chipset Driver</p><p>eth1 Intel 2200BG/2915ABG ipw2200 - [phy0]mon0: ERROR while getting interface flags: No such device</p><pre><code>            (monitor mode enabled on mon0)</code></pre><p>I have enabled monitor mode on eth1 using the command line as well.</p></div><div id="comment-23790-info" class="comment-info"><span class="comment-age">(15 Aug '13, 00:54)</span> <span class="comment-user userinfo">Programmer</span></div></div><span id="23875"></span><div id="comment-23875" class="comment"><div id="post-23875-score" class="comment-score"></div><div class="comment-text"><p>It still doesn't work. Help please ;(</p></div><div id="comment-23875-info" class="comment-info"><span class="comment-age">(20 Aug '13, 05:27)</span> <span class="comment-user userinfo">Programmer</span></div></div><span id="23876"></span><div id="comment-23876" class="comment"><div id="post-23876-score" class="comment-score"></div><div class="comment-text"><blockquote><p>you may want to kill (some of) them! -e PID Name 2117 NetworkManager 2215 wpa_supplicant 2333 dhclient Process with PID 2333 (dhclient) is running on interface eth1</p></blockquote><p>you cannot use a Wifi interface to connect to a wireless network <strong>and</strong> have it in monitor mode. Please remove the interface from the Network Manager and then try again.</p></div><div id="comment-23876-info" class="comment-info"><span class="comment-age">(20 Aug '13, 08:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23879"></span><div id="comment-23879" class="comment"><div id="post-23879-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>you cannot use a Wifi interface to connect to a wireless network and have it in monitor mode.</p></blockquote><p>Depends on the interface and the OS; the (Broadcom-based) interface on my MacBook Pro can, at least under OS X, go into monitor mode and still remain associated with a network.</p></div><div id="comment-23879-info" class="comment-info"><span class="comment-age">(20 Aug '13, 10:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23880"></span><div id="comment-23880" class="comment"><div id="post-23880-score" class="comment-score"></div><div class="comment-text"><p>Ah, good to know. I rather have problems with that on Linux.</p></div><div id="comment-23880-info" class="comment-info"><span class="comment-age">(20 Aug '13, 10:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23905"></span><div id="comment-23905" class="comment not_top_scorer"><div id="post-23905-score" class="comment-score"></div><div class="comment-text"><p>you cannot use a Wifi interface to connect to a wireless network and have it in monitor mode. Please remove the interface from the Network Manager and then try again. I am kind of new to Kali Linux and wireshark, could you please be more specific or tell me how. :)</p></div><div id="comment-23905-info" class="comment-info"><span class="comment-age">(21 Aug '13, 05:08)</span> <span class="comment-user userinfo">Programmer</span></div></div><span id="24211"></span><div id="comment-24211" class="comment not_top_scorer"><div id="post-24211-score" class="comment-score"></div><div class="comment-text"><p>So the problem still persists..... help please :(</p></div><div id="comment-24211-info" class="comment-info"><span class="comment-age">(30 Aug '13, 12:48)</span> <span class="comment-user userinfo">Programmer</span></div></div></div><div id="comment-tools-23787" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-23787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


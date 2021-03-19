+++
type = "question"
title = "&quot;failed to set hardware filter to promiscuous mode&quot; error when capture attempted on a wireless adapter on Windows"
description = '''When i run WireShark, this one Popup. The capture session could not be initiated (failed to set hardware filter to promiscuous mode). Please check that &quot;DeviceNPF_{62909DBD-56C7-48BB-B75B-EC68FF237032}&quot; is the proper interface. Help can be found at:  http://wiki.wireshark.org/WinPcap  http://wiki.wi...'''
date = "2011-03-03T06:46:00Z"
lastmod = "2011-03-03T11:51:00Z"
weight = 2647
keywords = [ "lancard", "errors", "wireshark" ]
aliases = [ "/questions/2647" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["failed to set hardware filter to promiscuous mode" error when capture attempted on a wireless adapter on Windows](/questions/2647/failed-to-set-hardware-filter-to-promiscuous-mode-error-when-capture-attempted-on-a-wireless-adapter-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2647-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i run WireShark, this one Popup.</p><p>The capture session could not be initiated (failed to set hardware filter to promiscuous mode). Please check that "DeviceNPF_{62909DBD-56C7-48BB-B75B-EC68FF237032}" is the proper interface. Help can be found at: http://wiki.wireshark.org/WinPcap http://wiki.wireshark.org/CaptureSetup What should I do for it?</p></div><div id="question-tags" class="tags-container tags">lancard errors wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '11, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/41da58c7ab0112ba05406da70f9ea168?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taehunzzang&#39;s gravatar image" /><p>taehunzzang<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taehunzzang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '11, 23:21</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-2647" class="comments-container"><span id="2649"></span><div id="comment-2649" class="comment"><div id="post-2649-score" class="comment-score"></div><div class="comment-text"><p>wireless card ?</p></div><div id="comment-2649-info" class="comment-info"><span class="comment-age">(03 Mar '11, 08:46)</span> Landi</div></div></div><div id="comment-tools-2647" class="comment-tools"></div><div class="clear"></div><div id="comment-2647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2653"></span>

<div id="answer-container-2653" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2653-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>If (as Landi suggested) this is a wireless adapter, some of them don't support promiscuous mode on Windows. Try un-checking the "Promiscuous mode" checkbox in the "Capture options" dialog box.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '11, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2653" class="comments-container"><span id="2655"></span><div id="comment-2655" class="comment"><div id="post-2655-score" class="comment-score"></div><div class="comment-text"><p>I use wireless card. I tried "un-checking the "Promiscuous mode" checkbox in the "Capture options" dialog box." It work. Thank you Guy Harris and PaulStewart.</p></div><div id="comment-2655-info" class="comment-info"><span class="comment-age">(03 Mar '11, 14:44)</span> taehunzzang</div></div><span id="2656"></span><div id="comment-2656" class="comment"><div id="post-2656-score" class="comment-score"></div><div class="comment-text"><p>One of my laptops does that, but it doesn't produce the error. It simply doesn't capture anything.</p></div><div id="comment-2656-info" class="comment-info"><span class="comment-age">(03 Mar '11, 16:10)</span> Paul Stewart</div></div><span id="2658"></span><div id="comment-2658" class="comment"><div id="post-2658-score" class="comment-score"></div><div class="comment-text"><p>Yes, that's driver-dependent - some drivers explicitly reject attempts to set promiscuous mode, others just go into a mode, or put the adapter into a mode, where nothing is captured. <a href="http://www.wireshark.org/faq.html#q8.7">A question in the Wireshark FAQ</a> and <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#windows">an item in the CaptureSetup/WLAN page in the Wireshark Wiki</a> both mention this.</p></div><div id="comment-2658-info" class="comment-info"><span class="comment-age">(03 Mar '11, 23:20)</span> Guy Harris ♦♦</div></div><span id="2671"></span><div id="comment-2671" class="comment"><div id="post-2671-score" class="comment-score"></div><div class="comment-text"><p>I am having the same error. I have an IEEE 802.11n wireless card on my WinVista 64-bit system. I have downloaded the latest versions of Wireshark and WinPcap. Can you please explain how can i try disabling the promiscuous mode? Under Capture options i do not see that option. Capturing packets does work if I use the LAN connection but i would like this other option to work. Is this supported?</p></div><div id="comment-2671-info" class="comment-info"><span class="comment-age">(04 Mar '11, 21:10)</span> elirqv76</div></div><span id="2672"></span><div id="comment-2672" class="comment"><div id="post-2672-score" class="comment-score"></div><div class="comment-text"><p>I finally was able to disable the promiscuous mode and i can capture!Thank you.</p></div><div id="comment-2672-info" class="comment-info"><span class="comment-age">(04 Mar '11, 21:16)</span> elirqv76</div></div><span id="6225"></span><div id="comment-6225" class="comment not_top_scorer"><div id="post-6225-score" class="comment-score"></div><div class="comment-text"><p>For me I do receive packet captures when I uncheck promiscuous mode, but I question if I am reaching full capabilities by running this way.</p></div><div id="comment-6225-info" class="comment-info"><span class="comment-age">(08 Sep '11, 21:36)</span> wshrkmkn</div></div><span id="6233"></span><div id="comment-6233" class="comment not_top_scorer"><div id="post-6233-score" class="comment-score"></div><div class="comment-text"><p>If you're not in promiscuous mode, you're only capturing traffic sent by or to your machine, and broadcast and multicast packets seen by your machine. If you want to capture traffic between other machines on your wireless network, you'd need to capture in monitor mode, which WinPcap currently doesn't support (and couldn't support on Windows XP or earlier).</p></div><div id="comment-6233-info" class="comment-info"><span class="comment-age">(09 Sep '11, 09:39)</span> Guy Harris ♦♦</div></div><span id="6848"></span><div id="comment-6848" class="comment not_top_scorer"><div id="post-6848-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip, the Capture option had "Capture packet in promiscuous mode", just uncheck and wireshark be ready to capture in wireless adapter.</p><p>Great help!!</p></div><div id="comment-6848-info" class="comment-info"><span class="comment-age">(11 Oct '11, 10:09)</span> Eliodoro</div></div><span id="50260"></span><div id="comment-50260" class="comment not_top_scorer"><div id="post-50260-score" class="comment-score"></div><div class="comment-text"><p>I disabled the promiscuous mode in capture options, but still Im seeing this issue.</p><p>Im trying with Atheros Card with latest wireshark 2.0</p></div><div id="comment-50260-info" class="comment-info"><span class="comment-age">(17 Feb '16, 02:59)</span> Deepak Dominic</div></div></div><div id="comment-tools-2653" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-2653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2651"></span>

<div id="answer-container-2651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2651-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is actually more likely an issue with winpcap/libpcap. Wireshark simply happens to use it. What type of interface is this? Does it work properly if you deselect promiscuous mode?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2651" class="comments-container"></div><div id="comment-tools-2651" class="comment-tools"></div><div class="clear"></div><div id="comment-2651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "It sees my wireless interfaces as &quot;Microsoft&quot;"
description = '''It sees my Ethernet interface, but my wireless interfaces are displayed as &quot;Microsoft&quot; and of coarse don&#x27;t have a properties of a wireless interfaces! I used to capture packets with my Belkin USB wireless adaptor on CommView, because my built-in wi-fi card doesn&#x27;t support monitor mode, so I know it ...'''
date = "2012-10-04T13:05:00Z"
lastmod = "2012-10-04T18:42:00Z"
weight = 14715
keywords = [ "wireless", "interface", "name", "windows", "wireshark" ]
aliases = [ "/questions/14715" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [It sees my wireless interfaces as "Microsoft"](/questions/14715/it-sees-my-wireless-interfaces-as-microsoft)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It sees my Ethernet interface, but my wireless interfaces are displayed as "Microsoft" and of coarse don't have a properties of a wireless interfaces! I used to capture packets with my Belkin USB wireless adaptor on CommView, because my built-in wi-fi card doesn't support monitor mode, so I know it works. At that moment I had WinPcap 4.1.1. I tryed to roll back WinPcap, but it didn't help!</p></div><div id="question-tags" class="tags-container tags">wireless interface name windows wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/6e2fcfd731e5fe29c6566c4330efeb5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fureous%20George&#39;s gravatar image" /><p>Fureous George<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fureous George has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '12, 14:43</p></div></div><div id="comments-container-14715" class="comments-container"></div><div id="comment-tools-14715" class="comment-tools"></div><div class="clear"></div><div id="comment-14715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14718"></span>

<div id="answer-container-14718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14718-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, the adapter is just called "Microsoft" because that is the name the driver reported. You can change it at the Prefences -&gt; Capture -&gt; Edit Interfaces -&gt; Comment. Second, if you're capturing on Windows you need AirPCAP adapters to be able to record 802.11 layer information with Wireshark, but I guess you already know that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '12, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14718" class="comments-container"><span id="14720"></span><div id="comment-14720" class="comment"><div id="post-14720-score" class="comment-score"></div><div class="comment-text"><p>I didn't know that could u explain it in more detail, please?</p></div><div id="comment-14720-info" class="comment-info"><span class="comment-age">(04 Oct '12, 13:37)</span> Fureous George</div></div><span id="14721"></span><div id="comment-14721" class="comment"><div id="post-14721-score" class="comment-score"></div><div class="comment-text"><p>I'm currently logged on in Mc'Donalds on my built-in card, and one of these interfaces is capturing packets - I don't know if it's the one connected, because I know that u can't be connected if u in a monitor mode, and it must be in a active mode! I want to use my built-in card to connect, and my Belkin to capture!</p></div><div id="comment-14721-info" class="comment-info"><span class="comment-age">(04 Oct '12, 13:47)</span> Fureous George</div></div><span id="14723"></span><div id="comment-14723" class="comment"><div id="post-14723-score" class="comment-score"></div><div class="comment-text"><p>I disconnected my Belkin USB and my built-in card is capturing packets in active mode! I want to capture packets with Belkin in monitor mode!</p></div><div id="comment-14723-info" class="comment-info"><span class="comment-age">(04 Oct '12, 14:12)</span> Fureous George</div></div><span id="14724"></span><div id="comment-14724" class="comment"><div id="post-14724-score" class="comment-score"></div><div class="comment-text"><p>Usually - when capturing WiFI - you want to see the radio layer, meaning beacon frames, association requests, signal strength etc. which you can only do on Windows if you use an AirPCAP USB adapter. Of course you can capture on any WiFi card on Windows and see frames but you will not see this radio layer (802.11) unless it is an AirPCAP adapter.</p><p>Oh, and Wireshark will most likely not be able to capture on USB network cards on Windows. There are tons of questions here about that topic, for example <a href="http://ask.wireshark.org/questions/12791/wireshark-doesnt-detect-usb-datacards">http://ask.wireshark.org/questions/12791/wireshark-doesnt-detect-usb-datacards</a></p></div><div id="comment-14724-info" class="comment-info"><span class="comment-age">(04 Oct '12, 15:10)</span> Jasper ♦♦</div></div></div><div id="comment-tools-14718" class="comment-tools"></div><div class="clear"></div><div id="comment-14718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14725"></span>

<div id="answer-container-14725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14725-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to use CommView (which probably provides its own driver for the adapter) or possibly <a href="http://support.microsoft.com/kb/933741">Microsoft Network Monitor</a>, which will use the adapter's own driver <em>but</em> which has a driver that connects to the adapter driver and, unlike the WinPcap driver, does so in a way that, on Windows Vista and later, supports monitor mode <em>if</em> the adapter's driver does (although there are adapters that have drivers that "support" it but with bugs). (Network Monitor doesn't support monitor mode on Windows XP.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '12, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14725" class="comments-container"></div><div id="comment-tools-14725" class="comment-tools"></div><div class="clear"></div><div id="comment-14725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


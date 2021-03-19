+++
type = "question"
title = "Win 7 Firewall rule when capturing using switch&#x27;s monitor mode?"
description = '''Hi I want to use Wireshark to capture all packets mirrored by a switch, as described in: http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch Supposing that the Wireshark PC has Windows 7 installed, what Firewall rule should I define to ensure that Wireshark get...'''
date = "2014-07-31T05:45:00Z"
lastmod = "2014-08-01T00:11:00Z"
weight = 35029
keywords = [ "firewall", "mirroring" ]
aliases = [ "/questions/35029" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Win 7 Firewall rule when capturing using switch's monitor mode?](/questions/35029/win-7-firewall-rule-when-capturing-using-switchs-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35029-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I want to use Wireshark to capture all packets mirrored by a switch, as described in:</p><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</a></p><p>Supposing that the Wireshark PC has Windows 7 installed, what Firewall rule should I define to ensure that Wireshark gets all the mirrored traffic?</p><p>Would I specify the rule for Wireshark or for WinPCap?</p><p>BR David</p></div><div id="question-tags" class="tags-container tags">firewall mirroring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '14, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/127322d117e02480a76c4efde0a67594?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA&#39;s gravatar image" /><p>DavidA<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA has no accepted answers">0%</span></p></div></div><div id="comments-container-35029" class="comments-container"></div><div id="comment-tools-35029" class="comment-tools"></div><div class="clear"></div><div id="comment-35029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35042"></span>

<div id="answer-container-35042" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35042-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Supposing that the Wireshark PC has Windows 7 installed, what Firewall rule should I define to ensure that Wireshark gets all the mirrored traffic?</p></blockquote><p>Forget about configuring firewall rules (;-), for two reasons:</p><ul><li>We have had a lot of problem reports regarding all kinds of security software (firewalls, av, vpn clients, endpoint security, etc.) that caused massive trouble while capturing packets.</li><li>you don't know what kind of traffic will be on the line, so you can't configure a rule other than to <strong>allow anything</strong>, which is the same as disabling the firewall.</li></ul><p>So, the only <strong>reliable</strong> way to get <strong>correct captures</strong> is to disable the firewall while you are capturing. If you are afraid of an attack during that period of time, you can disable the IPv4 and/or IPv6 protocol binding on that interface (interface settings).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '14, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35042" class="comments-container"></div><div id="comment-tools-35042" class="comment-tools"></div><div class="clear"></div><div id="comment-35042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


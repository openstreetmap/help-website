+++
type = "question"
title = "Multiple ARP Request for Nonexistent IP Address"
description = '''Before i start, i need to say that i&#x27;m a new Wireshark User that just started using it for two days. However, i already watched some video online explaining how it works.  Anyway, i don&#x27;t know if this is common or not, but every time i capture my Wireless Network, i almost see 100 + line containing ...'''
date = "2015-09-16T02:05:00Z"
lastmod = "2015-09-16T03:50:00Z"
weight = 45872
keywords = [ "arp", "multiple", "wireshark" ]
aliases = [ "/questions/45872" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple ARP Request for Nonexistent IP Address](/questions/45872/multiple-arp-request-for-nonexistent-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45872-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Before i start, i need to say that i'm a new Wireshark User that just started using it for two days. However, i already watched some video online explaining how it works.</p><p>Anyway, i don't know if this is common or not, but every time i capture my Wireless Network, i almost see 100 + line containing " Gratious ARP for 192.168.1.2 (Request) " at the info tab every time i capture. The problem is, our DHCP Start IP Address is above 40 (192.168.1.40 &lt;- ) so what i want to know is ;</p><ol><li>Why the system request nonexistent ip ?</li><li>Is it normal for ARP to request multiple times (above 20+) like in the capture file bellow ?</li><li>When that message show up, our internet become laggy. Is this the reason behind it ?</li><li>How can i solve this multiple ARP problem ?</li></ol><p>This is the <a href="https://osqa-ask.wireshark.org/upfiles/1_r2nFFAd.PNG">link</a> for my modem and the <a href="https://drive.google.com/open?id=0B7xyxLOLfrxRRXk4SEs3ZW9TRlE">capture file</a> showing the ARP problem</p><p>NB : My IP Address in this capture file are 198.168.1.50</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">arp multiple wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/58836c7f49882454c437177476f0331a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Opang&#39;s gravatar image" /><p>Opang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Opang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Sep '15, 03:48</p></div></div><div id="comments-container-45872" class="comments-container"></div><div id="comment-tools-45872" class="comment-tools"></div><div class="clear"></div><div id="comment-45872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45874"></span>

<div id="answer-container-45874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45874-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>It's not requesting the IP, it's saying it has it. You can read about Gratuitous ARP <a href="https://wiki.wireshark.org/Gratuitous_ARP">here</a>.</p></li><li><p>No, not at this rate. Gratuitous ARP is used for duplicate IP detection and also in ARP cache poisoning attacks.</p></li><li><p>I don't think so, unless you use 192.168.1.2 or 192.168.1.254 as a default gateway or dns server.</p></li><li><p>Check the devices in your network: SamsungE_77:79:c4, Tp-LinkT_3b:8e:a0, Routerbo_f9:f3:9f</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '15, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-45874" class="comments-container"><span id="45875"></span><div id="comment-45875" class="comment"><div id="post-45875-score" class="comment-score"></div><div class="comment-text"><p>Note that as @Roland mentions there are duplicate IP addresses found in the capture, two systems fighting over 192.168.1.2 (with MAC addresses c0:bd:d1:77:79:c4, 10:fe:ed:bb:84:53) and two fighting over 192.168.1.254 (f8:1a:67:3b:8e:a0 and 4c:5e:0c:f9:f3:9f).</p><p>You can try to look up the manufacturer of the MAC addresses to give you some indication of which device it is in Wireshark by enabling "Resolve MAC addresses" in Preferences | Name Resolution, or at <a href="http://www.macvendorlookup.com/">http://www.macvendorlookup.com/</a></p></div><div id="comment-45875-info" class="comment-info"><span class="comment-age">(16 Sep '15, 04:14)</span> grahamb ♦</div></div><span id="45892"></span><div id="comment-45892" class="comment"><div id="post-45892-score" class="comment-score"></div><div class="comment-text"><p>@Roland : So that means there's a device manufactured by Samsung that keep telling people on our network he has that IP ? Well, if it's not disturbing our network traffic, i guess it's fine for now. Does this means we just have to find that device and then turn off it's wi-fi connection to solve the problem (multiple arp request showing up in the Wireshark) ?</p><p>@grahamb Thanks for the MAC list. Based on the MAC, two of them belonged to TP-Link, which is our wifi devices. Is it possible / common for wifi devices to have multiple MAC ?</p></div><div id="comment-45892-info" class="comment-info"><span class="comment-age">(16 Sep '15, 15:30)</span> Opang</div></div><span id="45905"></span><div id="comment-45905" class="comment"><div id="post-45905-score" class="comment-score"></div><div class="comment-text"><p>It's possible but not all that usual. Regardless of that the fact that 2 different MAC addresses are claiming the same IP is bad and should be fixed.</p></div><div id="comment-45905-info" class="comment-info"><span class="comment-age">(17 Sep '15, 01:44)</span> grahamb ♦</div></div><span id="45974"></span><div id="comment-45974" class="comment"><div id="post-45974-score" class="comment-score">1</div><div class="comment-text"><p>@Opang The amount of gratuitous arps the Samsung is sending is not normal. I would check why it's doing that.</p></div><div id="comment-45974-info" class="comment-info"><span class="comment-age">(20 Sep '15, 11:33)</span> Roland</div></div></div><div id="comment-tools-45874" class="comment-tools"></div><div class="clear"></div><div id="comment-45874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


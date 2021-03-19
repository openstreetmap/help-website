+++
type = "question"
title = "Wifi sniffing only outgoing packets"
description = '''When I am setting my wifi card in monitor mode and disconnecting it from wifi I am able to sniff every packet coming in and out from my tablet (http requests and responses) but when I connect to network while sniffing. I am only able to sniff packets coming out of my tablet (http requsests). I am ve...'''
date = "2014-12-26T07:46:00Z"
lastmod = "2014-12-27T10:53:00Z"
weight = 38717
keywords = [ "sniffing", "wifi", "networking", "wireshark" ]
aliases = [ "/questions/38717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wifi sniffing only outgoing packets](/questions/38717/wifi-sniffing-only-outgoing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I am setting my wifi card in monitor mode and disconnecting it from wifi I am able to sniff every packet coming in and out from my tablet (http requests and responses) but when I connect to network while sniffing. I am only able to sniff packets coming out of my tablet (http requsests). I am very curious what might be the cause of this.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">sniffing wifi networking wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '14, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/eed1969cb8eb9f95031e0cdb697ff66e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sewci0&#39;s gravatar image" /><p>Sewci0<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sewci0 has no accepted answers">0%</span></p></div></div><div id="comments-container-38717" class="comments-container"><span id="38719"></span><div id="comment-38719" class="comment"><div id="post-38719-score" class="comment-score"></div><div class="comment-text"><p>Are you doing the capturing on your tablet or on some other machine? What OS is the machine doing the capturing running? How are you putting it in monitor mode? What software are you using to capture the traffic?</p></div><div id="comment-38719-info" class="comment-info"><span class="comment-age">(26 Dec '14, 16:56)</span> Guy Harris ♦♦</div></div><span id="38721"></span><div id="comment-38721" class="comment"><div id="post-38721-score" class="comment-score"></div><div class="comment-text"><p>I am sniffing packets from my tablet using wireshark on my laptop running Linux. When I enable monitor mode using airmon and disconnect from my AP (on a laptop) I am able to sniff and decrypt every incoming and outgoing packet from my tablet. But when I run the airmon and connect to AP on my laptop I am only able to see packets outgoing from my tablet. That means that I see http requests but I can't see http responses. I think that the problem might be in decrypting because when I turn off encryption on my AP I was able to sniff incoming and outgoing packets while being connected to the AP.</p></div><div id="comment-38721-info" class="comment-info"><span class="comment-age">(26 Dec '14, 17:09)</span> Sewci0</div></div><span id="38722"></span><div id="comment-38722" class="comment"><div id="post-38722-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But when I run the airmon and connect to AP on my laptop I am only able to see packets outgoing from my tablet.</p></blockquote><p>I.e., when you're running airmon on your laptop, and the laptop is connected to the AP, it sees packets from your tablet to the AP but not packets from your AP to the tablet? Does it see traffic from your laptop to the AP, and does it see traffic from the AP to your laptop?</p><blockquote><p>I think that the problem might be in decrypting because when I turn off encryption on my AP I was able to sniff incoming and outgoing packets while being connected to the AP.</p></blockquote><p>Is it, at the <em>link</em> layer (i.e., look at the MAC addresses), seeing traffic from your table to the AP - even if they just show up as "802.11" packets, not HTTP packets?</p></div><div id="comment-38722-info" class="comment-info"><span class="comment-age">(26 Dec '14, 17:20)</span> Guy Harris ♦♦</div></div><span id="38729"></span><div id="comment-38729" class="comment"><div id="post-38729-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I.e., when you're running airmon on your laptop, and the laptop is connected to the AP, it sees packets from your tablet to the AP but not packets from your AP to the tablet?</p></blockquote><p>I can see packets from my router to my tablet but every of them is LLC. It seams that instead of http responses I get those weird LLC packets.</p><blockquote><p>Does it see traffic from your laptop to the AP, and does it see traffic from the AP to your laptop?</p></blockquote><p>Yes, traffic from my laptop is being properly decrypted both ways.</p><blockquote><p>Is it, at the link layer (i.e., look at the MAC addresses), seeing traffic from your table to the AP - even if they just show up as "802.11" packets, not HTTP packets?</p></blockquote><p>From my tablet to AP packet are being sniffed and decrypted but packet from AP to tablet are being shown as LLC packets.</p><p>I am attaching dump from Wireshark ESSID:OpenWrt WPA-PWD:test_network <a href="https://www.dropbox.com/s/c43j0pr87x991ae/weird_packets.pcapng?dl=0">https://www.dropbox.com/s/c43j0pr87x991ae/weird_packets.pcapng?dl=0</a> My tablet:10.11.11. My laptop:10.11.11.129</p></div><div id="comment-38729-info" class="comment-info"><span class="comment-age">(27 Dec '14, 03:27)</span> Sewci0</div></div><span id="38730"></span><div id="comment-38730" class="comment"><div id="post-38730-score" class="comment-score"></div><div class="comment-text"><p>I've checked once more and I realized that I had marked "Ignore the VI protection" bit now those packets are ordinary 802.11 but encrypted. Still I don't know how to decrypt them.</p></div><div id="comment-38730-info" class="comment-info"><span class="comment-age">(27 Dec '14, 03:54)</span> Sewci0</div></div></div><div id="comment-tools-38717" class="comment-tools"></div><div class="clear"></div><div id="comment-38717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38742"></span>

<div id="answer-container-38742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On a protected network, a monitor mode capture will see encrypted packets. See <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki "How to decrypt 802.11" page</a> for information on how to decrypt them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38742" class="comments-container"><span id="38743"></span><div id="comment-38743" class="comment"><div id="post-38743-score" class="comment-score"></div><div class="comment-text"><p>I know how to decrypt packets, I just can't decrypt packets incoming to my sniffed device using promiscuous mode.</p></div><div id="comment-38743-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:01)</span> Sewci0</div></div></div><div id="comment-tools-38742" class="comment-tools"></div><div class="clear"></div><div id="comment-38742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


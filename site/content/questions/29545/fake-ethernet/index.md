+++
type = "question"
title = "Fake Ethernet"
description = '''I want Wireshark to give me all/at least Data packet into Fake Ethernet format in monitor mode. How Wireshark can be set for converting wireless packet to fake Ethernet packet? and can I use analysis tool of real Ethernet packet on this Fake Ethernet ? '''
date = "2014-02-07T20:48:00Z"
lastmod = "2014-02-08T23:41:00Z"
weight = 29545
keywords = [ "sniffing", "security", "wireshark" ]
aliases = [ "/questions/29545" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Fake Ethernet](/questions/29545/fake-ethernet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want Wireshark to give me all/at least Data packet into Fake Ethernet format in monitor mode. How Wireshark can be set for converting wireless packet to fake Ethernet packet? and can I use analysis tool of real Ethernet packet on this Fake Ethernet ?<br />
</p></div><div id="question-tags" class="tags-container tags">sniffing security wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '14, 20:48</strong></p><img src="https://secure.gravatar.com/avatar/4f2e12b298828a7bdd200478480606da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIDS&#39;s gravatar image" /><p>WIDS<br />
<span class="score" title="25 reputation points">25</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIDS has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Feb '14, 21:42</p></div></div><div id="comments-container-29545" class="comments-container"></div><div id="comment-tools-29545" class="comment-tools"></div><div class="clear"></div><div id="comment-29545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29548"></span>

<div id="answer-container-29548" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29548-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a converter tool, it decodes and displays packet captures. If you need to edit/convert your trace files you should take a look at the command line tool editcap, which you can find in the Wireshark installation directory. It doesn't come with a converter option for packets as well, but it can cut away bytes at the end or beginning of a packet, which can often help with topics like yours.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '14, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29548" class="comments-container"><span id="29550"></span><div id="comment-29550" class="comment"><div id="post-29550-score" class="comment-score"></div><div class="comment-text"><p>thank you Jasper but-&gt; The Wi-Fi Wiki page ( <a href="http://wiki.wireshark.org/Wi-Fi">http://wiki.wireshark.org/Wi-Fi</a> ) says that sometimes the hardware/driver translates 802.11 headers into Ethernet headers........</p></div><div id="comment-29550-info" class="comment-info"><span class="comment-age">(08 Feb '14, 06:21)</span> WIDS</div></div><span id="29551"></span><div id="comment-29551" class="comment"><div id="post-29551-score" class="comment-score"></div><div class="comment-text"><p>Correct. If you capture on a card in promiscuous mode (but not monitor mode) you'll not see the radio layers, only Ethernet and up. That happens when you capture on a standard WiFi card on Windows because it cannot be put into monitor mode. Which is why Wifi captures on Windows require additional AirPCAP adapters.</p></div><div id="comment-29551-info" class="comment-info"><span class="comment-age">(08 Feb '14, 06:30)</span> Jasper ♦♦</div></div><span id="29559"></span><div id="comment-29559" class="comment"><div id="post-29559-score" class="comment-score"></div><div class="comment-text"><p>Can i use promiscuous mode on Ubuntu PC (12.04 ) with external wireless card ( card detail: Ralink 2573 driver rt73usb ) to do above.</p></div><div id="comment-29559-info" class="comment-info"><span class="comment-age">(08 Feb '14, 19:12)</span> WIDS</div></div><span id="29569"></span><div id="comment-29569" class="comment"><div id="post-29569-score" class="comment-score"></div><div class="comment-text"><p>I don't know that card, but you could just try and see what Wireshark displays when capturing on that card.</p></div><div id="comment-29569-info" class="comment-info"><span class="comment-age">(09 Feb '14, 03:01)</span> Jasper ♦♦</div></div></div><div id="comment-tools-29548" class="comment-tools"></div><div class="clear"></div><div id="comment-29548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29564"></span>

<div id="answer-container-29564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29564-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want Wireshark to give me all/at least Data packet into Fake Ethernet format in monitor mode.</p></blockquote><p>Unfortunately, to quote Sir Michael Philip Jagger, "you can't always get what you want". The only OS/driver/adapter combinations I've seen that provide fake Ethernet headers rather than 802.11 headers in monitor mode was FreeBSD, and I'm not even sure they support it any more.</p><p>If Wireshark doesn't offer Ethernet as a link-layer header type when you select monitor mode, that's because the OS/driver/adapter combination doesn't support it.</p><p>As for promiscuous mode, it often isn't implemented on wireless devices; you could try it, but whether it will be any different from non-promiscuous mode - i.e., whether it will capture any traffic other than traffic to and from your machine - would depend on the OS/driver/adapter combination.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '14, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29564" class="comments-container"></div><div id="comment-tools-29564" class="comment-tools"></div><div class="clear"></div><div id="comment-29564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


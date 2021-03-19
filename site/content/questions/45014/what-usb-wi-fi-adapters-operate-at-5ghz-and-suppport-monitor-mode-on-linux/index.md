+++
type = "question"
title = "What USB Wi-FI adapters operate at 5GHz and suppport monitor mode on Linux?"
description = '''Hi, I&#x27;m looking for a Wi-Fi USB dongle that operates at 5GHz and supports monitor mode. Could be an 802.11n only card or 802.11ac. There are various lists like this one available (https://wikidevi.com/wiki/Wireless_adapters/Chipset_table), but it&#x27;s hard to find any products to buy and I really want ...'''
date = "2015-08-12T10:51:00Z"
lastmod = "2015-08-13T06:14:00Z"
weight = 45014
keywords = [ "wi-fi", "monitor", "linux" ]
aliases = [ "/questions/45014" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What USB Wi-FI adapters operate at 5GHz and suppport monitor mode on Linux?](/questions/45014/what-usb-wi-fi-adapters-operate-at-5ghz-and-suppport-monitor-mode-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45014-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm looking for a Wi-Fi USB dongle that operates at 5GHz and supports monitor mode. Could be an 802.11n only card or 802.11ac. There are various lists like this one available (<a href="https://wikidevi.com/wiki/Wireless_adapters/Chipset_table),">https://wikidevi.com/wiki/Wireless_adapters/Chipset_table),</a> but it's hard to find any products to buy and I really want something with a Linux driver that works (preferably on RPi). So I wonder if someone has something to recommend? Have done quite a lot of Googling on this subject but the fog out there is massive. ;)</p><p>Cheers! Sam</p></div><div id="question-tags" class="tags-container tags">wi-fi monitor linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p>SamA<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '15, 19:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-45014" class="comments-container"></div><div id="comment-tools-45014" class="comment-tools"></div><div class="clear"></div><div id="comment-45014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45056"></span>

<div id="answer-container-45056" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45056-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have used the Linksys AE6000 adapter. The only limitation is that it supports 1x1 streams. It also does not support LDPC which limits capturing to devices that only support BCC coding.</p><p>I did query on WikiDevi for USB WiFi adapters that support abgn protocols and had the Atheros WiFi chipset. Atheros has very good support for Linux drivers. You should look for an adapter/chipset that supports LDPC coding as most new AP's/clients use LDPC.</p><p><a href="https://wikidevi.com/w/index.php?title=Special%3AAsk&amp;q=%5B%5BCategory%3AWireless+adapter%5D%5D+%5B%5BChip1+brand%3A%3AAtheros%5D%5D+%5B%5BSupported+802dot11+protocols%3A%3Aabgn%5D%5D&amp;po=%3FSupported+802dot11+protocols%0D%0A%3FInterface%0D%0A%3FChip1+brand%0D%0A%3FChip1+model%0D%0A%3FChip2+brand%0D%0A%3FChip2+model%0D%0A&amp;eq=yes&amp;p%5Bformat%5D=broadtable&amp;sort_num=&amp;order_num=ASC&amp;p%5Blimit%5D=&amp;p%5Boffset%5D=&amp;p%5Blink%5D=all&amp;p%5Bsort%5D=&amp;p%5Bheaders%5D=show&amp;p%5Bmainlabel%5D=&amp;p%5Bintro%5D=&amp;p%5Boutro%5D=&amp;p%5Bsearchlabel%5D=...+further+results&amp;p%5Bdefault%5D=&amp;p%5Bclass%5D=sortable+wikitable+smwtable&amp;p%5Bsep%5D=&amp;eq=yes">https://wikidevi.com/w/index.php?title=Special%3AAsk&amp;q=%5B%5BCategory%3AWireless+adapter%5D%5D+%5B%5BChip1+brand%3A%3AAtheros%5D%5D+%5B%5BSupported+802dot11+protocols%3A%3Aabgn%5D%5D&amp;po=%3FSupported+802dot11+protocols%0D%0A%3FInterface%0D%0A%3FChip1+brand%0D%0A%3FChip1+model%0D%0A%3FChip2+brand%0D%0A%3FChip2+model%0D%0A&amp;eq=yes&amp;p%5Bformat%5D=broadtable&amp;sort_num=&amp;order_num=ASC&amp;p%5Blimit%5D=&amp;p%5Boffset%5D=&amp;p%5Blink%5D=all&amp;p%5Bsort%5D=&amp;p%5Bheaders%5D=show&amp;p%5Bmainlabel%5D=&amp;p%5Bintro%5D=&amp;p%5Boutro%5D=&amp;p%5Bsearchlabel%5D=...+further+results&amp;p%5Bdefault%5D=&amp;p%5Bclass%5D=sortable+wikitable+smwtable&amp;p%5Bsep%5D=&amp;eq=yes</a></p><p>Happy hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-45056" class="comments-container"><span id="45063"></span><div id="comment-45063" class="comment"><div id="post-45063-score" class="comment-score"></div><div class="comment-text"><p>Thanks for suggestions! What does LDPC and BBC coding refer to?</p></div><div id="comment-45063-info" class="comment-info"><span class="comment-age">(13 Aug '15, 08:16)</span> SamA</div></div><span id="45064"></span><div id="comment-45064" class="comment"><div id="post-45064-score" class="comment-score"></div><div class="comment-text"><p>Both are a type of error correcting code used in WiFi.</p><p>LDPC = Low-density parity-check</p><p>BCC = Binary Convolutional Code</p><p>Low density parity check (LDPC) is an optional coding method supported by some 802.11n devices and provides an increase in rate-over-range. LDPC is part of the 802.11n specification, but was never widely implemented in the past. However, LDPC is becoming more prevalent both in smartphones, access points, and smart accessories.</p><p>You can determine if your AP supports LDPC by looking at the the HT Capabilities Info element within a Beacon sent from your AP.</p></div><div id="comment-45064-info" class="comment-info"><span class="comment-age">(13 Aug '15, 08:31)</span> Amato_C</div></div><span id="45065"></span><div id="comment-45065" class="comment"><div id="post-45065-score" class="comment-score"></div><div class="comment-text"><p>If the supplied answer assisted you, please accept the solution. This helps others with similar questions.</p><p>Thank you.</p></div><div id="comment-45065-info" class="comment-info"><span class="comment-age">(13 Aug '15, 09:44)</span> Amato_C</div></div><span id="45145"></span><div id="comment-45145" class="comment"><div id="post-45145-score" class="comment-score"></div><div class="comment-text"><p>Thanks again!</p></div><div id="comment-45145-info" class="comment-info"><span class="comment-age">(16 Aug '15, 09:22)</span> SamA</div></div><span id="51163"></span><div id="comment-51163" class="comment not_top_scorer"><div id="post-51163-score" class="comment-score"></div><div class="comment-text"><p>Hi again, After quite some digging, I decided to go for Edimax EW-7811UTC (AC600). This one is supposed to support monitoring mode, but I simply can't find a Linux driver that works. Any suggestions where to look?</p><p>BR Sam</p></div><div id="comment-51163-info" class="comment-info"><span class="comment-age">(24 Mar '16, 14:56)</span> SamA</div></div><span id="51166"></span><div id="comment-51166" class="comment"><div id="post-51166-score" class="comment-score">1</div><div class="comment-text"><p>Try this: <a href="http://www.edimax.com/images/Image/Driver_Utility/Wireless/NIC/EW-7822UAC/EW-7822UAC_linux_v4.2.2_7502.20130517.tar.gz">http://www.edimax.com/images/Image/Driver_Utility/Wireless/NIC/EW-7822UAC/EW-7822UAC_linux_v4.2.2_7502.20130517.tar.gz</a></p></div><div id="comment-51166-info" class="comment-info"><span class="comment-age">(24 Mar '16, 18:41)</span> Amato_C</div></div><span id="61659"></span><div id="comment-61659" class="comment not_top_scorer"><div id="post-61659-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/3386/amato_c">@Amato_C</a> Were you able to get AE6000 to work in monitor mode at 5Ghz? If so, any pointers on which FW to use, and how you did it? Thanks!</p></div><div id="comment-61659-info" class="comment-info"><span class="comment-age">(27 May '17, 10:22)</span> JBaczuk</div></div></div><div id="comment-tools-45056" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-45056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


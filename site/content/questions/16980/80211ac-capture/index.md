+++
type = "question"
title = "802.11ac capture"
description = '''Hey Are there any adapters supporting 802.11ac packet capture today? Any that wireshark supports? JP'''
date = "2012-12-17T08:58:00Z"
lastmod = "2012-12-17T10:22:00Z"
weight = 16980
keywords = [ "adapter", "802.11ac" ]
aliases = [ "/questions/16980" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11ac capture](/questions/16980/80211ac-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16980-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey</p><p>Are there any adapters supporting 802.11ac packet capture today? Any that wireshark supports?</p><p>JP</p></div><div id="question-tags" class="tags-container tags">adapter 802.11ac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/4024dbaac347819d3608939fe44990ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JP-NYC&#39;s gravatar image" /><p>JP-NYC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JP-NYC has no accepted answers">0%</span></p></div></div><div id="comments-container-16980" class="comments-container"></div><div id="comment-tools-16980" class="comment-tools"></div><div class="clear"></div><div id="comment-16980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16982"></span>

<div id="answer-container-16982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16982-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not primarily a problem of Wireshark, but rather a problem of driver support for the OS.</p><p><strong>Windows</strong><br />
The driver needs to be compliant with WinPcap to be able to capture packets in promiscuous mode. If you want to enable monitor mode, you need a driver that is fully NDIS6 compliant. And even then it is uncertain if you can enable monitor mode. So, hard business on Windows.</p><p><strong>Linux</strong><br />
You need support for such a device in the kernel, which might be hard for a standard that is barely released.</p><p>Netgear offers a 802.11ac adapter (<a href="http://www.netgear.com/home/products/wireless-adapters/ultimate-wireless-adapters/a6200.aspx#),">http://www.netgear.com/home/products/wireless-adapters/ultimate-wireless-adapters/a6200.aspx#),</a> however I'm not sure if there is a Linux driver available for that.</p><p>You might get better answers to your question in the <a href="http://www.backtrack-linux.org/">BackTrack</a> or <a href="http://www.aircrack-ng.org/">Aircrakc-ng</a> forum. As soon as a new adapter works with one of those systems/tools, it will work with Wireshark on Linux as well.</p><p><strong>UPDATE</strong></p><p>Here is a list of 802.11ac 'compatible' devices</p><blockquote><p><code>http://wikidevi.com/wiki/List_of_802.11ac_Hardware</code><br />
</p></blockquote><p>For the few USB adapters you can read: Linux driver <strong>none</strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 12:44</p></div></div><div id="comments-container-16982" class="comments-container"><span id="17049"></span><div id="comment-17049" class="comment"><div id="post-17049-score" class="comment-score"></div><div class="comment-text"><p>And WinPcap doesn't handle NDIS 6, so it can't enable monitor mode in any case; we don't support monitor mode on WIndows.</p></div><div id="comment-17049-info" class="comment-info"><span class="comment-age">(18 Dec '12, 20:32)</span> Guy Harris ♦♦</div></div><span id="17052"></span><div id="comment-17052" class="comment"><div id="post-17052-score" class="comment-score"></div><div class="comment-text"><p>Of course you are right. I should have mentioned Microsoft Network Monitor in conjunction with NDIS6 and monitor mode. It is possible there if the driver supports it.</p></div><div id="comment-17052-info" class="comment-info"><span class="comment-age">(19 Dec '12, 00:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16982" class="comment-tools"></div><div class="clear"></div><div id="comment-16982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


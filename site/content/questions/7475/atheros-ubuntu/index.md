+++
type = "question"
title = "atheros ubuntu"
description = '''Hi! I have a pci atheros card AR5212/AR5213 (rev 01) with madwifi driver and ubuntu 11.10. I installed wireshark 1.6.2. I created an interface in monitor mode but wireshark doesn&#x27;t see it in monitor mode (the check box is grey). Could you please help me? Sboong PS. This card works great with kismet.'''
date = "2011-11-16T12:56:00Z"
lastmod = "2012-01-23T15:05:00Z"
weight = 7475
keywords = [ "atheros" ]
aliases = [ "/questions/7475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [atheros ubuntu](/questions/7475/atheros-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I have a pci atheros card AR5212/AR5213 (rev 01) with madwifi driver and ubuntu 11.10. I installed wireshark 1.6.2. I created an interface in monitor mode but wireshark doesn't see it in monitor mode (the check box is grey).</p><p>Could you please help me?</p><p>Sboong</p><p>PS. This card works great with kismet.</p></div><div id="question-tags" class="tags-container tags">atheros</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '11, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/a7d5d51d1873b590d8c218aaa911cbfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_sbOOng_&#39;s gravatar image" /><p>_sbOOng_<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_sbOOng_ has no accepted answers">0%</span></p></div></div><div id="comments-container-7475" class="comments-container"><span id="8563"></span><div id="comment-8563" class="comment"><div id="post-8563-score" class="comment-score"></div><div class="comment-text"><p>Did you happen to find a solution to your problem? I am experiencing the same things. Only i am trying to use ath5k.</p></div><div id="comment-8563-info" class="comment-info"><span class="comment-age">(23 Jan '12, 08:02)</span> red</div></div></div><div id="comment-tools-7475" class="comment-tools"></div><div class="clear"></div><div id="comment-7475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8572"></span>

<div id="answer-container-8572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just try capturing on the monitor device <em>without</em> checking the monitor mode box. Checking the monitor mode box causes Wireshark to ask libpcap to set up monitor mode; in Linux distributions where libpcap is not linked with libnl, which includes Debian and its derivatives such as Ubuntu, that doesn't work with libpcap 1.1.0 or 1.1.1, as provided with Ubuntu. Therefore, you need to run airmon-ng to set up the monitor device (as libpcap isn't linked with libnl, it won't set up the monitor device itself) and, as the monitor device is already in monitor mode, there's no need to have Wireshark ask libpcap to put it into monitor mode and, in fact, libpcap's attempt to do so won't work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8572" class="comments-container"></div><div id="comment-tools-8572" class="comment-tools"></div><div class="clear"></div><div id="comment-8572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


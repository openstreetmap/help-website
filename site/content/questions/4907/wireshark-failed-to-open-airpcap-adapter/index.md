+++
type = "question"
title = "Wireshark Failed to Open Airpcap adapter"
description = '''Dell laptop running Windows 7 64-bit. Airpcap 4.1.1 Wireshark 1.6.0 When I launch Wireshark with the Airpcap Classic plugged in. I get a Wireshark dialog box that says &quot;Failed to open Airpcap adapters!&quot;. Airpcap Control Panel is able to communicate with the Airpcap classic and blink the LED. Craig'''
date = "2011-07-05T07:39:00Z"
lastmod = "2011-07-06T09:09:00Z"
weight = 4907
keywords = [ "airpcap" ]
aliases = [ "/questions/4907" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Failed to Open Airpcap adapter](/questions/4907/wireshark-failed-to-open-airpcap-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dell laptop running Windows 7 64-bit. Airpcap 4.1.1 Wireshark 1.6.0</p><p>When I launch Wireshark with the Airpcap Classic plugged in. I get a Wireshark dialog box that says "Failed to open Airpcap adapters!".</p><p>Airpcap Control Panel is able to communicate with the Airpcap classic and blink the LED.</p><p>Craig</p></div><div id="question-tags" class="tags-container tags">airpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/d2af0042bfdc0bd7eb948253f7aa2d3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="craigmellor&#39;s gravatar image" /><p>craigmellor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="craigmellor has no accepted answers">0%</span></p></div></div><div id="comments-container-4907" class="comments-container"></div><div id="comment-tools-4907" class="comment-tools"></div><div class="clear"></div><div id="comment-4907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4928"></span>

<div id="answer-container-4928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4928-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although you may have your user account in the Admin group, you may still need to right click on the Wireshark program icon and select 'Run as administrator'. 'Run-as-Admin' is a unique requirement of the 64bit versions of Wireshark and other utilities when accessing the AirPcap adapter and UAC is enabled on Windows 7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/15027727481e943949beeb6dae10aa5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Janices&#39;s gravatar image" /><p>Janices<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Janices has no accepted answers">0%</span></p></div></div><div id="comments-container-4928" class="comments-container"><span id="14732"></span><div id="comment-14732" class="comment"><div id="post-14732-score" class="comment-score"></div><div class="comment-text"><p>Janices is correct - you need to run the 64-bit Wiresehark using 'Run as Administrator'. Once you do, all your packets belong to us.</p></div><div id="comment-14732-info" class="comment-info"><span class="comment-age">(05 Oct '12, 05:23)</span> HenryStukenborg</div></div></div><div id="comment-tools-4928" class="comment-tools"></div><div class="clear"></div><div id="comment-4928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4908"></span>

<div id="answer-container-4908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This seems to be a problem with the 64-bit version of Wireshark. Even though you're using a 64-bit operating system, try installing the 32-bit version of Wireshark. I was able to use my Airpcap adapter on Windows 7 Professional 64-bit when I switched to the 32-bit version of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4908" class="comments-container"></div><div id="comment-tools-4908" class="comment-tools"></div><div class="clear"></div><div id="comment-4908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4914"></span>

<div id="answer-container-4914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could also try to contact <a href="http://www.cacetech.com/support/tech_support.html">Riverbed technical support</a>. I did not see any limitations related to this problem mentioned on the <a href="http://www.cacetech.com/support/airpcap_faq.html">AirPcap FAQ</a> page, so maybe they have a solution for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4914" class="comments-container"></div><div id="comment-tools-4914" class="comment-tools"></div><div class="clear"></div><div id="comment-4914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


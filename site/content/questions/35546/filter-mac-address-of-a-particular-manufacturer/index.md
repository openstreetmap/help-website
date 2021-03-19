+++
type = "question"
title = "Filter MAC address of a particular manufacturer"
description = '''I have set up a statiion to capture WiFi data with Wireshark. The station is a Ubuntu laptop with a TP-Link TP-WN722M WiFi adaptor. The WiFi network interface is configured to capture in monitor mode and Wireshark in promiscuous mode. I want to filter all traffic from a particular WiFi chip manufact...'''
date = "2014-08-18T21:13:00Z"
lastmod = "2014-08-18T21:31:00Z"
weight = 35546
keywords = [ "filter", "mac", "wifi" ]
aliases = [ "/questions/35546" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filter MAC address of a particular manufacturer](/questions/35546/filter-mac-address-of-a-particular-manufacturer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35546-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have set up a statiion to capture WiFi data with Wireshark. The station is a Ubuntu laptop with a TP-Link TP-WN722M WiFi adaptor. The WiFi network interface is configured to capture in monitor mode and Wireshark in promiscuous mode.</p><p>I want to filter all traffic from a particular WiFi chip manufacture. I know its ID in the first 24bits of the MAC address, such as AA:BB:CC:xx:xx:xx. How can I set the filter?</p><p>Thank you. :)</p></div><div id="question-tags" class="tags-container tags">filter mac wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/d075420fd2ed7d78364856553fcbe705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garypty&#39;s gravatar image" /><p>garypty<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garypty has no accepted answers">0%</span></p></div></div><div id="comments-container-35546" class="comments-container"></div><div id="comment-tools-35546" class="comment-tools"></div><div class="clear"></div><div id="comment-35546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35547"></span>

<div id="answer-container-35547" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35547-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the 7th example on <a href="http://wiki.wireshark.org/DisplayFilters">Wiresjhark Display Filters</a> :</p><p>"The "slice" feature is also useful to filter on the vendor identifier part (OUI) of the MAC address, see the Ethernet page for details. Thus you may restrict the display to only packets from a specific device manufacturer. E.g. for DELL machines only:</p><pre><code>  eth.src[0:3]==00:06:5B</code></pre><p>(Note: this is a <em>display</em> filter not a <em>capture</em> filter)</p><p>It appears that a capture filter of the form <code>ether[6:3] == 0xnnnnnn</code> should also work (altho I haven't tried it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 21:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '14, 21:50</p></div></div><div id="comments-container-35547" class="comments-container"><span id="35565"></span><div id="comment-35565" class="comment"><div id="post-35565-score" class="comment-score"></div><div class="comment-text"><p>As I am capturing WiFi data, the fitler is <code>wlan.sa[0:3]==00:06:5B</code> . Thanks.</p></div><div id="comment-35565-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:53)</span> garypty</div></div></div><div id="comment-tools-35547" class="comment-tools"></div><div class="clear"></div><div id="comment-35547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "how do i analysis 802.11n by wireshark,please!"
description = '''I want to analysis standard 802.11n by wireshark. Maybe i do not knowledge enough to do it exactly. Can help me do it??? This is an important project with me!'''
date = "2010-11-30T01:22:00Z"
lastmod = "2011-03-21T21:53:00Z"
weight = 1175
keywords = [ "802.11n" ]
aliases = [ "/questions/1175" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do i analysis 802.11n by wireshark,please!](/questions/1175/how-do-i-analysis-80211n-by-wiresharkplease)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to analysis standard 802.11n by wireshark. Maybe i do not knowledge enough to do it exactly. Can help me do it??? This is an important project with me!</p></div><div id="question-tags" class="tags-container tags">802.11n</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/4f406866b1740fdc247ba628d2515395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haquyen&#39;s gravatar image" /><p>haquyen<br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haquyen has no accepted answers">0%</span></p></div></div><div id="comments-container-1175" class="comments-container"><span id="1205"></span><div id="comment-1205" class="comment"><div id="post-1205-score" class="comment-score"></div><div class="comment-text"><p>What steps have you taken to understand 802.11n already? Have you captured 802.11n traffic? What is your precise question? (Asking to analyze 802.11n traffic is like saying 'how does weather work?') Can you be a bit more specific about what is puzzling you?</p></div><div id="comment-1205-info" class="comment-info"><span class="comment-age">(02 Dec '10, 00:24)</span> lchappell ♦</div></div><span id="2342"></span><div id="comment-2342" class="comment"><div id="post-2342-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I'm using Wireshark Version 1.2.7. I would like to capture the traffic I transmit between 2 laptops configured in ad-hoc mode (channel 36 HT40+). With my current configuration I'm only able to see non-HT packets, and beacons (where it is reported that my ad-hoc networks has HT capabilities) Can you please tell me how to capture the 802.11n traffic? Thanks in advance, Baldomero</p></div><div id="comment-2342-info" class="comment-info"><span class="comment-age">(15 Feb '11, 03:18)</span> Baldo</div></div></div><div id="comment-tools-1175" class="comment-tools"></div><div class="clear"></div><div id="comment-1175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3001"></span>

<div id="answer-container-3001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3001-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture 802.11n traffic, including data, management, and control frames along with 802.11n-specific information such as HT information, aggregate MPDUs, and aggregate MSDUs, then you'll first need a device capable of this. If you're running Windows, then you might try <a href="http://www.cacetech.com/products/airpcap_nx.html">AirPcap Nx</a>. There might be other devices out there as well, but none that I'm aware of.</p><p>In addition, you might want to read more about 802.11n. Two quick links that might be of use to you:</p><ul><li>The <a href="http://standards.ieee.org/getieee802/download/802.11n-2009.pdf">802.11n published standard</a> from the IEEE.</li><li>An <a href="http://www.airmagnet.com/assets/whitepaper/WP-802.11nPrimer.pdf">802.11n Primer</a>, from AirMagnet.</li><li>The <a href="http://en.wikipedia.org/wiki/IEEE_802.11">802.11</a> Wikipedia article.</li><li><a href="http://www.wiresharkbook.com/">Wireshark Network Analysis</a>, by Laura Chappell. Of particular relevance is Chapter 26, entitled, <em>"Introduction to 802.11 (WLAN) Analysis"</em></li></ul><p>I'm sure if you search the web or various bookstores, etc., you can find many more books, articles, and information to help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3001" class="comments-container"></div><div id="comment-tools-3001" class="comment-tools"></div><div class="clear"></div><div id="comment-3001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


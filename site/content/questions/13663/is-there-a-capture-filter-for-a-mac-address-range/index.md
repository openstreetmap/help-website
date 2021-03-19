+++
type = "question"
title = "Is there a capture filter for a MAC address range?"
description = '''I am using Wireshark 1.6.9 currently, but have no particular requirement to use that version and plan to upgrade at some point anyway. I know that I can filter on a specific Ethernet MAC address using the capture filter ether host 00:04:a3:00:00:00. Furthermore, I know I can filter on a particular I...'''
date = "2012-08-15T15:47:00Z"
lastmod = "2012-08-15T19:51:00Z"
weight = 13663
keywords = [ "filter", "ethernet", "capture-filter", "mac-address" ]
aliases = [ "/questions/13663" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a capture filter for a MAC address range?](/questions/13663/is-there-a-capture-filter-for-a-mac-address-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.6.9 currently, but have no particular requirement to use that version and plan to upgrade at some point anyway. I know that I can filter on a specific Ethernet MAC address using the capture filter <code>ether host 00:04:a3:00:00:00</code>. Furthermore, I know I can filter on a particular IP subnet with <code>ip net 10.0.0.0/24</code>. Is there a similar capture filter syntax for Ethernet MAC addresses?</p><p>For example, <code>ether net 00:04:a3:00:00:0/24</code> would capture only those packets with a Microchip MAC address, but it gets rejected by the capture filter dialog. How can I capture only traffic sourced from or destined to an Ethernet MAC with a given prefix?</p></div><div id="question-tags" class="tags-container tags">filter ethernet capture-filter mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '12, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-13663" class="comments-container"></div><div id="comment-tools-13663" class="comment-tools"></div><div class="clear"></div><div id="comment-13663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13667"></span>

<div id="answer-container-13667" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13667-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are no keywords that let you do that, but you can accomplish what you want with a byte offset filter. I was able to limit my capture to traffic to and from Netopia devices (OUI 00:0f:cc) with:</p><p>(ether [0:4] &amp; 0xffffff00 = 0x000fcc00) or (ether [6:4] &amp; 0xffffff00 = 0x000fcc00)</p><p>This was only a first attempt for me at using byte offset notation in a capture filter, so maybe someone can shorten the syntax. The problem I ran into was that we're trying to examine three bytes, but the length value in a capture filter byte offset expression can only be 1, 2, or 4 bytes. So "ether[0]" is valid, as is "ether[0:2]" or "ether[0:4]" but not "ether[0:3]". This filter uses "ether[0:4]" and "ether[6:4]" to examine the first four bytes of the destination MAC address and source MAC address, but then uses "&amp; 0xffffff00" to mask the fourth byte before making the comparison.</p><p>You could also just examine each byte individually:</p><p>(ether[0]=0x0 and ether[1]=0x0f and ether[2]=0xcc) or (ether[6]=0x0 and ether[7]=0x0f and ether[8]=0xcc)</p><p>This is a longer and more awkward looking filter, but you might finder it easier to create since the comparison logic is more straightforward.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 19:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13667" class="comments-container"></div><div id="comment-tools-13667" class="comment-tools"></div><div class="clear"></div><div id="comment-13667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


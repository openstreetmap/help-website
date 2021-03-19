+++
type = "question"
title = "802.11 radiotap header"
description = '''hello, i have been sniffing using wireshark and wanted to know about the 802.11 radio tap header whichshows the rssi values. where is the radio tap header located in the 802.11 frame structure? thank you'''
date = "2016-09-30T21:30:00Z"
lastmod = "2016-10-01T00:40:00Z"
weight = 56036
keywords = [ "radiotap" ]
aliases = [ "/questions/56036" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 radiotap header](/questions/56036/80211-radiotap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, i have been sniffing using wireshark and wanted to know about the 802.11 radio tap header whichshows the rssi values. where is the radio tap header located in the 802.11 frame structure? thank you</p></div><div id="question-tags" class="tags-container tags">radiotap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '16, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/11d703ea8508cf72c52f1718280bb7bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misbah&#39;s gravatar image" /><p>misbah<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misbah has no accepted answers">0%</span></p></div></div><div id="comments-container-56036" class="comments-container"></div><div id="comment-tools-56036" class="comment-tools"></div><div class="clear"></div><div id="comment-56036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56038"></span>

<div id="answer-container-56038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56038-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The radiotap header is <strong>not</strong> part of the 802.11 frame structure. It is a container for frame metadata which has been developed, like other pseudo-headers, in the absence of any dedicated container for metadata in the pcap file format. The newer pcapng format has introduced the idea of providing space for metadata clearly separated from the actual frame bytes, yet there is no proposed standard for any pcapng container replacing the radiotap header.</p><p>More details about the radiotap header can be found at <a href="http://www.radiotap.org/">its home page</a>.</p><p>There are also competing solutions to the same issue, like e.g. the <a href="https://en.wikipedia.org/wiki/TZSP">TZSP</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '16, 00:40</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56038" class="comments-container"></div><div id="comment-tools-56038" class="comment-tools"></div><div class="clear"></div><div id="comment-56038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


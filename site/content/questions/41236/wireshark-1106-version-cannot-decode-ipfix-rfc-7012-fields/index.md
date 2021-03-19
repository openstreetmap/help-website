+++
type = "question"
title = "Wireshark 1.10.6 version cannot decode IPFIX RFC 7012 fields"
description = '''Hi, I am running wireshark version 1.10.6 on my ubuntu version. I am exporting IPFIX flows. However WLAN fields like, 365 staMacAddress 366 staIPv4Address 367 wtpMacAddress are not decoded in wireshark. Its reported as unknown. These fields are from IPFIX RFC 7012. Any help will be appreciated. Than...'''
date = "2015-04-06T16:03:00Z"
lastmod = "2015-04-06T17:42:00Z"
weight = 41236
keywords = [ "decode" ]
aliases = [ "/questions/41236" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.10.6 version cannot decode IPFIX RFC 7012 fields](/questions/41236/wireshark-1106-version-cannot-decode-ipfix-rfc-7012-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41236-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am running wireshark version 1.10.6 on my ubuntu version. I am exporting IPFIX flows. However WLAN fields like, 365 staMacAddress 366 staIPv4Address 367 wtpMacAddress are not decoded in wireshark. Its reported as unknown. These fields are from IPFIX RFC 7012.</p><p>Any help will be appreciated.</p><p>Thanks SUNNY</p></div><div id="question-tags" class="tags-container tags">decode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/b749d51dfe735b74b5d8446f0ff59b50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnycs&#39;s gravatar image" /><p>sunnycs<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnycs has no accepted answers">0%</span></p></div></div><div id="comments-container-41236" class="comments-container"></div><div id="comment-tools-41236" class="comment-tools"></div><div class="clear"></div><div id="comment-41236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41237"></span>

<div id="answer-container-41237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41237-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>These fields were implemented in development in the Wireshark netflow(ipfix) dissector in Sep 2014..</p><p>The added code was considered an "enhancement" and thus was not backported to Wireshark 1.10 or 1.12.</p><p>So: (to be able to see these fields)</p><ol><li><p>You can download a Windows "development version" (1.99.5) and examine capture files as needed on a Windows PC (see wireshark.org/download.html).</p></li><li><p>You can build a "development" Wireshark on Ubuntu from the Wireshark development sources.</p></li><li><p>You can wait until the next major Wireshark release (1.14) which I expect will be available sometime in May/June 2015.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '15, 17:42</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '15, 17:45</p></div></div><div id="comments-container-41237" class="comments-container"></div><div id="comment-tools-41237" class="comment-tools"></div><div class="clear"></div><div id="comment-41237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


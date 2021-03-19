+++
type = "question"
title = "Is it possible in wireshark and t-shark to capture only data frame ( in monitor mode) for WIRELESS network?"
description = '''Want to capture only data frame on wireless network ( avoiding management and control frame )'''
date = "2014-02-16T02:09:00Z"
lastmod = "2014-02-16T02:59:00Z"
weight = 29903
keywords = [ "wireless", "frame", "data", "tshark", "wireshark" ]
aliases = [ "/questions/29903" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible in wireshark and t-shark to capture only data frame ( in monitor mode) for WIRELESS network?](/questions/29903/is-it-possible-in-wireshark-and-t-shark-to-capture-only-data-frame-in-monitor-mode-for-wireless-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29903-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Want to capture only data frame on wireless network ( avoiding management and control frame )</p></div><div id="question-tags" class="tags-container tags">wireless frame data tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/4f2e12b298828a7bdd200478480606da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIDS&#39;s gravatar image" /><p>WIDS<br />
<span class="score" title="25 reputation points">25</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIDS has no accepted answers">0%</span></p></div></div><div id="comments-container-29903" class="comments-container"></div><div id="comment-tools-29903" class="comment-tools"></div><div class="clear"></div><div id="comment-29903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29908"></span>

<div id="answer-container-29908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this</p><blockquote><p>tcpdump -ni mon0 'wlan type data'<br />
dumpcap -ni mon0 -f 'wlan type data'</p></blockquote><p><strong>Hint:</strong> If your (Unix/Linux/*BSD) system does not support the 'wlan' capture filter, you will need a newer release of libpcap on that system.</p><p>See also here (wlan type and subtype):</p><blockquote><p><a href="http://www.tcpdump.org/manpages/pcap-filter.7.txt">http://www.tcpdump.org/manpages/pcap-filter.7.txt</a><br />
<a href="http://sparebits.wikispaces.com/tcpdump+wireless+filters">http://sparebits.wikispaces.com/tcpdump+wireless+filters</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '14, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '14, 03:00</p></div></div><div id="comments-container-29908" class="comments-container"><span id="29918"></span><div id="comment-29918" class="comment"><div id="post-29918-score" class="comment-score"></div><div class="comment-text"><p>The same capture filter (<code>wlan type data</code>) can also be used by TShark and Wireshark as a capture filter. (<code>type data</code> by itself would work the same.)</p></div><div id="comment-29918-info" class="comment-info"><span class="comment-age">(16 Feb '14, 15:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-29908" class="comment-tools"></div><div class="clear"></div><div id="comment-29908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


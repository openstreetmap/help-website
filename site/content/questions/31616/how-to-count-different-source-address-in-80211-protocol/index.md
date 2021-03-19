+++
type = "question"
title = "How to count different source address in 802.11 protocol"
description = '''I want to count different source address in 802.11 protocol, and set &quot;wlan.fc.subtype eq 0 and wlan.fc.type eq 0&quot; as the display filter. The problem is how to count?'''
date = "2014-04-08T02:07:00Z"
lastmod = "2014-04-08T12:32:00Z"
weight = 31616
keywords = [ "count", "source", "802.11", "address" ]
aliases = [ "/questions/31616" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to count different source address in 802.11 protocol](/questions/31616/how-to-count-different-source-address-in-80211-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31616-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to count different source address in 802.11 protocol, and set "wlan.fc.subtype eq 0 and wlan.fc.type eq 0" as the display filter. The problem is how to count?</p></div><div id="question-tags" class="tags-container tags">count source 802.11 address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-31616" class="comments-container"></div><div id="comment-tools-31616" class="comment-tools"></div><div class="clear"></div><div id="comment-31616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31644"></span>

<div id="answer-container-31644" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31644-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this command:</p><pre><code>tshark -r file.pcap -R &quot;wlan.fc.subtype eq 0 and wlan.fc.type eq 0&quot; -T fields -e wlan.sa | sort | uniq -c | sort -nr</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '14, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '14, 12:32</p></div></div><div id="comments-container-31644" class="comments-container"></div><div id="comment-tools-31644" class="comment-tools"></div><div class="clear"></div><div id="comment-31644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


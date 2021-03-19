+++
type = "question"
title = "cannot join tshark packet capture filters"
description = '''The following two filters work fine individually to block unwanted packets tshark -i mon0 -f &quot;not ether host AA:AA:AA:AA:AA:AA&quot; tshark -i mon0 -f &quot;not ether host BB:BB:BB:BB:BB:BB&quot; but if i join the above filters,as shown below, then they do not block any packets. tshark -i mon0 -f &quot;not ether host A...'''
date = "2015-07-14T11:38:00Z"
lastmod = "2015-07-14T13:16:00Z"
weight = 44148
keywords = [ "capture-filter" ]
aliases = [ "/questions/44148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot join tshark packet capture filters](/questions/44148/cannot-join-tshark-packet-capture-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following two filters work fine individually to block unwanted packets</p><p>tshark -i mon0 -f "not ether host AA:AA:AA:AA:AA:AA"</p><p>tshark -i mon0 -f "not ether host BB:BB:BB:BB:BB:BB"</p><p>but if i join the above filters,as shown below, then they do not block any packets.</p><p>tshark -i mon0 -f "not ether host AA:AA:AA:AA:AA:AA and not ether host BB:BB:BB:BB:BB:BB"</p><p>tshark ver = 1.10.2</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/e095bc52921a2096b4ca9b6f20b9eecc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetgeek&#39;s gravatar image" /><p>packetgeek<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetgeek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '15, 11:44</p></div></div><div id="comments-container-44148" class="comments-container"></div><div id="comment-tools-44148" class="comment-tools"></div><div class="clear"></div><div id="comment-44148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44151"></span>

<div id="answer-container-44151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44151-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're using the wrong logical operator. Your filter as written will only block packets <em>from</em> AA:AA:AA:AA:AA:AA (hereafter "A") <em>to</em> BB:BB:BB:BB:BB:BB (hereafter "B") and <em>from</em> B <em>to</em> A. It sounds like you want to block all packets to and from A, and all packets to and from B, not just packets between A and B. Change your capture filter to:</p><p>-f "not (ether host AA:AA:AA:AA:AA:AA or ether host BB:BB:BB:BB:BB:BB)"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-44151" class="comments-container"></div><div id="comment-tools-44151" class="comment-tools"></div><div class="clear"></div><div id="comment-44151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


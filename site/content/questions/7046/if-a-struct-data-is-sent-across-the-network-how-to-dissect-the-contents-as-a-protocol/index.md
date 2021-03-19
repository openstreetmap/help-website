+++
type = "question"
title = "If a struct data is sent across the network how to dissect the contents as a protocol?"
description = '''If I send a structure data across then network, then can you tell me the best method to dissect the individual data? Network byte ordering is a problem. And why is the tcpdump program skipping some packets sometimes? I&#x27;ll be very thankful if you provide me a solution to the deadlock I&#x27;m facing.'''
date = "2011-10-23T11:24:00Z"
lastmod = "2012-02-28T11:45:00Z"
weight = 7046
keywords = [ "dissect", "structure" ]
aliases = [ "/questions/7046" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [If a struct data is sent across the network how to dissect the contents as a protocol?](/questions/7046/if-a-struct-data-is-sent-across-the-network-how-to-dissect-the-contents-as-a-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7046-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I send a structure data across then network, then can you tell me the best method to dissect the individual data? Network byte ordering is a problem. And why is the tcpdump program skipping some packets sometimes? I'll be very thankful if you provide me a solution to the deadlock I'm facing.</p></div><div id="question-tags" class="tags-container tags">dissect structure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '11, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/c1e23c746f5aca40005b6108e8e007ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aakash%20Tripathi&#39;s gravatar image" /><p>Aakash Tripathi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aakash Tripathi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:26</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7046" class="comments-container"></div><div id="comment-tools-7046" class="comment-tools"></div><div class="clear"></div><div id="comment-7046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9273"></span>

<div id="answer-container-9273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK, tcpdump will not process packets that are malformed. As for your other question "dissect the individual data" - you have to write your own plugin that would work with wireshark /tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '12, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/c2f093aae48ae803c3409e8eb2b2eb39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramesh&#39;s gravatar image" /><p>Ramesh<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramesh has no accepted answers">0%</span></p></div></div><div id="comments-container-9273" class="comments-container"></div><div id="comment-tools-9273" class="comment-tools"></div><div class="clear"></div><div id="comment-9273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


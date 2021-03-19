+++
type = "question"
title = "DDS - pcap or pcapng"
description = '''Hello, I am trying to get a handle on DDS, Are the wireshark versions that are out the built on 1.8 and greater where they capture pcapng. Or are they still on pcap. Doest the expanded metadata of pcapng lend itself to the DDS data like ID, Topic, Type and maybe QOS? - thanks'''
date = "2014-01-23T13:15:00Z"
lastmod = "2014-01-23T14:19:00Z"
weight = 29128
keywords = [ "dds", "captures" ]
aliases = [ "/questions/29128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DDS - pcap or pcapng](/questions/29128/dds-pcap-or-pcapng)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to get a handle on DDS, Are the wireshark versions that are out the built on 1.8 and greater where they capture pcapng. Or are they still on pcap. Doest the expanded metadata of pcapng lend itself to the DDS data like ID, Topic, Type and maybe QOS? - thanks</p></div><div id="question-tags" class="tags-container tags">dds captures</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '14, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/7a0eb204e0076bd694f571fcd0637e79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lostokie&#39;s gravatar image" /><p>lostokie<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lostokie has no accepted answers">0%</span></p></div></div><div id="comments-container-29128" class="comments-container"><span id="29129"></span><div id="comment-29129" class="comment"><div id="post-29129-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "DDS"?</p></div><div id="comment-29129-info" class="comment-info"><span class="comment-age">(23 Jan '14, 13:26)</span> Jasper ♦♦</div></div></div><div id="comment-tools-29128" class="comment-tools"></div><div class="clear"></div><div id="comment-29128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29130"></span>

<div id="answer-container-29130" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29130-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no relationship between DDS and pcapng! pcapng is a file format used to store network capture data, while DDS is a standard for data/message transport (for real-time systems).</p><p>So, what exactly is your question?</p><p>BTW: if you want to capture DDS messages, Wireshark does not care if you store the captured data in a pcap or pcapng file, as the DDS data structure is in the network frames, not the capture file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '14, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '14, 15:30</p></div></div><div id="comments-container-29130" class="comments-container"><span id="29132"></span><div id="comment-29132" class="comment"><div id="post-29132-score" class="comment-score"></div><div class="comment-text"><p>Kurt, you are definitely pointing me in the right direction. I will follow up soon - thanks</p></div><div id="comment-29132-info" class="comment-info"><span class="comment-age">(23 Jan '14, 19:29)</span> lostokie</div></div></div><div id="comment-tools-29130" class="comment-tools"></div><div class="clear"></div><div id="comment-29130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


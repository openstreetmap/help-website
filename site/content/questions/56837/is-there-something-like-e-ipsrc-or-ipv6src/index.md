+++
type = "question"
title = "Is there something like -e &quot;ip.src or ipv6.src&quot;"
description = '''Hi all, I want to use tshark -T and -e to extract data from PCAP file. Some of the data are ipv4 data, some are ipv6 data.  I&#x27;m using this line now: tshark -r test.pcap -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ipv6.src -e ip.dst -e ipv6.dst -e frame.len -E header=y -E separator=,...'''
date = "2016-10-30T14:14:00Z"
lastmod = "2016-10-30T14:39:00Z"
weight = 56837
keywords = [ "field", "selection" ]
aliases = [ "/questions/56837" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there something like -e "ip.src or ipv6.src"](/questions/56837/is-there-something-like-e-ipsrc-or-ipv6src)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56837-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I want to use tshark -T and -e to extract data from PCAP file. Some of the data are ipv4 data, some are ipv6 data.</p><p>I'm using this line now:</p><p>tshark -r test.pcap -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ipv6.src -e ip.dst -e ipv6.dst -e frame.len -E header=y -E separator=, &gt; test1.csv</p><p>then there would be empty fields in test1.csv, since the ipv4 data won't have ipv6.src and ipv6.dst.</p><p>Is there a way to select ip.src or ipv6.src, like -e "ip.src or ipv6.src"</p></div><div id="question-tags" class="tags-container tags">field selection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '16, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/ae67873a1f9c6cc6e852327f81a1a947?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zpymyyn&#39;s gravatar image" /><p>zpymyyn<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zpymyyn has no accepted answers">0%</span></p></div></div><div id="comments-container-56837" class="comments-container"></div><div id="comment-tools-56837" class="comment-tools"></div><div class="clear"></div><div id="comment-56837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56840"></span>

<div id="answer-container-56840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56840-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing like <code>-e "field_1 or field_2"</code> exists for a generic case, but in your particular one, <code>-e _ws.col.Source</code> should output either <code>ip.src</code> or <code>ipv6.src</code>, depending on their presence in the frame. I have no clue which one is output if both are present in the same frame, though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '16, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56840" class="comments-container"><span id="56841"></span><div id="comment-56841" class="comment"><div id="post-56841-score" class="comment-score"></div><div class="comment-text"><p>Hi sindy, thanks a lot!</p></div><div id="comment-56841-info" class="comment-info"><span class="comment-age">(30 Oct '16, 15:01)</span> zpymyyn</div></div><span id="56855"></span><div id="comment-56855" class="comment"><div id="post-56855-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-56855-info" class="comment-info"><span class="comment-age">(31 Oct '16, 02:43)</span> Jaap ♦</div></div><span id="56856"></span><div id="comment-56856" class="comment"><div id="post-56856-score" class="comment-score"></div><div class="comment-text"><p>But beware of <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13020">bug 13020</a>.</p></div><div id="comment-56856-info" class="comment-info"><span class="comment-age">(31 Oct '16, 02:44)</span> Jaap ♦</div></div></div><div id="comment-tools-56840" class="comment-tools"></div><div class="clear"></div><div id="comment-56840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


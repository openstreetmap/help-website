+++
type = "question"
title = "How do I know whether my network is half- or full-duplex?"
description = '''In Wireshark Network Analysis, Chapter 3 mentions half-duplex and full-duplex networks (and traffic). How can I determine which type of network I&#x27;m on?'''
date = "2010-11-30T17:38:00Z"
lastmod = "2010-11-30T19:46:00Z"
weight = 1185
keywords = [ "duplex", "half-duplex", "full-duplex" ]
aliases = [ "/questions/1185" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I know whether my network is half- or full-duplex?](/questions/1185/how-do-i-know-whether-my-network-is-half-or-full-duplex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark Network Analysis, Chapter 3 mentions half-duplex and full-duplex networks (and traffic). How can I determine which type of network I'm on?</p></div><div id="question-tags" class="tags-container tags">duplex half-duplex full-duplex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/71ecdbc454ca99d847bc355c5126e8c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sutch&#39;s gravatar image" /><p>sutch<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sutch has no accepted answers">0%</span></p></div></div><div id="comments-container-1185" class="comments-container"></div><div id="comment-tools-1185" class="comment-tools"></div><div class="clear"></div><div id="comment-1185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1186"></span>

<div id="answer-container-1186" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1186-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't really tell. If you hard code a switch port side (or the NIC side), it will not send any link pulses used by auto negotiation. However, if you hard code both sides (switch and the NIC), you will be running in FD network. So absence of link pulses is not enough to determine what type of network you are on.</p><p>In modern day networks, the vast majority of devices are running in FD mode. Not that HD was all that much slower than FD, but with switching being a commodity technology, almost no one runs in HD mode.</p><p>Exceptions to the FD rule include older printers, some industrial and vertical appliances. But the vast majority of today's network is running FD.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '10, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-1186" class="comments-container"><span id="1191"></span><div id="comment-1191" class="comment"><div id="post-1191-score" class="comment-score"></div><div class="comment-text"><p>This is true for 10/100 MBit networks using the 802.3u standard of negotiating HD/FD. Gigabit networks have a new standard (802.3z), where link pulses are sent even when the card is hard coded to avoid HD/FD mismatch errors. Correct me if I'm wrong :-)</p></div><div id="comment-1191-info" class="comment-info"><span class="comment-age">(01 Dec '10, 09:37)</span> Jasper ♦♦</div></div><span id="1195"></span><div id="comment-1195" class="comment"><div id="post-1195-score" class="comment-score"></div><div class="comment-text"><p>Off the top of my head, I don't recall if FLPs are sent in hard coded Gig world or not. But it's a moot point because there is no half duplex Gig. It's in the standard, but no manufacturer created nor sold a half duplex PHY. The idea of having to support carrier extensions etc probably scared them off! :)</p><p>I just wish I could go back in time and implore the 802.3 folks to make the "fallback" be FD. At the time it made sense to specify 100/HD as the "safe fallback" but nowadays, it's just damn annoying!!! It causes so many duplex mismatches.</p></div><div id="comment-1195-info" class="comment-info"><span class="comment-age">(01 Dec '10, 17:21)</span> hansangb</div></div><span id="1203"></span><div id="comment-1203" class="comment"><div id="post-1203-score" class="comment-score"></div><div class="comment-text"><p>Going back in time should be added to Wireshark v 1.6! &lt;g&gt;</p></div><div id="comment-1203-info" class="comment-info"><span class="comment-age">(02 Dec '10, 00:17)</span> lchappell ♦</div></div></div><div id="comment-tools-1186" class="comment-tools"></div><div class="clear"></div><div id="comment-1186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


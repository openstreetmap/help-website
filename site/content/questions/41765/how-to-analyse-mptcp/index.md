+++
type = "question"
title = "how to analyse mptcp"
description = '''almost every guide book says that mptcp protocol has been supported since the 1.7.1 version of wireshark ,but i cannot find the mptcp in the enabled-protocol in either 1.7.1 or 1.12.1.I want to analyse my simulation result using mptcp. Hope you guy help me to work with wireshark to analyse mptcp.'''
date = "2015-04-23T18:16:00Z"
lastmod = "2015-04-23T20:31:00Z"
weight = 41765
keywords = [ "mptcp" ]
aliases = [ "/questions/41765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to analyse mptcp](/questions/41765/how-to-analyse-mptcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>almost every guide book says that mptcp protocol has been supported since the 1.7.1 version of wireshark ,but i cannot find the mptcp in the enabled-protocol in either 1.7.1 or 1.12.1.I want to analyse my simulation result using mptcp. Hope you guy help me to work with wireshark to analyse mptcp.</p></div><div id="question-tags" class="tags-container tags">mptcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/b44cf28eb3409e80f2f30424bf5fd8e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryanhuang&#39;s gravatar image" /><p>ryanhuang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryanhuang has no accepted answers">0%</span></p></div></div><div id="comments-container-41765" class="comments-container"></div><div id="comment-tools-41765" class="comment-tools"></div><div class="clear"></div><div id="comment-41765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41766"></span>

<div id="answer-container-41766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41766-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A quick look at the Wireshark TCP dissector shows code related to mptcp.</p><p>I'm not familiar with mptcp, but the Wireshark code related to mptcp seems to be about dissecting tcp options.</p><p>So it appears that mptcp is not treated as a separate protocol but is handled in the TCP dissector.</p><p>Note: A web search for "mptcp wireshark" finds some hits which may provide additional info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-41766" class="comments-container"><span id="41767"></span><div id="comment-41767" class="comment"><div id="post-41767-score" class="comment-score"></div><div class="comment-text"><p>@ryanhuang: Wireshark dissects the MPTCP options in the TCP header. AFIAK it does not corelate the streams or generate any special mptcp statistics.</p><p>If you need that, the following tool might be interesting:</p><blockquote><p><a href="https://github.com/joaomlneto/mptcp-pcap-parser">https://github.com/joaomlneto/mptcp-pcap-parser</a></p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-41767-info" class="comment-info"><span class="comment-age">(23 Apr '15, 23:40)</span> Kurt Knochner ♦</div></div><span id="41775"></span><div id="comment-41775" class="comment"><div id="post-41775-score" class="comment-score"></div><div class="comment-text"><p>oops,according to your advice,i verify the packet by wireshark, and i found the mptcp option in the tcp option. There may be some errors in my simulation packets.Thanks a lot!</p></div><div id="comment-41775-info" class="comment-info"><span class="comment-age">(24 Apr '15, 05:32)</span> ryanhuang</div></div><span id="41781"></span><div id="comment-41781" class="comment"><div id="post-41781-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41781-info" class="comment-info"><span class="comment-age">(24 Apr '15, 07:35)</span> Jaap ♦</div></div></div><div id="comment-tools-41766" class="comment-tools"></div><div class="clear"></div><div id="comment-41766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


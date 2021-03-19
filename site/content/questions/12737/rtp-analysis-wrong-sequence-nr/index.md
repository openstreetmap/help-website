+++
type = "question"
title = "RTP Analysis: Wrong sequence nr."
description = '''Doing an RTP analysis to a file. After the RTP sequence number loops from 65534 to 18 (some packets missing in between), the rest of the packets are reported with status of &quot;Wrong sequence nr.&quot;. It seems like a bug??? '''
date = "2012-07-16T01:20:00Z"
lastmod = "2012-07-16T03:34:00Z"
weight = 12737
keywords = [ "nr", "rtp", "analysis", "sequence" ]
aliases = [ "/questions/12737" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Analysis: Wrong sequence nr.](/questions/12737/rtp-analysis-wrong-sequence-nr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12737-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Doing an RTP analysis to a file. After the RTP sequence number loops from 65534 to 18 (some packets missing in between), the rest of the packets are reported with status of "Wrong sequence nr.".</p><p>It seems like a bug???</p><p><img src="http://i.imgur.com/mFYW3.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">nr rtp analysis sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/3a24c77ae704b9a5fce1771c624af63c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jussivee&#39;s gravatar image" /><p>jussivee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jussivee has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '12, 01:21</p></div></div><div id="comments-container-12737" class="comments-container"></div><div id="comment-tools-12737" class="comment-tools"></div><div class="clear"></div><div id="comment-12737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12743"></span>

<div id="answer-container-12743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>what is your Wireshark version?</p><p>Can you post a sample capture file on <a href="http://cloudshark.org">cloudshark.org</a>?</p><p>HINT: As you cannot delete an anonymously uploaded file on <a href="http://cloudshark.org">cloudshark.org</a>, you better don't post any private data. Post just those packets in a capture file, that are required to analyze the problem.</p><p>UPDATE: looks like this bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5958">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5958</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-12743" class="comments-container"><span id="12911"></span><div id="comment-12911" class="comment"><div id="post-12911-score" class="comment-score"></div><div class="comment-text"><p>Converted Kurt's comment to an Answer since the update (with a link to the bug) is the answer. NOTE to jussivee: that bug is still awaiting a sample capture. It is unlikely anyone will be able to work on the bug until a sample capture is provided.</p></div><div id="comment-12911-info" class="comment-info"><span class="comment-age">(23 Jul '12, 06:45)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-12743" class="comment-tools"></div><div class="clear"></div><div id="comment-12743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


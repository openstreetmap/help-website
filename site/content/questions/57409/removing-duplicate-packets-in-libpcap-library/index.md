+++
type = "question"
title = "Removing duplicate packets in libpcap library"
description = '''I know about editcap which removes duplicate packets from capture files. However, I want to remove duplicate packets from libpcap itself. Is there any facility in libpcap ? If not then,  Is there any other way to achieve it ?  I mean by analyzing editcap source code, taking logic of removing duplica...'''
date = "2016-11-16T02:13:00Z"
lastmod = "2016-11-16T02:24:00Z"
weight = 57409
keywords = [ "duplicate", "libpcap" ]
aliases = [ "/questions/57409" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Removing duplicate packets in libpcap library](/questions/57409/removing-duplicate-packets-in-libpcap-library)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57409-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know about editcap which removes duplicate packets from capture files.</p><p>However, I want to remove duplicate packets from libpcap itself. Is there any facility in libpcap ?</p><p>If not then, Is there any other way to achieve it ?</p><p>I mean by analyzing editcap source code, taking logic of removing duplicates from it and adding that into libpcap. Is it the proper way ?</p></div><div id="question-tags" class="tags-container tags">duplicate libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '16, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p>Mehul28<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div></div><div id="comments-container-57409" class="comments-container"></div><div id="comment-tools-57409" class="comment-tools"></div><div class="clear"></div><div id="comment-57409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57412"></span>

<div id="answer-container-57412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57412-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The proper "unix" way would be to write a filter which would read the output of dumpcap from a pipe, store the frames in a history window of a depth stated as a command line parameter, and forward the frames to its output pipe on which tshark or Wireshark would be listening. This way, you'd not risk breaking anything in the libpcap. But it doesn't actually matter whether you implement the algorithm into libpcap or as a separate filter.</p><p>You would compare each new frame with all those in the buffer, ignoring the timestamp while comparing, and only forward it to the output if it would not match any of them. It is actually what editcap does, except it seems not to be able to act as a filter, i.e. to read its input and write its output from/to a pipe.</p><p>You just have to bear in mind that the first chunk of data you receive is the pcap or pcapng header, and that you must copy it to the output unchanged, and that by interpreting it you recognize how the individual frames are formatted.</p><p>Another thing to bear in mind is that the window must be controlled both by depth (number of frames) and time elapsed between the original and the suspected duplicate. Some frames carrying low level protocols which really exist in the network may be undistinguishable from one another, so only those really close by timestamp are duplicates caused by e.g. port mirroring on a VLAN, which may cause each packet to be captured twice (or even more times if a broadcast packet comes in through one port and gets out through ten others), depending on how the mirroring is implemented on the switch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Nov '16, 04:50</p></div></div><div id="comments-container-57412" class="comments-container"><span id="57413"></span><div id="comment-57413" class="comment"><div id="post-57413-score" class="comment-score"></div><div class="comment-text"><p>Ok. Your suggestion is very good.</p><p>But my requirement is to make some changes in libpcap code to filter duplicates.</p><p>Do you have any idea on that ?</p></div><div id="comment-57413-info" class="comment-info"><span class="comment-age">(16 Nov '16, 03:27)</span> Mehul28</div></div><span id="57414"></span><div id="comment-57414" class="comment"><div id="post-57414-score" class="comment-score"></div><div class="comment-text"><p>As stated above, the filtering algorithm is the same regardless whether you place it into libpcap or into a userspace executable. libpcap has no additional information which you could use to identify the duplicates easier than that - it sends out all the information it has itself.</p></div><div id="comment-57414-info" class="comment-info"><span class="comment-age">(16 Nov '16, 03:35)</span> sindy</div></div><span id="57416"></span><div id="comment-57416" class="comment"><div id="post-57416-score" class="comment-score"></div><div class="comment-text"><p>ok. Thanks @sindy</p></div><div id="comment-57416-info" class="comment-info"><span class="comment-age">(16 Nov '16, 03:49)</span> Mehul28</div></div></div><div id="comment-tools-57412" class="comment-tools"></div><div class="clear"></div><div id="comment-57412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


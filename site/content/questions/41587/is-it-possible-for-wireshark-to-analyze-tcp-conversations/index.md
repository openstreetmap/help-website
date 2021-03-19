+++
type = "question"
title = "Is it possible for Wireshark to analyze (TCP) conversations?"
description = '''Good day everyone. I am interested in application protocols analysis, especially those whose data (or payload) can&#x27;t be transferred by means of only one network packet. My question so, is it possible for Wireshark to analyze for example assembled TCP-conversations to extract application layer protoc...'''
date = "2015-04-20T01:26:00Z"
lastmod = "2015-04-20T02:09:00Z"
weight = 41587
keywords = [ "conversations", "protocols", "analysis", "application" ]
aliases = [ "/questions/41587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible for Wireshark to analyze (TCP) conversations?](/questions/41587/is-it-possible-for-wireshark-to-analyze-tcp-conversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good day everyone.</p><p>I am interested in application protocols analysis, especially those whose data (or payload) can't be transferred by means of only one network packet. My question so, is it possible for Wireshark to analyze for example assembled TCP-conversations to extract application layer protocols data? As far as I know Wireshark tries to make such an analysis (application protocol extraction) for each network packet separately, except IPv4 defragmentation. If I'm wrong, please explain me how Wireshark can help me with my problem. Otherwise don't you want to add such an opportunity (I mean an analysis of assembled conversations) at least for some application layer protocols?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">conversations protocols analysis application</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/c701a53dad43a1abbb8fc95d7b555e7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ustas&#39;s gravatar image" /><p>ustas<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ustas has no accepted answers">0%</span></p></div></div><div id="comments-container-41587" class="comments-container"></div><div id="comment-tools-41587" class="comment-tools"></div><div class="clear"></div><div id="comment-41587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41591"></span>

<div id="answer-container-41591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41591-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Wireshark does packet reassembly for content that spans over multiple packets. You can see that it does if you try the "export objects" menu option in the file menu.</p><p>So it's already there, for IP fragmentation as well as TCP segments and SSL.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41591" class="comments-container"><span id="41791"></span><div id="comment-41791" class="comment"><div id="post-41791-score" class="comment-score"></div><div class="comment-text"><p>Jasper thanks for a fast answer. I found that Wireshark may export objects transferred through HTTP, DICOM, SMB/SMB2. This is useful for me but not exactly what I want. For example some proprietary protocol uses TCP as a transport for its own packets and each packet spans over multiple TCP packets. I want to parse packets of that proprietary protocol. Can Wireshark help me with such a problem? How does Wireshark operate on reassembled TCP? Is it possible to apply "the same" parser both to packets and reassembled conversations?</p></div><div id="comment-41791-info" class="comment-info"><span class="comment-age">(24 Apr '15, 09:18)</span> ustas</div></div><span id="41792"></span><div id="comment-41792" class="comment"><div id="post-41792-score" class="comment-score"></div><div class="comment-text"><p>You'll need to write a dissector for that protocol, and the dissector will require code to manage the reassembly of protocol data spread over multiple packets.</p><p>This is all standard fare for Wireshark dissectors.</p></div><div id="comment-41792-info" class="comment-info"><span class="comment-age">(24 Apr '15, 09:27)</span> grahamb ♦</div></div></div><div id="comment-tools-41591" class="comment-tools"></div><div class="clear"></div><div id="comment-41591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


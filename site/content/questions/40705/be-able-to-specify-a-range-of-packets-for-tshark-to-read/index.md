+++
type = "question"
title = "Be able to specify a range of packets for tshark to read"
description = '''Have a bunch of big pcap files to be processed by tshark. Would like tshark to read first 20 packets of each pcap files first. The benefit is that I can use a script to control whether it&#x27;s worth to let tshark to consume the entire pcap file. Wonder if there is a command line option to do it. Thanks...'''
date = "2015-03-19T20:05:00Z"
lastmod = "2015-03-19T20:18:00Z"
weight = 40705
keywords = [ "tshark" ]
aliases = [ "/questions/40705" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Be able to specify a range of packets for tshark to read](/questions/40705/be-able-to-specify-a-range-of-packets-for-tshark-to-read)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have a bunch of big pcap files to be processed by tshark. Would like tshark to read first 20 packets of each pcap files first. The benefit is that I can use a script to control whether it's worth to let tshark to consume the entire pcap file. Wonder if there is a command line option to do it.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p>sharkfun<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span></p></div></div><div id="comments-container-40705" class="comments-container"></div><div id="comment-tools-40705" class="comment-tools"></div><div class="clear"></div><div id="comment-40705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40706"></span>

<div id="answer-container-40706" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40706-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, there is a <code>tshark</code> command-line option available to limit the number of packets read from a capture file. It is the "<code>-c</code>" option. Refer to the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40706" class="comments-container"><span id="40707"></span><div id="comment-40707" class="comment"><div id="post-40707-score" class="comment-score"></div><div class="comment-text"><p>Thank you cmaynard for the quick answer! It works.</p></div><div id="comment-40707-info" class="comment-info"><span class="comment-age">(19 Mar '15, 20:20)</span> sharkfun</div></div></div><div id="comment-tools-40706" class="comment-tools"></div><div class="clear"></div><div id="comment-40706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


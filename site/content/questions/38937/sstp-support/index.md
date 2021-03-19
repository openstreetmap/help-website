+++
type = "question"
title = "SSTP support"
description = '''Hi I would like to know does Wireshark 1.12.x supports SSTP protocol? http://wiki.wireshark.org/SSTP From the above site it seems that it does however when I type in the SSTP as the display filter it does not exist. Regards Sieg'''
date = "2015-01-08T00:30:00Z"
lastmod = "2015-01-08T03:47:00Z"
weight = 38937
keywords = [ "sstp" ]
aliases = [ "/questions/38937" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSTP support](/questions/38937/sstp-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38937-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I would like to know does Wireshark 1.12.x supports SSTP protocol?</p><p><a href="http://wiki.wireshark.org/SSTP">http://wiki.wireshark.org/SSTP</a></p><p>From the above site it seems that it does however when I type in the SSTP as the display filter it does not exist.</p><p>Regards Sieg</p></div><div id="question-tags" class="tags-container tags">sstp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/515842adc9a4a6d0da2b7cd5ad32a6c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sieg9198&#39;s gravatar image" /><p>Sieg9198<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sieg9198 has no accepted answers">0%</span></p></div></div><div id="comments-container-38937" class="comments-container"></div><div id="comment-tools-38937" class="comment-tools"></div><div class="clear"></div><div id="comment-38937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38943"></span>

<div id="answer-container-38943" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38943-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8239">Bug 8239</a> the Author of the SSTP dissector already created the SSTP Wiki page, but the SSTP dissector was not yet added to the "official" code base, due to some open questions.</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8239">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8239</a></p></blockquote><p>So, to answer your question: No, Wireshark does not yet support SSTP, however the dissector code already exists. It just needs somebody to finish it, so it can be included in the wireshark code base.</p><p>Rgards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '15, 05:33</p></div></div><div id="comments-container-38943" class="comments-container"><span id="38984"></span><div id="comment-38984" class="comment"><div id="post-38984-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. Hopefully it will be supported in the near future.</p></div><div id="comment-38984-info" class="comment-info"><span class="comment-age">(08 Jan '15, 19:41)</span> Sieg9198</div></div><span id="39007"></span><div id="comment-39007" class="comment"><div id="post-39007-score" class="comment-score">2</div><div class="comment-text"><p>I updated the wiki to indicate that the dissector hasn't been merged.</p></div><div id="comment-39007-info" class="comment-info"><span class="comment-age">(09 Jan '15, 10:41)</span> JeffMorriss ♦</div></div><span id="39017"></span><div id="comment-39017" class="comment"><div id="post-39017-score" class="comment-score"></div><div class="comment-text"><p>@JeffMorriss: I moved your comment to the top of the wiki page, as it was a bit hard to spot.</p></div><div id="comment-39017-info" class="comment-info"><span class="comment-age">(10 Jan '15, 04:34)</span> Kurt Knochner ♦</div></div><span id="39992"></span><div id="comment-39992" class="comment"><div id="post-39992-score" class="comment-score"></div><div class="comment-text"><p>BTW I fixed up the SSTP dissector and it was merged a few days ago. So: you can now pick up an <a href="http://www.wireshark.org/download/automated/">automated build</a> with SSTP support and version 1.99.3 will include it (whenever it comes out).</p></div><div id="comment-39992-info" class="comment-info"><span class="comment-age">(20 Feb '15, 12:18)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-38943" class="comment-tools"></div><div class="clear"></div><div id="comment-38943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


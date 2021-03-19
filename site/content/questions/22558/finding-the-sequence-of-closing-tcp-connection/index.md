+++
type = "question"
title = "Finding the sequence of closing TCP connection"
description = '''how to identify the sequence of closing TCP connection from a saved trace?'''
date = "2013-07-02T10:02:00Z"
lastmod = "2013-07-02T10:38:00Z"
weight = 22558
keywords = [ "network", "networking", "trace", "tcp", "wireshark" ]
aliases = [ "/questions/22558" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding the sequence of closing TCP connection](/questions/22558/finding-the-sequence-of-closing-tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22558-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to identify the sequence of closing TCP connection from a saved trace?</p></div><div id="question-tags" class="tags-container tags">network networking trace tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/03b3862efeee5519aa5b05e0e01d6e98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irock732&#39;s gravatar image" /><p>Irock732<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irock732 has no accepted answers">0%</span></p></div></div><div id="comments-container-22558" class="comments-container"></div><div id="comment-tools-22558" class="comment-tools"></div><div class="clear"></div><div id="comment-22558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22559"></span>

<div id="answer-container-22559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22559-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP connection will be closed with segments with either FIN flag set or RST Flag set.Check out the tcp segments with these Flags set to start with to identify the closing sequence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '13, 10:51</p></div></div><div id="comments-container-22559" class="comments-container"><span id="22573"></span><div id="comment-22573" class="comment"><div id="post-22573-score" class="comment-score"></div><div class="comment-text"><p>you can use the following display filter:</p><blockquote><p>tcp.flags.fin eq 1 or tcp.flags.reset eq 1</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-22573-info" class="comment-info"><span class="comment-age">(02 Jul '13, 14:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22559" class="comment-tools"></div><div class="clear"></div><div id="comment-22559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


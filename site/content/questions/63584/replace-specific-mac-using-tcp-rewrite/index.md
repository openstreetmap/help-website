+++
type = "question"
title = "Replace specific MAC using tcp-rewrite"
description = '''I&#x27;m trying to replace a specific MAC address in a pcap using tcp-rewrite and can&#x27;t figure out how to do it.  It looks like it replace ALL the macs when I use the -enet-dmac command (or -enet-smac).  I want to substitute one specific MAC with another specific MAC.'''
date = "2017-09-12T00:07:00Z"
lastmod = "2017-09-12T01:11:00Z"
weight = 63584
keywords = [ "tcprewrite" ]
aliases = [ "/questions/63584" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Replace specific MAC using tcp-rewrite](/questions/63584/replace-specific-mac-using-tcp-rewrite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to replace a specific MAC address in a pcap using tcp-rewrite and can't figure out how to do it. It looks like it replace ALL the macs when I use the -enet-dmac command (or -enet-smac). I want to substitute one specific MAC with another specific MAC.</p></div><div id="question-tags" class="tags-container tags">tcprewrite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '17, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/b50e05a5f1954d250dd908dacce081c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdani&#39;s gravatar image" /><p>kdani<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdani has no accepted answers">0%</span></p></div></div><div id="comments-container-63584" class="comments-container"><span id="63588"></span><div id="comment-63588" class="comment"><div id="post-63588-score" class="comment-score"></div><div class="comment-text"><p>Arguably, questions about tcprewrite are off topic for this site although there are a number of folks around that can help or suggest alternative approaches so I'll let these slide for now.</p></div><div id="comment-63588-info" class="comment-info"><span class="comment-age">(12 Sep '17, 04:37)</span> grahamb ♦</div></div></div><div id="comment-tools-63584" class="comment-tools"></div><div class="clear"></div><div id="comment-63584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63585"></span>

<div id="answer-container-63585" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63585-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't have the requirement of using tcprewrite it may be easier to do that with <a href="https://www.tracewrangler.com">TraceWrangler</a>. It requires Windows or running it using WINE on Linux.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '17, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63585" class="comments-container"><span id="63589"></span><div id="comment-63589" class="comment"><div id="post-63589-score" class="comment-score"></div><div class="comment-text"><p>thanks, it is possible solution - I managed to do it using another tool: <a href="http://www.lovemytool.com/blog/2011/05/bittwiste-pcap-capture-file-editor-by-joke-snelders.html">http://www.lovemytool.com/blog/2011/05/bittwiste-pcap-capture-file-editor-by-joke-snelders.html</a></p></div><div id="comment-63589-info" class="comment-info"><span class="comment-age">(12 Sep '17, 05:09)</span> kdani</div></div></div><div id="comment-tools-63585" class="comment-tools"></div><div class="clear"></div><div id="comment-63585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


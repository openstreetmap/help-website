+++
type = "question"
title = "Display HTTP Header"
description = '''Hello. I am using WireShark on the Windows 7 platform. I was wondering if someone could tell me the settings I should use in my WireShark to log the full HTTP header for any traces I run in the program? Many thanks in advance. DC.'''
date = "2012-08-06T02:28:00Z"
lastmod = "2012-08-06T03:22:00Z"
weight = 13384
keywords = [ "header", "http", "log", "address.", "ip" ]
aliases = [ "/questions/13384" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display HTTP Header](/questions/13384/display-http-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I am using WireShark on the Windows 7 platform.</p><p>I was wondering if someone could tell me the settings I should use in my WireShark to log the full HTTP header for any traces I run in the program?</p><p>Many thanks in advance. DC.</p></div><div id="question-tags" class="tags-container tags">header http log address. ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/bad885338a1b55b021a5426449cc44ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DustinCook&#39;s gravatar image" /><p>DustinCook<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DustinCook has no accepted answers">0%</span></p></div></div><div id="comments-container-13384" class="comments-container"><span id="13385"></span><div id="comment-13385" class="comment"><div id="post-13385-score" class="comment-score"></div><div class="comment-text"><p>Can I also setup WireShark to detect if a web-based proxy site is being used?</p></div><div id="comment-13385-info" class="comment-info"><span class="comment-age">(06 Aug '12, 03:06)</span> DustinCook</div></div></div><div id="comment-tools-13384" class="comment-tools"></div><div class="clear"></div><div id="comment-13384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13386"></span>

<div id="answer-container-13386" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13386-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark captures full packets by default, so all HTTP headers are included anyway. You just need to open the HTTP section in the decode pane to see them all.</p><p>If someone uses a proxy you can often see a "X-Forwarded-For" header that tells you for which original IP address the request was processed by the proxy. If the proxy administrator is aware of this he might choose to hide it or replace it with some anonymized address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13386" class="comments-container"></div><div id="comment-tools-13386" class="comment-tools"></div><div class="clear"></div><div id="comment-13386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


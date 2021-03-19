+++
type = "question"
title = "School wireshark"
description = '''I have run Wireshark on my school but can i read passwords or a remote desktop IP or something? And which filters should i use?'''
date = "2013-04-02T10:35:00Z"
lastmod = "2013-04-02T10:39:00Z"
weight = 20026
keywords = [ "school", "wireshark" ]
aliases = [ "/questions/20026" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [School wireshark](/questions/20026/school-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20026-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have run Wireshark on my school but can i read passwords or a remote desktop IP or something? And which filters should i use?</p></div><div id="question-tags" class="tags-container tags">school wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/545b15bbff79b8b6e4d9ca2991c16ecf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anony1&#39;s gravatar image" /><p>anony1<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anony1 has no accepted answers">0%</span></p></div></div><div id="comments-container-20026" class="comments-container"><span id="20028"></span><div id="comment-20028" class="comment"><div id="post-20028-score" class="comment-score"></div><div class="comment-text"><p>what is your use case?</p></div><div id="comment-20028-info" class="comment-info"><span class="comment-age">(02 Apr '13, 10:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20026" class="comment-tools"></div><div class="clear"></div><div id="comment-20026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20027"></span>

<div id="answer-container-20027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20027-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on the network setup at your school. If they're still on steam powered technology like hubs (okay, not really steam powered, but it feels that way) then you might be able to capture packets of other computers. If there are switches, you can't unless you're able to configure a monitor session on the switch.</p><p>But even if you capture some packets you're usually not going to see much in regard to remote desktop passwords since the protocols are all encrypted. There are also not filters that help with reading passwords from remote desktop protocols; the only passwords you could gather would be those of plain text protocols like FTP or POP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20027" class="comments-container"><span id="20029"></span><div id="comment-20029" class="comment"><div id="post-20029-score" class="comment-score"></div><div class="comment-text"><blockquote><p>the only passwords you could gather would be those of plain text protocols like FTP or POP</p></blockquote><p>...as opposed to non-plain-text protocols such as, for example, FTP or POP over SSL. I.e., even nominally plain-text protocol might be encrypted by running them over SSL, so it'll be a bit hard to find passwords on the wire.</p></div><div id="comment-20029-info" class="comment-info"><span class="comment-age">(02 Apr '13, 11:16)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-20027" class="comment-tools"></div><div class="clear"></div><div id="comment-20027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Get Stream index for a given packet number"
description = '''Hi, In wireshark is there a way to get Stream index if we give packet number? What I want is a stream index so I can feed the stream index and get the whole TCP Session data. '''
date = "2016-04-25T12:20:00Z"
lastmod = "2016-04-25T12:48:00Z"
weight = 51933
keywords = [ "tshark", "tcp" ]
aliases = [ "/questions/51933" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Get Stream index for a given packet number](/questions/51933/get-stream-index-for-a-given-packet-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51933-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, In wireshark is there a way to get Stream index if we give packet number? What I want is a stream index so I can feed the stream index and get the whole TCP Session data.</p></div><div id="question-tags" class="tags-container tags">tshark tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '16, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/7caa9119ad86b6419829d6e3cabdb12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WSharkUser&#39;s gravatar image" /><p>WSharkUser<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WSharkUser has no accepted answers">0%</span></p></div></div><div id="comments-container-51933" class="comments-container"></div><div id="comment-tools-51933" class="comment-tools"></div><div class="clear"></div><div id="comment-51933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51936"></span>

<div id="answer-container-51936" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51936-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>yes, like this, e.g. for file "test.pcapng" and frame number 100:</p><p>tshark -r "test.pcapng" -Y "frame.number==100" -Tfields -e tcp.stream</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51936" class="comments-container"><span id="51937"></span><div id="comment-51937" class="comment"><div id="post-51937-score" class="comment-score"></div><div class="comment-text"><p>awesome. That worked like a charm. Thanks so much Jasper.</p></div><div id="comment-51937-info" class="comment-info"><span class="comment-age">(25 Apr '16, 12:52)</span> WSharkUser</div></div><span id="51949"></span><div id="comment-51949" class="comment"><div id="post-51949-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51949-info" class="comment-info"><span class="comment-age">(26 Apr '16, 00:43)</span> Jaap ♦</div></div></div><div id="comment-tools-51936" class="comment-tools"></div><div class="clear"></div><div id="comment-51936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


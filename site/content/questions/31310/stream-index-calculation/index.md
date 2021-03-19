+++
type = "question"
title = "Stream index calculation"
description = '''I have a question about Stream index... it is calculated by some mathematical formula or some other ways? or its related to source port and destination port?'''
date = "2014-03-31T02:20:00Z"
lastmod = "2014-03-31T03:41:00Z"
weight = 31310
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/31310" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Stream index calculation](/questions/31310/stream-index-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a question about Stream index... it is calculated by some mathematical formula or some other ways? or its related to source port and destination port?</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/2778b8a828c134235c29e2a34f72a70b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Petrusca%20Victor&#39;s gravatar image" /><p>Petrusca Victor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Petrusca Victor has no accepted answers">0%</span></p></div></div><div id="comments-container-31310" class="comments-container"></div><div id="comment-tools-31310" class="comment-tools"></div><div class="clear"></div><div id="comment-31310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31312"></span>

<div id="answer-container-31312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31312-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is counted by conversation, which is based on TCP and UDP socket pairs. So each socket pair (consisting of IP_1:Port_1 - IP_2:Port_2) is a conversation, with TCP and UDP being calculated separately.</p><p>The first conversation has stream index 0, the second has stream index 1, and so on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '14, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31312" class="comments-container"><span id="31313"></span><div id="comment-31313" class="comment"><div id="post-31313-score" class="comment-score"></div><div class="comment-text"><p>thanx for answer Jasper</p></div><div id="comment-31313-info" class="comment-info"><span class="comment-age">(31 Mar '14, 06:51)</span> Petrusca Victor</div></div><span id="51934"></span><div id="comment-51934" class="comment"><div id="post-51934-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, is there a way to get the stream index number if we provide packet number to tshark?</p></div><div id="comment-51934-info" class="comment-info"><span class="comment-age">(25 Apr '16, 12:36)</span> WSharkUser</div></div><span id="51935"></span><div id="comment-51935" class="comment"><div id="post-51935-score" class="comment-score"></div><div class="comment-text"><p>yes, like this, e.g. for file "test.pcapng" and frame number 100:</p><p>tshark -r "test.pcapng" -Y "frame.number==100" -Tfields -e tcp.stream</p></div><div id="comment-51935-info" class="comment-info"><span class="comment-age">(25 Apr '16, 12:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-31312" class="comment-tools"></div><div class="clear"></div><div id="comment-31312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


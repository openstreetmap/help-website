+++
type = "question"
title = "Query on tcp segment of a reassembled pdu option"
description = '''I am aware of what this feature does but i would like to know more on when to enable this feature and when to disable it. When i enable the tcp reassembly i am not seeing any HTTP 200 OK Responses but seeing tcp segment of reassembled pdu. When i disable the tcp reassembly i am seeing HTTP 200 OK re...'''
date = "2013-04-08T12:14:00Z"
lastmod = "2013-04-08T12:17:00Z"
weight = 20193
keywords = [ "reassembled", "pdu", "tcp" ]
aliases = [ "/questions/20193" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Query on tcp segment of a reassembled pdu option](/questions/20193/query-on-tcp-segment-of-a-reassembled-pdu-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am aware of what this feature does but i would like to know more on when to enable this feature and when to disable it.</p><p>When i enable the tcp reassembly i am not seeing any HTTP 200 OK Responses but seeing tcp segment of reassembled pdu.</p><p>When i disable the tcp reassembly i am seeing HTTP 200 OK response.</p><p>As i told earlier i want to know more on when to enable and when to disable this option.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">reassembled pdu tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '13, 13:11</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-20193" class="comments-container"></div><div id="comment-tools-20193" class="comment-tools"></div><div class="clear"></div><div id="comment-20193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20194"></span>

<div id="answer-container-20194" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20194-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should see the HTTP 200 OK in the info column either way, but with reassembly enabled it is displayed in the <strong>last</strong> packet of the content, not the first (where it is in reality, if you check the payload)</p><p>My rule of thumb: disable TCP reassembly by default. Enable if you need to reconstruct payload content, e.g. for forensic analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20194" class="comments-container"><span id="20196"></span><div id="comment-20196" class="comment"><div id="post-20196-score" class="comment-score"></div><div class="comment-text"><p>Thanks.As you mentioned i am seeing http 200 Ok in both cases.In case of tcp reassembly disabled the 200 OK packet size is 1502 but when it is enabled the 200 OK packet size is 712 bytes. Can you please clear me the reason behind this?</p></div><div id="comment-20196-info" class="comment-info"><span class="comment-age">(08 Apr '13, 12:28)</span> krishnayeddula</div></div><span id="20198"></span><div id="comment-20198" class="comment"><div id="post-20198-score" class="comment-score">2</div><div class="comment-text"><p>That's because the packet size is the size of the current packet, not of the reassembled higher layer PDU. And the last segment of a reassembled PDU is usually smaller than the others...</p></div><div id="comment-20198-info" class="comment-info"><span class="comment-age">(08 Apr '13, 12:42)</span> SYN-bit ♦♦</div></div><span id="20199"></span><div id="comment-20199" class="comment"><div id="post-20199-score" class="comment-score"></div><div class="comment-text"><p>Got it.Thanks</p></div><div id="comment-20199-info" class="comment-info"><span class="comment-age">(08 Apr '13, 12:45)</span> krishnayeddula</div></div></div><div id="comment-tools-20194" class="comment-tools"></div><div class="clear"></div><div id="comment-20194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Help decoding MoldUDP64 payload as Nasdaq ITCH"
description = '''Greetings, How do I get wireshark to decode the Payload of all MoldUDP64 packets as &quot;Nasdaq-ITCH&quot;? When I right-click Payload and do &quot;Decode as...&quot;, the ITCH protocol is not listed as an option. Thanks in advance, MB'''
date = "2015-10-23T09:01:00Z"
lastmod = "2015-10-23T16:49:00Z"
weight = 46882
keywords = [ "moldudp64", "nasdaq" ]
aliases = [ "/questions/46882" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help decoding MoldUDP64 payload as Nasdaq ITCH](/questions/46882/help-decoding-moldudp64-payload-as-nasdaq-itch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46882-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>How do I get wireshark to decode the Payload of all MoldUDP64 packets as "Nasdaq-ITCH"?</p><p>When I right-click Payload and do "Decode as...", the ITCH protocol is not listed as an option.</p><p>Thanks in advance,</p><p>MB</p></div><div id="question-tags" class="tags-container tags">moldudp64 nasdaq</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '15, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/f97757ee0d0e7371de0299c61701765f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marsblack&#39;s gravatar image" /><p>marsblack<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marsblack has no accepted answers">0%</span></p></div></div><div id="comments-container-46882" class="comments-container"></div><div id="comment-tools-46882" class="comment-tools"></div><div class="clear"></div><div id="comment-46882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46897"></span>

<div id="answer-container-46897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46897-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MoldUDP64 dissector goes so far as to dissect message blocks. There's no relation to Nasdaq-ITCH made. I've no sample capture to work out if that could be made so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '15, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46897" class="comments-container"><span id="46898"></span><div id="comment-46898" class="comment"><div id="post-46898-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap.</p><p>Suppose I want to force the Payload field of all MoldUDP64 packets to be dissected as Nasdaq-ITCH in my capture.</p><ol><li>Can that be done through the GUI?</li><li>If not, I assume I might have to customize <code>proto_reg_handoff_nasdaq_itch()</code> in packet-nasdaq-itch.c to add a dissector to moldudp64. Am I on the right track? Can you advise on what the call to <code>dissector_add_uint()</code> would look like?</li></ol><p>Kind regards.</p></div><div id="comment-46898-info" class="comment-info"><span class="comment-age">(23 Oct '15, 14:59)</span> marsblack</div></div><span id="46905"></span><div id="comment-46905" class="comment"><div id="post-46905-score" class="comment-score"></div><div class="comment-text"><p>As Michael Mann says in his answer, "it doesn't appear like MoldUDP64 has a "unique identifier" to determine Nasdaq-ITCH", so there's nothing to use in a call to <code>dissector_add_uint()</code>, and that call shouldn't exist.</p><p>See the code review he linked to in the comment he made to his reply.</p></div><div id="comment-46905-info" class="comment-info"><span class="comment-age">(24 Oct '15, 11:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-46897" class="comment-tools"></div><div class="clear"></div><div id="comment-46897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46899"></span>

<div id="answer-container-46899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need 2 things: 1. A dissector table created in MoldUDP64. The Nasdaq-ITCH dissector would register with this table. 2. A "Decode As" structure created in MoldUDP64 (using register_decode_as).</p><p>Based on the information provided, it doesn't appear like MoldUDP64 has a "unique identifier" to determine Nasdaq-ITCH, so I recommend using the "sample code" in packet-socketcan.c or packet-enip.c for how their "subdissectors" are exposed through Decode As.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '15, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/84070f0cd61650ab31aad30384b959f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Mann&#39;s gravatar image" /><p>Michael Mann<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Mann has no accepted answers">0%</span></p></div></div><div id="comments-container-46899" class="comments-container"><span id="46902"></span><div id="comment-46902" class="comment"><div id="post-46902-score" class="comment-score"></div><div class="comment-text"><p>Threw something together here: <a href="https://code.wireshark.org/review/11235/">https://code.wireshark.org/review/11235/</a></p></div><div id="comment-46902-info" class="comment-info"><span class="comment-age">(23 Oct '15, 17:37)</span> Michael Mann</div></div></div><div id="comment-tools-46899" class="comment-tools"></div><div class="clear"></div><div id="comment-46899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


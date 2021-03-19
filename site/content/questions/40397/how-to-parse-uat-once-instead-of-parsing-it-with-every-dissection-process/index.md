+++
type = "question"
title = "How to parse UAT once instead of parsing it with every dissection process?"
description = '''My dissector has a (User Accsess Table) UAT related to it. I found that it is parsed every time wireshark dissects a relevant packet. I only want the UAT parsed once not every time wiresharks dissect a packet by using my dissector. Can I control this? if yes, how can I do so?  Note: My parsing funct...'''
date = "2015-03-09T12:50:00Z"
lastmod = "2015-03-10T11:06:00Z"
weight = 40397
keywords = [ "wireshark", "uat", "parsing" ]
aliases = [ "/questions/40397" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to parse UAT once instead of parsing it with every dissection process?](/questions/40397/how-to-parse-uat-once-instead-of-parsing-it-with-every-dissection-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My dissector has a (User Accsess Table) UAT related to it. I found that it is parsed every time wireshark dissects a relevant packet. I only want the UAT parsed once not every time wiresharks dissect a packet by using my dissector. Can I control this? if yes, how can I do so? Note: My parsing function currently is defined in packet-foo.c and is called in dissect_foo().</p><p>Thanks flora</p></div><div id="question-tags" class="tags-container tags">wireshark uat parsing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '15, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '15, 08:40</p></div></div><div id="comments-container-40397" class="comments-container"></div><div id="comment-tools-40397" class="comment-tools"></div><div class="clear"></div><div id="comment-40397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40444"></span>

<div id="answer-container-40444" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40444-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By placing the call to the parsing function in proto_reg_handoff_foo() instead of dissect_foo().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '15, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-40444" class="comments-container"></div><div id="comment-tools-40444" class="comment-tools"></div><div class="clear"></div><div id="comment-40444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40435"></span>

<div id="answer-container-40435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40435-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about <code>placing uat_new()</code> and <code>prefs_register_uat_preference()</code> in <code>proto_register()</code> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '15, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40435" class="comments-container"><span id="40439"></span><div id="comment-40439" class="comment"><div id="post-40439-score" class="comment-score"></div><div class="comment-text"><p>Is this a different function from proto_register_foo()? I already have uat_new() and prefs_register_uat_preference() in proto_register_foo()</p></div><div id="comment-40439-info" class="comment-info"><span class="comment-age">(10 Mar '15, 09:52)</span> flora</div></div><span id="40445"></span><div id="comment-40445" class="comment"><div id="post-40445-score" class="comment-score"></div><div class="comment-text"><p>thanks Jaap. I've just resolved the issue.</p></div><div id="comment-40445-info" class="comment-info"><span class="comment-age">(10 Mar '15, 11:07)</span> flora</div></div></div><div id="comment-tools-40435" class="comment-tools"></div><div class="clear"></div><div id="comment-40435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "How to write a postdissector in C?"
description = '''I have been able to find instructions on writing postdissectors for Wireshark in Lua, but have been able to find any such instruction for C. All I&#x27;ve been able to find is that it is indeed possible. Does such a resource exist?'''
date = "2016-05-26T10:50:00Z"
lastmod = "2016-05-26T14:40:00Z"
weight = 52968
keywords = [ "lua", "c", "dissector", "postdissector", "wireshark" ]
aliases = [ "/questions/52968" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to write a postdissector in C?](/questions/52968/how-to-write-a-postdissector-in-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52968-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been able to find instructions on writing postdissectors for Wireshark in Lua, but have been able to find any such instruction for C. All I've been able to find is that it is indeed possible. Does such a resource exist?</p></div><div id="question-tags" class="tags-container tags">lua c dissector postdissector wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/69337c614f643f05439087eb2c42ac6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osarkar&#39;s gravatar image" /><p>osarkar<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osarkar has no accepted answers">0%</span></p></div></div><div id="comments-container-52968" class="comments-container"></div><div id="comment-tools-52968" class="comment-tools"></div><div class="clear"></div><div id="comment-52968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52972"></span>

<div id="answer-container-52972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52972-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're looking for <code>void register_postdissector(dissector_handle_t);</code> in <code>epan/packet.h</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52972" class="comments-container"><span id="52975"></span><div id="comment-52975" class="comment"><div id="post-52975-score" class="comment-score"></div><div class="comment-text"><p>And a dissector that calls that, for example epan/dissectors/packet-prp.c .</p><p>There isn't really much documentation of post-dissectors because they're not really something people use much. They were created to meet a very special case. (In fact, there's a reasonable chance what you're trying to do could be better handled another way.)</p></div><div id="comment-52975-info" class="comment-info"><span class="comment-age">(26 May '16, 15:00)</span> JeffMorriss ♦</div></div><span id="53116"></span><div id="comment-53116" class="comment"><div id="post-53116-score" class="comment-score"></div><div class="comment-text"><p>How do I go about fetching fields as I would in Lua? in Lua its Field.new(&lt;fieldname&gt;), which then requires some conversion from userdata to usable types.</p></div><div id="comment-53116-info" class="comment-info"><span class="comment-age">(01 Jun '16, 12:21)</span> osarkar</div></div><span id="53117"></span><div id="comment-53117" class="comment"><div id="post-53117-score" class="comment-score"></div><div class="comment-text"><p>To get started with C development for Wireshark I'd suggest you take a look at README.developer and/or the Developer's Guide (available on the web site). It won't make sense to start learning via Q&amp;A.</p></div><div id="comment-53117-info" class="comment-info"><span class="comment-age">(01 Jun '16, 13:05)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-52972" class="comment-tools"></div><div class="clear"></div><div id="comment-52972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


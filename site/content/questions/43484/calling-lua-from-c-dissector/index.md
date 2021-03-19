+++
type = "question"
title = "Calling Lua from C Dissector"
description = '''Hello, I was given a lua dissector and I need to call this dissector from another dissector that I wrote in C. Is there anyway that I can accomplish this. My dissector currently calls another C dissector without issue using the find_dissector(string) function. When I do this with the lua script, it ...'''
date = "2015-06-23T14:16:00Z"
lastmod = "2015-06-24T13:28:00Z"
weight = 43484
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/43484" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calling Lua from C Dissector](/questions/43484/calling-lua-from-c-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43484-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I was given a lua dissector and I need to call this dissector from another dissector that I wrote in C. Is there anyway that I can accomplish this. My dissector currently calls another C dissector without issue using the find_dissector(string) function. When I do this with the lua script, it just return null. I know that the all dissectors work on their own.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/9f9573fb088670649a5dd3f70df4adb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheSuperShoe&#39;s gravatar image" /><p>TheSuperShoe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheSuperShoe has no accepted answers">0%</span></p></div></div><div id="comments-container-43484" class="comments-container"></div><div id="comment-tools-43484" class="comment-tools"></div><div class="clear"></div><div id="comment-43484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43520"></span>

<div id="answer-container-43520" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43520-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found a "fix" to my issue.</p><p>I had to check in my dissect function if the handle was null, then call find_dissector() again. The other C dissectors I use are fine being called from my proto_reg_handoff_() function.</p><p>My guess is that the lua dissectors are not registered at the same time as the C dissectors, therefor the C dissector could not find the lua until it was dissecting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/9f9573fb088670649a5dd3f70df4adb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheSuperShoe&#39;s gravatar image" /><p>TheSuperShoe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheSuperShoe has no accepted answers">0%</span></p></div></div><div id="comments-container-43520" class="comments-container"><span id="43522"></span><div id="comment-43522" class="comment"><div id="post-43522-score" class="comment-score"></div><div class="comment-text"><p>Yes, something has to be done "first", and it's the C-code dissectors. Really the Lua scripts don't even get loaded until all the C-code based initialization is done.</p><p>If you can change the Lua script, you could have the Lua-based dissector register itself to be invoked by the C-code based one. In other words, instead of making the C-code find the Lua-based dissector to invoke it, reverse it and have the C-code based one create a dissector table (register_dissector_table()), so the Lua script can register itself in that table (using DissectorTable.get("myCCodeDissector") in Lua).</p></div><div id="comment-43522-info" class="comment-info"><span class="comment-age">(24 Jun '15, 14:50)</span> Hadriel</div></div></div><div id="comment-tools-43520" class="comment-tools"></div><div class="clear"></div><div id="comment-43520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


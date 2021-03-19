+++
type = "question"
title = "search for a specific bit"
description = '''Is there a way to search for a specific bit at a wireshark log in a specific message? For example i want to search for the fifty eight (58) bit in a specific message or packet in a wireshark log and i would like to see what value this bit has.'''
date = "2015-01-12T12:53:00Z"
lastmod = "2015-01-15T01:00:00Z"
weight = 39084
keywords = [ "packetsearch", "search" ]
aliases = [ "/questions/39084" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [search for a specific bit](/questions/39084/search-for-a-specific-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39084-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to search for a specific bit at a wireshark log in a specific message?</p><p>For example i want to search for the fifty eight (58) bit in a specific message or packet in a wireshark log and i would like to see what value this bit has.</p></div><div id="question-tags" class="tags-container tags">packetsearch search</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '15, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/d8a12d1a9f0522530f85690edda833ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thodoris&#39;s gravatar image" /><p>Thodoris<br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thodoris has no accepted answers">0%</span></p></div></div><div id="comments-container-39084" class="comments-container"></div><div id="comment-tools-39084" class="comment-tools"></div><div class="clear"></div><div id="comment-39084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39147"></span>

<div id="answer-container-39147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no built-in functionality in Wireshark to do that.</p><p><strong>However</strong>, you can write a Post-Dissector in Lua to do exatly that.</p><blockquote><p><a href="http://wiki.wireshark.org/Lua">http://wiki.wireshark.org/Lua</a><br />
<a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a><br />
<a href="http://wiki.wireshark.org/Lua/Examples/PostDissector">http://wiki.wireshark.org/Lua/Examples/PostDissector</a></p></blockquote><p>Examples:</p><blockquote><p><a href="https://ask.wireshark.org/questions/26247/dissect-data-using-lua-post-dissector">https://ask.wireshark.org/questions/26247/dissect-data-using-lua-post-dissector</a><br />
<a href="https://ask.wireshark.org/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format">https://ask.wireshark.org/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-39147" class="comments-container"><span id="40070"></span><div id="comment-40070" class="comment"><div id="post-40070-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Kurt, I will try this.</p><p>Best Regards, Thodoris</p></div><div id="comment-40070-info" class="comment-info"><span class="comment-age">(25 Feb '15, 06:37)</span> Thodoris</div></div></div><div id="comment-tools-39147" class="comment-tools"></div><div class="clear"></div><div id="comment-39147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


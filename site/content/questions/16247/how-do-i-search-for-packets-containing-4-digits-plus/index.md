+++
type = "question"
title = "How do I search for packets containing  4 digits plus ;"
description = '''How in Wireshark do I find TCP packets containing in their data a string consisting of 4 digits plus a semicolon? I have tried matches with strings &#92;d&#92;d&#92;d&#92;d; and [0-9]{4}; and various others but it rejects them all as not a valid byte string. Thanks - Rowan'''
date = "2012-11-23T09:53:00Z"
lastmod = "2012-11-23T10:26:00Z"
weight = 16247
keywords = [ "matches", "regex" ]
aliases = [ "/questions/16247" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I search for packets containing 4 digits plus ;](/questions/16247/how-do-i-search-for-packets-containing-4-digits-plus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How in Wireshark do I find TCP packets containing in their data a string consisting of 4 digits plus a semicolon? I have tried matches with strings \d\d\d\d; and [0-9]{4}; and various others but it rejects them all as not a valid byte string.</p><p>Thanks - Rowan</p></div><div id="question-tags" class="tags-container tags">matches regex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '12, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/fd3bc17dd17d9e0301f9329394be1539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rowan&#39;s gravatar image" /><p>Rowan<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rowan has no accepted answers">0%</span></p></div></div><div id="comments-container-16247" class="comments-container"></div><div id="comment-tools-16247" class="comment-tools"></div><div class="clear"></div><div id="comment-16247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16249"></span>

<div id="answer-container-16249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16249-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>this works for me with Wireshark 1.8.3 (Win XP)</p><p>Match a 4 digit ASCII string<br />
</p><blockquote><p><code>tcp matches "[0-9]{4};"</code><br />
</p></blockquote><p>Match a time string, like 09:05:15<br />
</p><blockquote><p><code>tcp matches "[0-9]{2}:[0-9]{2}:[0-9]{2}"</code><br />
</p></blockquote><p>However, this will only match ASCII in the TCP payload. Do you want to match ASCII values or binary digits?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '12, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '12, 10:26</p></div></div><div id="comments-container-16249" class="comments-container"><span id="16250"></span><div id="comment-16250" class="comment"><div id="post-16250-score" class="comment-score"></div><div class="comment-text"><p>You probably meant <code>tcp.data</code>.</p></div><div id="comment-16250-info" class="comment-info"><span class="comment-age">(23 Nov '12, 10:41)</span> helloworld</div></div><span id="16252"></span><div id="comment-16252" class="comment"><div id="post-16252-score" class="comment-score"></div><div class="comment-text"><p>the match on <strong>tcp.data</strong> does not work. I have not yet checked why.</p></div><div id="comment-16252-info" class="comment-info"><span class="comment-age">(23 Nov '12, 10:47)</span> Kurt Knochner ♦</div></div><span id="16255"></span><div id="comment-16255" class="comment"><div id="post-16255-score" class="comment-score"></div><div class="comment-text"><p>Hmm. It seems to work for me (as in, it properly filters packets in the list that match the pattern). I'm running Wireshark 1.8.1 in OSX.</p></div><div id="comment-16255-info" class="comment-info"><span class="comment-age">(23 Nov '12, 10:57)</span> helloworld</div></div><span id="16256"></span><div id="comment-16256" class="comment"><div id="post-16256-score" class="comment-score"></div><div class="comment-text"><p>I tested with WinXP. Test with Ubuntu follows.</p></div><div id="comment-16256-info" class="comment-info"><span class="comment-age">(23 Nov '12, 10:59)</span> Kurt Knochner ♦</div></div><span id="16257"></span><div id="comment-16257" class="comment"><div id="post-16257-score" class="comment-score"></div><div class="comment-text"><p>It also works for me in Wireshark 1.9.0 in Windows 7.</p></div><div id="comment-16257-info" class="comment-info"><span class="comment-age">(23 Nov '12, 11:18)</span> helloworld</div></div><span id="16267"></span><div id="comment-16267" class="comment not_top_scorer"><div id="post-16267-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I'm sure I tried this before, but now I find that this works fine. It is the ASCII data that I'm trying to filter.</p><p>Rowan</p></div><div id="comment-16267-info" class="comment-info"><span class="comment-age">(24 Nov '12, 15:29)</span> Rowan</div></div><span id="16269"></span><div id="comment-16269" class="comment not_top_scorer"><div id="post-16269-score" class="comment-score"></div><div class="comment-text"><p>@Rowan</p><p>I converted your "answer" to a comment as that is how this site works, please read the FAQ for more info.</p><p>If an answer solves your issue please accept it by clicking the checkmark icon next to the answer as this helps other users of the site with a similar question. This is also in the FAQ.</p></div><div id="comment-16269-info" class="comment-info"><span class="comment-age">(25 Nov '12, 02:29)</span> grahamb ♦</div></div></div><div id="comment-tools-16249" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-16249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


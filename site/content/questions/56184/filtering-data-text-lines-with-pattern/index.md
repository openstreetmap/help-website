+++
type = "question"
title = "filtering data-text-lines with pattern"
description = '''Hi, Is there a way to use pattern filtering in tshark/Wireshark?  I would like to search for the HTTP requests by filtering all the data-text-lines that contain sequence of digits, for example 14521-12425-22 - is there something that i could use with filter: data-text-lines contains &quot;XXXXX-XXXXX-XX&quot;...'''
date = "2016-10-06T05:15:00Z"
lastmod = "2016-10-06T06:32:00Z"
weight = 56184
keywords = [ "data-text-lines", "http", "pattern" ]
aliases = [ "/questions/56184" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filtering data-text-lines with pattern](/questions/56184/filtering-data-text-lines-with-pattern)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56184-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there a way to use pattern filtering in tshark/Wireshark?</p><p>I would like to search for the HTTP requests by filtering all the data-text-lines that contain sequence of digits, for example 14521-12425-22 - is there something that i could use with filter: data-text-lines contains "XXXXX-XXXXX-XX" where X would be any digit from 0-9?</p></div><div id="question-tags" class="tags-container tags">data-text-lines http pattern</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '16, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/e750e2e9de08299bb56a1a347d922669?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JSJ&#39;s gravatar image" /><p>JSJ<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JSJ has no accepted answers">0%</span></p></div></div><div id="comments-container-56184" class="comments-container"></div><div id="comment-tools-56184" class="comment-tools"></div><div class="clear"></div><div id="comment-56184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56189"></span>

<div id="answer-container-56189" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the display filter "matches" operator and a regular expression.</p><p>For your pattern you would need an expression such as <code>... matches "[0-9]{5}-[0-9]{5}-[0-9]{2}"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56189" class="comments-container"><span id="56209"></span><div id="comment-56209" class="comment"><div id="post-56209-score" class="comment-score"></div><div class="comment-text"><p>Thank you, works perfect!</p><p>A follow up; can you define more digits/characters in the brackets, for example like [0-9,A-Z,a-z] ?</p></div><div id="comment-56209-info" class="comment-info"><span class="comment-age">(06 Oct '16, 22:32)</span> JSJ</div></div><span id="56215"></span><div id="comment-56215" class="comment"><div id="post-56215-score" class="comment-score"></div><div class="comment-text"><p>the square brackets define a regex character class which can have any distinct characters in them, and using ranges as you've suggested.</p><p>However there are other definitions that are somewhat more succinct that mean the same thing, e.g. the posix character classes such as <code>[[:alnum:]]</code> or the generic character types such as <code>\w</code>, although this includes the "_".</p><p>The full syntax available for Wireshark regular expressions is shown <a href="https://developer.gnome.org/glib/stable/glib-regex-syntax.html">here</a>.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-56215-info" class="comment-info"><span class="comment-age">(07 Oct '16, 02:32)</span> grahamb ♦</div></div></div><div id="comment-tools-56189" class="comment-tools"></div><div class="clear"></div><div id="comment-56189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


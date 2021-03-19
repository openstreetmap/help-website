+++
type = "question"
title = "Filtering with a regular expression"
description = '''I am trying to do a regex in wireshark on the following http header and want to filter the ones with an empty value. User-Agent:  in the trace it shows User-Agent: &#92;r&#92;n I tried a regex like the following to match User-Agent: followed by a space, then end of line. frame matches &quot;User-Agent:[&#92;s]$&quot; but...'''
date = "2013-06-26T15:28:00Z"
lastmod = "2013-06-27T09:20:00Z"
weight = 22376
keywords = [ "regex" ]
aliases = [ "/questions/22376" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filtering with a regular expression](/questions/22376/filtering-with-a-regular-expression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22376-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to do a regex in wireshark on the following http header and want to filter the ones with an empty value.</p><p>User-Agent:</p><p>in the trace it shows User-Agent: \r\n</p><p>I tried a regex like the following to match User-Agent: followed by a space, then end of line.</p><p>frame matches "User-Agent:[\s]$"</p><p>but it doesnt work.</p><p>Can someone advise whats wrong? thanks</p></div><div id="question-tags" class="tags-container tags">regex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/3e7d3a929b8db7c975caea8dfe94feac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brumik&#39;s gravatar image" /><p>brumik<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brumik has no accepted answers">0%</span></p></div></div><div id="comments-container-22376" class="comments-container"></div><div id="comment-tools-22376" class="comment-tools"></div><div class="clear"></div><div id="comment-22376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22417"></span>

<div id="answer-container-22417" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22417-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe the "$" will anchor the regex to the end of the whole frame, not one particular line in the frame. Could you try:</p><pre><code>frame matches &quot;\\r\\nUser-Agent: \\r\\n&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jun '13, 15:11</p></div></div><div id="comments-container-22417" class="comments-container"><span id="22426"></span><div id="comment-22426" class="comment"><div id="post-22426-score" class="comment-score"></div><div class="comment-text"><p>I assume you meant "matches" ? but yes it did work without the $ Also without the \r\n at the start. Thanks everyone for the help.</p></div><div id="comment-22426-info" class="comment-info"><span class="comment-age">(27 Jun '13, 13:49)</span> brumik</div></div><span id="22430"></span><div id="comment-22430" class="comment"><div id="post-22430-score" class="comment-score"></div><div class="comment-text"><p>Yes I did, it's corrected :-)</p><p>Glad the filter works for you!</p></div><div id="comment-22430-info" class="comment-info"><span class="comment-age">(27 Jun '13, 15:12)</span> SYN-bit ♦♦</div></div><span id="22434"></span><div id="comment-22434" class="comment"><div id="post-22434-score" class="comment-score"></div><div class="comment-text"><p>If a response answers your question, please mark it as the accepted answer for the benefit of others. Refer to the FAQ for more information.</p></div><div id="comment-22434-info" class="comment-info"><span class="comment-age">(27 Jun '13, 20:02)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-22417" class="comment-tools"></div><div class="clear"></div><div id="comment-22417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22378"></span>

<div id="answer-container-22378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22378-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p><code>frame matches "User-Agent: \\r\\n$"</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-22378" class="comments-container"><span id="22393"></span><div id="comment-22393" class="comment"><div id="post-22393-score" class="comment-score"></div><div class="comment-text"><p>thanks,</p><p>frame matches "User-Agent: \r\n$"</p><p>it still didnt match though.</p><p>However</p><p>http.user_agent == "" matches it but I wanted to use a regex.</p></div><div id="comment-22393-info" class="comment-info"><span class="comment-age">(27 Jun '13, 00:25)</span> brumik</div></div><span id="22395"></span><div id="comment-22395" class="comment"><div id="post-22395-score" class="comment-score"></div><div class="comment-text"><p>Correction I meant:</p><p>frame matches "User-Agent: \r\n$"</p><p>still didnt do the trick</p></div><div id="comment-22395-info" class="comment-info"><span class="comment-age">(27 Jun '13, 00:27)</span> brumik</div></div><span id="22398"></span><div id="comment-22398" class="comment"><div id="post-22398-score" class="comment-score"></div><div class="comment-text"><p>@brumik,</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-22398-info" class="comment-info"><span class="comment-age">(27 Jun '13, 02:27)</span> grahamb ♦</div></div><span id="22402"></span><div id="comment-22402" class="comment"><div id="post-22402-score" class="comment-score"></div><div class="comment-text"><p>did you try '<strong>double backslash</strong>'? Only that works in my test capture file.</p><blockquote><p><code>frame matches "User-Agent: \\r\\n$"</code><br />
</p></blockquote><p>instead of</p><blockquote><p><code>frame matches "User-Agent: \r\n$"</code></p></blockquote></div><div id="comment-22402-info" class="comment-info"><span class="comment-age">(27 Jun '13, 05:50)</span> Kurt Knochner ♦</div></div><span id="22416"></span><div id="comment-22416" class="comment"><div id="post-22416-score" class="comment-score"></div><div class="comment-text"><p>Yes I did, strangely enough it didn't match with double backslash either.</p></div><div id="comment-22416-info" class="comment-info"><span class="comment-age">(27 Jun '13, 08:53)</span> brumik</div></div><span id="22419"></span><div id="comment-22419" class="comment not_top_scorer"><div id="post-22419-score" class="comment-score"></div><div class="comment-text"><p>it does for me. What is your Wireshark version?</p></div><div id="comment-22419-info" class="comment-info"><span class="comment-age">(27 Jun '13, 13:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22378" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


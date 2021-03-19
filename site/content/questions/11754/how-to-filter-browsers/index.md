+++
type = "question"
title = "How to filter browsers?"
description = '''How can i filter browsers for GET / HTTP/1.1? I want to get list of browsers that have been used in capture file. Thanks.'''
date = "2012-06-08T03:51:00Z"
lastmod = "2012-06-08T03:58:00Z"
weight = 11754
keywords = [ "filter", "list", "browser" ]
aliases = [ "/questions/11754" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter browsers?](/questions/11754/how-to-filter-browsers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can i filter browsers for GET / HTTP/1.1? I want to get list of browsers that have been used in capture file. Thanks.</p></div><div id="question-tags" class="tags-container tags">filter list browser</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/3ee31036011b0ca130f74445bd1d2572?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="besomuk&#39;s gravatar image" /><p>besomuk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="besomuk has no accepted answers">0%</span></p></div></div><div id="comments-container-11754" class="comments-container"></div><div id="comment-tools-11754" class="comment-tools"></div><div class="clear"></div><div id="comment-11754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11756"></span>

<div id="answer-container-11756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p><code>tshark -r input.cap -R http.request -T fields -e http.user_agent</code><br />
</p></blockquote><p>and with a filter on HTTP/1.1</p><blockquote><p><code>tshark.exe -r http_sample.cap -R 'http.request.version eq HTTP/1.1' -T fields -e http.user_agent</code></p></blockquote><p><strong>HINT</strong>: String quoting may be difficult in a Windows DOS box due to the slash ('/')! The DOS shell tries to interpret this as the start of a parameter.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '12, 04:34</p></div></div><div id="comments-container-11756" class="comments-container"><span id="11757"></span><div id="comment-11757" class="comment"><div id="post-11757-score" class="comment-score"></div><div class="comment-text"><p>Hmm...i get only empty list. Here is something else. When i select "GET / HTTP/1.1" within HTTP protocol, and apply filter, i get the list i want. Or at least i think it is complete list.</p></div><div id="comment-11757-info" class="comment-info"><span class="comment-age">(08 Jun '12, 04:10)</span> besomuk</div></div><span id="11760"></span><div id="comment-11760" class="comment"><div id="post-11760-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, there was a typo in my answer. user-agent (wrong) instead of user_agent (correct)! Please try again.</p></div><div id="comment-11760-info" class="comment-info"><span class="comment-age">(08 Jun '12, 04:23)</span> Kurt Knochner ♦</div></div><span id="11762"></span><div id="comment-11762" class="comment"><div id="post-11762-score" class="comment-score"></div><div class="comment-text"><p>Oh yes, that's it. Thanks.</p></div><div id="comment-11762-info" class="comment-info"><span class="comment-age">(08 Jun '12, 04:56)</span> besomuk</div></div><span id="11763"></span><div id="comment-11763" class="comment"><div id="post-11763-score" class="comment-score"></div><div class="comment-text"><p>Fine.</p><p>BTW: I converted your answer to a comment, as that's how this Q&amp;A site works.</p></div><div id="comment-11763-info" class="comment-info"><span class="comment-age">(08 Jun '12, 05:11)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11756" class="comment-tools"></div><div class="clear"></div><div id="comment-11756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Search for string in compressed/gzipped HTTP content"
description = '''Let&#x27;s say I want to find the point at which a site sends a particular string to my machine. However, even if the connection is not encrypted, it&#x27;s still likely to be gzipped, so I can&#x27;t just use http contains MYSTRING.'''
date = "2014-05-02T01:47:00Z"
lastmod = "2014-05-02T03:30:00Z"
weight = 32384
keywords = [ "gzipped", "http", "compressed" ]
aliases = [ "/questions/32384" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Search for string in compressed/gzipped HTTP content](/questions/32384/search-for-string-in-compressedgzipped-http-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let's say I want to find the point at which a site sends a particular string to my machine. However, even if the connection is not encrypted, it's still likely to be gzipped, so I can't just use <code>http contains MYSTRING</code>.</p></div><div id="question-tags" class="tags-container tags">gzipped http compressed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/cf04366fafdd38ba6dbb9a24ba61acf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sashoalm&#39;s gravatar image" /><p>sashoalm<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sashoalm has no accepted answers">0%</span></p></div></div><div id="comments-container-32384" class="comments-container"></div><div id="comment-tools-32384" class="comment-tools"></div><div class="clear"></div><div id="comment-32384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32388"></span>

<div id="answer-container-32388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32388-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can do it this way:</p><p>You need to enable the following option (enabled by default):</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; Uncompress Entity Bodies</p></blockquote><p>and then use the following display filter:</p><blockquote><p>http.response and <strong>data-text-lines contains "xxxxx"</strong></p></blockquote><p>where "xxxxx" is your search string.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 May '14, 03:31</p></div></div><div id="comments-container-32388" class="comments-container"></div><div id="comment-tools-32388" class="comment-tools"></div><div class="clear"></div><div id="comment-32388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


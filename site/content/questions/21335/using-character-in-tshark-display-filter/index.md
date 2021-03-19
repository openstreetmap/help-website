+++
type = "question"
title = "Using &quot;;&quot; character in tshark display filter"
description = '''I&#x27;m trying to write a display filter in tshark where the value I&#x27;m searaching for includes the &quot;;&quot; character. The problem is this character seems to have some special significance with tshark and it complains that it was unexpected. This is true even when the display filter is cleanly encapsulated i...'''
date = "2013-05-20T16:03:00Z"
lastmod = "2013-05-21T19:38:00Z"
weight = 21335
keywords = [ "tshark" ]
aliases = [ "/questions/21335" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using ";" character in tshark display filter](/questions/21335/using-character-in-tshark-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21335-score" class="post-score" title="current number of votes">0</div><span id="post-21335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a display filter in tshark where the value I'm searaching for includes the ";" character. The problem is this character seems to have some special significance with tshark and it complains that it was unexpected. This is true even when the display filter is cleanly encapsulated in quotation marks. For example:</p><p><code>tshark -r file.pcap -R "diameter.Session-Id==a;b;c;d"</code></p><p>Also tried:</p><p><code>tshark -r file.pcap -R "diameter.Session-Id=="a;b;c;d""</code></p><p>So... is there some kind of character expected to be used to tell tshark that the ; character should be treated as part of the string in the display filter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21335" class="comments-container"></div><div id="comment-tools-21335" class="comment-tools"></div><div class="clear"></div><div id="comment-21335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21337"></span>

<div id="answer-container-21337" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21337-score" class="post-score" title="current number of votes">1</div><span id="post-21337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Quadratic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please use the following syntax:</p><p>Linux:</p><blockquote><p>tshark -r file.pcap -R 'diameter.Session-Id=="a;b;c;d"'</p></blockquote><p>Windows (uses different quoting rules on the CLI):</p><blockquote><p>tshark -r file.pcap -R "diameter.Session-Id==""a;b;c;d"""</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '13, 16:40</strong> </span></p></div></div><div id="comments-container-21337" class="comments-container"><span id="21343"></span><div id="comment-21343" class="comment"><div id="post-21343-score" class="comment-score"></div><div class="comment-text"><p>And for completeness, when using PowerShell, use single quote marks to group the argument and then escaped double quotes to quote the parameter value:</p><pre><code>tshark -r file.pcap -R &#39;diameter.Session-Id==\&quot;a;b;c;d\&quot;&#39;</code></pre></div><div id="comment-21343-info" class="comment-info"><span class="comment-age">(21 May '13, 01:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="21362"></span><div id="comment-21362" class="comment"><div id="post-21362-score" class="comment-score"></div><div class="comment-text"><p>Ah, thanks. That works.</p></div><div id="comment-21362-info" class="comment-info"><span class="comment-age">(21 May '13, 19:38)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-21337" class="comment-tools"></div><div class="clear"></div><div id="comment-21337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Search for HTTP requests that don&#x27;t have User-Agent header"
description = '''How to find all the HTTP requests that don&#x27;t have &quot;User-Agent&quot; field.  I tried the following two filters but neither worked: http.user_agent == &quot;&quot;  ! http.user_agent  Any ideas? '''
date = "2015-08-26T16:16:00Z"
lastmod = "2015-08-26T17:02:00Z"
weight = 45375
keywords = [ "wireshark" ]
aliases = [ "/questions/45375" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Search for HTTP requests that don't have User-Agent header](/questions/45375/search-for-http-requests-that-dont-have-user-agent-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45375-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to find all the HTTP requests that don't have "User-Agent" field. I tried the following two filters but neither worked:</p><pre><code>http.user_agent == &quot;&quot;

! http.user_agent</code></pre><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45375" class="comments-container"></div><div id="comment-tools-45375" class="comment-tools"></div><div class="clear"></div><div id="comment-45375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45376"></span>

<div id="answer-container-45376" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45376-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>http.request.method &amp;&amp; !http.user_agent</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '15, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45376" class="comments-container"><span id="45379"></span><div id="comment-45379" class="comment"><div id="post-45379-score" class="comment-score"></div><div class="comment-text"><p>Thanks @jim-aragon. It works. <code>http.request &amp;&amp; !http.user_agent</code> works too.</p></div><div id="comment-45379-info" class="comment-info"><span class="comment-age">(26 Aug '15, 18:48)</span> pktUser1001</div></div></div><div id="comment-tools-45376" class="comment-tools"></div><div class="clear"></div><div id="comment-45376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "extract all HTTP requests whose User-Agent length is less than a limit"
description = '''Wonder if it is possible to extract all HTTP requests whose User-Agent length is less than 10.'''
date = "2015-12-07T06:41:00Z"
lastmod = "2015-12-07T06:58:00Z"
weight = 48324
keywords = [ "wireshark" ]
aliases = [ "/questions/48324" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [extract all HTTP requests whose User-Agent length is less than a limit](/questions/48324/extract-all-http-requests-whose-user-agent-length-is-less-than-a-limit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48324-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wonder if it is possible to extract all HTTP requests whose User-Agent length is less than 10.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '15, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-48324" class="comments-container"></div><div id="comment-tools-48324" class="comment-tools"></div><div class="clear"></div><div id="comment-48324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48325"></span>

<div id="answer-container-48325" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48325-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The clean way to do that is by matching the parameter value to a regular expression:</p><pre><code>http.user_agent matches &quot;^.{1,9}$&quot;</code></pre><p>Translation: between the start of the string, <code>^</code>, and the end of the string, <code>$</code>, there is a minimum of one and a maximum of 9 "any characters", represented by <code>.</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '15, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '15, 21:38</p></div></div><div id="comments-container-48325" class="comments-container"><span id="48326"></span><div id="comment-48326" class="comment"><div id="post-48326-score" class="comment-score"></div><div class="comment-text"><p>Thanks @sindy for the quick reply. Did you mean to say <code>http.user_agent and !http.user_agent[10]&gt;0</code>?</p></div><div id="comment-48326-info" class="comment-info"><span class="comment-age">(07 Dec '15, 07:09)</span> pktUser1001</div></div><span id="48327"></span><div id="comment-48327" class="comment"><div id="post-48327-score" class="comment-score"></div><div class="comment-text"><p>Yes, I've just missed you've given the particular value of 10 in the question, so I!ve just fixed my answer yet another time.</p></div><div id="comment-48327-info" class="comment-info"><span class="comment-age">(07 Dec '15, 07:10)</span> sindy</div></div><span id="48338"></span><div id="comment-48338" class="comment"><div id="post-48338-score" class="comment-score"></div><div class="comment-text"><p>It looks like this is a good workaround, but I feel <code>user_agent[10]</code> may index into unspecified memory, so this behavior may not be well defined. What do you think?</p></div><div id="comment-48338-info" class="comment-info"><span class="comment-age">(07 Dec '15, 12:41)</span> pktUser1001</div></div><span id="48339"></span><div id="comment-48339" class="comment"><div id="post-48339-score" class="comment-score"></div><div class="comment-text"><p>That's why I wrote it was dirty. There is a safe method but I had problems to realize what should be selected and what not. I'll edit the answer accordingly in a second.</p></div><div id="comment-48339-info" class="comment-info"><span class="comment-age">(07 Dec '15, 13:36)</span> sindy</div></div><span id="48340"></span><div id="comment-48340" class="comment"><div id="post-48340-score" class="comment-score"></div><div class="comment-text"><p>Thanks, a "dirty" solution is better than no solution -)</p></div><div id="comment-48340-info" class="comment-info"><span class="comment-age">(07 Dec '15, 20:14)</span> pktUser1001</div></div></div><div id="comment-tools-48325" class="comment-tools"></div><div class="clear"></div><div id="comment-48325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


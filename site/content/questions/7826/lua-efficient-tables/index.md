+++
type = "question"
title = "Lua - Efficient tables"
description = '''I&#x27;ve written a small script, that logs some data about each connection.  Each connection is uniquely identified by IP1,port1,IP2,port2 - where direction doesn&#x27;t matter.   For small dumps - the script works fine.  However,  as the dumps get bigger, and the number of unique connections follows - the t...'''
date = "2011-12-07T09:18:00Z"
lastmod = "2011-12-07T13:51:00Z"
weight = 7826
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/7826" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua - Efficient tables](/questions/7826/lua-efficient-tables)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7826-score" class="post-score" title="current number of votes">0</div><span id="post-7826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a small script, that logs some data about each connection.<br />
Each connection is uniquely identified by IP1,port1,IP2,port2 - where direction doesn't matter.<br />
</p><p>For small dumps - the script works fine.<br />
However,<br />
as the dumps get bigger, and the number of unique connections follows - the table becomes very large - making the key look-up very long.<br />
</p><p>Can anyone suggest an efficient way/structure to handle/map unique connections.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '11, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/920a90d8a3dca941060cc1e39cc76346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trevor&#39;s gravatar image" /><p><span>Trevor</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trevor has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-7826" class="comments-container"><span id="7842"></span><div id="comment-7842" class="comment"><div id="post-7842-score" class="comment-score"></div><div class="comment-text"><p>I think the question is off-topic since it's a pure Lua question. General Lua programming questions should be asked in <a href="http://www.stackoverflow.com">StackOverflow</a>. The author of Lua (Roberto Ierusalimschy) wrote a <a href="http://www.lua.org/gems/sample.pdf">gem</a> on Lua performance tips, where he discusses how tables are implemented. It might shed a little light on the situation.</p></div><div id="comment-7842-info" class="comment-info"><span class="comment-age">(07 Dec '11, 13:51)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-7826" class="comment-tools"></div><div class="clear"></div><div id="comment-7826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7841"></span>

<div id="answer-container-7841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7841-score" class="post-score" title="current number of votes">0</div><span id="post-7841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming that tables in lua are done with hashes, so it should be pretty efficient anyway. Maybe that's not the case. What I'm saying is, maybe it's your code, not tables. It's hard to tell witout seeing your code.</p><p>Each TCP connection has a unique number: tcp.stream. It's how the wireshark "Follow TCP stream" code is implemented. Try using that instead.</p><p>Aside: Before the existance of tcp.stream "Follow" used to use the same "unique" pattern. I don't think it was terribly efficient, but it's also not unique, even if it seems so in practice. A truly unique pattern involves the addition of a timestamp: IP1,port1,IP2,port2,time. tcp.stream implicitly incorporates a timestamp, making it truly unique.</p><p>You can always resort to segmenting the table. Example: you discover that most of your traffic is coming from 3 IPs in your local network. IP1 = 192.168.1.[123]. You could set up 4 tables, one for each IP, and one for all the other IPs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/88d413834375dbc71f5d3146aca1cd3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studog&#39;s gravatar image" /><p><span>studog</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studog has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-7841" class="comments-container"></div><div id="comment-tools-7841" class="comment-tools"></div><div class="clear"></div><div id="comment-7841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


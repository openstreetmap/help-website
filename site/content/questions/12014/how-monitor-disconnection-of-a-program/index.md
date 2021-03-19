+++
type = "question"
title = "How monitor disconnection of a program."
description = '''Hi everyone, We have a program like telnet, the wireshark installation is on the host machine. ¿How I can monitor the client and how I can filter this connections (client to host) to know then a network or program disconnect from the host server? I ready tryed with tcp.flags.reset==1 or tcp.flags.fi...'''
date = "2012-06-18T04:08:00Z"
lastmod = "2012-06-18T05:01:00Z"
weight = 12014
keywords = [ "program", "monitor" ]
aliases = [ "/questions/12014" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How monitor disconnection of a program.](/questions/12014/how-monitor-disconnection-of-a-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12014-score" class="post-score" title="current number of votes">0</div><span id="post-12014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>We have a program like telnet, the wireshark installation is on the host machine. ¿How I can monitor the client and how I can filter this connections (client to host) to know then a network or program disconnect from the host server?</p><p>I ready tryed with tcp.flags.reset==1 or tcp.flags.fin==1 but this is not usefull to me, i'm looking a way to get more deep info like what port the client app opens to the host server, etc.</p><p>Another thing related is how i can simply detect a network disconnect.</p><p>Hope you can understand what i'm trying to say.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-program" rel="tag" title="see questions tagged &#39;program&#39;">program</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/59dea9ddd0b9d1bbc17d163c0edaf615?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cavemanweb&#39;s gravatar image" /><p><span>cavemanweb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cavemanweb has no accepted answers">0%</span></p></div></div><div id="comments-container-12014" class="comments-container"></div><div id="comment-tools-12014" class="comment-tools"></div><div class="clear"></div><div id="comment-12014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12017"></span>

<div id="answer-container-12017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12017-score" class="post-score" title="current number of votes">0</div><span id="post-12017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I ready tryed with tcp.flags.reset==1 or tcp.flags.fin==1 but this is not usefull to me,</p></blockquote><p>why is that not usefull for you?</p><p>Did you try to combine those filters with the port number?</p><blockquote><p><code>tcp.port == 1234 and (tcp.flags.reset==1 or tcp.flags.fin==1)</code><br />
</p></blockquote><p>where 1234 is the port of your application on the server.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '12, 05:03</strong> </span></p></div></div><div id="comments-container-12017" class="comments-container"></div><div id="comment-tools-12017" class="comment-tools"></div><div class="clear"></div><div id="comment-12017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Filter(show)a  URL Webserver using a wireshark"
description = '''How can I see which particular web server has been used on particular URL(Web Site)? Which filter and command do I have to use?'''
date = "2012-10-10T06:18:00Z"
lastmod = "2012-10-23T04:54:00Z"
weight = 14885
keywords = [ "web", "server" ]
aliases = [ "/questions/14885" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter(show)a URL Webserver using a wireshark](/questions/14885/filtershowa-url-webserver-using-a-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14885-score" class="post-score" title="current number of votes">0</div><span id="post-14885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I see which particular web server has been used on particular URL(Web Site)? Which filter and command do I have to use?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-web" rel="tag" title="see questions tagged &#39;web&#39;">web</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/138aa869c0284e18802057d83c031754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marsal&#39;s gravatar image" /><p><span>marsal</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marsal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '12, 06:23</strong> </span></p></div></div><div id="comments-container-14885" class="comments-container"></div><div id="comment-tools-14885" class="comment-tools"></div><div class="clear"></div><div id="comment-14885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14891"></span>

<div id="answer-container-14891" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14891-score" class="post-score" title="current number of votes">1</div><span id="post-14891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>which particular web server has been used on particular URL(Web Site)?</p></blockquote><p>Maybe I'm getting your question wrong, but the HTTP Host header (the accessed server) is usually the same as the host part in the URL (what you type in the browser - <a href="http://host/xxxx).">http://host/xxxx).</a> So, the accessed web server is the same as the host in the URL !??!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14891" class="comments-container"><span id="14978"></span><div id="comment-14978" class="comment"><div id="post-14978-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answering my question(s)!! Well I would like to elaborate my question. I have to find which webserver has been used for example for <a href="http://www.conrad.ch">http://www.conrad.ch</a>, <a href="http://www.sbb.ch">www.sbb.ch</a>, <a href="http://www.microsoft.ch">www.microsoft.ch</a>. Thank you Kurt in advance!</p><p>Regards</p><p>marsal</p></div><div id="comment-14978-info" class="comment-info"><span class="comment-age">(13 Oct '12, 00:11)</span> <span class="comment-user userinfo">marsal</span></div></div><span id="14982"></span><div id="comment-14982" class="comment"><div id="post-14982-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but I still don't get it :-)</p><p>What do you mean be "which webserver has been used for example for <a href="http://www.conrad.ch">http://www.conrad.ch</a>"?</p><ul><li>What exactly do you need? The IP address of that server?</li><li>The server name?</li><li>The IP address of the clients accessing that server?</li><li>Anything else?</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-14982-info" class="comment-info"><span class="comment-age">(13 Oct '12, 01:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14985"></span><div id="comment-14985" class="comment"><div id="post-14985-score" class="comment-score"></div><div class="comment-text"><p>the name please! and the command on the wireshark how do I filter that! I am sorry but my technical English is not so good.</p></div><div id="comment-14985-info" class="comment-info"><span class="comment-age">(13 Oct '12, 02:28)</span> <span class="comment-user userinfo">marsal</span></div></div><span id="14991"></span><div id="comment-14991" class="comment"><div id="post-14991-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I am sorry but my technical English is not so good.</p></blockquote><p>Your english is not worse than mine ;-)</p><p>O.K. isn't the name of the server in the URL <a href="http://www.sbb.ch">http://www.sbb.ch</a> equal to <a href="http://www.sbb.ch">www.sbb.ch</a>?</p><p>So, the best I can tell you is this. Use a Display Filter like this:</p><blockquote><p><code>http.request and http.host eq "www.sbb.ch"</code><br />
</p></blockquote><p>and you will get</p><ul><li>the IP address(es) of all clients talking to that host</li><li>the IP address(es) of <a href="http://www.sbb.ch">www.sbb.ch</a></li><li>the 'name' of the server in the HTTP Host header (open the HTTP details to see the 'Host:' header)</li><li>the requested URL (in the Info column or in the HTTP details)</li></ul><p>Please tell me, if you need any other information.</p></div><div id="comment-14991-info" class="comment-info"><span class="comment-age">(13 Oct '12, 12:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15184"></span><div id="comment-15184" class="comment"><div id="post-15184-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt!</p></div><div id="comment-15184-info" class="comment-info"><span class="comment-age">(23 Oct '12, 04:54)</span> <span class="comment-user userinfo">marsal</span></div></div></div><div id="comment-tools-14891" class="comment-tools"></div><div class="clear"></div><div id="comment-14891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


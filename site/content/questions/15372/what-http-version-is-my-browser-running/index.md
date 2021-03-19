+++
type = "question"
title = "what http version is my browser running?"
description = '''I&#x27;m a beginner to learning wireshark, so please go easy on me. How can I find out if my browser is running HTTP version 1.0 or 1.1? Also, how can I find out what version of HTTP the server running?  Is there a specific part of wireshark which displays this information every time? Thanks'''
date = "2012-10-30T09:08:00Z"
lastmod = "2012-10-30T10:13:00Z"
weight = 15372
keywords = [ "version", "http", "server" ]
aliases = [ "/questions/15372" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what http version is my browser running?](/questions/15372/what-http-version-is-my-browser-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15372-score" class="post-score" title="current number of votes">0</div><span id="post-15372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a beginner to learning wireshark, so please go easy on me. How can I find out if my browser is running HTTP version 1.0 or 1.1? Also, how can I find out what version of HTTP the server running?</p><p>Is there a specific part of wireshark which displays this information every time?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '12, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/25bfab3fbdcc85732922e9d5de11cae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smc20&#39;s gravatar image" /><p><span>smc20</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smc20 has no accepted answers">0%</span></p></div></div><div id="comments-container-15372" class="comments-container"></div><div id="comment-tools-15372" class="comment-tools"></div><div class="clear"></div><div id="comment-15372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15373"></span>

<div id="answer-container-15373" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15373-score" class="post-score" title="current number of votes">3</div><span id="post-15373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smc20 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. Capture while you browse the internet, and find any GET request your browser does (which means "hello, I want something"). If you have many packets that make it hard to see such requests you can find them by filtering on "http.request.method==GET".</p><p>In the packet list you'll see that the info column says "GET / HTTP/1.1" or "GET / HTTP/1.0".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '12, 09:15</strong> </span></p></div></div><div id="comments-container-15373" class="comments-container"><span id="15375"></span><div id="comment-15375" class="comment"><div id="post-15375-score" class="comment-score"></div><div class="comment-text"><p>thankyou Jasper that makes sense.</p><p>One more question if that's ok. I have a website and according to my cPanel it says:</p><p>Apache version 2.2.23 and Operating System linux</p><p>I captured packets and browsed to my website. The Hypertext Transfer Protocol in Wireshark picked up my website as:</p><p>Server: Apache\r\n</p><p>Is this correct? I assumed it would say Linux? Can you explain why it says Apache? Sorry if it's a silly Q.</p><p>Thanks again.</p></div><div id="comment-15375-info" class="comment-info"><span class="comment-age">(30 Oct '12, 09:23)</span> <span class="comment-user userinfo">smc20</span></div></div><span id="15378"></span><div id="comment-15378" class="comment"><div id="post-15378-score" class="comment-score"></div><div class="comment-text"><p>It says "Server: Apache" because that is what the <strong>HTTP Server application</strong> software is. You're looking at the HTTP protocol, so "Linux" would be the wrong answer, because Linux is not an HTTP server application :-)</p><p>So yes, that is correct. And it is not a silly Question... it is better to ask to improve knowledge than keeping wondering why things are like they are ;-)</p></div><div id="comment-15378-info" class="comment-info"><span class="comment-age">(30 Oct '12, 09:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="15382"></span><div id="comment-15382" class="comment"><div id="post-15382-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I captured packets and browsed to my website. The Hypertext Transfer Protocol in Wireshark picked up my website as: Server: Apache.</p></blockquote><p>Well that's what is probably configured for Apache. It does not necessarily report it's full version information. Sometimes the version information is done intentionally to keep away script kiddies with their automatic scan/attack tools.</p><p>If you set the following Apache config option, it will only report "Apache" in the Server header.</p><blockquote><p><code>ServerTokens Prod</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-15382-info" class="comment-info"><span class="comment-age">(30 Oct '12, 10:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15384"></span><div id="comment-15384" class="comment"><div id="post-15384-score" class="comment-score"></div><div class="comment-text"><p>thanks guys, very much appreciated.</p></div><div id="comment-15384-info" class="comment-info"><span class="comment-age">(30 Oct '12, 10:13)</span> <span class="comment-user userinfo">smc20</span></div></div></div><div id="comment-tools-15373" class="comment-tools"></div><div class="clear"></div><div id="comment-15373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


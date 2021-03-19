+++
type = "question"
title = "TCP exchange works but no web page"
description = '''I am working on a small embedded web server for a &quot;friendlyarm&quot; with no OS.  http://www.cttestset.com/gothru.JPG As shown in this picture it appears to go thru the connection negotiation just fine but IE still says it can&#x27;t show the webpage. Any ideas ?'''
date = "2013-04-06T16:12:00Z"
lastmod = "2013-04-07T00:52:00Z"
weight = 20140
keywords = [ "server", "ie", "tcp", "wireshark" ]
aliases = [ "/questions/20140" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP exchange works but no web page](/questions/20140/tcp-exchange-works-but-no-web-page)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20140-score" class="post-score" title="current number of votes">0</div><span id="post-20140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on a small embedded web server for a "friendlyarm" with no OS.</p><p><a href="http://www.cttestset.com/gothru.JPG">http://www.cttestset.com/gothru.JPG</a></p><p>As shown in this picture it appears to go thru the connection negotiation just fine but IE still says it can't show the webpage. Any ideas ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-ie" rel="tag" title="see questions tagged &#39;ie&#39;">ie</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '13, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/9a78648dd7bbea058b5e1adef678f8fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vernon%20Lermond&#39;s gravatar image" /><p><span>Vernon Lermond</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vernon Lermond has no accepted answers">0%</span></p></div></div><div id="comments-container-20140" class="comments-container"><span id="20141"></span><div id="comment-20141" class="comment"><div id="post-20141-score" class="comment-score"></div><div class="comment-text"><p>that Screenshot doesn't help much because it doesn't show decoded HTTP, probably because you didn't use port 80 or any other well known HTTP port on your server.</p><p>Can you force HTTP decoding by right clicking on a packet of the conversation and selecting "decode as" -&gt; HTTP? Or better yet, if this is just a test trace: put it on <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the URL.</p></div><div id="comment-20141-info" class="comment-info"><span class="comment-age">(06 Apr '13, 16:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-20140" class="comment-tools"></div><div class="clear"></div><div id="comment-20140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20146"></span>

<div id="answer-container-20146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20146-score" class="post-score" title="current number of votes">2</div><span id="post-20146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While I totally agree with <span>@Jasper</span> that an image is not really handy to analyze packets (that's why we have Wireshark, to look at packets in detail), it does show what is wrong.</p><p>After accepting the connection, the server does receive the request from the client (frame 26) and acknowledges it's reception (frame 27). However, the server does not send back any data to the client (based on the TCP sequence numbers) and closes the connection (frame 28).</p><p>So it looks like your webserver does not properly send a response...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '13, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20146" class="comments-container"></div><div id="comment-tools-20146" class="comment-tools"></div><div class="clear"></div><div id="comment-20146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


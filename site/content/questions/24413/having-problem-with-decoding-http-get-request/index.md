+++
type = "question"
title = "Having problem with decoding Http Get request"
description = '''Hi All, I am facing an issue with customer network wherein when i request an HTTP/GET request it is going as a data payload in the TCP request to the server. due to this I am unable to do http based enhancements to the URL. The PSH, ACK flag is set and when I follow the TCP request i see it as a pro...'''
date = "2013-09-06T01:18:00Z"
lastmod = "2013-09-11T00:23:00Z"
weight = 24413
keywords = [ "http", "get" ]
aliases = [ "/questions/24413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Having problem with decoding Http Get request](/questions/24413/having-problem-with-decoding-http-get-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24413-score" class="post-score" title="current number of votes">0</div><span id="post-24413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am facing an issue with customer network wherein when i request an HTTP/GET request it is going as a data payload in the TCP request to the server. due to this I am unable to do http based enhancements to the URL. The PSH, ACK flag is set and when I follow the TCP request i see it as a proper GET request</p><p><em>GET / HTTP/1.1 Connection: Keep-Alive Host: x.x.x.x:8180</em></p><p>The communication with server is also happening fine.</p><p>Whereas for another URL with the same process I m seeing a proper Http/Get request.</p><p>I m not able to understand what is this issue pertaining to. Is it an issue with the sending application settings? How do i resolve this</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/4fce2b94a73d40386ea20c38fccdc15e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vinay%20Pagadal&#39;s gravatar image" /><p><span>Vinay Pagadal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vinay Pagadal has no accepted answers">0%</span></p></div></div><div id="comments-container-24413" class="comments-container"></div><div id="comment-tools-24413" class="comment-tools"></div><div class="clear"></div><div id="comment-24413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24484"></span>

<div id="answer-container-24484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24484-score" class="post-score" title="current number of votes">2</div><span id="post-24484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>GET / HTTP/1.1 Connection: Keep-Alive Host: x.x.x.x:<strong>8180</strong></p></blockquote><p>The reason why you don't see the HTTP REQUEST in Wireshark is the port. Wireshark 'detects' HTTP mainly on the port and the standard ports for HTTP do <strong>not</strong> include port 8180.</p><p>There are two options.</p><ol><li>Right click one of the packets and choose: Decode As -&gt; HTTP</li><li>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP Ports: [add port 8180 to this list]</li></ol><p>After that, you will see the conversation as HTTP and you should be able to use these display filters:</p><blockquote><p>http.request or http.response</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24484" class="comments-container"><span id="24550"></span><div id="comment-24550" class="comment"><div id="post-24550-score" class="comment-score"></div><div class="comment-text"><p>Oh so there is no problem with my client or server sending the request...its just that wireshark is unable to decode it as an Http request due to a non standard TCP port number.</p><p>Thanks a lot for your help Kurt :)</p></div><div id="comment-24550-info" class="comment-info"><span class="comment-age">(11 Sep '13, 00:23)</span> <span class="comment-user userinfo">Vinay Pagadal</span></div></div></div><div id="comment-tools-24484" class="comment-tools"></div><div class="clear"></div><div id="comment-24484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


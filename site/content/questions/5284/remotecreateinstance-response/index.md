+++
type = "question"
title = "RemoteCreateInstance response"
description = '''Hello, We have just recently installed our application on a windows 2008 server. My client connects to the server using dcom. On this server only (so far) we get errors saying that we can&#x27;t find the server. This message is basically a catch all. I have setup a wireshark trace and captured the messag...'''
date = "2011-07-26T14:56:00Z"
lastmod = "2011-07-27T12:30:00Z"
weight = 5284
keywords = [ "remotecreateinstance", "response" ]
aliases = [ "/questions/5284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RemoteCreateInstance response](/questions/5284/remotecreateinstance-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5284-score" class="post-score" title="current number of votes">0</div><span id="post-5284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, We have just recently installed our application on a windows 2008 server. My client connects to the server using dcom. On this server only (so far) we get errors saying that we can't find the server. This message is basically a catch all. I have setup a wireshark trace and captured the message using the protocol ISystemActivator with the information stating "RemoteCreateInstance response" . In looking at the message i see an HResult:Unknown (0x80004027) message. I believe that the error messagge is "The component or application containing the component has been disabled". This message is sent from my server IP to the requesting PC. I am not sure what or where I need to make a change to enable it. I have gone through the settings that I know for DCOM. I would appreciate any information you can provide. Thanks. Sunny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remotecreateinstance" rel="tag" title="see questions tagged &#39;remotecreateinstance&#39;">remotecreateinstance</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/e64cdfdb8784168031865b9ad3bc97a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnystrain&#39;s gravatar image" /><p><span>sunnystrain</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnystrain has no accepted answers">0%</span></p></div></div><div id="comments-container-5284" class="comments-container"><span id="5285"></span><div id="comment-5285" class="comment"><div id="post-5285-score" class="comment-score"></div><div class="comment-text"><p>Have you tried Googling for</p><p>dcom "The component or application containing the component has been disabled" ?</p><p>I see a number of hits....</p></div><div id="comment-5285-info" class="comment-info"><span class="comment-age">(26 Jul '11, 16:09)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="5318"></span><div id="comment-5318" class="comment"><div id="post-5318-score" class="comment-score"></div><div class="comment-text"><p>I found part of the problem. When windows 2008 was installed they did not add the application server role and install com+ and dtc. I have atleast changed my error. now i am getting Malformed packet (exception occurred)</p></div><div id="comment-5318-info" class="comment-info"><span class="comment-age">(27 Jul '11, 09:04)</span> <span class="comment-user userinfo">sunnystrain</span></div></div><span id="5319"></span><div id="comment-5319" class="comment"><div id="post-5319-score" class="comment-score"></div><div class="comment-text"><blockquote><p>now i am getting Malformed packet (exception occurred)</p></blockquote><p>In Wireshark ? If so: "malformed" is Wireshark's opinion and doesn't necessarily mean there's an actual problem.</p><p>The real question: what error message (if any) are you getting from your client ?</p></div><div id="comment-5319-info" class="comment-info"><span class="comment-age">(27 Jul '11, 09:26)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="5320"></span><div id="comment-5320" class="comment"><div id="post-5320-score" class="comment-score"></div><div class="comment-text"><p>Hi Bill, Yes it was in Wireshark that i found the error. What my client gets is an HResults error: (0x800706ba) which I believe is "The RPC server is unavailable." I am trying to see if I have missed another setting in Windows 2008. I have checked and the RPC services is running. Thanks for your help.</p></div><div id="comment-5320-info" class="comment-info"><span class="comment-age">(27 Jul '11, 09:32)</span> <span class="comment-user userinfo">sunnystrain</span></div></div><span id="5321"></span><div id="comment-5321" class="comment"><div id="post-5321-score" class="comment-score"></div><div class="comment-text"><p>My suggestion: :)<br />
</p><p>First focus on the client error messages rather than Wireshark dissection.</p><p>For example: Wireshark showing "malformed" is much more likely to be some Wireshark issue with respect to the capture/decode (rather than an actual protocol error) when looking at a "standard" protocol.</p></div><div id="comment-5321-info" class="comment-info"><span class="comment-age">(27 Jul '11, 09:50)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-5284" class="comment-tools"></div><div class="clear"></div><div id="comment-5284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5327"></span>

<div id="answer-container-5327" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5327-score" class="post-score" title="current number of votes">0</div><span id="post-5327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When I added the Application Server role corrected my issue. The other issue that I said about the HResults error was a different issue isolated to one user. Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/e64cdfdb8784168031865b9ad3bc97a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnystrain&#39;s gravatar image" /><p><span>sunnystrain</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnystrain has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5327" class="comments-container"></div><div id="comment-tools-5327" class="comment-tools"></div><div class="clear"></div><div id="comment-5327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


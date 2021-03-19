+++
type = "question"
title = "how to find Master-key and Session-ID on windows for decryption of SSl/TLS traffic using wireshark?"
description = '''I have a C++ application that has a SSL/TLS communication with its own server and i don&#x27;t have any access to that server. I&#x27;m trying to find out what is it sending from my PC to the server. I tried burp and fiddler as man-in-middle but it didn&#x27;t work. The application does not support Proxy so i trie...'''
date = "2014-08-04T06:36:00Z"
lastmod = "2014-08-04T08:50:00Z"
weight = 35157
keywords = [ "session-id", "master-key", "wireshark" ]
aliases = [ "/questions/35157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to find Master-key and Session-ID on windows for decryption of SSl/TLS traffic using wireshark?](/questions/35157/how-to-find-master-key-and-session-id-on-windows-for-decryption-of-ssltls-traffic-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35157-score" class="post-score" title="current number of votes">0</div><span id="post-35157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a C++ application that has a SSL/TLS communication with its own server and i don't have any access to that server. I'm trying to find out what is it sending from my PC to the server.</p><p>I tried burp and fiddler as man-in-middle but it didn't work. The application does not support Proxy so i tried routing the traffic using proxifier to burp and fiddler but it didn't work.</p><p>So I came up with these articles <a href="https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets+/16415">https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets+/16415</a> and <a href="http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id</a></p><p>I just need to know , How I can find Master-key and Session-ID to decrypt SSL/TLS trafic.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session-id" rel="tag" title="see questions tagged &#39;session-id&#39;">session-id</span> <span class="post-tag tag-link-master-key" rel="tag" title="see questions tagged &#39;master-key&#39;">master-key</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '14, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/74915461f591b189cb22ee98b5cf3ecc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izeid&#39;s gravatar image" /><p><span>izeid</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izeid has no accepted answers">0%</span></p></div></div><div id="comments-container-35157" class="comments-container"></div><div id="comment-tools-35157" class="comment-tools"></div><div class="clear"></div><div id="comment-35157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35158"></span>

<div id="answer-container-35158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35158-score" class="post-score" title="current number of votes">1</div><span id="post-35158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I just need to know , How I can find Master-key and Session-ID to decrypt SSL/TLS trafic.</p></blockquote><p>That's a feature of certain <strong>web browsers</strong>, and in the case of your posted link, the openssl client.</p><p>If you did not add that functionality to your own C++ application, meaning to export the SSL session keys, it won't be there.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '14, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35158" class="comments-container"><span id="35160"></span><div id="comment-35160" class="comment"><div id="post-35160-score" class="comment-score"></div><div class="comment-text"><p>First of all, The application is not mine.So in my case, What should i do step by step ?</p></div><div id="comment-35160-info" class="comment-info"><span class="comment-age">(04 Aug '14, 07:56)</span> <span class="comment-user userinfo">izeid</span></div></div><span id="35162"></span><div id="comment-35162" class="comment"><div id="post-35162-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So in my case, <strong>What should i do step by step</strong> ?</p></blockquote><p>Contact the vendor of that software. Unless he added code to export the SSL session keys, there is nothing you can do. Sorry!</p></div><div id="comment-35162-info" class="comment-info"><span class="comment-age">(04 Aug '14, 08:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35158" class="comment-tools"></div><div class="clear"></div><div id="comment-35158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


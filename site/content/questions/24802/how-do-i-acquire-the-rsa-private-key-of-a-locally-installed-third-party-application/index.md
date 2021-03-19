+++
type = "question"
title = "How do I acquire the RSA private key of a locally installed third party application?"
description = '''I&#x27;m working on reverse engineering an online game (League of Legends). While a lot of traffic is unencrypted and easily available through your great tool, is some data e.g. the chat, pub-private key encrypted. I know I can add this private key to wireshark to monitor the data, but how can I find the...'''
date = "2013-09-17T03:42:00Z"
lastmod = "2013-09-17T04:12:00Z"
weight = 24802
keywords = [ "private", "rsa", "key", "reverse-engineering" ]
aliases = [ "/questions/24802" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I acquire the RSA private key of a locally installed third party application?](/questions/24802/how-do-i-acquire-the-rsa-private-key-of-a-locally-installed-third-party-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24802-score" class="post-score" title="current number of votes">0</div><span id="post-24802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on reverse engineering an online game (League of Legends). While a lot of traffic is unencrypted and easily available through your great tool, is some data e.g. the chat, pub-private key encrypted. I know I can add this private key to wireshark to monitor the data, but how can I find the private key?</p><p>It must be on my computer since the game is able to connect. It can be in the executable, but it should be possible to retrieve non the less, or am I wrong?</p><p>Any help or pointers would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-rsa" rel="tag" title="see questions tagged &#39;rsa&#39;">rsa</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-reverse-engineering" rel="tag" title="see questions tagged &#39;reverse-engineering&#39;">reverse-engineering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/00b7b76f66d194878bb23a73f6a119dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramvi&#39;s gravatar image" /><p><span>ramvi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramvi has no accepted answers">0%</span></p></div></div><div id="comments-container-24802" class="comments-container"></div><div id="comment-tools-24802" class="comment-tools"></div><div class="clear"></div><div id="comment-24802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24806"></span>

<div id="answer-container-24806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24806-score" class="post-score" title="current number of votes">0</div><span id="post-24806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sorry, but this is totally unrelated to Wireshark.</p><p>There are tons of web pages out there with game cheating tools and I'm sure those guys will also be able to help you find the key within the memory of the game client.</p><p>As soon as you have the SSL/TLS session key (if it is SSL/TLS at all), you can try to decrypt the communication.</p><blockquote><p><a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a><br />
<a href="https://www.google.com/?q=wireshark%20ssl%20decryption%20tutorial">https://www.google.com/?q=wireshark%20ssl%20decryption%20tutorial</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '13, 04:10</strong> </span></p></div></div><div id="comments-container-24806" class="comments-container"><span id="24807"></span><div id="comment-24807" class="comment"><div id="post-24807-score" class="comment-score"></div><div class="comment-text"><p>Find the key within memory. Thanks for the pointer! And sorry for asking in the wrong place</p></div><div id="comment-24807-info" class="comment-info"><span class="comment-age">(17 Sep '13, 04:08)</span> <span class="comment-user userinfo">ramvi</span></div></div><span id="24808"></span><div id="comment-24808" class="comment"><div id="post-24808-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Find the key within memory. Thanks for the pointer!</p></blockquote><p>Yes, the session key must be in memory to be able to encrypt/decrypt data. There are tools available for various game clients to extract that key (and other data) from the process memory.</p></div><div id="comment-24808-info" class="comment-info"><span class="comment-age">(17 Sep '13, 04:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24806" class="comment-tools"></div><div class="clear"></div><div id="comment-24806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


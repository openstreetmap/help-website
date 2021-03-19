+++
type = "question"
title = "Need to decode ssl locally"
description = '''I want to decode the traffic between a desktop application (on my desktop) and a server out over the Internet. This is HTTPS traffic, but not from a web browser. There is no pre-shared key or such, but it is traffic on my machine so I don&#x27;t think it&#x27;s unreasonable to be able to decode this stream to...'''
date = "2012-09-17T08:35:00Z"
lastmod = "2012-09-17T15:32:00Z"
weight = 14321
keywords = [ "ssl", "https" ]
aliases = [ "/questions/14321" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to decode ssl locally](/questions/14321/need-to-decode-ssl-locally)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14321-score" class="post-score" title="current number of votes">0</div><span id="post-14321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to decode the traffic between a desktop application (on my desktop) and a server out over the Internet. This is HTTPS traffic, but not from a web browser.</p><p>There is no pre-shared key or such, but it is traffic on my machine so I don't think it's unreasonable to be able to decode this stream to see what information is being sent.</p><p>Is there some way to do this? I have concerns over the data being uploaded and separately want to analysis the communications because it's somewhat slow.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '12, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/a867a9cae8a2bb37380c3a706c86472a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klamerus&#39;s gravatar image" /><p><span>klamerus</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klamerus has no accepted answers">0%</span></p></div></div><div id="comments-container-14321" class="comments-container"></div><div id="comment-tools-14321" class="comment-tools"></div><div class="clear"></div><div id="comment-14321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14330"></span>

<div id="answer-container-14330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14330-score" class="post-score" title="current number of votes">0</div><span id="post-14330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need either of the following to decrypt SSL traffic:</p><ul><li>access to the private key of the server (you don't have access to that, as it's a server on the internet)</li><li>your client 'spits out' the session key (it won't, as it' not a browser).</li></ul><p>So, what can you do?</p><p>Use a local ssl proxy that is able to intercept ssl connections, like Fiddler2.</p><blockquote><p><code>http://www.fiddler2.com/fiddler2/</code><br />
</p></blockquote><p>See also my answer in a similar question.</p><blockquote><p><code>http://ask.wireshark.org/questions/11744/how-to-find-the-symmetric-key-generated-by-the-browser</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '12, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14330" class="comments-container"><span id="14340"></span><div id="comment-14340" class="comment"><div id="post-14340-score" class="comment-score"></div><div class="comment-text"><p>My understanding is that fiddler only works with web browsers and this is not a web application (or at least it's not a browser-based client). Can fiddler capture non-browser traffic?</p></div><div id="comment-14340-info" class="comment-info"><span class="comment-age">(17 Sep '12, 14:40)</span> <span class="comment-user userinfo">klamerus</span></div></div><span id="14341"></span><div id="comment-14341" class="comment"><div id="post-14341-score" class="comment-score"></div><div class="comment-text"><p>can you set a proxy in that application? If so, chances are good that you can use Fiddler.</p></div><div id="comment-14341-info" class="comment-info"><span class="comment-age">(17 Sep '12, 14:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14342"></span><div id="comment-14342" class="comment"><div id="post-14342-score" class="comment-score"></div><div class="comment-text"><p>And if you can't set a proxy in the application and it does not use the system's proxy if one is configured, then you can use a Backtrack DVD and run:</p><ul><li>arpspoof to make traffic go through your backtrack box</li><li>sslsniff to decrypt and reencrypt traffic</li></ul><p>This setup will present a new dynamically generated certificate, signed by a CA created by sslsniff. You might need to import that CA certificate in windows or the application.</p></div><div id="comment-14342-info" class="comment-info"><span class="comment-age">(17 Sep '12, 15:32)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-14330" class="comment-tools"></div><div class="clear"></div><div id="comment-14330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


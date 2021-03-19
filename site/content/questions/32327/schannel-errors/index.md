+++
type = "question"
title = "schannel errors"
description = '''I have a capture file of a network during the time schannel alerts were generated on an exchange server running outlook web access. What should I be looking at in the capture file to determine what is causing these schannel alerts? I marked down the times the schannel alerts were generated and looke...'''
date = "2014-04-30T15:33:00Z"
lastmod = "2014-05-01T07:09:00Z"
weight = 32327
keywords = [ "schannel", "ssl" ]
aliases = [ "/questions/32327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [schannel errors](/questions/32327/schannel-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32327-score" class="post-score" title="current number of votes">0</div><span id="post-32327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file of a network during the time schannel alerts were generated on an exchange server running outlook web access. What should I be looking at in the capture file to determine what is causing these schannel alerts? I marked down the times the schannel alerts were generated and looked at the capture file, but can't seem to get much from this. Please see the posts on stackexchange below for additional information.</p><p><a href="http://serverfault.com/questions/586530/schannel-ssl-3-0-error-owa-windows-server-2008-r2/592369#592369">http://serverfault.com/questions/586530/schannel-ssl-3-0-error-owa-windows-server-2008-r2/592369#592369</a></p><p><a href="http://serverfault.com/questions/592408/schannel-errors-fatal-20-and-40">http://serverfault.com/questions/592408/schannel-errors-fatal-20-and-40</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-schannel" rel="tag" title="see questions tagged &#39;schannel&#39;">schannel</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/30ffd6f177b036b37b615a93aebceef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studentofsecurity&#39;s gravatar image" /><p><span>studentofsec...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studentofsecurity has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '14, 05:39</strong> </span></p></div></div><div id="comments-container-32327" class="comments-container"></div><div id="comment-tools-32327" class="comment-tools"></div><div class="clear"></div><div id="comment-32327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32346"></span>

<div id="answer-container-32346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32346-score" class="post-score" title="current number of votes">0</div><span id="post-32346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Schannel Error 36874 &quot;An TLS 1.0 connection was recieved from a remote client application, but dodne of the cipher suites supported by the client are supported by the server. The SSL connection request has failed.&quot;

Schannel Error 36888 &quot;The following fatal alert was generated: 40. The internal error state is 1204&quot;</code></pre><p>So, the first error is quite 'normal'. You'll sometimes have TLS clients with either very new ciphers/options or clients with outdated ciphers/options.</p><p>The second error is different. Maybe you are able to see something unusual in the TLS handshake with Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32346" class="comments-container"></div><div id="comment-tools-32346" class="comment-tools"></div><div class="clear"></div><div id="comment-32346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


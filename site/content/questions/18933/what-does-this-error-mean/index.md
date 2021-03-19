+++
type = "question"
title = "What does this error mean?"
description = '''Can any one explain the follow Wireshark error? Can&#x27;t get list of interfaces: Is the server properly installed on ip? connect() failed: No connection could be made because the target machine actively refused it. (code 10061)  I can ftp into server using host name and password.'''
date = "2013-02-27T11:23:00Z"
lastmod = "2013-02-27T11:40:00Z"
weight = 18933
keywords = [ "rpcap" ]
aliases = [ "/questions/18933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does this error mean?](/questions/18933/what-does-this-error-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18933-score" class="post-score" title="current number of votes">1</div><span id="post-18933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can any one explain the follow Wireshark error?</p><pre><code>Can&#39;t get list of interfaces: Is the server properly installed on ip?  connect() failed: No connection could be made because the target machine actively refused it. (code 10061)</code></pre><p>I can ftp into server using host name and password.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/095c76981bef0ed1de91928e615f6ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrayRyder&#39;s gravatar image" /><p><span>GrayRyder</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrayRyder has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Feb '13, 11:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18933" class="comments-container"></div><div id="comment-tools-18933" class="comment-tools"></div><div class="clear"></div><div id="comment-18933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18934"></span>

<div id="answer-container-18934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18934-score" class="post-score" title="current number of votes">1</div><span id="post-18934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're trying to connect to an interface on a remote machine to capture on one of its interfaces, and have it send the captured packets over the network to your machine.</p><p>The "remote capture" server isn't allowing that for some reason. Did you install the rpcap server on that machine?</p><blockquote><p>I can ftp into server using host name and password.</p></blockquote><p>That doesn't mean that you can capture using its interfaces; that requires a different server program (the rpcap server).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '13, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18934" class="comments-container"></div><div id="comment-tools-18934" class="comment-tools"></div><div class="clear"></div><div id="comment-18934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


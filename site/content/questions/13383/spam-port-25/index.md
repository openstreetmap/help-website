+++
type = "question"
title = "Spam port 25"
description = '''Can someone explain me in detailed how can i setup wireshark to locate which ip address of our network is causing problem to port 25'''
date = "2012-08-06T02:02:00Z"
lastmod = "2014-09-03T09:42:00Z"
weight = 13383
keywords = [ "port25", "virus", "spam" ]
aliases = [ "/questions/13383" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Spam port 25](/questions/13383/spam-port-25)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13383-score" class="post-score" title="current number of votes">0</div><span id="post-13383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone explain me in detailed how can i setup wireshark to locate which ip address of our network is causing problem to port 25</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port25" rel="tag" title="see questions tagged &#39;port25&#39;">port25</span> <span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-spam" rel="tag" title="see questions tagged &#39;spam&#39;">spam</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/c4824f7487642be6a44dbbaddcf60541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kosman&#39;s gravatar image" /><p><span>kosman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kosman has no accepted answers">0%</span></p></div></div><div id="comments-container-13383" class="comments-container"></div><div id="comment-tools-13383" class="comment-tools"></div><div class="clear"></div><div id="comment-13383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13462"></span>

<div id="answer-container-13462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13462-score" class="post-score" title="current number of votes">0</div><span id="post-13462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By "problem", you mean spam, right?</p><p>O.K. you need to capture the traffic "in front" of your internet access router. Please take a look at the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Capture Setup</a> to learn how to do that.</p><p>Then start capturing TCP connections on port 25. See <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> to learn how to do that (Filter: port 25).</p><p>Wait some time (minutes, hours). Then analyze the captured data.</p><p>First look at the conversations:</p><blockquote><p><code>Statistics -&gt; Conversation List -&gt; TCP</code></p></blockquote><p>Sort the output for "Address A". The host with the most entries (IGNORE your internal mail server), is most likely the one that sends spam mails directly.</p><p>However: If the spam bot sends mail through your mail server, it will be more work to find the system that sent the mail. Please come back, think this is the case, and after you have done the fist step.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '12, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13462" class="comments-container"><span id="35965"></span><div id="comment-35965" class="comment"><div id="post-35965-score" class="comment-score"></div><div class="comment-text"><p>Hi I have the same problem than the guy in the first post. I have done all your advice and i have the TCP Conversation list, what I supposed to do next Thanks</p></div><div id="comment-35965-info" class="comment-info"><span class="comment-age">(03 Sep '14, 09:42)</span> <span class="comment-user userinfo">rafacomu</span></div></div></div><div id="comment-tools-13462" class="comment-tools"></div><div class="clear"></div><div id="comment-13462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


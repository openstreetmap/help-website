+++
type = "question"
title = "How can I identify the instant at which a webage is refreshed?"
description = '''Is way to know when a webpage is refreshed based on the information in a packet? I ran Wireshark for different websites, and refreshed them when the capturing was in progress. I couldn&#x27;t find a concrete pattern as to which packet in particular indicates that the page has been refreshed.'''
date = "2012-02-14T11:51:00Z"
lastmod = "2012-02-14T12:07:00Z"
weight = 9001
keywords = [ "webpage", "http", "analysis", "packet" ]
aliases = [ "/questions/9001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I identify the instant at which a webage is refreshed?](/questions/9001/how-can-i-identify-the-instant-at-which-a-webage-is-refreshed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9001-score" class="post-score" title="current number of votes">0</div><span id="post-9001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is way to know when a webpage is refreshed based on the information in a packet? I ran Wireshark for different websites, and refreshed them when the capturing was in progress. I couldn't find a concrete pattern as to which packet in particular indicates that the page has been refreshed.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webpage" rel="tag" title="see questions tagged &#39;webpage&#39;">webpage</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/84da5ede7d868490afe7e099e42aeed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhiya&#39;s gravatar image" /><p><span>Rhiya</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhiya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Feb '12, 12:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9001" class="comments-container"></div><div id="comment-tools-9001" class="comment-tools"></div><div class="clear"></div><div id="comment-9001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9003"></span>

<div id="answer-container-9003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9003-score" class="post-score" title="current number of votes">2</div><span id="post-9003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no guarantee that refreshing a webpage in your browser will actually generate a new request to the server since modern browsers aggressively cache content from servers. Detecting this condition will be dependent upon the specific browser being used and the specific contents of the page being viewed.<br />
If your page is mostly quiet once it is loaded, you can look for another <code>HTTP GET</code> (possibly preceded by a <code>TCP</code> handshake). Most modern browsers allow you to refresh a page without looking at the local cache, so you should make sure you are doing that when attempting this (e.g. in Firefox on Windows, <code>CTRL+F5</code> is the default shortcut for this).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-9003" class="comments-container"></div><div id="comment-tools-9003" class="comment-tools"></div><div class="clear"></div><div id="comment-9003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


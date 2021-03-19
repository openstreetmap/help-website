+++
type = "question"
title = "Filter based on Content"
description = '''I have a windows service that uses winsock communicating to another windows service that uses winsock. We are talking over TCP/IP using JSON.  I am trying to prove that my service is behaving properly and that the service it communicates to is not sending the expected data. I set up wireshark to cap...'''
date = "2017-06-28T08:48:00Z"
lastmod = "2017-06-28T10:01:00Z"
weight = 62368
keywords = [ "capture-filter" ]
aliases = [ "/questions/62368" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter based on Content](/questions/62368/filter-based-on-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62368-score" class="post-score" title="current number of votes">0</div><span id="post-62368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a windows service that uses winsock communicating to another windows service that uses winsock. We are talking over TCP/IP using JSON.</p><p>I am trying to prove that my service is behaving properly and that the service it communicates to is not sending the expected data.</p><p>I set up wireshark to capture on the Ethernet card I am using on my local machine and filter on ip.addr == &lt;remote ip="" address=""&gt; and I can see the traffic.</p><p>I am expecting messages that contain "Message One" and I can see them, thousands of them. While I am receiving all those, I expect a few messages that contain "Message Two"</p><p>How do I set up the filter to prove that I am not receiving the "Message Two" messages?</p><p>I Googled a little bit and someone said use data-text-lines contains "Message Two", but that doesn't work. I can verify it doesn't work by looking at the messages that contain "Message One" and then filtering data-text-line contains "Message One" and they all disappear when they shouldn't. I have a feeling that is for http only.</p><p>What do I use for a filter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '17, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/d43fc82681b19691a007ddbc63c2512d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fleshbits&#39;s gravatar image" /><p><span>Fleshbits</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fleshbits has no accepted answers">0%</span></p></div></div><div id="comments-container-62368" class="comments-container"></div><div id="comment-tools-62368" class="comment-tools"></div><div class="clear"></div><div id="comment-62368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62369"></span>

<div id="answer-container-62369" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62369-score" class="post-score" title="current number of votes">0</div><span id="post-62369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Fleshbits has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just use a display filter <code>frame contains "Message Two"</code>. This filter doesn't care about how the packet is dissected and searches in the raw bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '17, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62369" class="comments-container"></div><div id="comment-tools-62369" class="comment-tools"></div><div class="clear"></div><div id="comment-62369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


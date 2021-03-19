+++
type = "question"
title = "How to Identify DES traffic?"
description = '''Hi, I&#x27;m new to Wireshark and I will find time to learn it. But at the moment I need help to identify and possible DES encrypted traffic on my network.  This is to help with system upgrades that are taking place. I don&#x27;t need to decrypt anything just identify it and its source/destination. Cheers'''
date = "2014-11-27T04:29:00Z"
lastmod = "2014-11-27T07:56:00Z"
weight = 38204
keywords = [ "traffic", "encrypted", "identify", "network" ]
aliases = [ "/questions/38204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Identify DES traffic?](/questions/38204/how-to-identify-des-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38204-score" class="post-score" title="current number of votes">0</div><span id="post-38204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm new to Wireshark and I will find time to learn it. But at the moment I need help to identify and possible DES encrypted traffic on my network. This is to help with system upgrades that are taking place.</p><p>I don't need to decrypt anything just identify it and its source/destination.</p><p>Cheers</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-encrypted" rel="tag" title="see questions tagged &#39;encrypted&#39;">encrypted</span> <span class="post-tag tag-link-identify" rel="tag" title="see questions tagged &#39;identify&#39;">identify</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '14, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/c39641f2875c054b4a31f53873eeba17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeordieUK&#39;s gravatar image" /><p><span>GeordieUK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeordieUK has no accepted answers">0%</span></p></div></div><div id="comments-container-38204" class="comments-container"></div><div id="comment-tools-38204" class="comment-tools"></div><div class="clear"></div><div id="comment-38204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38212"></span>

<div id="answer-container-38212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38212-score" class="post-score" title="current number of votes">0</div><span id="post-38212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But at the moment I need <strong>help to identify and possible DES encrypted</strong></p></blockquote><p>DES encrypted data is simply a stream of binary data and there is no sign or signature that "marks" it as DES encrypted. All you can do is to analyze the protocols beeing used to <strong>transmit</strong> the data and then try to find signs for DES usage, like SSL/TLS ciphers in the handshake, etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38212" class="comments-container"></div><div id="comment-tools-38212" class="comment-tools"></div><div class="clear"></div><div id="comment-38212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


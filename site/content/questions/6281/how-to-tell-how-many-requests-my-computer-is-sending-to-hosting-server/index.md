+++
type = "question"
title = "How to tell how many requests my computer is sending to hosting server"
description = '''Our web host is saying that they are getting 500 requests a second from our computer. This triggers an autoblock on the server and locks out our IP. How can I see what is causing those requests in Wireshark?'''
date = "2011-09-12T06:48:00Z"
lastmod = "2011-09-12T07:43:00Z"
weight = 6281
keywords = [ "request" ]
aliases = [ "/questions/6281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tell how many requests my computer is sending to hosting server](/questions/6281/how-to-tell-how-many-requests-my-computer-is-sending-to-hosting-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6281-score" class="post-score" title="current number of votes">0</div><span id="post-6281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our web host is saying that they are getting 500 requests a second from our computer. This triggers an autoblock on the server and locks out our IP. How can I see what is causing those requests in Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/80187d987f1662a3e2a487f06aea08e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ohno&#39;s gravatar image" /><p><span>Ohno</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ohno has no accepted answers">0%</span></p></div></div><div id="comments-container-6281" class="comments-container"><span id="6283"></span><div id="comment-6283" class="comment"><div id="post-6283-score" class="comment-score"></div><div class="comment-text"><p>For s atart: Do a short capture and then look at the capture... :)</p><p>500 requests/sec should be pretty obvious in the capture.</p></div><div id="comment-6283-info" class="comment-info"><span class="comment-age">(12 Sep '11, 06:59)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="6285"></span><div id="comment-6285" class="comment"><div id="post-6285-score" class="comment-score"></div><div class="comment-text"><p>Of course, if the server has locked out your IP you may see nothing or just attempts to connect to the server which are rejected (or which timeout).</p></div><div id="comment-6285-info" class="comment-info"><span class="comment-age">(12 Sep '11, 07:43)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-6281" class="comment-tools"></div><div class="clear"></div><div id="comment-6281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6282"></span>

<div id="answer-container-6282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6282-score" class="post-score" title="current number of votes">0</div><span id="post-6282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Simply put an IP filter to your IP address and your hosting servers IP address and verify if there are 500 request per second.</p><p>If true read this other thread:</p><p><a href="http://ask.wireshark.org/questions/6232/is-it-possible-to-see-what-on-my-computer-is-requesting-a-webpage-to-be-opened">http://ask.wireshark.org/questions/6232/is-it-possible-to-see-what-on-my-computer-is-requesting-a-webpage-to-be-opened</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '11, 07:00</strong> </span></p></div></div><div id="comments-container-6282" class="comments-container"></div><div id="comment-tools-6282" class="comment-tools"></div><div class="clear"></div><div id="comment-6282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Finding a Particular IP Address"
description = '''Hello All, I am new to Wireshark and actually to packet capture altogether. So far I have successfully done a packet capture on my computer&#x27;s NIC and now I want to find out if a particular IP address or part of an IP address is present. I have tried to go through the help file that comes with Wiresh...'''
date = "2010-12-22T16:31:00Z"
lastmod = "2010-12-22T17:02:00Z"
weight = 1459
keywords = [ "filter" ]
aliases = [ "/questions/1459" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding a Particular IP Address](/questions/1459/finding-a-particular-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1459-score" class="post-score" title="current number of votes">0</div><span id="post-1459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am new to Wireshark and actually to packet capture altogether. So far I have successfully done a packet capture on my computer's NIC and now I want to find out if a particular IP address or part of an IP address is present. I have tried to go through the help file that comes with Wireshark but I am not sure how to go about setting a filter or whatever to look for the particular IP address. Example, I want to see if any packets were sent to or received from 68.77.<em>.</em> how would I set that up?</p><p>Thank You So Much,</p><p>Val</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '10, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/492124bf20a69a0209d3603f747a3367?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Valek%20Hawke&#39;s gravatar image" /><p><span>Valek Hawke</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Valek Hawke has no accepted answers">0%</span></p></div></div><div id="comments-container-1459" class="comments-container"></div><div id="comment-tools-1459" class="comment-tools"></div><div class="clear"></div><div id="comment-1459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1460"></span>

<div id="answer-container-1460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1460-score" class="post-score" title="current number of votes">0</div><span id="post-1460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In display filter format</p><p>ip.addr -- this will look at source and destination address for a match</p><p>we can use slash notation, so in your example 68.77.0.0/16</p><p>So the following display filter should work for you.</p><p>ip.addr==68.77.0.0/16</p><p>If we were doing this with a capture filter--</p><p>ip net 68.77.0.0/16</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '10, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1460" class="comments-container"><span id="1461"></span><div id="comment-1461" class="comment"><div id="post-1461-score" class="comment-score"></div><div class="comment-text"><p>Paul, thank you so much, so in your example the zeroes will act as wildcards? Is that correct? And is the subnet mask switch necessary?</p><p>Edit: I figured it out. I had actually typed the IP Address wrong when I put it in the filter field. Once I corrected it I found what I was looking for.</p><p>Again, Thank You</p></div><div id="comment-1461-info" class="comment-info"><span class="comment-age">(22 Dec '10, 16:41)</span> <span class="comment-user userinfo">Valek Hawke</span></div></div><span id="1462"></span><div id="comment-1462" class="comment"><div id="post-1462-score" class="comment-score"></div><div class="comment-text"><p>The 0's will act as a wildcard in conjunction with the /xx notation. Think of the /xx as the subnet mask. So if you understand subnet masks, the /xx, the xx represents the number of 1's in binary.</p><p>255.0.0.0=/8 (binary - 1111 1111 . 0000 0000 . 0000 0000 . 0000 0000)</p><p>255.255.0.0=/16 (binary - 1111 1111 . 1111 1111 . 0000 0000 . 0000 0000)</p><p>255.255.255.0=/24 (binary - 1111 1111 . 1111 1111 . 1111 1111 . 0000 0000)</p><p>255.255.255.128=/25 (binary - 1111 1111 . 1111 1111 . 1111 1111 . 1000 0000)</p></div><div id="comment-1462-info" class="comment-info"><span class="comment-age">(22 Dec '10, 17:02)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div></div><div id="comment-tools-1460" class="comment-tools"></div><div class="clear"></div><div id="comment-1460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


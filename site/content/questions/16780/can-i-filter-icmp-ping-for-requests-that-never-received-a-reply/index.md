+++
type = "question"
title = "Can i filter ICMP PING for requests that never received a Reply?"
description = '''I have a large capture with thousands of PINGS. I know at one time i saw Request timed out on the node i was monitoring, indicating it never received a reply for those PINGS. Can i use a Wireshark filter to find the Requests that never received a Reply?'''
date = "2012-12-11T13:20:00Z"
lastmod = "2015-03-09T07:36:00Z"
weight = 16780
keywords = [ "icmp", "filters" ]
aliases = [ "/questions/16780" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can i filter ICMP PING for requests that never received a Reply?](/questions/16780/can-i-filter-icmp-ping-for-requests-that-never-received-a-reply)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16780-score" class="post-score" title="current number of votes">0</div><span id="post-16780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large capture with thousands of PINGS. I know at one time i saw Request timed out on the node i was monitoring, indicating it never received a reply for those PINGS. Can i use a Wireshark filter to find the Requests that never received a Reply?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/296153260733c8ad390f33c23cdddaf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philliplew&#39;s gravatar image" /><p><span>philliplew</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philliplew has no accepted answers">0%</span></p></div></div><div id="comments-container-16780" class="comments-container"></div><div id="comment-tools-16780" class="comment-tools"></div><div class="clear"></div><div id="comment-16780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16781"></span>

<div id="answer-container-16781" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16781-score" class="post-score" title="current number of votes">3</div><span id="post-16781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="philliplew has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try using "not icmp.resp_in and icmp.type==8" which will give you all icmp requests where wireshark doesn't have the according response inside the capture file</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16781" class="comments-container"><span id="16783"></span><div id="comment-16783" class="comment"><div id="post-16783-score" class="comment-score"></div><div class="comment-text"><p>This worked great thank you. My only issue was i was Port Mirroring on my Switch 2 ports (source server and gateway) so i had two instances of each packet, 1 from each Switch port.</p><p>This meant Wireshark found 1 instance of every packet without a matching reply.</p><p>Luckily there were few enough packets after applying the above filter that i could manually go down the list and find the occurrences where there were 2.</p><p>Thanks again.</p></div><div id="comment-16783-info" class="comment-info"><span class="comment-age">(11 Dec '12, 13:55)</span> <span class="comment-user userinfo">philliplew</span></div></div><span id="16784"></span><div id="comment-16784" class="comment"><div id="post-16784-score" class="comment-score"></div><div class="comment-text"><p>(based on sequence number BE)</p></div><div id="comment-16784-info" class="comment-info"><span class="comment-age">(11 Dec '12, 13:56)</span> <span class="comment-user userinfo">philliplew</span></div></div><span id="16785"></span><div id="comment-16785" class="comment"><div id="post-16785-score" class="comment-score">1</div><div class="comment-text"><p>You could use editcap -d to remove duplicate packets before analyzing them. editcap is a command line tool that can be found in the wireshark installation directory.</p></div><div id="comment-16785-info" class="comment-info"><span class="comment-age">(11 Dec '12, 13:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="40382"></span><div id="comment-40382" class="comment"><div id="post-40382-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much¡ I was searching in a 201998 packets file and found out 313 w/o answer¡ All of this in 5 minutes thank you¡¡</p></div><div id="comment-40382-info" class="comment-info"><span class="comment-age">(09 Mar '15, 07:36)</span> <span class="comment-user userinfo">paristiz</span></div></div></div><div id="comment-tools-16781" class="comment-tools"></div><div class="clear"></div><div id="comment-16781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


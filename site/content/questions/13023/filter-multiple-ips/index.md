+++
type = "question"
title = "Filter multiple IPs"
description = '''I want to filter IPs on a .cap file , I use the command ip.addr == 123.456.789 but this only filters out one IP , I was wondering if there was a way to filter out multiple IPs ? thanks '''
date = "2012-07-26T09:04:00Z"
lastmod = "2012-07-26T12:28:00Z"
weight = 13023
keywords = [ "filter", "ip", "pcap", "tshark", "wireshark" ]
aliases = [ "/questions/13023" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filter multiple IPs](/questions/13023/filter-multiple-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13023-score" class="post-score" title="current number of votes">0</div><span id="post-13023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to filter IPs on a .cap file , I use the command ip.addr == 123.456.789 but this only filters out one IP , I was wondering if there was a way to filter out multiple IPs ? thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p><span>helloworld0722</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span></p></div></div><div id="comments-container-13023" class="comments-container"></div><div id="comment-tools-13023" class="comment-tools"></div><div class="clear"></div><div id="comment-13023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13027"></span>

<div id="answer-container-13027" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13027-score" class="post-score" title="current number of votes">3</div><span id="post-13027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="helloworld0722 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ip.addr==x.x.x.x || ip.addr==y.y.y.y || ip.addr=z.z.z.z</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13027" class="comments-container"><span id="13028"></span><div id="comment-13028" class="comment"><div id="post-13028-score" class="comment-score"></div><div class="comment-text"><p>It works ,thanks</p></div><div id="comment-13028-info" class="comment-info"><span class="comment-age">(26 Jul '12, 09:19)</span> <span class="comment-user userinfo">helloworld0722</span></div></div></div><div id="comment-tools-13027" class="comment-tools"></div><div class="clear"></div><div id="comment-13027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13032"></span>

<div id="answer-container-13032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13032-score" class="post-score" title="current number of votes">2</div><span id="post-13032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another way, if they are contiguous, is to use:-</p><p>ip.addr==10.10.10.10/24</p><p>This would display 10.10.10.1 - 10.10.10.254</p><p>This is also the way to filter on a subnet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-13032" class="comments-container"><span id="13034"></span><div id="comment-13034" class="comment"><div id="post-13034-score" class="comment-score"></div><div class="comment-text"><p>Ok thank you !</p></div><div id="comment-13034-info" class="comment-info"><span class="comment-age">(26 Jul '12, 12:28)</span> <span class="comment-user userinfo">helloworld0722</span></div></div></div><div id="comment-tools-13032" class="comment-tools"></div><div class="clear"></div><div id="comment-13032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


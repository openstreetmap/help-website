+++
type = "question"
title = "count number of submit_sm counts per second"
description = '''Hi all, I have been using wireshark for quite some time..However i am stuck at a place where the requirement is to count the number of Submit_sm packets(SMPP) per second from a tcpdump of 1 hour(30min,15min) to know the TPS(Transactions per second) at which my application is hitting the SMSC. Please...'''
date = "2013-09-14T07:17:00Z"
lastmod = "2013-09-14T19:59:00Z"
weight = 24679
keywords = [ "smpp" ]
aliases = [ "/questions/24679" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [count number of submit\_sm counts per second](/questions/24679/count-number-of-submit_sm-counts-per-second)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24679-score" class="post-score" title="current number of votes">0</div><span id="post-24679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have been using wireshark for quite some time..However i am stuck at a place where the requirement is to count the number of Submit_sm packets(SMPP) per second from a tcpdump of 1 hour(30min,15min) to know the TPS(Transactions per second) at which my application is hitting the SMSC. Please suggest me if there is a way out</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/0d0b7e3a100106a49580ffdc6954b3fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harish&#39;s gravatar image" /><p><span>harish</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harish has no accepted answers">0%</span></p></div></div><div id="comments-container-24679" class="comments-container"></div><div id="comment-tools-24679" class="comment-tools"></div><div class="clear"></div><div id="comment-24679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24693"></span>

<div id="answer-container-24693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24693-score" class="post-score" title="current number of votes">0</div><span id="post-24693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark and a script or Excel.</p><blockquote><p>tshark -nr input.pcap -R "smpp.command_id == 0x80000004" -T fields -E header=y -E separator=; -e frame.time_relative -e frame.number</p></blockquote><p>Then use that output and process it with a script (perl, python, whatever) or with Excel to calculate the number of <strong>submit_sm</strong> packtes per second.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24693" class="comments-container"><span id="24700"></span><div id="comment-24700" class="comment"><div id="post-24700-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your respnse..Will give a try and let u know the result</p></div><div id="comment-24700-info" class="comment-info"><span class="comment-age">(14 Sep '13, 19:59)</span> <span class="comment-user userinfo">harish</span></div></div></div><div id="comment-tools-24693" class="comment-tools"></div><div class="clear"></div><div id="comment-24693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


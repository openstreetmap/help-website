+++
type = "question"
title = "SGsAP-MM-INFORMATION-REQUEST showing extraneous data."
description = '''Hello,  I am using wireshark Version 1.10.1 (SVN Rev 50926 from /trunk-1.10). I used wireshark to capture SGsAP-MM-INFORMATION-REQUEST message with following values: MM information IE length 5, Protocol discriminator 8, MM Information message type 49, Network Daylight Saving Time 2. But wireshark di...'''
date = "2013-09-02T22:12:00Z"
lastmod = "2013-09-03T00:33:00Z"
weight = 24292
keywords = [ "sgsap", "data", "extraneous", "lte" ]
aliases = [ "/questions/24292" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SGsAP-MM-INFORMATION-REQUEST showing extraneous data.](/questions/24292/sgsap-mm-information-request-showing-extraneous-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24292-score" class="post-score" title="current number of votes">0</div><span id="post-24292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using wireshark Version 1.10.1 (SVN Rev 50926 from /trunk-1.10). I used wireshark to capture SGsAP-MM-INFORMATION-REQUEST message with following values: MM information IE length 5, Protocol discriminator 8, MM Information message type 49, Network Daylight Saving Time 2. But wireshark displayed it as an extraneous data, though by looking at the hex values, IE seems to be in correct order with proper value. I have uploaded capture file, you can get it here: <a href="http://goo.gl/LLghjo.">http://goo.gl/LLghjo.</a> Please help in solving the issue.</p><p>Thanks, Rahul Kumar Bhadani, LTE Software Engineer</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sgsap" rel="tag" title="see questions tagged &#39;sgsap&#39;">sgsap</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-extraneous" rel="tag" title="see questions tagged &#39;extraneous&#39;">extraneous</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '13, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/a2465250a1af67f8fc203bf577256b5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahul%20Salvatore%20Bhadani&#39;s gravatar image" /><p><span>Rahul Salvat...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahul Salvatore Bhadani has no accepted answers">0%</span></p></div></div><div id="comments-container-24292" class="comments-container"></div><div id="comment-tools-24292" class="comment-tools"></div><div class="clear"></div><div id="comment-24292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24293"></span>

<div id="answer-container-24293" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24293-score" class="post-score" title="current number of votes">1</div><span id="post-24293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rahul Salvatore Bhadani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>the encoding of the MM Information element is incorrect. According to 3GPP 29.118 chapter 9.4.12 and 29.018 chapter 18.4.16:</p><p>"This field is composed of one or more of the information elements of the MM information message as defined in 3GPP TS 24.008 [11], excluding the Protocol discriminator, Skip indicator and Message type. This field includes the IEI and length indicator of the other information elements".</p><p>So the IE should be coded instead as: 17 02 49 02</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '13, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-24293" class="comments-container"><span id="24298"></span><div id="comment-24298" class="comment"><div id="post-24298-score" class="comment-score"></div><div class="comment-text"><p>Thanks Pascal.</p></div><div id="comment-24298-info" class="comment-info"><span class="comment-age">(03 Sep '13, 00:33)</span> <span class="comment-user userinfo">Rahul Salvat...</span></div></div></div><div id="comment-tools-24293" class="comment-tools"></div><div class="clear"></div><div id="comment-24293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "tcp segment of a reassembled PDU"
description = '''In the captured packets(by wireshark),there are a lot of tcp segment of a reassembled PDU.the packet have data,but if i want export the packet out in a text file, in the text file i can not see the data?'''
date = "2012-05-07T06:09:00Z"
lastmod = "2012-05-07T19:00:00Z"
weight = 10727
keywords = [ "tcp-segment" ]
aliases = [ "/questions/10727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp segment of a reassembled PDU](/questions/10727/tcp-segment-of-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10727-score" class="post-score" title="current number of votes">0</div><span id="post-10727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the captured packets(by wireshark),there are a lot of tcp segment of a reassembled PDU.the packet have data,but if i want export the packet out in a text file, in the text file i can not see the data?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-segment" rel="tag" title="see questions tagged &#39;tcp-segment&#39;">tcp-segment</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/feb2695b239215e2418903e11af7035f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yizhibi&#39;s gravatar image" /><p><span>yizhibi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yizhibi has no accepted answers">0%</span></p></div></div><div id="comments-container-10727" class="comments-container"></div><div id="comment-tools-10727" class="comment-tools"></div><div class="clear"></div><div id="comment-10727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10728"></span>

<div id="answer-container-10728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10728-score" class="post-score" title="current number of votes">1</div><span id="post-10728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can disable "Allow subdissector to reassemble TCP streams" in the TCP protocol preferences to prevent Wireshark to do reassembly at the TCP level.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10728" class="comments-container"><span id="10760"></span><div id="comment-10760" class="comment"><div id="post-10760-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer!If I disable this option,I can not get the reassembled data!I want to get every TCP segment when I export the packet out to the text file.What should I do?</p></div><div id="comment-10760-info" class="comment-info"><span class="comment-age">(07 May '12, 19:00)</span> <span class="comment-user userinfo">yizhibi</span></div></div></div><div id="comment-tools-10728" class="comment-tools"></div><div class="clear"></div><div id="comment-10728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


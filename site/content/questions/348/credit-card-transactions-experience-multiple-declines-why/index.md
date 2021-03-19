+++
type = "question"
title = "Credit card transactions experience multiple declines. Why?"
description = '''We have a internal site at a golf course. They submit credit card transactions to an credit card firm at a site on the internet. They get multiple declines on credit cards many times each day before the transaction goes through. We, in the network support unit, have been tasked with investigating an...'''
date = "2010-09-28T11:39:00Z"
lastmod = "2010-09-29T15:51:00Z"
weight = 348
keywords = [ "rst", "credit-card", "declines" ]
aliases = [ "/questions/348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Credit card transactions experience multiple declines. Why?](/questions/348/credit-card-transactions-experience-multiple-declines-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-348-score" class="post-score" title="current number of votes">0</div><span id="post-348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a internal site at a golf course. They submit credit card transactions to an credit card firm at a site on the internet. They get multiple declines on credit cards many times each day before the transaction goes through.</p><p>We, in the network support unit, have been tasked with investigating and solving this issue. We captured traffic from the site to the credit card server on the outside of our firewall. We see the golf course host issue a SYN to begin the session, after several seconds it issues another SYN. The credit card server replies with SYN,ACK. The golf course host then issues an RST which consitutes a "decline" of the credit card. This occrs from once to 15 or more times before the transaction goes through.</p><p>I ran a test from another host issuing a TCP/443 connect to the credit card server every second for 1 day. 94% of the connects occurred in less than 100 millisec. The golf course host sees much longer delays, on the order of 3-10 seconds. I have a 58-packet Wireshark trace of this behaviour.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-credit-card" rel="tag" title="see questions tagged &#39;credit-card&#39;">credit-card</span> <span class="post-tag tag-link-declines" rel="tag" title="see questions tagged &#39;declines&#39;">declines</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '10, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/ddef9df115118ff5828188edcce5de5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AbeFroman&#39;s gravatar image" /><p><span>AbeFroman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AbeFroman has no accepted answers">0%</span></p></div></div><div id="comments-container-348" class="comments-container"></div><div id="comment-tools-348" class="comment-tools"></div><div class="clear"></div><div id="comment-348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="349"></span>

<div id="answer-container-349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-349-score" class="post-score" title="current number of votes">0</div><span id="post-349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First thing I'd look for is Sequence/ Acknowledgement number mismatches or TCP source/destination packet mismatches in the SYN/ACK. These would cause the TCP stack on the host initiating the socket to issue a RST.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '10, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/e458b44fd60b4064eb73fc42e67b3897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grossman&#39;s gravatar image" /><p><span>grossman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grossman has no accepted answers">0%</span></p></div></div><div id="comments-container-349" class="comments-container"><span id="350"></span><div id="comment-350" class="comment"><div id="post-350-score" class="comment-score"></div><div class="comment-text"><p>The problem seems to have more to do with the delays in the response of the credit card host. The golf course host is very time sensitive. The question is why it sees delays from the credit card host by another host on our network does not.</p></div><div id="comment-350-info" class="comment-info"><span class="comment-age">(28 Sep '10, 13:29)</span> <span class="comment-user userinfo">AbeFroman</span></div></div><span id="368"></span><div id="comment-368" class="comment"><div id="post-368-score" class="comment-score"></div><div class="comment-text"><p>lots of possible reasons. My default question always is "do they have sort sort device that is doing packet priority queues"? I have seen so called "WAN accelerators" and "traffic shapers" to keep packets up to 10 seconds before actually forwarding them. In your case I would try to find out exactly which devices are between your own network and the credit card host, and then compare that to what devices are in the route from the golf course to the credit card host. If there's nothing special (like mentioned shapers etc.) you need to find out if there are devices doing Quality of Service etc.</p></div><div id="comment-368-info" class="comment-info"><span class="comment-age">(29 Sep '10, 15:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-349" class="comment-tools"></div><div class="clear"></div><div id="comment-349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


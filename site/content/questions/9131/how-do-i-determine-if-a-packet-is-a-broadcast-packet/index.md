+++
type = "question"
title = "How do I determine if a packet is a broadcast packet?"
description = '''I know nothing about networking. I was asked to find a percentage of all packets that are broadcast packets from a capture I did. Can someone tell me how to do that please? '''
date = "2012-02-19T12:58:00Z"
lastmod = "2012-02-19T13:35:00Z"
weight = 9131
keywords = [ "broadcast", "packets", "analysis" ]
aliases = [ "/questions/9131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I determine if a packet is a broadcast packet?](/questions/9131/how-do-i-determine-if-a-packet-is-a-broadcast-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9131-score" class="post-score" title="current number of votes">0</div><span id="post-9131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know nothing about networking. I was asked to find a percentage of all packets that are broadcast packets from a capture I did. Can someone tell me how to do that please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '12, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/a3db010ac66d0db9efa2f8296a9cf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sssddd&#39;s gravatar image" /><p><span>sssddd</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sssddd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '12, 09:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9131" class="comments-container"></div><div id="comment-tools-9131" class="comment-tools"></div><div class="clear"></div><div id="comment-9131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9134"></span>

<div id="answer-container-9134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9134-score" class="post-score" title="current number of votes">1</div><span id="post-9134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you might want to look for packets that have either a MAC address of FF:FF:FF:FF:FF:FF or an IP address of 255.255.255.255 - but that might not include all broadcast messages, because for that you would need to know all subnets and subnets masks to be able to determine what the broadcast address of a subnet is. For example 172.16.0.255 could be a broadcast if the network is 172.16.0.0/24, but if it is 172.16.0.0/16 it isn't.</p><p>By the way, this looks like a lot of questions coming from some sort of homework assignment, so if that is the case I would advise you to study and find the answers for yourself ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '12, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9134" class="comments-container"></div><div id="comment-tools-9134" class="comment-tools"></div><div class="clear"></div><div id="comment-9134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


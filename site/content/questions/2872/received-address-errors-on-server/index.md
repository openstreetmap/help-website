+++
type = "question"
title = "Received Address Errors on server"
description = '''I have a server that is continually incrementing Received Address Errors. This is seen when using netstat -s. I have captures of the traffic but I am not sure how to go about displaying these errors in Wireshark or if that is possible. I tried using the following filter with no success: ipmi.tr04.rx...'''
date = "2011-03-16T10:54:00Z"
lastmod = "2011-03-17T06:03:00Z"
weight = 2872
keywords = [ "received", "errors", "address" ]
aliases = [ "/questions/2872" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Received Address Errors on server](/questions/2872/received-address-errors-on-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2872-score" class="post-score" title="current number of votes">1</div><span id="post-2872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a server that is continually incrementing Received Address Errors. This is seen when using netstat -s. I have captures of the traffic but I am not sure how to go about displaying these errors in Wireshark or if that is possible. I tried using the following filter with no success:</p><p>ipmi.tr04.rx_ipaddr_err</p><p>Anyone got any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-received" rel="tag" title="see questions tagged &#39;received&#39;">received</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '11, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/ee9eca5655ddca18749e71ed013732d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom&#39;s gravatar image" /><p><span>Tom</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom has no accepted answers">0%</span></p></div></div><div id="comments-container-2872" class="comments-container"></div><div id="comment-tools-2872" class="comment-tools"></div><div class="clear"></div><div id="comment-2872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2898"></span>

<div id="answer-container-2898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2898-score" class="post-score" title="current number of votes">1</div><span id="post-2898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may be seeing those packets an not realize it. Here's is IBM's definition for what NetStat is showing you.</p><blockquote><p>Datagrams Received Address Errors The number of input datagrams discarded because the IP address in their IP header destination field was not a valid address to be received at this entity. This count includes addresses that are not valid (for example, 0.0 0.0) and addresses for classes that are not supported (such as Class E). For entities that are not IP gateways and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address. Valid values are positive integers in the range 0 to 2147483647 and can include the use of the <em>AVG,</em> MIN, <em>MAX, or</em> SUM functions. For example, to express 52 for the number of IP datagrams that are discarded because of address errors, enter 52.</p></blockquote><p>There could be quite a few things causing this based on that first sentence in the definition.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2898" class="comments-container"></div><div id="comment-tools-2898" class="comment-tools"></div><div class="clear"></div><div id="comment-2898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


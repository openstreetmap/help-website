+++
type = "question"
title = "Why is there difference between MTU size and packet size in wireshark?"
description = '''My host machine is ubuntu and guest machine is windows 7. I&#x27;m generating traffic on windows 7 and capturing its traffic in the middle on ubuntu with wireshark. Both host and guest machines&#x27; MTU is 1500 bytes, but i see no packet with size more than 1430 bytes in wireshark. 1430 bytes is for (applica...'''
date = "2016-01-20T14:51:00Z"
lastmod = "2016-01-30T14:34:00Z"
weight = 49415
keywords = [ "mtu", "wireshark" ]
aliases = [ "/questions/49415" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is there difference between MTU size and packet size in wireshark?](/questions/49415/why-is-there-difference-between-mtu-size-and-packet-size-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49415-score" class="post-score" title="current number of votes">0</div><span id="post-49415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My host machine is ubuntu and guest machine is windows 7.</p><p>I'm generating traffic on windows 7 and capturing its traffic in the middle on ubuntu with wireshark.</p><p>Both host and guest machines' MTU is 1500 bytes, but i see no packet with size more than 1430 bytes in wireshark.</p><p>1430 bytes is for (application data + tcp and ip headers) and the size on wire is 1444 bytes.</p><p>My question is that why the packets don't have the size of 1500 considering (application data + tcp and ip headers) ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '16, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/2ed11d7d9c40141ad366b70bde2704db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amins&#39;s gravatar image" /><p><span>Amins</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amins has no accepted answers">0%</span></p></div></div><div id="comments-container-49415" class="comments-container"><span id="49418"></span><div id="comment-49418" class="comment"><div id="post-49418-score" class="comment-score"></div><div class="comment-text"><p>What's the MSS in the TCP SYN packets? Is one of them less than 1460?</p></div><div id="comment-49418-info" class="comment-info"><span class="comment-age">(20 Jan '16, 17:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="49422"></span><div id="comment-49422" class="comment"><div id="post-49422-score" class="comment-score"></div><div class="comment-text"><p>The MSS in the syn packet is 1460 bytes but in the syn-ack packet, the MSS is 1390 bytes and i also see the size of 1390 bytes for layer application in my packets.</p></div><div id="comment-49422-info" class="comment-info"><span class="comment-age">(20 Jan '16, 18:46)</span> <span class="comment-user userinfo">Amins</span></div></div></div><div id="comment-tools-49415" class="comment-tools"></div><div class="clear"></div><div id="comment-49415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49425"></span>

<div id="answer-container-49425" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49425-score" class="post-score" title="current number of votes">2</div><span id="post-49425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the SYN-ACK packet has 1390 it means that the Server supports only an MTU of 1390 + 20 (standard TCP header size) + 20 (standard IPv4 header size) = 1430. So even if your machine supports 1460 (= MTU 1500) it will not utilize it, because it knows that the server cannot receive packets of that size. And the server will not send anything greater than 1430 because it's MTU doesn't allow it.</p><p>While the MSS in the SYN packets is not really a negotiation both nodes are wise to use the lower number as a maximum size for their segments to avoid "fragmentation needed" problems.</p><p>So if you wonder why the server uses an MTU of 1430 you need to check it's stack/interface setting. Somewhere it must have been configured that way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '16, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '16, 01:18</strong> </span></p></div></div><div id="comments-container-49425" class="comments-container"><span id="49646"></span><div id="comment-49646" class="comment"><div id="post-49646-score" class="comment-score">1</div><div class="comment-text"><p>Jaspers answer has inspired me to write the following article about the mtu and the mss:</p><p><a href="http://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/">http://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/</a></p></div><div id="comment-49646-info" class="comment-info"><span class="comment-age">(30 Jan '16, 14:34)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-49425" class="comment-tools"></div><div class="clear"></div><div id="comment-49425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


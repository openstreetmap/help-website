+++
type = "question"
title = "Packet Size 40 Bytes - IP 20Bytes and Segment 20 Bytes"
description = '''Jasper, I have another one - Are all Tflags SYN should have an option enabled?  IP header 20 Bytes and Segment &quot;SYN&quot; 20 Bytes - Is it normal to see a packet 40 Size packet ? '''
date = "2016-01-02T08:59:00Z"
lastmod = "2016-01-04T19:01:00Z"
weight = 48792
keywords = [ "tcpflags", "tcp" ]
aliases = [ "/questions/48792" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Size 40 Bytes - IP 20Bytes and Segment 20 Bytes](/questions/48792/packet-size-40-bytes-ip-20bytes-and-segment-20-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48792-score" class="post-score" title="current number of votes">0</div><span id="post-48792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Jasper,</p><p>I have another one - Are all Tflags SYN should have an option enabled? IP header 20 Bytes and Segment "SYN" 20 Bytes - Is it normal to see a packet 40 Size packet ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCP_SYN.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpflags" rel="tag" title="see questions tagged &#39;tcpflags&#39;">tcpflags</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '16, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/5902c771c9609c2fa34087def265627e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dgo%20Vrgs&#39;s gravatar image" /><p><span>Dgo Vrgs</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dgo Vrgs has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>02 Jan '16, 09:01</strong> </span></p></div></div><div id="comments-container-48792" class="comments-container"></div><div id="comment-tools-48792" class="comment-tools"></div><div class="clear"></div><div id="comment-48792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48797"></span>

<div id="answer-container-48797" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48797-score" class="post-score" title="current number of votes">0</div><span id="post-48797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>20 bytes IPv4 is normal, 20 bytes TCP is a very common size, too. But for a TCP packet with the SYN flag set you usually see bigger TCP headers these days. Reason for that is that TCP SYN packets now carry options like MSS, SACK permitted and Window Scaling. Older stacks may omit one or more of those, of course, and they still work, but having them is better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '16, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48797" class="comments-container"><span id="48856"></span><div id="comment-48856" class="comment"><div id="post-48856-score" class="comment-score"></div><div class="comment-text"><p>Jasper thanks for the confirmation. One of our customers is getting tons of TCP SYN flood lately each with different variations.</p></div><div id="comment-48856-info" class="comment-info"><span class="comment-age">(04 Jan '16, 19:01)</span> <span class="comment-user userinfo">Dgo Vrgs</span></div></div></div><div id="comment-tools-48797" class="comment-tools"></div><div class="clear"></div><div id="comment-48797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


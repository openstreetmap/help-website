+++
type = "question"
title = "network connection intermittently hangs at same byte"
description = '''my server randomly hangs during centos yum update. I changed my centos mirrors couple times thinking it was related with the other server but I still experience the same problem. Here is tcpdump from my server https://www.cloudshark.org/captures/773ec35205bb I tried downloading same file couple time...'''
date = "2017-07-07T15:01:00Z"
lastmod = "2017-07-08T14:24:00Z"
weight = 62609
keywords = [ "fragment", "reassembly", "error", "timeout", "overlaps" ]
aliases = [ "/questions/62609" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [network connection intermittently hangs at same byte](/questions/62609/network-connection-intermittently-hangs-at-same-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62609-score" class="post-score" title="current number of votes">0</div><span id="post-62609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>my server randomly hangs during centos yum update. I changed my centos mirrors couple times thinking it was related with the other server but I still experience the same problem. Here is tcpdump from my server <a href="https://www.cloudshark.org/captures/773ec35205bb">https://www.cloudshark.org/captures/773ec35205bb</a></p><p>I tried downloading same file couple times and it either gets stuck on 8,354,960 bytes or downloads whole file without the problem. I am having trouble understanding what is causing this.</p><p>Has anyone come across similar issue? I would appreciate if you could guide me where to start troubleshooting. I was thinking it could be faulty cable but its weird that it always hangs at same spot or never hangs at all...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span> <span class="post-tag tag-link-overlaps" rel="tag" title="see questions tagged &#39;overlaps&#39;">overlaps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '17, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/f51ec049afbab6feac78771488d91300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="igagnidz&#39;s gravatar image" /><p><span>igagnidz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="igagnidz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '17, 15:03</strong> </span></p></div></div><div id="comments-container-62609" class="comments-container"></div><div id="comment-tools-62609" class="comment-tools"></div><div class="clear"></div><div id="comment-62609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62612"></span>

<div id="answer-container-62612" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62612-score" class="post-score" title="current number of votes">0</div><span id="post-62612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="igagnidz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like something is blocking a very specific pattern, because your client is requesting a retransmission via DUP ACKs near the end of the connection and never receives anything, finally giving up after 8 seconds. Especially if the problem always happens on the same offset it could point to some security device causing this.</p><p>If I were you I'd try to download the file from another network, excluding the normal network path your packets are taking, just to check if the same thing happens.</p><p>You tagged your question with "error" and "overlaps", but I think those are not really happening - you captured on the local machine that is part of the problem, and a capture like that is heavily biased - you can tell by seeing</p><ul><li>incorrect TCP checksums - if those were real the packet would have been destroyed, causing massive retransmissions</li><li>large incoming packets &gt; 1518 bytes, indicating "receive offloading" happening (these are not jumbo frames, because your MSS is 1460)</li></ul><p>So the capture quality is simply not good, and you can ignore those "errors". In case you're interested: to get correct capture results, capture on SPAN or TAP with a dedicated capture machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '17, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62612" class="comments-container"><span id="62621"></span><div id="comment-62621" class="comment"><div id="post-62621-score" class="comment-score"></div><div class="comment-text"><p>Thank you <a href="https://ask.wireshark.org/users/145/jasper">@Jasper</a>. I will contact my ISP to see if they have some firewall on gateway that can cause this.</p></div><div id="comment-62621-info" class="comment-info"><span class="comment-age">(08 Jul '17, 14:24)</span> <span class="comment-user userinfo">igagnidz</span></div></div></div><div id="comment-tools-62612" class="comment-tools"></div><div class="clear"></div><div id="comment-62612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


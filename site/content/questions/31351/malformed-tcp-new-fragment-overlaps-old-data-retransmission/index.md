+++
type = "question"
title = "Malformed TCP - New Fragment overlaps old data (retransmission?)"
description = '''Please check the below error i am getting on wire shark Malformed TCP - New Fragment overlaps old data (retransmission?) Once this error occurs the connection get closed by the source host by sending the FIN packet.What is the importance of this error and how can it be minimized? Please let me know ...'''
date = "2014-04-01T09:10:00Z"
lastmod = "2015-03-18T23:22:00Z"
weight = 31351
keywords = [ "tcp" ]
aliases = [ "/questions/31351" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed TCP - New Fragment overlaps old data (retransmission?)](/questions/31351/malformed-tcp-new-fragment-overlaps-old-data-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31351-score" class="post-score" title="current number of votes">0</div><span id="post-31351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please check the below error i am getting on wire shark</p><p>Malformed TCP - New Fragment overlaps old data (retransmission?)</p><p>Once this error occurs the connection get closed by the source host by sending the FIN packet.What is the importance of this error and how can it be minimized?</p><p>Please let me know of any questions.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/e22dbfd5e19273ddbc4ca06908e51698?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viral&#39;s gravatar image" /><p><span>Viral</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viral has no accepted answers">0%</span></p></div></div><div id="comments-container-31351" class="comments-container"><span id="31354"></span><div id="comment-31354" class="comment"><div id="post-31354-score" class="comment-score"></div><div class="comment-text"><p>Can you upload a trace at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> so that we can take a look?</p></div><div id="comment-31354-info" class="comment-info"><span class="comment-age">(01 Apr '14, 09:20)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35185"></span><div id="comment-35185" class="comment"><div id="post-35185-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am facing the same error type. Unfortunately I cannot upload a sequence because of confidentiality. Is there any description explaining why this error type appears?</p><p>Thanks a lot in advance.</p><p>BR</p></div><div id="comment-35185-info" class="comment-info"><span class="comment-age">(05 Aug '14, 01:48)</span> <span class="comment-user userinfo">FoNs</span></div></div><span id="35187"></span><div id="comment-35187" class="comment"><div id="post-35187-score" class="comment-score"></div><div class="comment-text"><p>AFAIK it means that a retransmission for a packet was seen where both original and retransmission are in the trace, and do not contain the same payload content. Basically, the new segment in the retransmission overlaps the existing bytes with something else. It's up to the stack how to handle those situations, but I can guess that resetting the connection is a common reaction.</p></div><div id="comment-35187-info" class="comment-info"><span class="comment-age">(05 Aug '14, 02:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="40677"></span><div id="comment-40677" class="comment"><div id="post-40677-score" class="comment-score"></div><div class="comment-text"><p>i have got the same error with a particular page on the site when try to go to this page , " new fragment overlaps old data "</p><p>interstigly it works over my 4G network but not on wired ethernet network . ?? replies to <span class="__cf_email__" data-cfemail="92fbeaf7eae2fefde0f7e0d2f5fff3fbfebcf1fdff">[email protected]</span></p></div><div id="comment-40677-info" class="comment-info"><span class="comment-age">(18 Mar '15, 23:22)</span> <span class="comment-user userinfo">ixexplorer</span></div></div></div><div id="comment-tools-31351" class="comment-tools"></div><div class="clear"></div><div id="comment-31351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35188"></span>

<div id="answer-container-35188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35188-score" class="post-score" title="current number of votes">0</div><span id="post-35188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The error is emitted by the reassembly routines (in four places) when the received packets overlap in some way with the already received and reassembled data, thus they are perceived as (partial) retransmissions. See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/reassemble.c">epan/reassemble.c</a></p><p>For any specific case the capture is required to explain the actual problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35188" class="comments-container"></div><div id="comment-tools-35188" class="comment-tools"></div><div class="clear"></div><div id="comment-35188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


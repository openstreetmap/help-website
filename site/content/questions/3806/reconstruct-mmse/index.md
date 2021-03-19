+++
type = "question"
title = "Reconstruct mmse"
description = '''Hi When I provide wireshark with a pcap file containing packages of an mms where some of the packages are tcp-retransmissions, wireshark fails to assemble the mmse protocol. If I &quot;manually&quot; remove the retransmission tcp packages then wireshark works as expected and shows me the mmse protocol element...'''
date = "2011-04-29T01:50:00Z"
lastmod = "2011-04-29T09:22:00Z"
weight = 3806
keywords = [ "reconstruct", "mmse" ]
aliases = [ "/questions/3806" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reconstruct mmse](/questions/3806/reconstruct-mmse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3806-score" class="post-score" title="current number of votes">0</div><span id="post-3806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>When I provide wireshark with a pcap file containing packages of an mms where some of the packages are tcp-retransmissions, wireshark fails to assemble the mmse protocol. If I "manually" remove the retransmission tcp packages then wireshark works as expected and shows me the mmse protocol elements.</p><p>Is there a way to achive this without having to remove the retransmission tcp packages? Any ideas or help is much appreciated.</p><p>Best regards Trym</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reconstruct" rel="tag" title="see questions tagged &#39;reconstruct&#39;">reconstruct</span> <span class="post-tag tag-link-mmse" rel="tag" title="see questions tagged &#39;mmse&#39;">mmse</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/aa8d3f2ee5e74e820b84fccdec1ac97c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trym&#39;s gravatar image" /><p><span>Trym</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trym has no accepted answers">0%</span></p></div></div><div id="comments-container-3806" class="comments-container"></div><div id="comment-tools-3806" class="comment-tools"></div><div class="clear"></div><div id="comment-3806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3807"></span>

<div id="answer-container-3807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3807-score" class="post-score" title="current number of votes">1</div><span id="post-3807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There has been some work done in this area recently. I'm not sure whether that made it into 1.4.6 or 1.5.1 already. You could try an <a href="http://www.wireshark.org/download/automated/">automated build</a> to see if it solves this for you.</p><p>If it does not, could you <a href="https://bugs.wireshark.org/bugzilla/">file a bug report</a> and attach the capture file in which you encounter the problem so it can get fixed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '11, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3807" class="comments-container"><span id="3811"></span><div id="comment-3811" class="comment"><div id="post-3811-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your quick answer. Version 1.5.1 solved the problem for me.</p></div><div id="comment-3811-info" class="comment-info"><span class="comment-age">(29 Apr '11, 05:31)</span> <span class="comment-user userinfo">Trym</span></div></div><span id="3813"></span><div id="comment-3813" class="comment"><div id="post-3813-score" class="comment-score"></div><div class="comment-text"><p>That was (I think) fixed in rev 36304. I just scheduled that for inclusion in 1.4.7.</p></div><div id="comment-3813-info" class="comment-info"><span class="comment-age">(29 Apr '11, 09:22)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-3807" class="comment-tools"></div><div class="clear"></div><div id="comment-3807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


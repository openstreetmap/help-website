+++
type = "question"
title = "How do you an decode Ethernet Frame?"
description = '''For example: How would one decode the following ethernet frame?  00 26 b9 e8 7e f1 00 12 f2 21 da 00 08 00 45 00 05 dc e3 cd 20 10 35 06 25 eb 0a 0a 0a 02 c0 a8 01 03 c3 9e 0f 40 00 00 10 00 00 00 14 00 70 10 00 5c 59 99 00 00 02 04 05 b4 01 03 03 06 00 00 01 98 64 34 e8 90 84 98 20 12 18 19 04 85 8...'''
date = "2014-04-30T08:29:00Z"
lastmod = "2014-04-30T08:31:00Z"
weight = 32311
keywords = [ "ethernet", "frame", "packet" ]
aliases = [ "/questions/32311" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you an decode Ethernet Frame?](/questions/32311/how-do-you-an-decode-ethernet-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32311-score" class="post-score" title="current number of votes">0</div><span id="post-32311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example: How would one decode the following ethernet frame?</p><p>00 26 b9 e8 7e f1 00 12 f2 21 da 00 08 00 45 00 05 dc e3 cd 20 10 35 06 25 eb 0a 0a 0a 02 c0 a8 01 03 c3 9e 0f 40 00 00 10 00 00 00 14 00 70 10 00 5c 59 99 00 00 02 04 05 b4 01 03 03 06 00 00 01 98 64 34 e8 90 84 98 20 12 18 19 04 85 80 00<br />
</p><p>I know that the first 6 bytes are the MAC destination address : 00 26 b9 e8 7e f1 The next 6 bytes are the source MAX address : 00 12 f2 21 da 00 The next 2 bytes show the ethernet type : 08 00 The next 4 bytes are : 45 00...Ipv4... "5" the number of bytes in the header.. and "00" means there are no differentiated services.</p><p>What I don't know is what anything after that is or how to read it.</p><p>Anyone help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/29b4e3397022f45e3e06ceb7f5456847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharmon1&#39;s gravatar image" /><p><span>aharmon1</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharmon1 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-32311" class="comments-container"></div><div id="comment-tools-32311" class="comment-tools"></div><div class="clear"></div><div id="comment-32311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32312"></span>

<div id="answer-container-32312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32312-score" class="post-score" title="current number of votes">0</div><span id="post-32312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Uhm, try Wireshark? It decodes it for you?</p><p>You can select the decoded fields and see what by bytes are selected in the hex view, which is where the decode is based upon. Other than that you're probably going to read RFCs if you want to know how the protocols are structured in greater detail.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '14, 08:31</strong> </span></p></div></div><div id="comments-container-32312" class="comments-container"><span id="32313"></span><div id="comment-32313" class="comment"><div id="post-32313-score" class="comment-score"></div><div class="comment-text"><p>I know Wireshark does it for you but I want to learn how to read it without the use of Wireshark.</p></div><div id="comment-32313-info" class="comment-info"><span class="comment-age">(30 Apr '14, 08:30)</span> <span class="comment-user userinfo">aharmon1</span></div></div><span id="32314"></span><div id="comment-32314" class="comment"><div id="post-32314-score" class="comment-score"></div><div class="comment-text"><p>Ok, as I added in my edit: play with Wireshark, see what it decodes to what, and other than that, books and RFCs ;-)</p><p>E.g: <a href="http://www.ietf.org/rfc/rfc791.txt">http://www.ietf.org/rfc/rfc791.txt</a> Section 3.1</p></div><div id="comment-32314-info" class="comment-info"><span class="comment-age">(30 Apr '14, 08:31)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-32312" class="comment-tools"></div><div class="clear"></div><div id="comment-32312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "removing duplicate SIP messages"
description = '''I am using a trace file from a SIP network and it contains duplicate SIP messages because multiple trace points are picking up the same SIP message as it travels from one SIP entity to another. Its not possible to filter using VLANs or using the TTL field, as suggested in an older post.  From the &quot;T...'''
date = "2013-09-05T09:11:00Z"
lastmod = "2013-09-06T04:16:00Z"
weight = 24381
keywords = [ "duplicate", "sip" ]
aliases = [ "/questions/24381" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [removing duplicate SIP messages](/questions/24381/removing-duplicate-sip-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24381-score" class="post-score" title="current number of votes">0</div><span id="post-24381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a trace file from a SIP network and it contains duplicate SIP messages because multiple trace points are picking up the same SIP message as it travels from one SIP entity to another. Its not possible to filter using VLANs or using the TTL field, as suggested in an older post. From the "Telepony" tab, SIP option, Wireshark is able to tell me that there are 50 "resent" packets out of the total of 359 packets. Is there some way to filter out these duplicates?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/e1e7c1c756ff088909643d01d8aedaa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="irebo&#39;s gravatar image" /><p><span>irebo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="irebo has no accepted answers">0%</span></p></div></div><div id="comments-container-24381" class="comments-container"></div><div id="comment-tools-24381" class="comment-tools"></div><div class="clear"></div><div id="comment-24381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24406"></span>

<div id="answer-container-24406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24406-score" class="post-score" title="current number of votes">0</div><span id="post-24406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there some way to filter out these duplicates?</p></blockquote><p><a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> provides some options to remove duplicate frames. See the <a href="http://www.wireshark.org/docs/man-pages/editcap.html">man page of editcap</a>, options: -d, -D, -w.</p><p>If your editcap version does not provide those options, please upgrade to the latest release.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24406" class="comments-container"></div><div id="comment-tools-24406" class="comment-tools"></div><div class="clear"></div><div id="comment-24406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24417"></span>

<div id="answer-container-24417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24417-score" class="post-score" title="current number of votes">0</div><span id="post-24417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the frames identified by the SIP stats as 'resent', those frames should match the display filter 'sip.resend == 1', so you could try to filter these out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p><span>MartinM</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-24417" class="comments-container"></div><div id="comment-tools-24417" class="comment-tools"></div><div class="clear"></div><div id="comment-24417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


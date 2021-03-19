+++
type = "question"
title = "NBNS or LLMNR"
description = '''Is there a way to view what website was visited with either of these protocols?'''
date = "2013-11-25T16:16:00Z"
lastmod = "2013-11-29T06:27:00Z"
weight = 27368
keywords = [ "llmnr", "nbns" ]
aliases = [ "/questions/27368" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NBNS or LLMNR](/questions/27368/nbns-or-llmnr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27368-score" class="post-score" title="current number of votes">0</div><span id="post-27368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to view what website was visited with either of these protocols?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-llmnr" rel="tag" title="see questions tagged &#39;llmnr&#39;">llmnr</span> <span class="post-tag tag-link-nbns" rel="tag" title="see questions tagged &#39;nbns&#39;">nbns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/e9f275152d7fc32f8e59c4421b5e32f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brad6547884&#39;s gravatar image" /><p><span>Brad6547884</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brad6547884 has no accepted answers">0%</span></p></div></div><div id="comments-container-27368" class="comments-container"><span id="27542"></span><div id="comment-27542" class="comment"><div id="post-27542-score" class="comment-score"></div><div class="comment-text"><p>"view what website was visited with either of these protocols?" in what sense?</p><p>As per my comment below, there are a couple of different ways to interpret that, with different answers.</p></div><div id="comment-27542-info" class="comment-info"><span class="comment-age">(28 Nov '13, 13:53)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-27368" class="comment-tools"></div><div class="clear"></div><div id="comment-27368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27418"></span>

<div id="answer-container-27418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27418-score" class="post-score" title="current number of votes">0</div><span id="post-27418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to view what website was visited with either of these protocols?</p></blockquote><p>If a 'website' is something on the internet for you, then the answer is: NO, as you need DNS (in most environments) to resolve the name of a server on the internet.</p><p>Your systems may however resolve names of internal web sites with NBNS and/or LLMNR. In that case the answer is: YES</p><p>In either way, it would be better to look for HTTP traffic in the capture file, because just the fact that a system resolved the name for a system does not mean it also connected to it via HTTP.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27418" class="comments-container"><span id="27457"></span><div id="comment-27457" class="comment"><div id="post-27457-score" class="comment-score"></div><div class="comment-text"><p>And if you're specifically trying to see which Web sites are being "found" (in the sense of the host name in the URL being translated to an IP address) using NBNS or LLMNR rather than DNS, capture NBNS, LLMNR, DNS, <em>and</em> HTTP traffic, look at the capture, and see which type of name request preceded an HTTP connection.</p><p>(No, there's no simple automated way to do that; you'll probably have to examine the traffic manually.)</p><p>Note also that the name resolver might be caching the results of a name lookup, so there might not be <em>any</em> name lookup before the HTTP connection, in which case you'd have to hope that you captured whatever earlier name lookup mapped the name to an IP address.</p></div><div id="comment-27457-info" class="comment-info"><span class="comment-age">(26 Nov '13, 14:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="27458"></span><div id="comment-27458" class="comment"><div id="post-27458-score" class="comment-score"></div><div class="comment-text"><blockquote><p>hope that you captured whatever earlier name lookup</p></blockquote><p>or look at the Host: header of the HTTP request....</p></div><div id="comment-27458-info" class="comment-info"><span class="comment-age">(26 Nov '13, 16:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27459"></span><div id="comment-27459" class="comment"><div id="post-27459-score" class="comment-score"></div><div class="comment-text"><blockquote><p>or look at the Host: header of the HTTP request....</p></blockquote><p>But will that tell you which protocol was used when the system translated the host name in the Host: header to the IP address to which the request was sent?</p></div><div id="comment-27459-info" class="comment-info"><span class="comment-age">(26 Nov '13, 16:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="27460"></span><div id="comment-27460" class="comment"><div id="post-27460-score" class="comment-score"></div><div class="comment-text"><p>No, but the OP want's to know 'what website was <strong>visited</strong>', which can be answered by looking at the Host: header.</p></div><div id="comment-27460-info" class="comment-info"><span class="comment-age">(26 Nov '13, 16:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27541"></span><div id="comment-27541" class="comment"><div id="post-27541-score" class="comment-score"></div><div class="comment-text"><p>I guess it's a question of how to interpret "Is there a way to view what website was visited with either of these protocols?" I interpreted it as meaning "find out for which web sites the IP address was resolved with NBNS or LLMNR"; it sounds as if you're interpreting it as "given that a given Web site had its IP address resolved with NBNS or LLMNR, find out what Web site that was" (i.e., what its host name was).</p><p>Either interpretation could be correct. For the first interpretation, you'd need to watch traffic for those protocols; for the second interpretation, the Host: header (at least for HTTP 1.1) would suffice <em>even if the host had its IP address resolved with DNS</em>.</p></div><div id="comment-27541-info" class="comment-info"><span class="comment-age">(28 Nov '13, 13:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="27564"></span><div id="comment-27564" class="comment not_top_scorer"><div id="post-27564-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I guess it's a question of how to interpret ...</p></blockquote><p>I agree and I believe we will never know, as it seems that <span>@Brad6547884</span> lost interest in the questions he asked ....</p></div><div id="comment-27564-info" class="comment-info"><span class="comment-age">(29 Nov '13, 06:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27418" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-27418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


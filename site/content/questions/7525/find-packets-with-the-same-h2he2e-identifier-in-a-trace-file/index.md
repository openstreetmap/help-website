+++
type = "question"
title = "Find packets with the same h2h/e2e identifier in a trace file"
description = '''I have a trace file from the Diameter protocol. My goal is to find all packets (either Answers or Requests) with the same hop-by-hop/end-to-end identifier. This identifier is being given for several hours, and it is unique for each Request-Answer pair of packets during this period of time. I suspect...'''
date = "2011-11-21T00:31:00Z"
lastmod = "2014-04-04T08:41:00Z"
weight = 7525
keywords = [ "diameter", "hbh", "e2e" ]
aliases = [ "/questions/7525" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find packets with the same h2h/e2e identifier in a trace file](/questions/7525/find-packets-with-the-same-h2he2e-identifier-in-a-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7525-score" class="post-score" title="current number of votes">0</div><span id="post-7525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace file from the Diameter protocol. My goal is to find all packets (either Answers or Requests) with the same hop-by-hop/end-to-end identifier. This identifier is being given for several hours, and it is unique for each Request-Answer pair of packets during this period of time. I suspect that there are some Requests, which have the same identifier and are very close to each other in time.</p><p>Thanks in advance!</p><p>Nick</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-hbh" rel="tag" title="see questions tagged &#39;hbh&#39;">hbh</span> <span class="post-tag tag-link-e2e" rel="tag" title="see questions tagged &#39;e2e&#39;">e2e</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '11, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/b81980a966f9de5b8b746daab20dd3f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikolay&#39;s gravatar image" /><p><span>Nikolay</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikolay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '11, 15:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7525" class="comments-container"></div><div id="comment-tools-7525" class="comment-tools"></div><div class="clear"></div><div id="comment-7525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7541"></span>

<div id="answer-container-7541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7541-score" class="post-score" title="current number of votes">4</div><span id="post-7541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To find all Diameter packets with a given hop-by-hop identifier, use the display filter <code>diameter.hopbyhopid =</code> <em>identifier-value</em>, where <em>identifier-value</em> is the value of the identifier. To find all Diameter packets with a given end-to-end identifier, use the display filter <code>diameter.endtoendid =</code> <em>identifier-value</em>, where <em>identifier-value</em> is the value of the identifier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '11, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7541" class="comments-container"><span id="7563"></span><div id="comment-7563" class="comment"><div id="post-7563-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but how can I find all the packets with the same identifiers - hop-by-hop, end-to-end or hbh/e2e combination?</p></div><div id="comment-7563-info" class="comment-info"><span class="comment-age">(22 Nov '11, 13:34)</span> <span class="comment-user userinfo">Nikolay</span></div></div><span id="7564"></span><div id="comment-7564" class="comment"><div id="post-7564-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "with the same identifiers"? What is the same as what?</p></div><div id="comment-7564-info" class="comment-info"><span class="comment-age">(22 Nov '11, 14:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7575"></span><div id="comment-7575" class="comment"><div id="post-7575-score" class="comment-score"></div><div class="comment-text"><p>I mean the different packets with the same identifier-value. I understand that this would be a mistake, but my goal is to find these mistaken packets, which are actually different, but have the same value of hop-by-hop or end-to-end identifiers. Do you follow me?</p></div><div id="comment-7575-info" class="comment-info"><span class="comment-age">(23 Nov '11, 00:09)</span> <span class="comment-user userinfo">Nikolay</span></div></div><span id="20737"></span><div id="comment-20737" class="comment"><div id="post-20737-score" class="comment-score"></div><div class="comment-text"><p>the answer is clear in the Guy Harrys comment. if you set the filter with hop by hop you will get 1 line. If you set the filter with end-to-end you will get the pair.</p></div><div id="comment-20737-info" class="comment-info"><span class="comment-age">(23 Apr '13, 08:22)</span> <span class="comment-user userinfo">fachav2</span></div></div></div><div id="comment-tools-7541" class="comment-tools"></div><div class="clear"></div><div id="comment-7541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31514"></span>

<div id="answer-container-31514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31514-score" class="post-score" title="current number of votes">0</div><span id="post-31514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>simply write a unix script,</p><p>1-in first step extract hop-by-hop id / end-to-end-id 2- in second step apply it as a read filter</p><p>for extraction use awk/sed etc. it would help. did in my case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '14, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-31514" class="comments-container"></div><div id="comment-tools-31514" class="comment-tools"></div><div class="clear"></div><div id="comment-31514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


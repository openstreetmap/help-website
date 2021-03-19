+++
type = "question"
title = "high tcp.time_delta on HTTP POST.."
description = '''Hey folks, new here, looking for a little guidance from you seasoned vets.. Let me start by saying that on page 80 of Ms Chappell&#x27;s &quot;Troubleshooting With Wireshark&quot; book, she explains some common areas where we would see normal delays. Specifically, GET requests. I&#x27;m analyzing a capture that has som...'''
date = "2014-10-03T09:22:00Z"
lastmod = "2014-10-03T11:54:00Z"
weight = 36822
keywords = [ "post", "tcp.time_delta", "http", "asp" ]
aliases = [ "/questions/36822" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [high tcp.time\_delta on HTTP POST..](/questions/36822/high-tcptime_delta-on-http-post)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36822-score" class="post-score" title="current number of votes">0</div><span id="post-36822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey folks, new here, looking for a little guidance from you seasoned vets..</p><p>Let me start by saying that on page 80 of Ms Chappell's "Troubleshooting With Wireshark" book, she explains some common areas where we would see normal delays. Specifically, GET requests.</p><p>I'm analyzing a capture that has some web traffic in it, and I have some VERY HIGH TCP delta times on some HTTP POST events going from workstation to server (source is workstation, dest is server).</p><p>My question is.. are HTTP POSTs the same as GETs in that there can be background delays that may not be the cause of the end user's issue? Or would a delay in a POST action directly affect their experience?</p><p>If I knew more about the application in question, I might be able to answer that myself, but I'm not a web guy, and the support staff that works with this application is unavailable.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-tcp.time_delta" rel="tag" title="see questions tagged &#39;tcp.time_delta&#39;">tcp.time_delta</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-asp" rel="tag" title="see questions tagged &#39;asp&#39;">asp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/eab06dcd69504dc40c68cf8fa84a390e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robotfish1911&#39;s gravatar image" /><p><span>robotfish1911</span><br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robotfish1911 has no accepted answers">0%</span></p></div></div><div id="comments-container-36822" class="comments-container"></div><div id="comment-tools-36822" class="comment-tools"></div><div class="clear"></div><div id="comment-36822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36823"></span>

<div id="answer-container-36823" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36823-score" class="post-score" title="current number of votes">0</div><span id="post-36823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="robotfish1911 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>GET, POST and other HTTP actions are initiated by the browser. Which means that when it takes a while for the next action to be sent, the user simply read the page or did other things.</p><p>What you need to look for is how fast stuff is coming back from the server when those actions are sent, so look for the delta time between the GET/POST and the start of the content. HTTP is request/response, so the server has to wait for the user to ask for something.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36823" class="comments-container"><span id="36824"></span><div id="comment-36824" class="comment"><div id="post-36824-score" class="comment-score"></div><div class="comment-text"><p>Got it, thank you</p></div><div id="comment-36824-info" class="comment-info"><span class="comment-age">(03 Oct '14, 11:54)</span> <span class="comment-user userinfo">robotfish1911</span></div></div></div><div id="comment-tools-36823" class="comment-tools"></div><div class="clear"></div><div id="comment-36823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


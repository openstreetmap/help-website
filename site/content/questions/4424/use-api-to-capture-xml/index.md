+++
type = "question"
title = "use API to capture XML"
description = '''I am developing an application to send a query from one database to another. I am wondering if it is possible to use an API to capture XML messages. '''
date = "2011-06-07T06:27:00Z"
lastmod = "2011-06-07T07:42:00Z"
weight = 4424
keywords = [ "query" ]
aliases = [ "/questions/4424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [use API to capture XML](/questions/4424/use-api-to-capture-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4424-score" class="post-score" title="current number of votes">0</div><span id="post-4424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing an application to send a query from one database to another. I am wondering if it is possible to use an API to capture XML messages.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '11, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/7fcd72cbf41525f2bf00623efa69b5d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbands2&#39;s gravatar image" /><p><span>mbands2</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbands2 has no accepted answers">0%</span></p></div></div><div id="comments-container-4424" class="comments-container"></div><div id="comment-tools-4424" class="comment-tools"></div><div class="clear"></div><div id="comment-4424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4425"></span>

<div id="answer-container-4425" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4425-score" class="post-score" title="current number of votes">0</div><span id="post-4425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why do you want to use an API? I would use Wireshark to capture the communication and then look through the decode. If your XML messages are plain ASCII you should also be able to spot it when using "Follow TCP stream" on a packet of the communication flow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4425" class="comments-container"><span id="4426"></span><div id="comment-4426" class="comment"><div id="post-4426-score" class="comment-score"></div><div class="comment-text"><p>I am trying to show it in a user-friendly way to prove that there is actually information going across. I am afraid that your suggestion might not be user-friendly enough.</p><p><em>converted to comment due to the Q&amp;A nature of this forum</em></p></div><div id="comment-4426-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:39)</span> <span class="comment-user userinfo">mbands2</span></div></div><span id="4429"></span><div id="comment-4429" class="comment"><div id="post-4429-score" class="comment-score"></div><div class="comment-text"><p>Correct, it's not exactly user friendly, but if you're required to prove that your solution works its the most exact way to do that. Why do you need it to be "user friendly"? Proving that something works usually doesn't require a user to check.</p></div><div id="comment-4429-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4430"></span><div id="comment-4430" class="comment"><div id="post-4430-score" class="comment-score"></div><div class="comment-text"><p>I need to display it in a way that non-computer savy people would be able to understand it, if that makes sense?</p></div><div id="comment-4430-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:56)</span> <span class="comment-user userinfo">mbands2</span></div></div><span id="4432"></span><div id="comment-4432" class="comment"><div id="post-4432-score" class="comment-score"></div><div class="comment-text"><p>Okay, for that you'd probably need to write a program that uses WinPCAP/LibPCAP and parses the incoming frames for the XML structures you're sending. That way you can present it whichever way you think is best for your users. Unfortunately I haven't written a progam like that myself yet, so my expertise in that area is slim at best. Maybe someone of the developers around here can help you out.</p></div><div id="comment-4432-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4435"></span><div id="comment-4435" class="comment"><div id="post-4435-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-4435-info" class="comment-info"><span class="comment-age">(07 Jun '11, 07:26)</span> <span class="comment-user userinfo">mbands2</span></div></div><span id="4436"></span><div id="comment-4436" class="comment not_top_scorer"><div id="post-4436-score" class="comment-score"></div><div class="comment-text"><p>Do you know anything about JPcap? it is a java library for capturing and sending network packets. I'm not sure if it is customizable.</p></div><div id="comment-4436-info" class="comment-info"><span class="comment-age">(07 Jun '11, 07:42)</span> <span class="comment-user userinfo">mbands2</span></div></div></div><div id="comment-tools-4425" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-4425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


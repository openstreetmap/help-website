+++
type = "question"
title = "Embedded image serial or parallel?"
description = '''here is a test site i&#x27;m using to learn wireshark: bitly.com/qPLPXp I was asked whether my web browser downloads the images download in serial, or in parallel?  first image is hosted by that website itself &amp;amp; the second image is on another server. how can I tell if they were downloaded in serial o...'''
date = "2012-10-31T15:47:00Z"
lastmod = "2014-01-02T14:58:00Z"
weight = 15436
keywords = [ "serial", "parallel" ]
aliases = [ "/questions/15436" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Embedded image serial or parallel?](/questions/15436/embedded-image-serial-or-parallel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15436-score" class="post-score" title="current number of votes">0</div><span id="post-15436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>here is a test site i'm using to learn wireshark: <a href="http://bitly.com/qPLPXp">bitly.com/qPLPXp</a></p><p>I was asked whether my web browser downloads the images download in serial, or in parallel?</p><p>first image is hosted by that website itself &amp; the second image is on another server.</p><p>how can I tell if they were downloaded in serial or parallel?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-serial" rel="tag" title="see questions tagged &#39;serial&#39;">serial</span> <span class="post-tag tag-link-parallel" rel="tag" title="see questions tagged &#39;parallel&#39;">parallel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '12, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/25bfab3fbdcc85732922e9d5de11cae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smc20&#39;s gravatar image" /><p><span>smc20</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smc20 has no accepted answers">0%</span></p></div></div><div id="comments-container-15436" class="comments-container"></div><div id="comment-tools-15436" class="comment-tools"></div><div class="clear"></div><div id="comment-15436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15444"></span>

<div id="answer-container-15444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15444-score" class="post-score" title="current number of votes">1</div><span id="post-15444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper would say "Nice, another homework assignment". Rather than just give you the answer, I'll give you some things to think about that should lead you to the answer.</p><ul><li>Do you know what protocol is used to download the images?</li><li>Do you know what "commands" the protocol uses to download a specific image?</li><li>Do you know how to determine the command has completed?</li><li>Can you see those commands in your Wireshark capture of the browser downloading the page?</li><li>Are those commands issued sequentially, i.e. is the 2nd command only sent after the first one has completed?</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15444" class="comments-container"><span id="28529"></span><div id="comment-28529" class="comment"><div id="post-28529-score" class="comment-score"></div><div class="comment-text"><p>what kind of answer is that? Answering a question with more questions?... better do not reply</p></div><div id="comment-28529-info" class="comment-info"><span class="comment-age">(02 Jan '14, 13:30)</span> <span class="comment-user userinfo">quitoart</span></div></div></div><div id="comment-tools-15444" class="comment-tools"></div><div class="clear"></div><div id="comment-15444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15452"></span>

<div id="answer-container-15452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15452-score" class="post-score" title="current number of votes">0</div><span id="post-15452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I was asked whether my web browser downloads the images download in serial, or in parallel?</p></blockquote><p>One <a href="http://bit.ly/ja5jN">answer to the question</a>.</p><p>what did you try to figure out what happened at the network level.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '12, 14:49</strong> </span></p></div></div><div id="comments-container-15452" class="comments-container"></div><div id="comment-tools-15452" class="comment-tools"></div><div class="clear"></div><div id="comment-15452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28530"></span>

<div id="answer-container-28530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28530-score" class="post-score" title="current number of votes">0</div><span id="post-28530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Can you tell whether your browser downl oaded the two images serially, or whether they were downloaded from th e two web sites in parallel? Explain. Answer: By checking the TCP ports we can see if our files were dow nloaded serially or in parallel. In this case the 2 images were transmitted over 2 TCP connections therefore they were downloaded serially.</li></ol><p>link <a href="http://inst.eecs.berkeley.edu/~ee122/sp06/Homeworks/Ethereal_HTTP_Solution.pdf">http://inst.eecs.berkeley.edu/~ee122/sp06/Homeworks/Ethereal_HTTP_Solution.pdf</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '14, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/943b277cd7fd65f7596780a1cbccb19a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quitoart&#39;s gravatar image" /><p><span>quitoart</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quitoart has no accepted answers">0%</span></p></div></div><div id="comments-container-28530" class="comments-container"><span id="28532"></span><div id="comment-28532" class="comment"><div id="post-28532-score" class="comment-score"></div><div class="comment-text"><p>In the specific case illustrated there may be some form of parallelism as frame 179 has an http continuation from 165.193.123.218 which may be part of the first image request and as this occurs after the start of the retrieval of the 2nd image looks like a parallel request.</p></div><div id="comment-28532-info" class="comment-info"><span class="comment-age">(02 Jan '14, 14:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="28535"></span><div id="comment-28535" class="comment"><div id="post-28535-score" class="comment-score"></div><div class="comment-text"><p>fair enough..</p></div><div id="comment-28535-info" class="comment-info"><span class="comment-age">(02 Jan '14, 14:58)</span> <span class="comment-user userinfo">quitoart</span></div></div></div><div id="comment-tools-28530" class="comment-tools"></div><div class="clear"></div><div id="comment-28530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


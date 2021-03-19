+++
type = "question"
title = "How to use  dissector_add function ?"
description = '''I am a newbie trying to make a plugin , and in my case criteria for wireshark to call my dissector has to be that either source or destination mac will be in this format - &quot;02 00 6f 0x 0y 01&quot; where only x and y are positive integers and can vary. Do we have option to use regex sort of thing here ? I...'''
date = "2012-05-29T04:58:00Z"
lastmod = "2012-06-05T23:39:00Z"
weight = 11435
keywords = [ "urgent-help" ]
aliases = [ "/questions/11435" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use dissector\_add function ?](/questions/11435/how-to-use-dissector_add-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11435-score" class="post-score" title="current number of votes">0</div><span id="post-11435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a newbie trying to make a plugin , and in my case criteria for wireshark to call my dissector has to be that either source or destination mac will be in this format - "02 00 6f 0x 0y 01" where only x and y are positive integers and can vary. Do we have option to use regex sort of thing here ? Its very urgent , any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-urgent-help" rel="tag" title="see questions tagged &#39;urgent-help&#39;">urgent-help</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11435" class="comments-container"><span id="11443"></span><div id="comment-11443" class="comment"><div id="post-11443-score" class="comment-score"></div><div class="comment-text"><p>Let me rephrase the question : I've noticed the function dissector_add() gets called to associate a particular identifier with a dissector handle. And i want it to associate it with packet having either source or destination mac is this format : "02:00:6f:0x:0y:01" . Here everything will remain fixed and only x and y can <a href="http://change.So">change.So</a> i was wondering if we have regex option which can match it properly.Hope i am clear.Please help</p></div><div id="comment-11443-info" class="comment-info"><span class="comment-age">(29 May '12, 06:59)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-11435" class="comment-tools"></div><div class="clear"></div><div id="comment-11435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11444"></span>

<div id="answer-container-11444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11444-score" class="post-score" title="current number of votes">2</div><span id="post-11444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer: There's no "regex" option.</p><p>However, you can register your dissector as an "eth" heuristic dissector which means your dissector will be called as a heuristic dissector before the frame body is dissected as ethernet.</p><p>If the MAC address in the frame matches your requirements, you can do your own dissection and then return TRUE to prevent any further dissection.</p><p>See epan/dissectors/packet-mim.c</p><p>packet-tte.c is another dissector which registers as a heuristic "eth" dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-11444" class="comments-container"><span id="11706"></span><div id="comment-11706" class="comment"><div id="post-11706-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am using heuristic dissector now for mac relevant to my protocol , but that would mean tvb will point to eth payload isn't it ? instead i want to dissect http payload so i need tvb to point to http payload. How can i do that ? thanks for your time</p></div><div id="comment-11706-info" class="comment-info"><span class="comment-age">(05 Jun '12, 23:39)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-11444" class="comment-tools"></div><div class="clear"></div><div id="comment-11444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


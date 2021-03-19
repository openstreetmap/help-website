+++
type = "question"
title = "Difference between running a Lua script in Wireshark and/or tshark"
description = '''Thanks @kurt,@helloworld, another question: what is the difference in running the script from wireshark or tshark? what are the benefits of each way? Comment: I converted the comment from this question: http://ask.wireshark.org/questions/16942/textwindownew-doesnt-work-well'''
date = "2012-12-20T05:14:00Z"
lastmod = "2012-12-20T23:21:00Z"
weight = 17094
keywords = [ "lua", "tshark", "wireshark" ]
aliases = [ "/questions/17094" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between running a Lua script in Wireshark and/or tshark](/questions/17094/difference-between-running-a-lua-script-in-wireshark-andor-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17094-score" class="post-score" title="current number of votes">0</div><span id="post-17094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks <span>@kurt</span>,<span>@helloworld</span>, another question: what is the difference in running the script from wireshark or tshark? what are the benefits of each way?</p><p>Comment: I converted the comment from this question: <a href="http://ask.wireshark.org/questions/16942/textwindownew-doesnt-work-well">http://ask.wireshark.org/questions/16942/textwindownew-doesnt-work-well</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '12, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Dec '12, 07:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-17094" class="comments-container"></div><div id="comment-tools-17094" class="comment-tools"></div><div class="clear"></div><div id="comment-17094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17108"></span>

<div id="answer-container-17108" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17108-score" class="post-score" title="current number of votes">1</div><span id="post-17108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The difference is that you can't do GUI stuff in TShark but you can in Wireshark.</p><p>The benefit of running a Lua script in TShark is that you can do stuff from the command line without having to push buttons in the UI.</p><p>The benefit of running a Lua script in Wireshark is that it can let you do stuff by pushing buttons in the UI.</p><p>Some scripts might be able to work in both environments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17108" class="comments-container"><span id="17119"></span><div id="comment-17119" class="comment"><div id="post-17119-score" class="comment-score"></div><div class="comment-text"><p>Thanks everybody,<span>@Kurt</span>,<span>@helloworld</span>,<span>@Guy Harris</span>,<span>@Jasper</span>,<span>@grahamb</span>,<span>@SYN-bit</span>,<span>@Landi</span>, you are always helping,I'm really glad to join this forum,where people are decent and helpful, next step I'll try to help other with my modest amount of knowledge. Regards</p></div><div id="comment-17119-info" class="comment-info"><span class="comment-age">(20 Dec '12, 23:21)</span> <span class="comment-user userinfo">Leena</span></div></div></div><div id="comment-tools-17108" class="comment-tools"></div><div class="clear"></div><div id="comment-17108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


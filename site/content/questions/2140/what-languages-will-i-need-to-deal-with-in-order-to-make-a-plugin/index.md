+++
type = "question"
title = "What languages will I need to deal with in order to make a plugin?"
description = '''So I&#x27;ve set out to make a plugin that displays(parses, whatever you want to call it) CDMI information for network traffic. But the protocol is not important. I&#x27;ve been told the API is extensive so I can write it in whatever language I want. With some base work in C.  Now I&#x27;m not comfortable using C ...'''
date = "2011-02-03T15:25:00Z"
lastmod = "2011-02-07T12:05:00Z"
weight = 2140
keywords = [ "languages", "lua", "plugins" ]
aliases = [ "/questions/2140" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What languages will I need to deal with in order to make a plugin?](/questions/2140/what-languages-will-i-need-to-deal-with-in-order-to-make-a-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2140-score" class="post-score" title="current number of votes">0</div><span id="post-2140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I've set out to make a plugin that displays(parses, whatever you want to call it) CDMI information for network traffic. But the protocol is not important.</p><p>I've been told the API is extensive so I can write it in whatever language I want. With some base work in C.</p><p>Now I'm not comfortable using C but by the looks of the docs(part 2) there is a nice guide written in C.</p><p>I heard Lua is another viable option and wireshark has it's own built-in lua interpretor. I've never worked with it before but by the looks of the syntax and such I can tell I'd be more comfortable writing in that as opposed to C.</p><p>So to put it formally: what should I expect as move along on this project. Keeping in mind, I'm somewhat of a beginner to writing software for software.</p><p>Ps: I use ubuntu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-languages" rel="tag" title="see questions tagged &#39;languages&#39;">languages</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '11, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p><span>Rodayo</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2140" class="comments-container"></div><div id="comment-tools-2140" class="comment-tools"></div><div class="clear"></div><div id="comment-2140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2153"></span>

<div id="answer-container-2153" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2153-score" class="post-score" title="current number of votes">2</div><span id="post-2153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rodayo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By far, the best way to write a dissector is in C, and especially since you don't already know Lua. Learning to program well in C will likely have a much larger return on your efforts than learning to program in Lua. Not only will you be able to write a much faster and more complete dissector, but you will learn skills that will allow you to participate in other open source projects, including Linux itself and most of the tools you use daily in Ubuntu.<br />
</p><p>There are many ways to learn C and many books available on the topic. (I originally learned by reading the first edition of "The C Programming Language" by Kernighan and Ritchie back in 1978.) Once you get a good grasp of the basics of C, you can quickly transfer this knowledge into writing your Wireshark dissector by starting with a copy of an existing dissector and then modifying it to suit your purposes.<br />
</p><p>You are likely to find that once you know C well, it will be that much easier to learn many other programming languages, including Lua.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p><span>beroset</span><br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span> </br></br></p></div></div><div id="comments-container-2153" class="comments-container"></div><div id="comment-tools-2153" class="comment-tools"></div><div class="clear"></div><div id="comment-2153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2157"></span>

<div id="answer-container-2157" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2157-score" class="post-score" title="current number of votes">0</div><span id="post-2157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't plan to become a programmer in the future. Becoming proficient in any language doesn't interest me. I just want to get the job done. Now, you're saying C is the better choice, but could you elaborate on why it's a better choice?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p><span>Rodayo</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2157" class="comments-container"><span id="2158"></span><div id="comment-2158" class="comment"><div id="post-2158-score" class="comment-score"></div><div class="comment-text"><p>The alternative is to write a dissector in Lua. The problems with this are that there are not as many working examples to start with, that you may need to look at the Lua implementation (written in C) to figure out how to do what you want and that a C implementation will run faster and be easier for you and others to maintain since the debugging tools are better. Those are the task-specific advantages. The generic advantages I think I already covered.</p></div><div id="comment-2158-info" class="comment-info"><span class="comment-age">(04 Feb '11, 13:36)</span> <span class="comment-user userinfo">beroset</span></div></div><span id="2196"></span><div id="comment-2196" class="comment"><div id="post-2196-score" class="comment-score"></div><div class="comment-text"><p>Hmm, well my project partner wants to go with C as well. I researched some more languages but it looks like C is the optimal choice whether I like it or not. Thank you for insight, and sorry if I came off a bit snippy before =P</p></div><div id="comment-2196-info" class="comment-info"><span class="comment-age">(07 Feb '11, 08:40)</span> <span class="comment-user userinfo">Rodayo</span></div></div><span id="2203"></span><div id="comment-2203" class="comment"><div id="post-2203-score" class="comment-score"></div><div class="comment-text"><p>No apology necessary! I didn't have any problem with the way you asked the question. It's good to state concisely what you do and do not want, and that's what you did. If you're satisfied with the answer, you can mark it as "answered" and that way it no longer shows up as an unanswered question for those of us who filter that way.</p></div><div id="comment-2203-info" class="comment-info"><span class="comment-age">(07 Feb '11, 11:48)</span> <span class="comment-user userinfo">beroset</span></div></div><span id="2204"></span><div id="comment-2204" class="comment"><div id="post-2204-score" class="comment-score"></div><div class="comment-text"><p>sorry, how do you mark it as answered? I only see options for upvoting individual answers</p></div><div id="comment-2204-info" class="comment-info"><span class="comment-age">(07 Feb '11, 12:04)</span> <span class="comment-user userinfo">Rodayo</span></div></div><span id="2205"></span><div id="comment-2205" class="comment"><div id="post-2205-score" class="comment-score"></div><div class="comment-text"><p>nevermind.</p></div><div id="comment-2205-info" class="comment-info"><span class="comment-age">(07 Feb '11, 12:05)</span> <span class="comment-user userinfo">Rodayo</span></div></div></div><div id="comment-tools-2157" class="comment-tools"></div><div class="clear"></div><div id="comment-2157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


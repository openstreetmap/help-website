+++
type = "question"
title = "How can I recognize a package that has already passed the dissect function once in my plugin?"
description = '''I am developing a plugin for Wireshark and I have some problems with the multiple passes of the dissect function (dissect_myprotocol) for the same package. I need to know if it is the first time a specific package passes this function. I only want to add some functionality if it is, otherwise I do n...'''
date = "2015-08-03T07:39:00Z"
lastmod = "2015-08-04T04:48:00Z"
weight = 44782
keywords = [ "recognize", "dissect", "package", "packet", "plugin" ]
aliases = [ "/questions/44782" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I recognize a package that has already passed the dissect function once in my plugin?](/questions/44782/how-can-i-recognize-a-package-that-has-already-passed-the-dissect-function-once-in-my-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44782-score" class="post-score" title="current number of votes">0</div><span id="post-44782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a plugin for Wireshark and I have some problems with the multiple passes of the dissect function (dissect_myprotocol) for the same package. I need to know if it is the first time a specific package passes this function. I only want to add some functionality if it is, otherwise I do not want to do anything. How can I be able to tell if it is the first pass or not?</p><p>The amount of captured packages will be very large so it will be difficult to store some well chosen data from all passes and compare them to be able to tell if it is a new pass of a specific package or not.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-recognize" rel="tag" title="see questions tagged &#39;recognize&#39;">recognize</span> <span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span> <span class="post-tag tag-link-package" rel="tag" title="see questions tagged &#39;package&#39;">package</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '15, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/700fdbce0e12ea13d88d310e180269d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sof&#39;s gravatar image" /><p><span>Sof</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sof has no accepted answers">0%</span></p></div></div><div id="comments-container-44782" class="comments-container"><span id="44811"></span><div id="comment-44811" class="comment"><div id="post-44811-score" class="comment-score"></div><div class="comment-text"><p>I might have been a little bit unclear. Maybe I can explain my problem better.</p><p>My problem is that I have a sequence counter for different subtypes of data packages that I want to check if they count up correctly. I store the old value of the sequence counter for every subtype and compare that value with the value of the next package of the same subtype that arrives, after that I update the stored value of the sequence counter. For this I need to know the first time the dissect function is called for a specific package or recognize that specific package next time it passes. I have problems with the multiple passes in a way that the program does not recognize packages that have already passed once, and therefore gives results from the comparison that says that the count up does not work correctly even if it should say that it does. If I have understood my problem correctly I would say that my program thinks that the same package is different ones if it passes several times through the dissect function.</p><p>I do all my implementation of the sequence counter check in the dissect function (dissect_myprotocol).</p><p>How can I recognize packages that have already passed once or know when the first pass is made for every package to be able to ignore the following passes? I do only want to do the sequence counter check once for every captured package.</p></div><div id="comment-44811-info" class="comment-info"><span class="comment-age">(04 Aug '15, 00:50)</span> <span class="comment-user userinfo">Sof</span></div></div><span id="44815"></span><div id="comment-44815" class="comment"><div id="post-44815-score" class="comment-score"></div><div class="comment-text"><p>The answer of <span>@grahamb</span> is still correct. When 'visited' is 1 your dissector has already seen this packet. The sequence counter you want to check, which has to be passed from one packet dissection to the next, should be added as conversation data. Go read README.dissector on how to use the conversation mechanism.</p></div><div id="comment-44815-info" class="comment-info"><span class="comment-age">(04 Aug '15, 02:42)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="44816"></span><div id="comment-44816" class="comment"><div id="post-44816-score" class="comment-score"></div><div class="comment-text"><p>Or perhaps you should use p_set_proto_data(), p_get_proto_data() to store the information on the first pass and retreive the result on subsequent passes.</p></div><div id="comment-44816-info" class="comment-info"><span class="comment-age">(04 Aug '15, 04:48)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-44782" class="comment-tools"></div><div class="clear"></div><div id="comment-44782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44784"></span>

<div id="answer-container-44784" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44784-score" class="post-score" title="current number of votes">2</div><span id="post-44784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sof has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>pinfo-&gt;fd-&gt;flags.visited</code> will be 0 the first time your dissector is called for a frame. There is a macro to help with such checks; <code>PINFO_FD_VISITED(pinfo)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44784" class="comments-container"></div><div id="comment-tools-44784" class="comment-tools"></div><div class="clear"></div><div id="comment-44784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


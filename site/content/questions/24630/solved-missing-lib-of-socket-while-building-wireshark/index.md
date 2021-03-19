+++
type = "question"
title = "[SOLVED] Missing Lib of Socket while building Wireshark"
description = '''Hi all, I&#x27;m adding a program of socket processing into WireShark source code in order to send data to server. I wrote a C program by Visual Studio 2010 and it runs well with the library for socket as below  But when I add it into Wireshark, there are many errors related to missing lib as shown below...'''
date = "2013-09-13T02:34:00Z"
lastmod = "2013-11-04T23:28:00Z"
weight = 24630
keywords = [ "socket", "lib", "build" ]
aliases = [ "/questions/24630" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[SOLVED\] Missing Lib of Socket while building Wireshark](/questions/24630/solved-missing-lib-of-socket-while-building-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24630-score" class="post-score" title="current number of votes">0</div><span id="post-24630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm adding a program of socket processing into WireShark source code in order to send data to server. I wrote a C program by Visual Studio 2010 and it runs well with the library for socket as below</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_3.png" alt="alt text" /></p><p>But when I add it into Wireshark, there are many errors related to missing lib as shown below</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_4.png" alt="alt text" /></p><p>I don't know how to fix these errors, do we have anything to replace "pragma comment ..." or do something to let the program be able to find out the lib? Please help if you have any idea or suggestion. Thank you so much and have a nice weekend.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-lib" rel="tag" title="see questions tagged &#39;lib&#39;">lib</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 02:56</strong> </span></p></div></div><div id="comments-container-24630" class="comments-container"></div><div id="comment-tools-24630" class="comment-tools"></div><div class="clear"></div><div id="comment-24630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26671"></span>

<div id="answer-container-26671" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26671-score" class="post-score" title="current number of votes">0</div><span id="post-26671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>They are differences between C and C++. I tried the program with VS 2010 C++ while Wireshark use .C, so I just made some modifications to match the format of C languages, in which all variables must be declared at the beginning of the block {}. Then, it works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '13, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div></div><div id="comments-container-26671" class="comments-container"></div><div id="comment-tools-26671" class="comment-tools"></div><div class="clear"></div><div id="comment-26671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24637"></span>

<div id="answer-container-24637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24637-score" class="post-score" title="current number of votes">1</div><span id="post-24637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem isn't one of missing libraries, but missing (or incorrect) includes. The compiler is complaining about missing definitions. This may be because those new includes require some definitions to be made before including them.</p><p>When you do manage to get compilation working then the "#pragma comment" entries may or may not allow the linker to find the required libraries. If they don't, then you will need to modify the Makefile to pass the required libs to the linker.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24637" class="comments-container"><span id="24641"></span><div id="comment-24641" class="comment"><div id="post-24641-score" class="comment-score"></div><div class="comment-text"><p>Problem solved. Thanks, grhamb. But there are some errors which are unbelievable because I checked on VS 2010 successfully but I don't know why it appears as a stupid mistake (or I'm stupid ( <em></em> !). Please see the picture as below. Thanks</p></div><div id="comment-24641-info" class="comment-info"><span class="comment-age">(13 Sep '13, 03:57)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24642"></span><div id="comment-24642" class="comment"><div id="post-24642-score" class="comment-score"></div><div class="comment-text"><p>The source is attached here <a href="http://www.mediafire.com/?h7hioao29j65toh">link text</a></p><p>And this is an error. I try to add the function attached above into packet-camel.c but it shows the results :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_5.png" alt="alt text" /></p></div><div id="comment-24642-info" class="comment-info"><span class="comment-age">(13 Sep '13, 04:04)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24731"></span><div id="comment-24731" class="comment"><div id="post-24731-score" class="comment-score"></div><div class="comment-text"><p>Problem solved. Thanks , all :-)</p></div><div id="comment-24731-info" class="comment-info"><span class="comment-age">(15 Sep '13, 19:57)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24738"></span><div id="comment-24738" class="comment"><div id="post-24738-score" class="comment-score"></div><div class="comment-text"><p>And how was the problem solved, for the benefit of others?</p><p>If you can't provide an answer then we might as well delete the question as it's of no use to anyone else.</p></div><div id="comment-24738-info" class="comment-info"><span class="comment-age">(16 Sep '13, 01:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-24637" class="comment-tools"></div><div class="clear"></div><div id="comment-24637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


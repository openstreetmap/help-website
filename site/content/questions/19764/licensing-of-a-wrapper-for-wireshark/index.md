+++
type = "question"
title = "Licensing of a wrapper for wireshark."
description = '''I have a proprietary application performance monitoring product that receives network data, decodes it, correlates it in various ways and then provides statistical, alerting, summary, and other information to users. I would like to use the Wireshark dissectors to get at a wider variety of protocols....'''
date = "2013-03-22T15:22:00Z"
lastmod = "2013-03-22T20:32:00Z"
weight = 19764
keywords = [ "gpl", "product", "licensing" ]
aliases = [ "/questions/19764" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Licensing of a wrapper for wireshark.](/questions/19764/licensing-of-a-wrapper-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19764-score" class="post-score" title="current number of votes">0</div><span id="post-19764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a proprietary application performance monitoring product that receives network data, decodes it, correlates it in various ways and then provides statistical, alerting, summary, and other information to users.</p><p>I would like to use the Wireshark dissectors to get at a wider variety of protocols.</p><p>The intent would be to either: (a) encapsulate the necessary libraries into a DLL which I would give out publicly (i.e. the complete DLL source and, of course, any wireshark code), OR (b) encapsulate the libraries into a separate C program which my proprietary code would communicate with over pipes (again giving out all source to the C program and any wireshark code). Of course, in both cases, any modifications I make to any dissectors and any new dissectors I write would be made public.</p><p>Is there any problem with doing this while still keeping my core APM application proprietary?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gpl" rel="tag" title="see questions tagged &#39;gpl&#39;">gpl</span> <span class="post-tag tag-link-product" rel="tag" title="see questions tagged &#39;product&#39;">product</span> <span class="post-tag tag-link-licensing" rel="tag" title="see questions tagged &#39;licensing&#39;">licensing</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '13, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/38225c395f7ec4d34af520e9a99799b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="angust&#39;s gravatar image" /><p><span>angust</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="angust has no accepted answers">0%</span></p></div></div><div id="comments-container-19764" class="comments-container"></div><div id="comment-tools-19764" class="comment-tools"></div><div class="clear"></div><div id="comment-19764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19766"></span>

<div id="answer-container-19766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19766-score" class="post-score" title="current number of votes">3</div><span id="post-19766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A DLL is a dynamically linked library, and therefore under the constraints of GPLv2 (which Wireshark is licensed under) you would be required to make all of your application source code available as well if you used it that way. Using a pipe, however, keeps it "at arms length" and does not create a derivative work and therefore does not require you to release your separate application source code. (IANAL, however, so this isn't legal advice)</p><p>See the <a href="http://www.wireshark.org/faq.html#q1.9">FAQ</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '13, 20:32</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-19766" class="comments-container"></div><div id="comment-tools-19766" class="comment-tools"></div><div class="clear"></div><div id="comment-19766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "What does USBPcap do and why would you use it?"
description = '''Hi all, I am currently learning WireShark and how to use it, understand it and diagnose problems on my network, unfortunately I cannot afford to go on an official course so I am learning from the books that are recommended by the WireShark website and also so suggestions by users on other forums, I ...'''
date = "2015-11-21T02:08:00Z"
lastmod = "2015-11-21T03:16:00Z"
weight = 47824
keywords = [ "other", "tstbour" ]
aliases = [ "/questions/47824" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does USBPcap do and why would you use it?](/questions/47824/what-does-usbpcap-do-and-why-would-you-use-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47824-score" class="post-score" title="current number of votes">0</div><span id="post-47824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am currently learning WireShark and how to use it, understand it and diagnose problems on my network, unfortunately I cannot afford to go on an official course so I am learning from the books that are recommended by the WireShark website and also so suggestions by users on other forums, I am doing really well and getting the hang of WireShark.</p><p>But, yesterday I decided to upgrade my WireShark to the latest version and I installed USBPcap which my books do not cover, so I was wondering if anyone could take two minutes to explain to me what this is, why would you capture USB traffic and what scenario would a USB capture apply to?</p><p>Any help would be much appreciated as my curiosity is getting the better of me :)</p><p>Thanks</p><p>Daz</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-other" rel="tag" title="see questions tagged &#39;other&#39;">other</span> <span class="post-tag tag-link-tstbour" rel="tag" title="see questions tagged &#39;tstbour&#39;">tstbour</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '15, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/256dc1a99f157d9aa3d7ca85cdd5d165?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JimBob321&#39;s gravatar image" /><p><span>JimBob321</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JimBob321 has no accepted answers">0%</span></p></div></div><div id="comments-container-47824" class="comments-container"></div><div id="comment-tools-47824" class="comment-tools"></div><div class="clear"></div><div id="comment-47824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47825"></span>

<div id="answer-container-47825" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47825-score" class="post-score" title="current number of votes">1</div><span id="post-47825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look at the <a href="http://desowin.org/usbpcap/">project home page</a>.</p><p>As an example of use case, it helped me debug a mysterious case of sound distortion in audio streams recorded from an USB audio "card" (thanks again, Tomasz).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '15, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '15, 02:25</strong> </span></p></div></div><div id="comments-container-47825" class="comments-container"><span id="47826"></span><div id="comment-47826" class="comment"><div id="post-47826-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that, I did look at the homepage already but it does not really tell me what it does and what you would use it for.</p><p>Daz</p></div><div id="comment-47826-info" class="comment-info"><span class="comment-age">(21 Nov '15, 02:47)</span> <span class="comment-user userinfo">JimBob321</span></div></div><span id="47828"></span><div id="comment-47828" class="comment"><div id="post-47828-score" class="comment-score"></div><div class="comment-text"><p>Think about USB the same way you normally think about Ethernet. It is a communication interface allowing you to connect your PC to various pieces of hardware (or vice versa if you prefer) and exchange information with them using various protocols. Sometimes you need to analyse the protocol conversations to find out why something works different from what you've expected or does not work at all, or possibly you need to have a look at the information transported using that protocols (usually called payload) to learn whether already the connected device is sending you corrupt data or whether it is your application which handles them improperly.</p><p>And note that in addition to Ethernet and USB, Wireshark can handle also protocols used on various types of serial channels, like those used in "legacy" telephony networks.</p></div><div id="comment-47828-info" class="comment-info"><span class="comment-age">(21 Nov '15, 03:02)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="47829"></span><div id="comment-47829" class="comment"><div id="post-47829-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much! :), that makes sense now, I am sure I will get round to it when I finish my books! :)</p><p>Thanks again for taking to time to explain it to me.</p></div><div id="comment-47829-info" class="comment-info"><span class="comment-age">(21 Nov '15, 03:16)</span> <span class="comment-user userinfo">JimBob321</span></div></div></div><div id="comment-tools-47825" class="comment-tools"></div><div class="clear"></div><div id="comment-47825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


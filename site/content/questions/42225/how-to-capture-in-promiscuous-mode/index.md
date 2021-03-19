+++
type = "question"
title = "How to capture in promiscuous mode ?"
description = '''Hello everyone, I need to use Wireshark to monitor mirrored traffic from switch. I&#x27;ve read that it&#x27;s needed to switch network card to promiscuous mode. How can I do that or Wireshark does it by itself ? And after I&#x27;m done, how can I switch it back to normal mode (or to what it was before) ? Thanks f...'''
date = "2015-05-08T11:15:00Z"
lastmod = "2015-05-08T13:22:00Z"
weight = 42225
keywords = [ "switch", "promiscuous-mode", "mode", "wireshark" ]
aliases = [ "/questions/42225" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture in promiscuous mode ?](/questions/42225/how-to-capture-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42225-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I need to use Wireshark to monitor mirrored traffic from switch. I've read that it's needed to switch network card to promiscuous mode. How can I do that or Wireshark does it by itself ? And after I'm done, how can I switch it back to normal mode (or to what it was before) ? Thanks for answers</p></div><div id="question-tags" class="tags-container tags">switch promiscuous-mode mode wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '15, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/26ee2975190aeb7e67ca1efabecb6e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razor268&#39;s gravatar image" /><p>razor268<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razor268 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '15, 15:25</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42225" class="comments-container"><span id="42232"></span><div id="comment-42232" class="comment"><div id="post-42232-score" class="comment-score"></div><div class="comment-text"><p>Which operating system are you using for the Wireshark program?</p></div><div id="comment-42232-info" class="comment-info"><span class="comment-age">(08 May '15, 13:01)</span> Amato_C</div></div><span id="42244"></span><div id="comment-42244" class="comment"><div id="post-42244-score" class="comment-score"></div><div class="comment-text"><p>I'm using Windows 7.</p></div><div id="comment-42244-info" class="comment-info"><span class="comment-age">(08 May '15, 18:21)</span> razor268</div></div><span id="42245"></span><div id="comment-42245" class="comment"><div id="post-42245-score" class="comment-score"></div><div class="comment-text"><p>Then Christian_R's answer should work. In fact, no matter <em>what</em> operating system you're using, Christian_R's answer should work.</p></div><div id="comment-42245-info" class="comment-info"><span class="comment-age">(08 May '15, 18:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42225" class="comment-tools"></div><div class="clear"></div><div id="comment-42225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42233"></span>

<div id="answer-container-42233" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42233-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Easily said: You can choose the promiscuous mode in the capture dialog of Wireshark. If you enable the highlighted checkbox (see below) the selected adapters will work and capture in promiscuous mode. And they will return to normal opertaion if capturing is stopped.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Prom1.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '15, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '15, 13:34</p></div></div><div id="comments-container-42233" class="comments-container"><span id="42234"></span><div id="comment-42234" class="comment"><div id="post-42234-score" class="comment-score"></div><div class="comment-text"><p>On a system which uses Windows you also need to install the WinPcap tool.</p></div><div id="comment-42234-info" class="comment-info"><span class="comment-age">(08 May '15, 13:36)</span> Christian_R</div></div><span id="42237"></span><div id="comment-42237" class="comment"><div id="post-42237-score" class="comment-score"></div><div class="comment-text"><blockquote><p>On a system which uses Windows you also need to install the WinPcap tool.</p></blockquote><p>...which the Wireshark installer for Windows does by default.</p></div><div id="comment-42237-info" class="comment-info"><span class="comment-age">(08 May '15, 14:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42233" class="comment-tools"></div><div class="clear"></div><div id="comment-42233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


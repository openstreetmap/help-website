+++
type = "question"
title = "How do I remove access_bpf group?"
description = '''Greetings, I installed Wireshark 1.6.7 on a 32-bit Intel processor MacBook running OSX 10.6.8. I now understand I need Wireshark for Snow Leopard and performed the uninstall process up to &quot;remove access_bpf group&quot;. How do I perform this step? Thank you for your help. Regards.'''
date = "2012-05-10T21:02:00Z"
lastmod = "2012-05-11T00:55:00Z"
weight = 10914
keywords = [ "osx" ]
aliases = [ "/questions/10914" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I remove access\_bpf group?](/questions/10914/how-do-i-remove-access_bpf-group)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10914-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I installed Wireshark 1.6.7 on a 32-bit Intel processor MacBook running OSX 10.6.8.</p><p>I now understand I need Wireshark for Snow Leopard and performed the uninstall process up to "remove access_bpf group".</p><p>How do I perform this step?</p><p>Thank you for your help.</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags">osx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '12, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/52bee3bce6648291703019e833439e13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BeachsideJim&#39;s gravatar image" /><p>BeachsideJim<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BeachsideJim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '12, 01:24</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10914" class="comments-container"></div><div id="comment-tools-10914" class="comment-tools"></div><div class="clear"></div><div id="comment-10914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10919"></span>

<div id="answer-container-10919" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10919-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Start a terminal window and run this command:</p><blockquote><p><code>sudo dscl . -delete /Groups/access_bpf</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-10919" class="comments-container"><span id="10922"></span><div id="comment-10922" class="comment"><div id="post-10922-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt -- dscl "worked as advertised"</p><p>Regards, Jim</p></div><div id="comment-10922-info" class="comment-info"><span class="comment-age">(11 May '12, 02:47)</span> BeachsideJim</div></div><span id="10925"></span><div id="comment-10925" class="comment"><div id="post-10925-score" class="comment-score">1</div><div class="comment-text"><p>@BeachsideJim</p><p>I converted your "answer" to a comment as that's how this site works, see the FAQ for info.</p><p>Also, if Kurt has provided an answer for your issue, you should accept it by clicking the checkmark icon next to the answer. This lets other folks coming after you know that it was a good answer for the issue.</p></div><div id="comment-10925-info" class="comment-info"><span class="comment-age">(11 May '12, 03:06)</span> grahamb ♦</div></div></div><div id="comment-tools-10919" class="comment-tools"></div><div class="clear"></div><div id="comment-10919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


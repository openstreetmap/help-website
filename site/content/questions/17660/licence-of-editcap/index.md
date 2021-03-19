+++
type = "question"
title = "Licence of editcap"
description = '''Hi, I am just wondering why there is no licence header in editcap.c such as in mergecap, capinfo etc. The man pages states &quot;Editcap is part of the Wireshark distribution.&quot; like to one of mergecap etc. also does. Isn&#x27;t it licenced under GPL?'''
date = "2013-01-14T05:42:00Z"
lastmod = "2013-01-14T07:27:00Z"
weight = 17660
keywords = [ "editcap", "licence" ]
aliases = [ "/questions/17660" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Licence of editcap](/questions/17660/licence-of-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17660-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am just wondering why there is no licence header in editcap.c such as in mergecap, capinfo etc. The man pages states "Editcap is part of the Wireshark distribution." like to one of mergecap etc. also does.</p><p>Isn't it licenced under GPL?</p></div><div id="question-tags" class="tags-container tags">editcap licence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '13, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/086053c8c3fa23e3cd01986ff4d9da0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FiroDev&#39;s gravatar image" /><p>FiroDev<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FiroDev has no accepted answers">0%</span></p></div></div><div id="comments-container-17660" class="comments-container"></div><div id="comment-tools-17660" class="comment-tools"></div><div class="clear"></div><div id="comment-17660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17666"></span>

<div id="answer-container-17666" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17666-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just contacted the original author and he confirmed his intention is that it is GPLv2+. I have added (in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=47063">r47063</a>) the license to the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17666" class="comments-container"></div><div id="comment-tools-17666" class="comment-tools"></div><div class="clear"></div><div id="comment-17666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17664"></span>

<div id="answer-container-17664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17664-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are right, there is no link to the GPL in the file itself. However, as it is heavily using GPL code, it inherits the GPL in that way. So, editcap.c needs to be GPL, as it is using GPL code.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '13, 07:21</p></div></div><div id="comments-container-17664" class="comments-container"><span id="17733"></span><div id="comment-17733" class="comment"><div id="post-17733-score" class="comment-score"></div><div class="comment-text"><p>And, as per Jeff Morriss's comment, it now is explicitly marked as being under the GPL.</p></div><div id="comment-17733-info" class="comment-info"><span class="comment-age">(16 Jan '13, 20:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17664" class="comment-tools"></div><div class="clear"></div><div id="comment-17664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


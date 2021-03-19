+++
type = "question"
title = "how to retrieve file from FTP"
description = '''there is trace file that has captured some FTP traffic between a server and a host. i need to retrieve the files that were transferred during this FTP communication.  i have found the files but i don&#x27;t know how to retrieve them. Its a assignment :)'''
date = "2013-11-22T09:14:00Z"
lastmod = "2013-11-24T17:16:00Z"
weight = 27284
keywords = [ "ftp", "capture", "wireshark" ]
aliases = [ "/questions/27284" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to retrieve file from FTP](/questions/27284/how-to-retrieve-file-from-ftp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>there is trace file that has captured some FTP traffic between a server and a host. i need to retrieve the files that were transferred during this FTP communication. i have found the files but i don't know how to retrieve them. Its a assignment :)</p></div><div id="question-tags" class="tags-container tags">ftp capture wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '13, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/ee9539ed81444b168151991111f26c5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lovey&#39;s gravatar image" /><p>lovey<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lovey has no accepted answers">0%</span></p></div></div><div id="comments-container-27284" class="comments-container"><span id="27286"></span><div id="comment-27286" class="comment"><div id="post-27286-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Its a assignment :)</p></blockquote><p>isn't the nature of an assignment to do it yourself. Just a crazy idea, but maybe you learn something if you try ;-)</p></div><div id="comment-27286-info" class="comment-info"><span class="comment-age">(22 Nov '13, 09:36)</span> Kurt Knochner ♦</div></div><span id="27290"></span><div id="comment-27290" class="comment"><div id="post-27290-score" class="comment-score"></div><div class="comment-text"><p>its not fun doing assignment when you are stuck form 3 hrs in it</p></div><div id="comment-27290-info" class="comment-info"><span class="comment-age">(22 Nov '13, 10:26)</span> lovey</div></div></div><div id="comment-tools-27284" class="comment-tools"></div><div class="clear"></div><div id="comment-27284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27292"></span>

<div id="answer-container-27292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27292-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>its not fun doing assignment when you are stuck form 3 hrs in it</p></blockquote><p>the purpose of an assignment is <strong>not</strong> to have fun, but to learn something, right? In an ideal situation, you'll learn something <strong>and</strong> have some fun. ;-)</p><p>Hint: Search the site and you will find similar questions. They will help you to understand how it works. Look for something that is called 'following a tcp stream' (or so).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Nov '13, 11:42</p></div></div><div id="comments-container-27292" class="comments-container"></div><div id="comment-tools-27292" class="comment-tools"></div><div class="clear"></div><div id="comment-27292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27330"></span>

<div id="answer-container-27330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Click on an FTP Packet , Follow TCP Stream --&gt; Save As (whatever it was)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/599929aa65406761d15533f022ed2d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctxsvc&#39;s gravatar image" /><p>ctxsvc<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctxsvc has one accepted answer">33%</span></p></div></div><div id="comments-container-27330" class="comments-container"></div><div id="comment-tools-27330" class="comment-tools"></div><div class="clear"></div><div id="comment-27330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Is it possible to modify the hf array as the packet is being parsed?"
description = '''So with the custom protocol I&#x27;m writing there are a lot of properties that need to be added to the hf array. I was wondering if it&#x27;s possible to add items to it as I&#x27;m parsing the packet. That is, not every packet will have a header for every single property so I would only add the ones that are pre...'''
date = "2011-02-14T15:13:00Z"
lastmod = "2011-02-14T22:46:00Z"
weight = 2333
keywords = [ "hf", "array", "proto_register" ]
aliases = [ "/questions/2333" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to modify the hf array as the packet is being parsed?](/questions/2333/is-it-possible-to-modify-the-hf-array-as-the-packet-is-being-parsed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2333-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So with the custom protocol I'm writing there are a lot of properties that need to be added to the hf array.</p><p>I was wondering if it's possible to add items to it as I'm parsing the packet. That is, not every packet will have a header for every single property so I would only add the ones that are present.</p></div><div id="question-tags" class="tags-container tags">hf array proto_register</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '11, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p>Rodayo<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '11, 15:14</p></div></div><div id="comments-container-2333" class="comments-container"></div><div id="comment-tools-2333" class="comment-tools"></div><div class="clear"></div><div id="comment-2333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2336"></span>

<div id="answer-container-2336" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2336-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer: All the needed hf[] entries should be specified in the proto_register function.</p><p>Even it might be possible to do late registration, I don't think anything is really gained and your code would definitely be more complex.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-2336" class="comments-container"><span id="2350"></span><div id="comment-2350" class="comment"><div id="post-2350-score" class="comment-score"></div><div class="comment-text"><p>Actually, I looked at packet-http.c and it looked like that file was doing just what I was proposing. I followed it as a guideline and it seems to have worked without any problems. Thanks anyways =]</p></div><div id="comment-2350-info" class="comment-info"><span class="comment-age">(15 Feb '11, 11:11)</span> Rodayo</div></div></div><div id="comment-tools-2336" class="comment-tools"></div><div class="clear"></div><div id="comment-2336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


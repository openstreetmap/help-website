+++
type = "question"
title = "http content length calculation"
description = '''Can anyone explain how do I calculate the content length in a http response? I do see the content length header with some value in the server response but would like to validate it. Is there any manual way? I tried adding the tcp lengths of all previous packets including the http response with the s...'''
date = "2012-09-25T20:28:00Z"
lastmod = "2012-09-26T01:19:00Z"
weight = 14524
keywords = [ "content", "length", "http" ]
aliases = [ "/questions/14524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [http content length calculation](/questions/14524/http-content-length-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone explain how do I calculate the content length in a http response? I do see the content length header with some value in the server response but would like to validate it. Is there any manual way?</p><p>I tried adding the tcp lengths of all previous packets including the http response with the status code but guess I need to subtract http header from the last packet. Please help!</p></div><div id="question-tags" class="tags-container tags">content length http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '12, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/8db593133b07b7462351f19f668a656a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshdg&#39;s gravatar image" /><p>yogeshdg<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshdg has no accepted answers">0%</span></p></div></div><div id="comments-container-14524" class="comments-container"></div><div id="comment-tools-14524" class="comment-tools"></div><div class="clear"></div><div id="comment-14524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14534"></span>

<div id="answer-container-14534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14534-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP header ends with an empty line ("CR/LF/CR/LF", 0d0a0d0a). The content of the HTTP body starts at the first byte after the "CR/LF/CR/LF". So count the bytes from that point. If all is well, the byte pointed to by the content length header should indeed be the last byte of the object being served by the HTTP server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '12, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14534" class="comments-container"><span id="14583"></span><div id="comment-14583" class="comment"><div id="post-14583-score" class="comment-score"></div><div class="comment-text"><p>Thanks. That makes sense. Appreciate your help. I didn't notice this:)(</p></div><div id="comment-14583-info" class="comment-info"><span class="comment-age">(27 Sep '12, 21:26)</span> yogeshdg</div></div></div><div id="comment-tools-14534" class="comment-tools"></div><div class="clear"></div><div id="comment-14534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


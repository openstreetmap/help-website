+++
type = "question"
title = "How do I view a raw HTTP request/response?"
description = '''Given an HTTP request/response in the packet list, how do I copy the raw data for it? I can see that I can click on it, and the &quot;packet bytes&quot; shows me some stuff, but it&#x27;s not what I want. It shows me a hex representation of the bytes, and the textual representation in another two columns. I can&#x27;t ...'''
date = "2013-11-27T15:43:00Z"
lastmod = "2013-11-27T15:55:00Z"
weight = 27515
keywords = [ "http" ]
aliases = [ "/questions/27515" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I view a raw HTTP request/response?](/questions/27515/how-do-i-view-a-raw-http-requestresponse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given an HTTP request/response in the packet list, how do I copy the raw data for it?</p><p>I can see that I can click on it, and the "packet bytes" shows me some stuff, but it's not what I want. It shows me a hex representation of the bytes, and the textual representation in another two columns. I can't use a simple regex to filter out the useless hex representation, since the textual representation is incomplete: some characters, such as newlines, are replaced with periods. I could manually parse the hex representation and convert it to standard ASCII, but this seems like a stupid amount of work simply to undo work that Wireshark is doing and that I don't want it to do anyway.</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '13, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/c037e51c81ff40b910e63b6f9dab5230?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jameshfisher&#39;s gravatar image" /><p>jameshfisher<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jameshfisher has no accepted answers">0%</span></p></div></div><div id="comments-container-27515" class="comments-container"></div><div id="comment-tools-27515" class="comment-tools"></div><div class="clear"></div><div id="comment-27515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27516"></span>

<div id="answer-container-27516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27516-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right click one of the frames and select 'Follow TCP stream'</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27516" class="comments-container"></div><div id="comment-tools-27516" class="comment-tools"></div><div class="clear"></div><div id="comment-27516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


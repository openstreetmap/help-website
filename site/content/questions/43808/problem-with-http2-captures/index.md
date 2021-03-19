+++
type = "question"
title = "Problem with http2 captures"
description = '''Hello, Until now, I have used wireshark 1.99.5 and it can recognise http2 traffic, but now I have updated to 1.99.7 and I need to actívate it with Analyze/Decode As option. Why do I need it?, what did it change? And I want to use it with tshark is there any command line option for telling it Decode ...'''
date = "2015-07-02T01:51:00Z"
lastmod = "2015-07-07T12:02:00Z"
weight = 43808
keywords = [ "http2.0" ]
aliases = [ "/questions/43808" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with http2 captures](/questions/43808/problem-with-http2-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43808-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Until now, I have used wireshark 1.99.5 and it can recognise http2 traffic, but now I have updated to 1.99.7 and I need to actívate it with Analyze/Decode As option. Why do I need it?, what did it change? And I want to use it with tshark is there any command line option for telling it Decode as http2? My captures files are done with last nghttp server and client and RFC is closed and when 1.99.5 version was published until 1.99.7 version nothing respect to frames structure has changed Best regards</p></div><div id="question-tags" class="tags-container tags">http2.0</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/2745a883c3d3014fdc8569a966ca8a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lespla&#39;s gravatar image" /><p>lespla<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lespla has no accepted answers">0%</span></p></div></div><div id="comments-container-43808" class="comments-container"><span id="43809"></span><div id="comment-43809" class="comment"><div id="post-43809-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture that has the described problem in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox, etc.?</p></div><div id="comment-43809-info" class="comment-info"><span class="comment-age">(02 Jul '15, 03:22)</span> grahamb ♦</div></div><span id="43842"></span><div id="comment-43842" class="comment"><div id="post-43842-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/c72a88d38c5d">https://www.cloudshark.org/captures/c72a88d38c5d</a> How can I change permissions file</p><p>Best regards</p></div><div id="comment-43842-info" class="comment-info"><span class="comment-age">(03 Jul '15, 03:16)</span> lespla</div></div></div><div id="comment-tools-43808" class="comment-tools"></div><div class="clear"></div><div id="comment-43808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43910"></span>

<div id="answer-container-43910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43910-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/41458/unable-to-decode-http2-traffic">https://ask.wireshark.org/questions/41458/unable-to-decode-http2-traffic</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-43910" class="comments-container"></div><div id="comment-tools-43910" class="comment-tools"></div><div class="clear"></div><div id="comment-43910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43938"></span>

<div id="answer-container-43938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43938-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For reference this is a regression that appeared post 1.99.5 release for unciphered data traffic over HTTP port, tracked by bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11331">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11331</a></p><p>EDIT: the issue is now fixed starting from nightly build v1.99.8rc0-354-gd36930e</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 10:07</p></div></div><div id="comments-container-43938" class="comments-container"></div><div id="comment-tools-43938" class="comment-tools"></div><div class="clear"></div><div id="comment-43938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


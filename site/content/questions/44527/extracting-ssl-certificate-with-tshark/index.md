+++
type = "question"
title = "Extracting SSL Certificate with tshark"
description = '''I know how to do it with wireshark and I see how to get the information about the cert with tshark, but I don&#x27;t see any way of getting just the cert (any format works).  Is this possible with tshark? '''
date = "2015-07-27T07:38:00Z"
lastmod = "2015-07-27T15:41:00Z"
weight = 44527
keywords = [ "ssl", "tshark", "certificate" ]
aliases = [ "/questions/44527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting SSL Certificate with tshark](/questions/44527/extracting-ssl-certificate-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know <a href="https://www.wireshark.org/lists/wireshark-users/201003/msg00080.html">how to do it with wireshark</a> and I see <a href="https://ask.wireshark.org/questions/41034/extract-certificate-info-with-tshark">how to get the information about the cert with tshark</a>, but I don't see any way of getting just the cert (any format works).</p><p>Is this possible with tshark?</p></div><div id="question-tags" class="tags-container tags">ssl tshark certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/f98f1a4e4eb1d8900f9957d7be1f9053?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddworken&#39;s gravatar image" /><p>ddworken<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddworken has no accepted answers">0%</span></p></div></div><div id="comments-container-44527" class="comments-container"></div><div id="comment-tools-44527" class="comment-tools"></div><div class="clear"></div><div id="comment-44527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44548"></span>

<div id="answer-container-44548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44548-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark does not have that functionality, so you'll have to use scripting to extract the required bytes. See my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/17260/x509-decode-with-tshark">https://ask.wireshark.org/questions/17260/x509-decode-with-tshark</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '15, 15:42</p></div></div><div id="comments-container-44548" class="comments-container"></div><div id="comment-tools-44548" class="comment-tools"></div><div class="clear"></div><div id="comment-44548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


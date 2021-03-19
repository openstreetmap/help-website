+++
type = "question"
title = "can otr be detected using wireshark?"
description = '''I&#x27;m running spark on openfire server and communicating to another client using otr. Is it possible to detect this using wireshark?'''
date = "2012-08-15T23:21:00Z"
lastmod = "2012-08-16T07:26:00Z"
weight = 13671
keywords = [ "otr" ]
aliases = [ "/questions/13671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can otr be detected using wireshark?](/questions/13671/can-otr-be-detected-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running spark on openfire server and communicating to another client using otr. Is it possible to detect this using wireshark?</p></div><div id="question-tags" class="tags-container tags">otr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '12, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/1bb1c0c7196c122b2174df24ad39cd29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mv93&#39;s gravatar image" /><p>mv93<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mv93 has no accepted answers">0%</span></p></div></div><div id="comments-container-13671" class="comments-container"></div><div id="comment-tools-13671" class="comment-tools"></div><div class="clear"></div><div id="comment-13671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13683"></span>

<div id="answer-container-13683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13683-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Spark tries to use TLS by default and Openfire has TLS enabled by default, as optional parameter for the client connection (Admin Console -&gt; Server -&gt; Server Settings -&gt; Security Settings -&gt; Client Connection Security -&gt; Custom -&gt; TLS method).</p><p>So, you <strong>cannot</strong> read the clear text communication (XMPP) between a spark client and openfire and thus you cannot detect the use of <a href="http://en.wikipedia.org/wiki/Off-the-Record_Messaging">OTR</a>.</p><p>If you disable TLS at the server (NOT a good idea !!), you can read the whole XMPP protocol and then you can detect the use of OTR. OTR messages start with '?OTR:'.</p><blockquote><p><code>type="chat"&gt;&lt;body&gt;?OTR:AAICAAAAxPyhsiLRM2ftQHjc88ySmNGjQUiYJEWB...</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '12, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '12, 07:27</p></div></div><div id="comments-container-13683" class="comments-container"></div><div id="comment-tools-13683" class="comment-tools"></div><div class="clear"></div><div id="comment-13683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


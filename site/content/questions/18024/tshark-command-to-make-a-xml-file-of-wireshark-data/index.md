+++
type = "question"
title = "Tshark Command to make a xml file of wireshark data"
description = '''Hey. I am new to wireshark &amp;amp; need some help. How can I make a xml file of wireshark data using tshark command? Tshark does not allow me to write anything initially. How to write a command on it?'''
date = "2013-01-29T03:18:00Z"
lastmod = "2013-01-29T03:32:00Z"
weight = 18024
keywords = [ "xml", "command", "tshark", "file", "wireshark" ]
aliases = [ "/questions/18024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark Command to make a xml file of wireshark data](/questions/18024/tshark-command-to-make-a-xml-file-of-wireshark-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18024-score" class="post-score" title="current number of votes">0</div><span id="post-18024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey. I am new to wireshark &amp; need some help. How can I make a xml file of wireshark data using tshark command? Tshark does not allow me to write anything initially. How to write a command on it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/a626dd40716dc7336f3934d5ba42eafb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hamra%20Rehan&#39;s gravatar image" /><p><span>Hamra Rehan</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hamra Rehan has no accepted answers">0%</span></p></div></div><div id="comments-container-18024" class="comments-container"></div><div id="comment-tools-18024" class="comment-tools"></div><div class="clear"></div><div id="comment-18024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18026"></span>

<div id="answer-container-18026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18026-score" class="post-score" title="current number of votes">1</div><span id="post-18026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the output of <code>tshark -h</code>:</p><pre><code>-T pdml|ps|psml|text|fields
   format of text output (def: text)</code></pre><p>And from the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>:</p><pre><code>-T pdml|psml|ps|text|fields

Set the format of the output when viewing decoded packet data. The options are one of:

pdml Packet Details Markup Language, an XML-based format for the details of a decoded packet. This information is equivalent to the packet details printed with the -V flag.

psml Packet Summary Markup Language, an XML-based format for the summary information of a decoded packet. This information is equivalent to the information shown in the one-line summary printed by default.</code></pre><p>So you can use either <code>-T pdml</code> or <code>-T psml</code> depending on your needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18026" class="comments-container"></div><div id="comment-tools-18026" class="comment-tools"></div><div class="clear"></div><div id="comment-18026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


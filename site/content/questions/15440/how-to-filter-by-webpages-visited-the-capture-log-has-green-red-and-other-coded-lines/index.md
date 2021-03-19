+++
type = "question"
title = "how to filter by webpages visited -- the capture log has green, red, and other coded lines"
description = '''how to filter by webpages visited -- the capture log has green, red, and other coded lines'''
date = "2012-10-31T18:18:00Z"
lastmod = "2012-11-01T02:46:00Z"
weight = 15440
keywords = [ "capture-filter" ]
aliases = [ "/questions/15440" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter by webpages visited -- the capture log has green, red, and other coded lines](/questions/15440/how-to-filter-by-webpages-visited-the-capture-log-has-green-red-and-other-coded-lines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15440-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to filter by webpages visited -- the capture log has green, red, and other coded lines</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '12, 18:18</strong></p><img src="https://secure.gravatar.com/avatar/b2a4006b4a0252f8be292c57acde97ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkhelpers&#39;s gravatar image" /><p>wiresharkhel...<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkhelpers has no accepted answers">0%</span></p></div></div><div id="comments-container-15440" class="comments-container"></div><div id="comment-tools-15440" class="comment-tools"></div><div class="clear"></div><div id="comment-15440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15451"></span>

<div id="answer-container-15451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15451-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use this display filter:</p><blockquote><p><code>http.request.full_uri contains "xxxxxx"</code><br />
</p></blockquote><p>Replace the xxxx with the websites or pages you are looking for.</p><blockquote><p><code>http.request.full_uri contains "ask.wireshark.org"</code><br />
<code>http.request.full_uri contains "/questions"</code><br />
</p></blockquote><p>You will then get all HTTP requests that contain those strings in the URI. Right click on one of those packets and select "Follow TCP Stream" to see the whole communication for that request.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '12, 02:47</p></div></div><div id="comments-container-15451" class="comments-container"></div><div id="comment-tools-15451" class="comment-tools"></div><div class="clear"></div><div id="comment-15451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


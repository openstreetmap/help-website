+++
type = "question"
title = "how to filter only m-post method"
description = '''I&#x27;m looking the way how to filter only m-post method via wireshark  M-POST is a new HTTP method defined using the HTTP Extension Framework located at http://www.w3.org/Protocols/HTTP/ietf-ext-wg. This method is used when you are including mandatory information in the HTTP header, just as you used th...'''
date = "2015-04-14T10:15:00Z"
lastmod = "2015-04-15T02:17:00Z"
weight = 41433
keywords = [ "m-post", "mpost" ]
aliases = [ "/questions/41433" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter only m-post method](/questions/41433/how-to-filter-only-m-post-method)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking the way how to filter only m-post method via wireshark</p><blockquote><p>M-POST is a new HTTP method defined using the HTTP Extension Framework located at <a href="http://www.w3.org/Protocols/HTTP/ietf-ext-wg.">http://www.w3.org/Protocols/HTTP/ietf-ext-wg.</a> This method is used when you are including mandatory information in the HTTP header, just as you used the mustUnderstand attribute in the SOAP header element.</p></blockquote></div><div id="question-tags" class="tags-container tags">m-post mpost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '15, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/013786becd46e2d2aac7039f4797b948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izdryk&#39;s gravatar image" /><p>izdryk<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izdryk has no accepted answers">0%</span></p></div></div><div id="comments-container-41433" class="comments-container"></div><div id="comment-tools-41433" class="comment-tools"></div><div class="clear"></div><div id="comment-41433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41443"></span>

<div id="answer-container-41443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41443-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP dissector allows you to add custom headers through the preferences. I'm not sure if that makes them filterable, but it's worth a try.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41443" class="comments-container"></div><div id="comment-tools-41443" class="comment-tools"></div><div class="clear"></div><div id="comment-41443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41444"></span>

<div id="answer-container-41444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41444-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this:</p><blockquote><p>tcp contains "M-POST"<br />
</p></blockquote><p><strong>Hint</strong>: Please keep in mind that the <strong>contains</strong> operator is case sensitive, so the above filter will only find "M-POST" not "m-POST" or "M-post", etc.</p><p>If you want/nned case insensitive filtering, please use the following one:</p><blockquote><p>tcp matches "(?i)M-POST"<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41444" class="comments-container"></div><div id="comment-tools-41444" class="comment-tools"></div><div class="clear"></div><div id="comment-41444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


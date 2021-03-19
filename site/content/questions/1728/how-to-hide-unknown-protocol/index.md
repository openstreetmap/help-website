+++
type = "question"
title = "How to hide &quot;Unknown&quot; Protocol?"
description = '''I checked only Kerberos protocols in &quot;Enabled Protocols&quot; list. But &quot;Capturing...&quot; window shows a lot of &quot;Unknown protocol&quot; records. Is it possible to hide these records?'''
date = "2011-01-13T00:52:00Z"
lastmod = "2011-01-13T02:55:00Z"
weight = 1728
keywords = [ "settings" ]
aliases = [ "/questions/1728" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to hide "Unknown" Protocol?](/questions/1728/how-to-hide-unknown-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1728-score" class="post-score" title="current number of votes">0</div><span id="post-1728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I checked only Kerberos protocols in "Enabled Protocols" list. But "Capturing..." window shows a lot of "Unknown protocol" records. Is it possible to hide these records?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/8f09d162cf66ea530a185a96310c64fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ateam&#39;s gravatar image" /><p><span>ateam</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ateam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '11, 00:53</strong> </span></p></div></div><div id="comments-container-1728" class="comments-container"></div><div id="comment-tools-1728" class="comment-tools"></div><div class="clear"></div><div id="comment-1728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1732"></span>

<div id="answer-container-1732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1732-score" class="post-score" title="current number of votes">0</div><span id="post-1732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "Enabled Protocols" preference controls which protocols are attempted to be examined and dissected by Wireshark. Hence by unchecking all of those protocols, Wireshark's only option is to display all of those frames as being "unknown" as you have instructed it to not attempt to find out what they are.</p><p>To only capture Kerberos packets, specify an appropriate capture filter, such as "tcp port 88 or udp 88" in the Capture options window.</p><p>Alternatively, you might choose to not filter during capture, and just apply a display filter after the fact, such as just plain "kerberos"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1732" class="comments-container"></div><div id="comment-tools-1732" class="comment-tools"></div><div class="clear"></div><div id="comment-1732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


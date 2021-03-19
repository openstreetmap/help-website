+++
type = "question"
title = "wireshark v2.0.2 USB display filter doesn&#x27;t work"
description = '''Hi All, I&#x27;m using Wireshark v2.0.2 in Ubuntu 16.04, to capture USB traffic as root user. I set a display filter as &quot;usb.addr == 2.9.0&quot;, however, it doesn&#x27;t work in capture and after capture. Should I know if there is anything wrong? I have noticed there is no &quot;Apply&quot; button in v2.0.2 for display fil...'''
date = "2017-02-11T18:04:00Z"
lastmod = "2017-02-20T23:45:00Z"
weight = 59348
keywords = [ "work", "doesnt", "usb", "display-filter" ]
aliases = [ "/questions/59348" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark v2.0.2 USB display filter doesn't work](/questions/59348/wireshark-v202-usb-display-filter-doesnt-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59348-score" class="post-score" title="current number of votes">0</div><span id="post-59348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I'm using Wireshark v2.0.2 in Ubuntu 16.04, to capture USB traffic as root user. I set a display filter as "usb.addr == 2.9.0", however, it doesn't work in capture and after capture. Should I know if there is anything wrong? I have noticed there is no "Apply" button in v2.0.2 for display filter now.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-work" rel="tag" title="see questions tagged &#39;work&#39;">work</span> <span class="post-tag tag-link-doesnt" rel="tag" title="see questions tagged &#39;doesnt&#39;">doesnt</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '17, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/45304f349d18e88ae1ab87c74747a8b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stndfir&#39;s gravatar image" /><p><span>stndfir</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stndfir has no accepted answers">0%</span></p></div></div><div id="comments-container-59348" class="comments-container"></div><div id="comment-tools-59348" class="comment-tools"></div><div class="clear"></div><div id="comment-59348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59358"></span>

<div id="answer-container-59358" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59358-score" class="post-score" title="current number of votes">1</div><span id="post-59358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stndfir has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a string, so <code>usb.addr == "2.9.0"</code> should work</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '17, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59358" class="comments-container"><span id="59578"></span><div id="comment-59578" class="comment"><div id="post-59578-score" class="comment-score"></div><div class="comment-text"><p>Yes, it works now. Thanks.</p></div><div id="comment-59578-info" class="comment-info"><span class="comment-age">(20 Feb '17, 23:45)</span> <span class="comment-user userinfo">stndfir</span></div></div></div><div id="comment-tools-59358" class="comment-tools"></div><div class="clear"></div><div id="comment-59358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


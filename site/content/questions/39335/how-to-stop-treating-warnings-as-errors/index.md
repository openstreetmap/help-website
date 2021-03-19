+++
type = "question"
title = "How to stop treating warnings as errors"
description = '''I&#x27;ve gotten to the point in my custom Wireshark build for Windows that all that&#x27;s left now is warnings--but these warnings are being treated as errors. As the vast majority of them are harmless (unused variabled, for example) is there any way to set it so that warnings are not treated as errors?'''
date = "2015-01-21T05:41:00Z"
lastmod = "2015-01-22T16:05:00Z"
weight = 39335
keywords = [ "windows", "source", "errors", "warnings" ]
aliases = [ "/questions/39335" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to stop treating warnings as errors](/questions/39335/how-to-stop-treating-warnings-as-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39335-score" class="post-score" title="current number of votes">0</div><span id="post-39335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've gotten to the point in my custom Wireshark build for Windows that all that's left now is warnings--but these warnings are being treated as errors. As the vast majority of them are harmless (unused variabled, for example) is there any way to set it so that warnings are not treated as errors?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-warnings" rel="tag" title="see questions tagged &#39;warnings&#39;">warnings</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '15, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p><span>mehubb985</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39335" class="comments-container"></div><div id="comment-tools-39335" class="comment-tools"></div><div class="clear"></div><div id="comment-39335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39338"></span>

<div id="answer-container-39338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39338-score" class="post-score" title="current number of votes">2</div><span id="post-39338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For Windows nmake builds, edit the following part of config.nmake as described in the comment:</p><pre><code>#Comment out the following if warnings are not to be treated as errors
WARNINGS_ARE_ERRORS=-WX</code></pre><p>As Jaap says though, there should be no warnings, all of the core Wireshark code is expected to build without any warnings and your custom code should too.</p><p>You might also run the perl check* scripts in tools, as they also pick up errors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39338" class="comments-container"></div><div id="comment-tools-39338" class="comment-tools"></div><div class="clear"></div><div id="comment-39338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39337"></span>

<div id="answer-container-39337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39337-score" class="post-score" title="current number of votes">1</div><span id="post-39337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at this configure option <code>--enable-warnings-as-errors</code>. Assigning it 'no' should prevent them from happening. But even better, clean up your code to get rid of them, if you can.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39337" class="comments-container"><span id="39359"></span><div id="comment-39359" class="comment"><div id="post-39359-score" class="comment-score"></div><div class="comment-text"><p>If a variable is reported as unused, either 1) it's not useful and should be removed or 2) it <em>is</em> useful and there's a typo or some other sort of bug in your code that means it's not being used when it should be.</p><p>That's why the Wireshark buildbots turn on warnings-as-errors whenever possible.</p></div><div id="comment-39359-info" class="comment-info"><span class="comment-age">(22 Jan '15, 16:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-39337" class="comment-tools"></div><div class="clear"></div><div id="comment-39337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


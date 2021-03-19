+++
type = "question"
title = "tshark string search on Windows"
description = '''Hi, When using   c:&#92;tshark -r input frame contains &quot;aaa&quot; -w output   everything is fine. When the string is &quot;aaa bbb&quot; I get an error on windows 7 saying &quot;bbb&quot; was unexpected in this context.  Any clue what is the issue? Thanks, zf'''
date = "2013-04-25T10:38:00Z"
lastmod = "2013-04-25T15:42:00Z"
weight = 20805
keywords = [ "tshark" ]
aliases = [ "/questions/20805" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark string search on Windows](/questions/20805/tshark-string-search-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20805-score" class="post-score" title="current number of votes">0</div><span id="post-20805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When using</p><blockquote><p><code>c:\tshark -r input frame contains "aaa" -w output</code></p></blockquote><p>everything is fine.</p><p>When the string is "aaa bbb" I get an error on windows 7 saying "bbb" was unexpected in this context.</p><p>Any clue what is the issue?</p><p>Thanks, zf</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '13, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/28f4bbeb0d0223301de3f19d1a312af1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zfme&#39;s gravatar image" /><p><span>zfme</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zfme has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '13, 11:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-20805" class="comments-container"></div><div id="comment-tools-20805" class="comment-tools"></div><div class="clear"></div><div id="comment-20805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20807"></span>

<div id="answer-container-20807" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20807-score" class="post-score" title="current number of votes">0</div><span id="post-20807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zfme has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a quoting 'problem' of the DOS box. Please try tripple-quotes.</p><blockquote><p><code>c:\tshark -r input frame contains """aaa bbb""" -w output</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '13, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20807" class="comments-container"><span id="20808"></span><div id="comment-20808" class="comment"><div id="post-20808-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. It works.</p></div><div id="comment-20808-info" class="comment-info"><span class="comment-age">(25 Apr '13, 14:38)</span> <span class="comment-user userinfo">zfme</span></div></div><span id="20809"></span><div id="comment-20809" class="comment"><div id="post-20809-score" class="comment-score"></div><div class="comment-text"><p><span>@zfme</span></p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-20809-info" class="comment-info"><span class="comment-age">(25 Apr '13, 15:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20811"></span><div id="comment-20811" class="comment"><div id="post-20811-score" class="comment-score"></div><div class="comment-text"><p>For PowerShell you'll need to use a double escape method to quote the argument, e.g. a "\" for the Windows command processor and with a "`" for the PowerShell processor giving:</p><p><code> c:\tshark -r input frame contains `"aaa bbb`" -w output</code></p><p>See this <a href="http://edgylogic.com/blog/powershell-and-external-commands-done-right/">blog</a> entry for more on the intricacies of calling external commands from Powershell.</p></div><div id="comment-20811-info" class="comment-info"><span class="comment-age">(25 Apr '13, 15:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-20807" class="comment-tools"></div><div class="clear"></div><div id="comment-20807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


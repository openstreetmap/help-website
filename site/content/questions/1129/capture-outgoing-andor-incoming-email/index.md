+++
type = "question"
title = "capture outgoing and/or incoming email"
description = '''how can I capture an outgoing or incoming email by the emailadress? thanks'''
date = "2010-11-26T06:25:00Z"
lastmod = "2010-12-01T01:02:00Z"
weight = 1129
keywords = [ "capture-filter" ]
aliases = [ "/questions/1129" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture outgoing and/or incoming email](/questions/1129/capture-outgoing-andor-incoming-email)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1129-score" class="post-score" title="current number of votes">0</div><span id="post-1129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can I capture an outgoing or incoming email by the emailadress?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '10, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/9205b68b37640454232f5b50fae15df5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kurtw&#39;s gravatar image" /><p><span>kurtw</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kurtw has no accepted answers">0%</span></p></div></div><div id="comments-container-1129" class="comments-container"><span id="1132"></span><div id="comment-1132" class="comment"><div id="post-1132-score" class="comment-score"></div><div class="comment-text"><p>I don't think you can do it easily w/o resorting to a complicated capture filter that looks for specific characters at certain offsets. And that won't even work reliably unless the emails are being sent individually.</p></div><div id="comment-1132-info" class="comment-info"><span class="comment-age">(26 Nov '10, 09:08)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-1129" class="comment-tools"></div><div class="clear"></div><div id="comment-1129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1136"></span>

<div id="answer-container-1136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1136-score" class="post-score" title="current number of votes">0</div><span id="post-1136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could just capture all the email based on the TCP port used and then apply a display filter such as:</p><pre><code>frame contains &quot;[email protected]&quot;</code></pre><p>or use</p><pre><code>frame contains &quot;userid&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '10, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-1136" class="comments-container"><span id="1141"></span><div id="comment-1141" class="comment"><div id="post-1141-score" class="comment-score"></div><div class="comment-text"><p>I had assumed the OP couldn't contend with the main SMTP feed's volume but I guess I could be wrong. I should stop thinking that <em>everyone</em> has to deal with massive scaling problems! :)</p></div><div id="comment-1141-info" class="comment-info"><span class="comment-age">(27 Nov '10, 18:25)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-1136" class="comment-tools"></div><div class="clear"></div><div id="comment-1136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1187"></span>

<div id="answer-container-1187" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1187-score" class="post-score" title="current number of votes">0</div><span id="post-1187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capturefilter I use: tcp port 110 or tcp port 25 or tcp port 143</p><p>Displayfilter I use: imf.from contains "<span class="__cf_email__" data-cfemail="8eebe3efe7e2cee3efe7e2a0ede1e3">[email protected]</span>" or imf.to contains "<span class="__cf_email__" data-cfemail="284d454941446845494144064b4745">[email protected]</span>" or imf.sender contains "<span class="__cf_email__" data-cfemail="5a3f373b33361a373b333674393537">[email protected]</span>"</p><p>How can I export the filtered Emails to separatly files?</p><p>thanks k.w.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '10, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/9205b68b37640454232f5b50fae15df5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kurtw&#39;s gravatar image" /><p><span>kurtw</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kurtw has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Dec '10, 01:03</strong> </span></p></div></div><div id="comments-container-1187" class="comments-container"></div><div id="comment-tools-1187" class="comment-tools"></div><div class="clear"></div><div id="comment-1187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


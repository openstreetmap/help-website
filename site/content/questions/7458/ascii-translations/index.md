+++
type = "question"
title = "ASCII Translations"
description = '''Pardon the (probably) stupid question, but I&#x27;m completely new to Wireshark. I&#x27;ve just captured some packets and am trying to read them. One of the lines from the capture looks like this: 0030 32 30 2d 32 32 30 32 53 05 f1 32 7d 05 f1 32 0b 2.-22.2. .12&#x27;.12.  I thought that the right side was suppose...'''
date = "2011-11-15T19:22:00Z"
lastmod = "2011-11-16T03:06:00Z"
weight = 7458
keywords = [ "ascii" ]
aliases = [ "/questions/7458" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ASCII Translations](/questions/7458/ascii-translations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7458-score" class="post-score" title="current number of votes">1</div><span id="post-7458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Pardon the (probably) stupid question, but I'm completely new to Wireshark. I've just captured some packets and am trying to read them. One of the lines from the capture looks like this:</p><pre><code>0030  32 30 2d 32 32 30 32 53  05 f1 32 7d 05 f1 32 0b   2.-22.2. .12&#39;.12.</code></pre><p>I thought that the right side was supposed to be the ASCII translation of the raw hex dump on the left. The first byte <code>32</code> is indeed the number "2" as shown on the right. However, the second byte, <code>30</code> is the digit "0". This is translated to "." on the ASCII side, which is wrong. The next 3 digits are right, but the forth one is wrong again. Is something configured incorrectly?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ascii" rel="tag" title="see questions tagged &#39;ascii&#39;">ascii</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '11, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/60393b54fe5dcc1f85954746740ec2cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prezt&#39;s gravatar image" /><p><span>prezt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prezt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Nov '11, 19:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7458" class="comments-container"><span id="7459"></span><div id="comment-7459" class="comment"><div id="post-7459-score" class="comment-score"></div><div class="comment-text"><p>That's strange. Can you upload this packet capture (sanitized as necessary) to <a href="http://www.cloudshark.org">cloudshark</a> and post a link here?</p></div><div id="comment-7459-info" class="comment-info"><span class="comment-age">(15 Nov '11, 19:31)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="7460"></span><div id="comment-7460" class="comment"><div id="post-7460-score" class="comment-score"></div><div class="comment-text"><p>I just validated tshark and Wireshark using a recent SVN build on OSX 10.7.2:</p><pre><code>0030  32 30 2d 32 32 30 32 0a                           20-2202.</code></pre><p>What version is your Wireshark and OS?</p></div><div id="comment-7460-info" class="comment-info"><span class="comment-age">(15 Nov '11, 19:52)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-7458" class="comment-tools"></div><div class="clear"></div><div id="comment-7458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7467"></span>

<div id="answer-container-7467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7467-score" class="post-score" title="current number of votes">0</div><span id="post-7467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could this be a font related problem? What font are you using (Edit -&gt; Preferences -&gt; Font)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '11, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-7467" class="comments-container"></div><div id="comment-tools-7467" class="comment-tools"></div><div class="clear"></div><div id="comment-7467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


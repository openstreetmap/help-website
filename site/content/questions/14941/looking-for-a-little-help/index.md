+++
type = "question"
title = "Looking for a little help"
description = '''I&#x27;m using a couple of Color Rules that were given to me during a WireShark class with Laura Chappell. The color rule that this network is hitting is as follows: (tcp.window_size &amp;lt; 1460) &amp;amp;&amp;amp; (tcp.flags.reset == 0) I know that this is a color rule to find Windows Zero Errors and Window Size ...'''
date = "2012-10-11T12:37:00Z"
lastmod = "2012-10-17T11:35:00Z"
weight = 14941
keywords = [ "network" ]
aliases = [ "/questions/14941" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Looking for a little help](/questions/14941/looking-for-a-little-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14941-score" class="post-score" title="current number of votes">0</div><span id="post-14941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a couple of Color Rules that were given to me during a WireShark class with Laura Chappell. The color rule that this network is hitting is as follows: <strong><em>(tcp.window_size &lt; 1460) &amp;&amp; (tcp.flags.reset == 0)</em></strong></p><p>I know that this is a color rule to find Windows Zero Errors and Window Size under 1460. The question: Is this rule correct or is there a better rule? Since it isn't exactly a Window Zero error should I worry about it? I've attached a screen shot of my Wireshark. Orange is the Color Rule above.</p><p>Thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/capture_3.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/a77c2eda1ae7229d29bc1c1623463655?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="q2srw77&#39;s gravatar image" /><p><span>q2srw77</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="q2srw77 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '12, 12:39</strong> </span></p></div></div><div id="comments-container-14941" class="comments-container"></div><div id="comment-tools-14941" class="comment-tools"></div><div class="clear"></div><div id="comment-14941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14942"></span>

<div id="answer-container-14942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14942-score" class="post-score" title="current number of votes">0</div><span id="post-14942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have a similar coloring rule, but mine does consider the possibility that Wireshark hasn't seen the Three Way Handshake and thus doesn't know about the scaling factor:</p><p><code>(tcp.window_size &lt; 1460) and not (tcp.flags.reset==1 or tcp.window_size_scalefactor == -1)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14942" class="comments-container"></div><div id="comment-tools-14942" class="comment-tools"></div><div class="clear"></div><div id="comment-14942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15066"></span>

<div id="answer-container-15066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15066-score" class="post-score" title="current number of votes">0</div><span id="post-15066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your coloring rule only shows frames with a window size under 1460 and TCP packets that do not have the RESET flag set. Jasper's reduces false positives further by taking the scale factor out of the equation. You could have a window size of less than 1460 and still not have a full window (yours are between 251 and 256).</p><p>You can use Wireshark's built-in analysis to write a coloring rule for zero window packets: tcp.analysis.zero_window</p><p>That will get you zero window packets while excluding small windows.</p><p>-Greg</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/6af533edcd07f58511d208454431454d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thechaosmachine&#39;s gravatar image" /><p><span>thechaosmachine</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thechaosmachine has no accepted answers">0%</span></p></div></div><div id="comments-container-15066" class="comments-container"></div><div id="comment-tools-15066" class="comment-tools"></div><div class="clear"></div><div id="comment-15066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


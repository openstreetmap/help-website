+++
type = "question"
title = "Error message shows up when I click capture new packets"
description = '''The following message shows up when I click on &#x27;Start a new live capture&#x27;: &#x27;The capture session could not be initiated (failed to set hardware filter to promiscuous mode). Please check that &quot;&#92;Device&#92;NPF_{27E9DDAE-C3B4-420D-9009-6FE117D94BAC}&quot; is the proper interface. Help can be found at:  http://wi...'''
date = "2014-03-17T06:35:00Z"
lastmod = "2014-03-17T12:54:00Z"
weight = 30883
keywords = [ "interface", "error" ]
aliases = [ "/questions/30883" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error message shows up when I click capture new packets](/questions/30883/error-message-shows-up-when-i-click-capture-new-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30883-score" class="post-score" title="current number of votes">0</div><span id="post-30883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following message shows up when I click on 'Start a new live capture':</p><p>'The capture session could not be initiated (failed to set hardware filter to promiscuous mode).</p><p>Please check that "\Device\NPF_{27E9DDAE-C3B4-420D-9009-6FE117D94BAC}" is the proper interface.</p><p>Help can be found at:</p><pre><code>   http://wiki.wireshark.org/WinPcap
   http://wiki.wireshark.org/CaptureSetup&#39;</code></pre><p>Please help me and tell me what to do.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/6e9e3fa1243a0402df6702d2e7c02e0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coolboy&#39;s gravatar image" /><p><span>Coolboy</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coolboy has no accepted answers">0%</span></p></div></div><div id="comments-container-30883" class="comments-container"><span id="30885"></span><div id="comment-30885" class="comment"><div id="post-30885-score" class="comment-score"></div><div class="comment-text"><p>Have you actually read the wiki pages? What section of CaptureSetup is applicable in your situation? What is your network setup, and how are you connected to it? What is the type of network interface you intend to use?</p></div><div id="comment-30885-info" class="comment-info"><span class="comment-age">(17 Mar '14, 07:03)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-30883" class="comment-tools"></div><div class="clear"></div><div id="comment-30883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30900"></span>

<div id="answer-container-30900" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30900-score" class="post-score" title="current number of votes">1</div><span id="post-30900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Coolboy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The capture session could not be initiated (failed to set hardware filter to promiscuous mode)</p></blockquote><p>Try using the Capture -&gt; Options menu item, selecting the interface on which you want to capture, turn off promiscuous mode, and start capturing. 802.11 interfaces often don't support promiscuous mode on Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '14, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30900" class="comments-container"></div><div id="comment-tools-30900" class="comment-tools"></div><div class="clear"></div><div id="comment-30900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


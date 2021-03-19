+++
type = "question"
title = "How to set up TCP receive window field as column?"
description = '''Hello, I would like to set up TCP RWIN as column in order to check the formula Throughput&amp;lt;or=RWIN/RTT. But, I don&#x27;t five where TCP Receive Window in my traces. Could U help me please? Thank U so much!'''
date = "2015-05-23T11:43:00Z"
lastmod = "2015-05-23T19:37:00Z"
weight = 42631
keywords = [ "custom_column" ]
aliases = [ "/questions/42631" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to set up TCP receive window field as column?](/questions/42631/how-to-set-up-tcp-receive-window-field-as-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42631-score" class="post-score" title="current number of votes">0</div><span id="post-42631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to set up TCP RWIN as column in order to check the formula Throughput&lt;or=RWIN/RTT. But, I don't five where TCP Receive Window in my traces.</p><p>Could U help me please?</p><p>Thank U so much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-custom_column" rel="tag" title="see questions tagged &#39;custom_column&#39;">custom_column</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '15, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/2cdecc30672e5166a3450085c3dff764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mattini&#39;s gravatar image" /><p><span>Mattini</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mattini has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '15, 19:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42631" class="comments-container"></div><div id="comment-tools-42631" class="comment-tools"></div><div class="clear"></div><div id="comment-42631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42632"></span>

<div id="answer-container-42632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42632-score" class="post-score" title="current number of votes">0</div><span id="post-42632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just go to Preferences -&gt; Columns and add a column with field type "custom", then enter "tcp.window_size_value" as Field Name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '15, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42632" class="comments-container"><span id="42634"></span><div id="comment-42634" class="comment"><div id="post-42634-score" class="comment-score"></div><div class="comment-text"><p>Or you use the field tcp.window_size if you want to work with the calculated scaling window value.</p></div><div id="comment-42634-info" class="comment-info"><span class="comment-age">(23 May '15, 19:37)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-42632" class="comment-tools"></div><div class="clear"></div><div id="comment-42632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


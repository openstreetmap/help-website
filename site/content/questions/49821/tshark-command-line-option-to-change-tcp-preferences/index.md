+++
type = "question"
title = "Tshark command-line option to change TCP preferences"
description = '''Hi guys, I am swathi. I have on doubt. what is Tshark command to disable and enable for &quot;Allow subdissector to reassemble TCP streams&quot;? Regards, Swathi.'''
date = "2016-02-04T07:07:00Z"
lastmod = "2016-02-04T07:12:00Z"
weight = 49821
keywords = [ "tshark", "command-line", "options" ]
aliases = [ "/questions/49821" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark command-line option to change TCP preferences](/questions/49821/tshark-command-line-option-to-change-tcp-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am swathi. I have on doubt.</p><p>what is Tshark command to disable and enable for "Allow subdissector to reassemble TCP streams"?</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags">tshark command-line options</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p>swathi jakkam<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '16, 13:47</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-49821" class="comments-container"></div><div id="comment-tools-49821" class="comment-tools"></div><div class="clear"></div><div id="comment-49821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49823"></span>

<div id="answer-container-49823" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49823-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to override a preference setting for this, using the "-o" parameter:</p><p>tshark -o tcp.desegment_tcp_streams:FALSE</p><p>tshark -o tcp.desegment_tcp_streams:TRUE</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '16, 07:12</p></div></div><div id="comments-container-49823" class="comments-container"><span id="49882"></span><div id="comment-49882" class="comment"><div id="post-49882-score" class="comment-score"></div><div class="comment-text"><p>Thanks,Jasper In wireshrk I am facing another issues.</p><p>I am sending HTTP requests for same url, So I am getting HTTP responses. But In Some HTTP responses Info field as "HTTP/1.1 403 Forbidden (text/html)" and Some Http responses Info field as "Continuation or non-</p><p>HTTP traffic".But data is seeing as TCP segments.Can u guys tell me the reason and solution about this issue.</p><p>Regards, Swathi.</p></div><div id="comment-49882-info" class="comment-info"><span class="comment-age">(04 Feb '16, 23:36)</span> swathi jakkam</div></div><span id="49886"></span><div id="comment-49886" class="comment"><div id="post-49886-score" class="comment-score"></div><div class="comment-text"><p>@swathi jakkam, your last comment is a separate question almost unrelated to the original one, so please do create a new Question of it (you should be able to use "convert to question" on your own comments to save you some typing).</p></div><div id="comment-49886-info" class="comment-info"><span class="comment-age">(05 Feb '16, 01:18)</span> sindy</div></div></div><div id="comment-tools-49823" class="comment-tools"></div><div class="clear"></div><div id="comment-49823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


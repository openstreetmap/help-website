+++
type = "question"
title = "No interface"
description = '''I installed wireshark on a dell laptop, 64 bit, windows 10. However when I go to try to capture packets no interface is shown? How do I get it to allow me to select my wireless interface?'''
date = "2017-06-06T14:16:00Z"
lastmod = "2017-06-06T17:34:00Z"
weight = 61805
keywords = [ "interface" ]
aliases = [ "/questions/61805" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No interface](/questions/61805/no-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61805-score" class="post-score" title="current number of votes">0</div><span id="post-61805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed wireshark on a dell laptop, 64 bit, windows 10. However when I go to try to capture packets no interface is shown? How do I get it to allow me to select my wireless interface?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '17, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/bac5b01b64f5482ba21673873a07e192?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kolive10&#39;s gravatar image" /><p><span>kolive10</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kolive10 has no accepted answers">0%</span></p></div></div><div id="comments-container-61805" class="comments-container"></div><div id="comment-tools-61805" class="comment-tools"></div><div class="clear"></div><div id="comment-61805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61806"></span>

<div id="answer-container-61806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61806-score" class="post-score" title="current number of votes">0</div><span id="post-61806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture wireless on Windows you should try to install <a href="https://nmap.org/npcap/">npcap</a> instead of WinPCAP. Because WinPCAP can only capture wireless on Windows with an AirPCAP adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '17, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61806" class="comments-container"></div><div id="comment-tools-61806" class="comment-tools"></div><div class="clear"></div><div id="comment-61806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61807"></span>

<div id="answer-container-61807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61807-score" class="post-score" title="current number of votes">0</div><span id="post-61807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You probably didn't select the option to start the NPF driver when Windows starts. Without the NPF driver running, you will not see any adapters.</p><p>From command prompt, enter: <strong>sc start npf</strong></p><p>This will start the npf driver.</p><p>If you want it to start with Windows, enter the command below:</p><p><strong>sc config npf start= auto</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '17, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-61807" class="comments-container"></div><div id="comment-tools-61807" class="comment-tools"></div><div class="clear"></div><div id="comment-61807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


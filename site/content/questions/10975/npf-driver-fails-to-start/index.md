+++
type = "question"
title = "NPF Driver fails to start"
description = '''Microsoft Windows [Version 6.1.7601] Copyright (c) 2009 Microsoft Corporation. All rights reserved.  C:&#92;Users&#92;JOURIS SIMBOLON&amp;gt;sc qc npf [SC] QueryServiceConfig SUCCESS  SERVICE_NAME: npf  TYPE : 1 KERNEL_DRIVER  START_TYPE : 3 DEMAND_START  ERROR_CONTROL : 1 NORMAL  BINARY_PATH_NAME : system32&#92;dr...'''
date = "2012-05-15T00:46:00Z"
lastmod = "2016-11-01T10:09:00Z"
weight = 10975
keywords = [ "windows", "winpcap", "npf" ]
aliases = [ "/questions/10975" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [NPF Driver fails to start](/questions/10975/npf-driver-fails-to-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10975-score" class="post-score" title="current number of votes">0</div><span id="post-10975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\JOURIS SIMBOLON&gt;sc qc npf
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: npf
        TYPE               : 1  KERNEL_DRIVER
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : system32\drivers\NPF.sys
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : WinPcap Packet Driver (NPF)
        DEPENDENCIES       :
        SERVICE_START_NAME :

C:\Users\JOURIS SIMBOLON&gt;sc start npf
[SC] StartService: OpenService FAILED 5:

Access is denied.

C:\Users\JOURIS SIMBOLON&gt;</code></pre><p>See my own... I don't know what happened with my computer...</p><p>Maybe, you have suggestion what should I do to fix it.. Thanks before.. GBU</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-npf" rel="tag" title="see questions tagged &#39;npf&#39;">npf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/c65893f227fbf7e91f2349a15dd33a6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Simbolon&#39;s gravatar image" /><p><span>Simbolon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Simbolon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>15 May '12, 01:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10975" class="comments-container"></div><div id="comment-tools-10975" class="comment-tools"></div><div class="clear"></div><div id="comment-10975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="10977"></span>

<div id="answer-container-10977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10977-score" class="post-score" title="current number of votes">0</div><span id="post-10977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need Administrator privilege to start a service. Open your command prompt by right clicking the icon and selecting "Run as administrator".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10977" class="comments-container"></div><div id="comment-tools-10977" class="comment-tools"></div><div class="clear"></div><div id="comment-10977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10979"></span>

<div id="answer-container-10979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10979-score" class="post-score" title="current number of votes">0</div><span id="post-10979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Error Nr. 5</strong> means: <strong>NO ACCESS</strong>. Please start the service as administrator using either of these ways:</p><p><strong>Elevated DOS prompt</strong><br />
</p><ol><li>Click the Start button</li><li>In the Search box, type command prompt.</li><li>In the list of results, right-click Command Prompt, and then click Run as administrator. If you are prompted for an administrator password or confirmation, type the password or provide confirmation.</li></ol><p>Within that DOS/CMD box run this command</p><blockquote><p><code>sc start npf</code></p></blockquote><p><strong>runas</strong><br />
Use <strong>runas</strong> to start the service in any DOS box.</p><blockquote><p><code>runas /user:administrator sc start npf</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '12, 01:34</strong> </span></p></div></div><div id="comments-container-10979" class="comments-container"></div><div id="comment-tools-10979" class="comment-tools"></div><div class="clear"></div><div id="comment-10979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39326"></span>

<div id="answer-container-39326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39326-score" class="post-score" title="current number of votes">0</div><span id="post-39326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can refer to this method <a href="https://ask.wireshark.org/questions/4843/the-npf-driver-isnt-running?page=1&amp;focusedAnswerId=38691#38691">https://ask.wireshark.org/questions/4843/the-npf-driver-isnt-running?page=1&amp;focusedAnswerId=38691#38691</a> to make your NPF driver start normally.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '15, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/0bc6696cb16a86e51f6ae1fd661a3bac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OliviaLewis&#39;s gravatar image" /><p><span>OliviaLewis</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OliviaLewis has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39326" class="comments-container"></div><div id="comment-tools-39326" class="comment-tools"></div><div class="clear"></div><div id="comment-39326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56904"></span>

<div id="answer-container-56904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56904-score" class="post-score" title="current number of votes">0</div><span id="post-56904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>run command prompt in administrator mode it will start.</p><p>enter code: net start npf</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/26cfc77e3e3c34b6ea1453dc6b3ae62c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karan9537&#39;s gravatar image" /><p><span>karan9537</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karan9537 has no accepted answers">0%</span></p></div></div><div id="comments-container-56904" class="comments-container"></div><div id="comment-tools-56904" class="comment-tools"></div><div class="clear"></div><div id="comment-56904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


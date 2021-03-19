+++
type = "question"
title = "NPF driver"
description = '''When I start Wireshark Legacy I get the message NFP driver not running. What does that mean?'''
date = "2016-10-17T06:59:00Z"
lastmod = "2016-10-19T03:21:00Z"
weight = 56467
keywords = [ "winpcap", "npf", "wireshark" ]
aliases = [ "/questions/56467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NPF driver](/questions/56467/npf-driver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56467-score" class="post-score" title="current number of votes">0</div><span id="post-56467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I start Wireshark Legacy I get the message NFP driver not running. What does that mean?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-npf" rel="tag" title="see questions tagged &#39;npf&#39;">npf</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/66a65f6737565c9d9be98cefcb91c3bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liverpool61&#39;s gravatar image" /><p><span>liverpool61</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liverpool61 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '16, 07:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56467" class="comments-container"><span id="56468"></span><div id="comment-56468" class="comment"><div id="post-56468-score" class="comment-score"></div><div class="comment-text"><p>Presumably you actually mean the NPF driver. This is the capture driver (WinPcap) used by Wireshark and is installed by default with Wireshark. Do you see the same error with the normal (Qt version)?</p></div><div id="comment-56468-info" class="comment-info"><span class="comment-age">(17 Oct '16, 07:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56467" class="comment-tools"></div><div class="clear"></div><div id="comment-56467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56501"></span>

<div id="answer-container-56501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56501-score" class="post-score" title="current number of votes">1</div><span id="post-56501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that you refer to the NPF driver (as mentioned by Graham) you might need to start the driver manually.</p><p>This is done by running cmd.exe with administrative right. On the command line enter <strong>sc qc npf</strong></p><pre><code>C:\&gt;sc qc npf
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: npf
        TYPE               : 1  KERNEL_DRIVER
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : system32\drivers\npf.sys
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : NetGroup Packet Filter Driver
        DEPENDENCIES       :
        SERVICE_START_NAME :</code></pre><p>If your driver is not properly started, activate it with the command <strong>sc start npf</strong></p><p>To start the service automatically, use the command <strong>sc config npf start= auto</strong></p><p>Looks like this is still causing grief, since we had the question quite a while back:</p><p><a href="https://ask.wireshark.org/questions/1281/npf-driver-problem-in-windows-7?page=1&amp;focusedAnswerId=1282#1282">https://ask.wireshark.org/questions/1281/npf-driver-problem-in-windows-7?page=1&amp;focusedAnswerId=1282#1282</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '16, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-56501" class="comments-container"><span id="56504"></span><div id="comment-56504" class="comment"><div id="post-56504-score" class="comment-score"></div><div class="comment-text"><p>This is a reasonably common complaint, but I've never identified how it comes about. I've never had this issue and I've installed WinPcap on many systems. I've tended to put it down to finger trouble and\or overzealous security\management apps or PC speedup apps.</p></div><div id="comment-56504-info" class="comment-info"><span class="comment-age">(19 Oct '16, 03:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56501" class="comment-tools"></div><div class="clear"></div><div id="comment-56501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


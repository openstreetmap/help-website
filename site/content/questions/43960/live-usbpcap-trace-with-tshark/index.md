+++
type = "question"
title = "live USBPcap trace with tshark"
description = '''Is it possible to use USBPcap with tshark to get a live trace like it is with wireshark?'''
date = "2015-07-08T04:55:00Z"
lastmod = "2015-07-08T10:24:00Z"
weight = 43960
keywords = [ "usbpcap", "tshark" ]
aliases = [ "/questions/43960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [live USBPcap trace with tshark](/questions/43960/live-usbpcap-trace-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43960-score" class="post-score" title="current number of votes">0</div><span id="post-43960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use USBPcap with tshark to get a live trace like it is with wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/e11c789e2599b67daa0b0db281ac60d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dippy&#39;s gravatar image" /><p><span>dippy</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dippy has no accepted answers">0%</span></p></div></div><div id="comments-container-43960" class="comments-container"></div><div id="comment-tools-43960" class="comment-tools"></div><div class="clear"></div><div id="comment-43960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43975"></span>

<div id="answer-container-43975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43975-score" class="post-score" title="current number of votes">0</div><span id="post-43975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I do not have a USBPcap setup with me rigth now, but given the tutorial found <a href="http://desowin.org/usbpcap/tour.html">here</a> I would expect the following command to work when using USBPcap 1.0.0.7:</p><pre><code>USBPcapCMD.exe -d \\.\USBPcap2 -o - | &quot;C:\Program Files\Wireshark\tshark.exe&quot; -i</code></pre><p>Where you replace USBPcap2 by the filter value you are interested by.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43975" class="comments-container"></div><div id="comment-tools-43975" class="comment-tools"></div><div class="clear"></div><div id="comment-43975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


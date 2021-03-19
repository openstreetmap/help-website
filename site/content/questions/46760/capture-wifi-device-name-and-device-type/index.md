+++
type = "question"
title = "Capture Wifi device name and device type"
description = '''Hi, is there a way to capture the names and types of wifi enabled devices? With the source address I am able to see the manufacture but how is possible to see for example  Device Name: Johns iPhone Device Type: mobile phone Best regards'''
date = "2015-10-20T07:46:00Z"
lastmod = "2015-10-21T08:16:00Z"
weight = 46760
keywords = [ "device", "type", "name", "class" ]
aliases = [ "/questions/46760" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Wifi device name and device type](/questions/46760/capture-wifi-device-name-and-device-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46760-score" class="post-score" title="current number of votes">0</div><span id="post-46760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is there a way to capture the names and types of wifi enabled devices? With the source address I am able to see the manufacture but how is possible to see for example</p><p>Device Name: Johns iPhone</p><p>Device Type: mobile phone</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-device" rel="tag" title="see questions tagged &#39;device&#39;">device</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-class" rel="tag" title="see questions tagged &#39;class&#39;">class</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/ec14be866de9b736dd5ad2ba564b74c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YYYs&#39;s gravatar image" /><p><span>YYYs</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YYYs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '15, 07:46</strong> </span></p></div></div><div id="comments-container-46760" class="comments-container"></div><div id="comment-tools-46760" class="comment-tools"></div><div class="clear"></div><div id="comment-46760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46800"></span>

<div id="answer-container-46800" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46800-score" class="post-score" title="current number of votes">1</div><span id="post-46800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The simple answer to this question is NO. However, the specification for WiFi Simple Configuration, version 2.0 (WSCv2) does exchange certain device information during the set-up. For example, the manufacturer, model name, model number etc.</p><p>So if the device connects to the WiFi network using WSCv2 (sometimes referred to as WPSv2), then this information could be extracted from the connection establishment. This also applies to other connections that also utilize WPSv2. For example, WiFi Peer-to-Peer (referred to as WiFi Direct) uses WPSv2 to establish a connection between devices. Since WPSv2 is used, then the device information will also be exchanged.</p><p>If the device does <strong>NOT</strong> connect using WPSv2, then the WiFi specification does not require devices to exchange device specific information.</p><p>As for the device name, I have never seen that information being exchanged.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-46800" class="comments-container"></div><div id="comment-tools-46800" class="comment-tools"></div><div class="clear"></div><div id="comment-46800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


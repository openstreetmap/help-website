+++
type = "question"
title = "Can&#x27;t get VLAN on RTL8168 (win7 x32 x64, latest RTL driver 7.80.218.2014)"
description = '''Hi! I use Wireshark with RTL chip 8168. I installed latest driver and &quot;Realtek diagnostic utility&quot; programm. Then I created some different VLANs. all is work but when I try to capture data, I not get VLAN ID in frames. I read many information about it (wiki wireshark to) and still not decided this p...'''
date = "2014-05-19T21:43:00Z"
lastmod = "2014-05-19T23:20:00Z"
weight = 32925
keywords = [ "rtl8168", "vlan" ]
aliases = [ "/questions/32925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get VLAN on RTL8168 (win7 x32 x64, latest RTL driver 7.80.218.2014)](/questions/32925/cant-get-vlan-on-rtl8168-win7-x32-x64-latest-rtl-driver-7802182014)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32925-score" class="post-score" title="current number of votes">0</div><span id="post-32925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I use Wireshark with RTL chip 8168. I installed latest driver and "Realtek diagnostic utility" programm. Then I created some different VLANs. all is work but when I try to capture data, I not get VLAN ID in frames. I read many information about it (wiki wireshark to) and still not decided this problem. Priority and VLAN enabled in properties.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtl8168" rel="tag" title="see questions tagged &#39;rtl8168&#39;">rtl8168</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/b9f92c44d5cc1c2159e6bf803e0b60fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexanderDakis&#39;s gravatar image" /><p><span>AlexanderDakis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexanderDakis has no accepted answers">0%</span></p></div></div><div id="comments-container-32925" class="comments-container"></div><div id="comment-tools-32925" class="comment-tools"></div><div class="clear"></div><div id="comment-32925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32927"></span>

<div id="answer-container-32927" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32927-score" class="post-score" title="current number of votes">0</div><span id="post-32927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I decided this problem. In registry HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class{4D36E972-E325-11CE-BFC1-08002BE10318}\00XX was already key "MonitorModeEnabled" whit value 0. I changed it on 1 and now I can see VLANs. I thought this key need only for Intel chips, but and RTL chips its need too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/b9f92c44d5cc1c2159e6bf803e0b60fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexanderDakis&#39;s gravatar image" /><p><span>AlexanderDakis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexanderDakis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '14, 23:21</strong> </span></p></div></div><div id="comments-container-32927" class="comments-container"></div><div id="comment-tools-32927" class="comment-tools"></div><div class="clear"></div><div id="comment-32927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


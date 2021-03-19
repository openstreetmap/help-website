+++
type = "question"
title = "SSID Displayed in Column"
description = '''Hi. I&#x27;m capturing packet data using a AirPcap NX and cannot get the SSID to be displayed in the column. I go to the preferences, select columns, select add and try to locate the SSID field type. I cannot find this field type in the pull down menu. Are there other options to get the SSID field type? ...'''
date = "2012-07-03T14:18:00Z"
lastmod = "2012-07-10T13:40:00Z"
weight = 12423
keywords = [ "column", "ssid" ]
aliases = [ "/questions/12423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSID Displayed in Column](/questions/12423/ssid-displayed-in-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12423-score" class="post-score" title="current number of votes">0</div><span id="post-12423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I'm capturing packet data using a AirPcap NX and cannot get the SSID to be displayed in the column. I go to the preferences, select columns, select add and try to locate the SSID field type. I cannot find this field type in the pull down menu. Are there other options to get the SSID field type?</p><p>Thanks</p><p>Martin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-ssid" rel="tag" title="see questions tagged &#39;ssid&#39;">ssid</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '12, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/69b3d6d9c26ffeff826e3bddc4f81344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mrodriguez&#39;s gravatar image" /><p><span>Mrodriguez</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mrodriguez has no accepted answers">0%</span></p></div></div><div id="comments-container-12423" class="comments-container"></div><div id="comment-tools-12423" class="comment-tools"></div><div class="clear"></div><div id="comment-12423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12429"></span>

<div id="answer-container-12429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12429-score" class="post-score" title="current number of votes">1</div><span id="post-12429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The pull-down menu only shows a small number of the most commonly used fields and the SSID is not one of them. You can add it in either of two ways:</p><ol><li>From Preferences &gt; Columns click "Add". Select "Custom" from the pull-down menu as the field type and enter "wlan_mgt.ssid" as the field name.</li><li>Find the SSID field in a packet, right-click, and select "Apply as Column."</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12429" class="comments-container"><span id="12573"></span><div id="comment-12573" class="comment"><div id="post-12573-score" class="comment-score"></div><div class="comment-text"><p>Hi Jim. I was able to get the new cloumn with the "wlan_mgt.ssid" in the field. However, when I find the SSID field in a packet and I right-click, the "Apply as Column" options does not come up. I get several option one of them being "Apply as Filter" but nothing for "Apply as Column".</p><p>Thanks</p><p>Martin</p></div><div id="comment-12573-info" class="comment-info"><span class="comment-age">(10 Jul '12, 13:05)</span> <span class="comment-user userinfo">Mrodriguez</span></div></div><span id="12574"></span><div id="comment-12574" class="comment"><div id="post-12574-score" class="comment-score"></div><div class="comment-text"><p>"Apply as Column" appears right above "Apply as Filter." Are you on the latest version of Wireshark? "Apply as Column" has been around for a while now, but if you're using an older version of Wireshark it might not have that feature. The current stable release if 1.8.0.</p></div><div id="comment-12574-info" class="comment-info"><span class="comment-age">(10 Jul '12, 13:40)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-12429" class="comment-tools"></div><div class="clear"></div><div id="comment-12429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


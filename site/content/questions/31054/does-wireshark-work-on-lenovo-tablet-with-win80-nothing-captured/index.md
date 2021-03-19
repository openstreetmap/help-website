+++
type = "question"
title = "Does Wireshark work on Lenovo Tablet with win8.0? (nothing captured)"
description = '''I am trying to find out why &quot;something&quot; is downloading hundreds of kbytes of data as soon as the internet connection is established. This kills the satellite phone which is connected via USB, but I see the same spurious data on a bluetooth connected 3G phone. I am running a new install of WS, with n...'''
date = "2014-03-21T08:58:00Z"
lastmod = "2014-03-24T03:10:00Z"
weight = 31054
keywords = [ "windows", "8" ]
aliases = [ "/questions/31054" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark work on Lenovo Tablet with win8.0? (nothing captured)](/questions/31054/does-wireshark-work-on-lenovo-tablet-with-win80-nothing-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31054-score" class="post-score" title="current number of votes">0</div><span id="post-31054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to find out why "something" is downloading hundreds of kbytes of data as soon as the internet connection is established. This kills the satellite phone which is connected via USB, but I see the same spurious data on a bluetooth connected 3G phone.</p><p>I am running a new install of WS, with no filters configured, and it shows absolutely no activity. This is despite me having set Properties for both Winpcap and Wireshark (executables) to run as Admin, and my own account is an Admin account. I have also reinstalled WS by running the install program as Administrator. What I have not done is installed Winpcap individually, as Administrator, but I have set its installed executable to run as Administrator.</p><p>There is something fundamentally wrong. I see four interfaces listed</p><p>Local area connection 1</p><p>Wifi</p><p>Local Area connection 2</p><p>Bluetooth Network Connection</p><p>and all four, under Details, show "Disconnected", which is obviously wrong since I hae a working and active connection to the bluetooth attached phone.</p><p>I have previously used WS under winXP and if I recall correctly it worked right away. It looks like the default config is NO filters, so the packet listing should show everything.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-8" rel="tag" title="see questions tagged &#39;8&#39;">8</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/610350468227f85be13d2346f37c1baf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Holtz&#39;s gravatar image" /><p><span>Peter Holtz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Holtz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '14, 09:27</strong> </span></p></div></div><div id="comments-container-31054" class="comments-container"></div><div id="comment-tools-31054" class="comment-tools"></div><div class="clear"></div><div id="comment-31054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31067"></span>

<div id="answer-container-31067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31067-score" class="post-score" title="current number of votes">0</div><span id="post-31067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WinPcap doesn't support Bluetooth capturing. If the phone appears as a PPP connection, that won't work either, as <a href="http://www.winpcap.org/misc/faq.htm#Q-5">WinPcap doesn't support capturing on PPP connections on Vista and later</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31067" class="comments-container"></div><div id="comment-tools-31067" class="comment-tools"></div><div class="clear"></div><div id="comment-31067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31107"></span>

<div id="answer-container-31107" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31107-score" class="post-score" title="current number of votes">0</div><span id="post-31107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I solved it finally with the win8 Resource Monitor. It shows traffic nicely, on all network connections.</p><p>What it often doesn't show is which process is generating the traffic. For example I see lots of small bits of data caused by PID 1424 but there is no obvious way to find which executable is PID 1424.</p><p>The issue was locating which win8 processes kill the connection to my satellite phone, which is only 9.6kbytes/sec. The biggest culprits turned out to be the Bing feature in IE10 (which can be uninstalled but you have to install another search engine first) and the Compatibility View feature in IE10 (which can be turned off, but it takes a while to find the checkbox). In comparison, Chrome is much worse and does a lot of background chatter and there is no way to disable it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '14, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/610350468227f85be13d2346f37c1baf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Holtz&#39;s gravatar image" /><p><span>Peter Holtz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Holtz has no accepted answers">0%</span></p></div></div><div id="comments-container-31107" class="comments-container"></div><div id="comment-tools-31107" class="comment-tools"></div><div class="clear"></div><div id="comment-31107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


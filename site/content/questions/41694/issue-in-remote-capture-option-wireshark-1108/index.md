+++
type = "question"
title = "Issue in remote capture option (Wireshark-1.10.8)"
description = '''Hi All We have a requirement to capture packets from a remote machine. We used the feature provided by Wireshark to get this done. But, i observed some issues while performing the remote capture. Following are the ones listed.   Remote interface link type listed as &quot;Unknown&quot;     When i forcefully st...'''
date = "2015-04-22T09:03:00Z"
lastmod = "2015-05-06T07:04:00Z"
weight = 41694
keywords = [ "remote-capture" ]
aliases = [ "/questions/41694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue in remote capture option (Wireshark-1.10.8)](/questions/41694/issue-in-remote-capture-option-wireshark-1108)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41694-score" class="post-score" title="current number of votes">0</div><span id="post-41694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All</p><p>We have a requirement to capture packets from a remote machine. We used the feature provided by Wireshark to get this done. But, i observed some issues while performing the remote capture. Following are the ones listed.</p><ul><li><p>Remote interface link type listed as "Unknown" <img src="https://osqa-ask.wireshark.org/upfiles/unknown-if.jpg" alt="alt text" /></p></li><li><p>When i forcefully start the capture i am getting error as "Could not set the capture buffer size!" <img src="https://osqa-ask.wireshark.org/upfiles/buffer-size.jpg" alt="alt text" /></p></li><li><p>Not able to apply capture filter, getting error as "Link type of the interface not specified". <img src="https://osqa-ask.wireshark.org/upfiles/capture-filter.jpg" alt="alt text" /></p></li></ul><p>Are these issues a known issues or is it due to a specific reason. I am using Wireshark-1.10.8 version (WinPcap-4.1.3) on Windows platform. Can anyone let me know what could be the issue. On the same interface i tried remote capture using Wireshark-1.6.1 version, it works fine.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Apr '15, 09:04</strong> </span></p></div></div><div id="comments-container-41694" class="comments-container"><span id="41695"></span><div id="comment-41695" class="comment"><div id="post-41695-score" class="comment-score"></div><div class="comment-text"><p>what is the WinPcap version on the remote machine and what is the OS and OS version there?</p></div><div id="comment-41695-info" class="comment-info"><span class="comment-age">(22 Apr '15, 09:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41779"></span><div id="comment-41779" class="comment"><div id="post-41779-score" class="comment-score"></div><div class="comment-text"><p>Remote machine OS and version = RHELv6.4 Since it is Linux we are using rpcapd to perform remote capture. We also observed that remote capturing works fine with Wireshark-1.6.x and 1.8.x versions. But fails in 1.10.x and 1.12.x versions.</p></div><div id="comment-41779-info" class="comment-info"><span class="comment-age">(24 Apr '15, 07:00)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="41882"></span><div id="comment-41882" class="comment"><div id="post-41882-score" class="comment-score"></div><div class="comment-text"><p>I am using rpcapd on Linux in order to connect remotely from Windows machine. Is there any constraint of using a specific version of rpcapd along with Wireshark-1.12.4 in order to work properly.</p></div><div id="comment-41882-info" class="comment-info"><span class="comment-age">(27 Apr '15, 05:55)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="42128"></span><div id="comment-42128" class="comment"><div id="post-42128-score" class="comment-score"></div><div class="comment-text"><p>Can anyone help on this issue ?</p></div><div id="comment-42128-info" class="comment-info"><span class="comment-age">(06 May '15, 07:04)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div></div><div id="comment-tools-41694" class="comment-tools"></div><div class="clear"></div><div id="comment-41694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


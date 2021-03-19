+++
type = "question"
title = "Weird Android DHCP"
description = '''I&#x27;m seeing strange DHCP behavior between Android and Windows and wanted to see if anyone here could make sense of it. It seems like Android is spamming a dozen or so discovers in a second, and ignoring anything the server says until the lease renewal time is up (from a prior connection). https://www...'''
date = "2015-09-02T09:22:00Z"
lastmod = "2015-09-04T10:31:00Z"
weight = 45599
keywords = [ "ics", "dhcp", "android", "windows7" ]
aliases = [ "/questions/45599" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Weird Android DHCP](/questions/45599/weird-android-dhcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45599-score" class="post-score" title="current number of votes">0</div><span id="post-45599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing strange DHCP behavior between Android and Windows and wanted to see if anyone here could make sense of it. It seems like Android is spamming a dozen or so discovers in a second, and ignoring anything the server says until the lease renewal time is up (from a prior connection).</p><p><a href="https://www.cloudshark.org/captures/e6dcb03e4e03">https://www.cloudshark.org/captures/e6dcb03e4e03</a></p><p>EDIT: There are comments attached to the capture.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ics" rel="tag" title="see questions tagged &#39;ics&#39;">ics</span> <span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/b3a36a856efb60f32f8d059c184a4102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lordbah&#39;s gravatar image" /><p><span>lordbah</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lordbah has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '15, 08:19</strong> </span></p></div></div><div id="comments-container-45599" class="comments-container"></div><div id="comment-tools-45599" class="comment-tools"></div><div class="clear"></div><div id="comment-45599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45629"></span>

<div id="answer-container-45629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45629-score" class="post-score" title="current number of votes">1</div><span id="post-45629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The DHCP server responses are broadcast, while the client asks for unicast responses. Therefore the responses don't seem to arrive.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '15, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-45629" class="comments-container"><span id="45636"></span><div id="comment-45636" class="comment"><div id="post-45636-score" class="comment-score"></div><div class="comment-text"><p>So that means Windows 7 ICS DHCP server isn't honoring the unicast flag. Well, it is only a SHOULD in the standard, right?</p><p>Sometimes Android does see the response even though it is broadcast.</p><p>There are a number of hits on setting this flag on Windows as a DHCP client. Nothing I can find about it with Windows as DHCP server. I'm interested to hear of workarounds - arcane registry settings or whatever that would cause Windows to unicast.</p><p>Windows Firewall has a setting "Allow unicast response to multicast or broadcast network traffic", but is set to Yes in all profiles so it shouldn't be causing this. (Action/Properties/Settings/Customize)</p></div><div id="comment-45636-info" class="comment-info"><span class="comment-age">(04 Sep '15, 10:31)</span> <span class="comment-user userinfo">lordbah</span></div></div></div><div id="comment-tools-45629" class="comment-tools"></div><div class="clear"></div><div id="comment-45629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


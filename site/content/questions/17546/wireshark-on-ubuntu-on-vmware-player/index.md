+++
type = "question"
title = "Wireshark on Ubuntu on VMware Player"
description = '''I recently installed Wireshark for Ubuntu on VMware Player. I had a problem with the interface, but that was solved when I ran Wireshark as root using sudo. I heard that was bad. How do I run it as a user with the interfaces appearing? I also get the below error when I decide to write it to a file. ...'''
date = "2013-01-07T21:02:00Z"
lastmod = "2013-01-08T09:54:00Z"
weight = 17546
keywords = [ "interface", "lua", "ubuntu", "vmware", "error" ]
aliases = [ "/questions/17546" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on Ubuntu on VMware Player](/questions/17546/wireshark-on-ubuntu-on-vmware-player)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17546-score" class="post-score" title="current number of votes">0</div><span id="post-17546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently installed Wireshark for Ubuntu on VMware Player. I had a problem with the interface, but that was solved when I ran Wireshark as root using sudo. I heard that was bad. How do I run it as a user with the interfaces appearing?</p><p>I also get the below error when I decide to write it to a file. Any idea how to resolve this?</p><blockquote><p>Lua: Error during loading: [string "/usr/share/wireshark/init.lua"]:45: dofile has been disabled</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '13, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/81c67f66311e7c60a0b1867f34570bb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalawh&#39;s gravatar image" /><p><span>dalawh</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalawh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '13, 21:02</strong> </span></p></div></div><div id="comments-container-17546" class="comments-container"></div><div id="comment-tools-17546" class="comment-tools"></div><div class="clear"></div><div id="comment-17546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17549"></span>

<div id="answer-container-17549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17549-score" class="post-score" title="current number of votes">1</div><span id="post-17549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges wiki page</a> for this.</p><p>The error comes from you forcing su root. This is a protective measure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17549" class="comments-container"><span id="17566"></span><div id="comment-17566" class="comment"><div id="post-17566-score" class="comment-score"></div><div class="comment-text"><p>I'm looking at: <a href="http://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup">http://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup</a></p><blockquote><p>The additional privileges are provided using the Linux Capabilities system where it is available and resort to setting the set-user-id bit of the dumpcap binary as a fall-back, where the Linux Capabilities system is not present (Debian GNU/kFreeBSD, Debian GNU/Hurd).</p></blockquote><p>Is there a tutorial on this?</p></div><div id="comment-17566-info" class="comment-info"><span class="comment-age">(08 Jan '13, 07:53)</span> <span class="comment-user userinfo">dalawh</span></div></div><span id="17568"></span><div id="comment-17568" class="comment"><div id="post-17568-score" class="comment-score"></div><div class="comment-text"><p>There is info on doing it manually yourself on the page Jaap linked to above. See the section headed "Setting network privileges for dumpcap".</p></div><div id="comment-17568-info" class="comment-info"><span class="comment-age">(08 Jan '13, 08:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="17572"></span><div id="comment-17572" class="comment"><div id="post-17572-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Thanks. I used "sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap" and everything started working.</p></div><div id="comment-17572-info" class="comment-info"><span class="comment-age">(08 Jan '13, 08:55)</span> <span class="comment-user userinfo">dalawh</span></div></div><span id="17575"></span><div id="comment-17575" class="comment"><div id="post-17575-score" class="comment-score"></div><div class="comment-text"><p>If Jaaps original answer helped (albeit with my little prompt) can you "accept" the answer (by clicking the checkmark icon next to it) for the benefit of others who may have the same issue.</p></div><div id="comment-17575-info" class="comment-info"><span class="comment-age">(08 Jan '13, 09:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-17549" class="comment-tools"></div><div class="clear"></div><div id="comment-17549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


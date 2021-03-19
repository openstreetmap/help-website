+++
type = "question"
title = "How do I capture packets on a Windows virtual server?"
description = '''Using Wireshark of course.'''
date = "2013-08-05T04:20:00Z"
lastmod = "2013-08-06T04:21:00Z"
weight = 23552
keywords = [ "packets", "virtual", "server" ]
aliases = [ "/questions/23552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture packets on a Windows virtual server?](/questions/23552/how-do-i-capture-packets-on-a-windows-virtual-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23552-score" class="post-score" title="current number of votes">0</div><span id="post-23552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark of course.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-virtual" rel="tag" title="see questions tagged &#39;virtual&#39;">virtual</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/36cc46dc73c9fa601464e94fc9edecb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhop&#39;s gravatar image" /><p><span>dhop</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhop has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '13, 13:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-23552" class="comments-container"><span id="23564"></span><div id="comment-23564" class="comment"><div id="post-23564-score" class="comment-score"></div><div class="comment-text"><p>Are you looking to capture on the VM host or in the VM itself?</p></div><div id="comment-23564-info" class="comment-info"><span class="comment-age">(05 Aug '13, 12:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="23582"></span><div id="comment-23582" class="comment"><div id="post-23582-score" class="comment-score"></div><div class="comment-text"><p>Looking at capturing in the VM itself. We have two VM host chassis with several virtual servers that were created in each one. One VM host is using Cisco 1000v for its virtual switch. The other one is currently using HP's virtual switch. I need to capture packets in both environments. I started with the 1000v environment and wanted to have a seperate VM server/workstation run Wireshark and have its virtual port be a destination SPAN port for another server's source port. When I do this, my virtual network to the wireshark virtual server (remote desktop access) is dropped. I will end up placing wireshark on the virtual server I want to capture packets to work around this issue. However, I want to be able to run wireshark on another virtual server so that it won't possibly cause problems on a production virtual server. I haven't started to work with the HP virtual switch.</p></div><div id="comment-23582-info" class="comment-info"><span class="comment-age">(06 Aug '13, 04:21)</span> <span class="comment-user userinfo">dhop</span></div></div></div><div id="comment-tools-23552" class="comment-tools"></div><div class="clear"></div><div id="comment-23552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23565"></span>

<div id="answer-container-23565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23565-score" class="post-score" title="current number of votes">1</div><span id="post-23565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps the following presentation given by <a href="https://ask.wireshark.org/users/145/jasper">Jasper Bongertz</a> at <a href="http://sharkfest.wireshark.org/sharkfest.11/index.html">Sharkfest '11</a> will be useful to you: <a href="http://sharkfest.wireshark.org/sharkfest.11/presentations/A-4_Bongertz-Wireshark_vs_the_Cloud.pdf">Wireshark vs. "The Cloud"</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23565" class="comments-container"><span id="23566"></span><div id="comment-23566" class="comment"><div id="post-23566-score" class="comment-score">1</div><div class="comment-text"><p>You can also check my blog for two posts explaining capture on VMware vSphere, in case that's what you need: <a href="http://blog.packet-foo.com/2013/04/capturing-packets-of-vmware-machines/">http://blog.packet-foo.com/2013/04/capturing-packets-of-vmware-machines/</a></p></div><div id="comment-23566-info" class="comment-info"><span class="comment-age">(05 Aug '13, 16:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-23565" class="comment-tools"></div><div class="clear"></div><div id="comment-23565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


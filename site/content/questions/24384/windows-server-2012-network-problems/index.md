+++
type = "question"
title = "Windows Server 2012 network problems"
description = '''I have setup Wireshark to run on a Windows Server 2012 machine. When starting a capture my response times from my remote locations and local traffic return a TTL timeout with the capture nics address. Connections for my users stop. I have setup a span port on my Cisco 3750 stack and triple check my ...'''
date = "2013-09-05T10:11:00Z"
lastmod = "2013-09-09T09:19:00Z"
weight = 24384
keywords = [ "windows", "problem", "2012", "server" ]
aliases = [ "/questions/24384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows Server 2012 network problems](/questions/24384/windows-server-2012-network-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24384-score" class="post-score" title="current number of votes">0</div><span id="post-24384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have setup Wireshark to run on a Windows Server 2012 machine. When starting a capture my response times from my remote locations and local traffic return a TTL timeout with the capture nics address. Connections for my users stop. I have setup a span port on my Cisco 3750 stack and triple check my setup to make sure they are setup correctly. I have the latest version of Wireshark and WinPcap. This is the only application running on the server. The server has 18 gb of ram and two Xeon processors. Is this a server 2012 issue? Could I have something set wrong? Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-2012" rel="tag" title="see questions tagged &#39;2012&#39;">2012</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/4f2fae4c7d2fcd477b1a4307f2db6f33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="na2013&#39;s gravatar image" /><p><span>na2013</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="na2013 has no accepted answers">0%</span></p></div></div><div id="comments-container-24384" class="comments-container"></div><div id="comment-tools-24384" class="comment-tools"></div><div class="clear"></div><div id="comment-24384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24487"></span>

<div id="answer-container-24487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24487-score" class="post-score" title="current number of votes">0</div><span id="post-24487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When starting a capture my response times from my remote locations and local traffic return a TTL timeout with the capture nics address.</p></blockquote><p>That could be caused by some kind of routing loop, created by the Win 2012 server.</p><p>If you capture on the server, it will receive packets that do not belong to itself (that's why you sniff on a mirror port ;-)). Now, if <strong>IP Forwarding</strong> is enabled on the server, it will receive those packets, Wireshark will see it, but the OS will <strong>not drop</strong> them. Instead it will froward them (route them ) to the appropriate next hop. This process will lower the TTL value of those packets by one <strong>and</strong> duplicate packets in your network!!</p><p>I'm not sure if that fully explains your problems, but it is worth checking if <strong>IP Forwarding is enabled on your Windows server 2012</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24487" class="comments-container"></div><div id="comment-tools-24487" class="comment-tools"></div><div class="clear"></div><div id="comment-24487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Which Interface to Monitor?"
description = '''Sorry, I&#x27;m a newbie to WireShark. After install on a workstation on my LAN, I see WireShark selects the local interface to monitor by default, but provides option to monitor a remote interface. This LAN has only one /24 subnet with an internet router (AdTran). Two wireless devices are also connected...'''
date = "2012-03-08T18:32:00Z"
lastmod = "2012-03-08T23:53:00Z"
weight = 9447
keywords = [ "interface" ]
aliases = [ "/questions/9447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which Interface to Monitor?](/questions/9447/which-interface-to-monitor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9447-score" class="post-score" title="current number of votes">0</div><span id="post-9447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sorry, I'm a newbie to WireShark. After install on a workstation on my LAN, I see WireShark selects the local interface to monitor by default, but provides option to monitor a remote interface. This LAN has only one /24 subnet with an internet router (AdTran). Two wireless devices are also connected on LAN side of router in bridge mode.</p><p>To accurately capture all traffic in/out from LAN/WAN, I think I need to monitor the LAN interface of my AdTran router, ya, i.e. monitoring my own interface will miss lots of traffic? But how do I cfg. WireShark to remotely monitor the LAN interface on the AdTran router/gateway? I see WireShark has option for remote interface but it asks for Host and Port. When I enter the LAN IP address of the Adtran router and guess Port 1, WireShark responds that it cannot find a server at that host.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/f7df6d5abe5f578848df8d0734711db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IT%20Tropolis&#39;s gravatar image" /><p><span>IT Tropolis</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IT Tropolis has no accepted answers">0%</span></p></div></div><div id="comments-container-9447" class="comments-container"></div><div id="comment-tools-9447" class="comment-tools"></div><div class="clear"></div><div id="comment-9447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9451"></span>

<div id="answer-container-9451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9451-score" class="post-score" title="current number of votes">0</div><span id="post-9451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The remote capture option requires WinPcap (with Rpcap) software on the remote machine to do the capturing. So unless your firewall is a windows system on which you can install WinPcap, you can't use the remote capture option to capture on the firewall.</p><p>Have a look at <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a> for strategies to capture the traffic of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '12, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9451" class="comments-container"></div><div id="comment-tools-9451" class="comment-tools"></div><div class="clear"></div><div id="comment-9451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


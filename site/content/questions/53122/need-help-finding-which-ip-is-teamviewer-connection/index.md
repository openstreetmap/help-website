+++
type = "question"
title = "Need help finding which IP is teamviewer connection"
description = '''I am trying to isolate the IP of a user who connects to my VM through Teamviewer, but can&#x27;t tell which IP is the connection through TeamViewer. What do I need to look for and what will tell me which connection is the one I&#x27;m looking for. I&#x27;m somewhat of a newbie with this program, and any and all he...'''
date = "2016-06-01T18:05:00Z"
lastmod = "2016-06-01T22:16:00Z"
weight = 53122
keywords = [ "ip", "teamviewer" ]
aliases = [ "/questions/53122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help finding which IP is teamviewer connection](/questions/53122/need-help-finding-which-ip-is-teamviewer-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53122-score" class="post-score" title="current number of votes">0</div><span id="post-53122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to isolate the IP of a user who connects to my VM through Teamviewer, but can't tell which IP is the connection through TeamViewer. What do I need to look for and what will tell me which connection is the one I'm looking for. I'm somewhat of a newbie with this program, and any and all help is appreciated. PS- capturing from VMWare Network Adapter VMNet8. My VM is a VirtualBox machine running Win10. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-teamviewer" rel="tag" title="see questions tagged &#39;teamviewer&#39;">teamviewer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/79f2a6bc0c588ed67afe5125e0e2762f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stark&#39;s gravatar image" /><p><span>stark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stark has no accepted answers">0%</span></p></div></div><div id="comments-container-53122" class="comments-container"></div><div id="comment-tools-53122" class="comment-tools"></div><div class="clear"></div><div id="comment-53122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53125"></span>

<div id="answer-container-53125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53125-score" class="post-score" title="current number of votes">1</div><span id="post-53125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TeamViewer needs to be able to traverse NATs and firewalls, so the application establishes, in both the "server" and "client" modes, a session to TeamViewer's servers on public IP addresses, and the TeamViewer's servers create tunnels between them (forward packets between the two sessions).</p><p>So searching for IP addresses from inside your company is useless as there is never a direct connection - unlike, e.g., in case of Remote Desktop or VNC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 22:16</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53125" class="comments-container"></div><div id="comment-tools-53125" class="comment-tools"></div><div class="clear"></div><div id="comment-53125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


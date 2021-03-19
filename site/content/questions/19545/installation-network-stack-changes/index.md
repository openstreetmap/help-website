+++
type = "question"
title = "Installation network stack changes"
description = '''I am seeing Network Stack differences on a mac Mini OS X Mountain Lion after installing WireShark.  What does Wireshark change in the system that might also effect my applications. Default socket buffer sizes? or something like that? What I saw before installing Wireshark were errors in a TCP/IP con...'''
date = "2013-03-15T14:15:00Z"
lastmod = "2013-03-15T17:32:00Z"
weight = 19545
keywords = [ "os", "installation", "changes" ]
aliases = [ "/questions/19545" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Installation network stack changes](/questions/19545/installation-network-stack-changes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19545-score" class="post-score" title="current number of votes">0</div><span id="post-19545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am seeing Network Stack differences on a mac Mini OS X Mountain Lion after installing WireShark.<br />
</p><p>What does Wireshark change in the system that might also effect my applications. Default socket buffer sizes? or something like that?</p><p>What I saw before installing Wireshark were errors in a TCP/IP connection under heavy load ( maxing out the 100MB switch between the two machines ).<br />
</p><p>As soon as I installed WireShark the errors suddenly disappeared.</p><p>Any Ideas would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-os" rel="tag" title="see questions tagged &#39;os&#39;">os</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/090bd9e0e75515e3cb25708579bb26a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcc&#39;s gravatar image" /><p><span>kcc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcc has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-19545" class="comments-container"></div><div id="comment-tools-19545" class="comment-tools"></div><div class="clear"></div><div id="comment-19545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19550"></span>

<div id="answer-container-19550" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19550-score" class="post-score" title="current number of votes">0</div><span id="post-19550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What does Wireshark change in the system that might also effect my applications.</p></blockquote><p>The permissions on the BPF devices, and the set of StartupItems (it installs one that changes the permissions on the BPF devices on a reboot). Those permissions have no effect on the networking stack (they're stored in the devfs file system, not in the networking stack).</p><blockquote><p>Default socket buffer sizes?</p></blockquote><p>No, it does not change the default socket buffer sizes or any other sysctl value.</p><p>Perhaps this is just a coincidence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19550" class="comments-container"></div><div id="comment-tools-19550" class="comment-tools"></div><div class="clear"></div><div id="comment-19550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


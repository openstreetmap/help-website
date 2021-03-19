+++
type = "question"
title = "Capture messages of remote cisco 7609 router interface on Linux"
description = '''Hi,  As the title says, i need to capture messages coming on a interface in cisco router from my linux system, IS there anyway? What configuration is required in cisco router'''
date = "2013-05-18T07:35:00Z"
lastmod = "2013-05-20T03:20:00Z"
weight = 21252
keywords = [ "router", "cisco", "remote" ]
aliases = [ "/questions/21252" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture messages of remote cisco 7609 router interface on Linux](/questions/21252/capture-messages-of-remote-cisco-7609-router-interface-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21252-score" class="post-score" title="current number of votes">0</div><span id="post-21252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, As the title says, i need to capture messages coming on a interface in cisco router from my linux system, IS there anyway? What configuration is required in cisco router</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/97e562765393e4c43615a9d3d11fc4d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chandra%20Sekhar&#39;s gravatar image" /><p><span>Chandra Sekhar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chandra Sekhar has no accepted answers">0%</span></p></div></div><div id="comments-container-21252" class="comments-container"></div><div id="comment-tools-21252" class="comment-tools"></div><div class="clear"></div><div id="comment-21252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21290"></span>

<div id="answer-container-21290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21290-score" class="post-score" title="current number of votes">0</div><span id="post-21290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm pretty sure your Linux system is connected to the 7609 via a switch (either separate access switch or directly to a switch blade in the 7609). So, you need to configure a mirror/span port on that switch (or use a physical TAP).</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</code><br />
</p></blockquote><p>If you want to capture 'remote' traffic take a look at RSPAN.</p><blockquote><p><code>http://www.cisco.com/en/US/docs/routers/7600/ios/15S/configuration/guide/span.html</code><br />
</p></blockquote><p>Another method would be a GRE tunnel to redirect the traffic</p><blockquote><p><code>http://www.infosecwriters.com/texts.php?op=display&amp;id=41</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21290" class="comments-container"></div><div id="comment-tools-21290" class="comment-tools"></div><div class="clear"></div><div id="comment-21290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


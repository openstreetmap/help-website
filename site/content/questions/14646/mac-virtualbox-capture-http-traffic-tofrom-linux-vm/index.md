+++
type = "question"
title = "Mac VirtualBox capture HTTP traffic to/from Linux VM"
description = '''I&#x27;ve got VirtualBox installed on a Mac running an Ubuntu VM. The VM is setup to use a Host-only Adapter on vboxnet0. The VM is running a web server on non-standard port 5000. I&#x27;ve got a vanilla installation of Wireshark running on the Mac and I start a capture on the vboxnet0 interface. My understan...'''
date = "2012-10-02T13:30:00Z"
lastmod = "2013-04-25T15:30:00Z"
weight = 14646
keywords = [ "mac", "virtualbox", "wireshark" ]
aliases = [ "/questions/14646" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mac VirtualBox capture HTTP traffic to/from Linux VM](/questions/14646/mac-virtualbox-capture-http-traffic-tofrom-linux-vm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14646-score" class="post-score" title="current number of votes">1</div><span id="post-14646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've got VirtualBox installed on a Mac running an Ubuntu VM. The VM is setup to use a Host-only Adapter on vboxnet0. The VM is running a web server on non-standard port 5000.</p><p>I've got a vanilla installation of Wireshark running on the Mac and I start a capture on the vboxnet0 interface. My understanding is that wireshark should capture everything on all ports on an interface out of the box.</p><p>When I fire up a web browser I can see HTTP and TCP responses from the VM to the Mac but I can't see the requests from the Mac to the VM.</p><p>Does anyone know why that might be? Am I missing some Wireshark settings?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/39ffccdc20c86a170de39e22f43959c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Everett&#39;s gravatar image" /><p><span>Everett</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Everett has no accepted answers">0%</span></p></div></div><div id="comments-container-14646" class="comments-container"><span id="20810"></span><div id="comment-20810" class="comment"><div id="post-20810-score" class="comment-score"></div><div class="comment-text"><p>I'm having the same problem. I'm curious if you found a solution.</p></div><div id="comment-20810-info" class="comment-info"><span class="comment-age">(25 Apr '13, 15:30)</span> <span class="comment-user userinfo">ckwilcox</span></div></div></div><div id="comment-tools-14646" class="comment-tools"></div><div class="clear"></div><div id="comment-14646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14659"></span>

<div id="answer-container-14659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14659-score" class="post-score" title="current number of votes">1</div><span id="post-14659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may be missing some <em>VirtualBox</em> settings. I suspect tcpdump will be no more successful at capturing the traffic than Wireshark; Wireshark should capture everything <em>provided to it by the packet capture mechanism and network device driver on the OS on which it's running</em> (as should tcpdump, for example, given that it and Wireshark use the same packet capture library), but that might not be all traffic - the network device might not see all the traffic, the device driver might not put the device into a mode where it <em>can</em> see all the traffic, or the packet capture mechanism might not pass all the traffic.</p><p>I'd suggest checking the VirtualBox documentation and asking in a VirtualBox forum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '12, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14659" class="comments-container"></div><div id="comment-tools-14659" class="comment-tools"></div><div class="clear"></div><div id="comment-14659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


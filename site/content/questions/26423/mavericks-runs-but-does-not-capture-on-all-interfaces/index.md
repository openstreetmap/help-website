+++
type = "question"
title = "Mavericks - runs but does not capture on all interfaces"
description = '''Upgraded from Mountain Lion to Mavericks. Reinstalled XQuartz and then reinstalled Wireshark 1.10.2. Wireshark runs correctly, and in the list of available interfaces it lists them all.  However only traffic on the WiFi connection (en0) is being detected and captured. Traffic on the ethernets that a...'''
date = "2013-10-26T10:06:00Z"
lastmod = "2013-10-28T15:31:00Z"
weight = 26423
keywords = [ "osx", "macbook", "mavericks" ]
aliases = [ "/questions/26423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mavericks - runs but does not capture on all interfaces](/questions/26423/mavericks-runs-but-does-not-capture-on-all-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26423-score" class="post-score" title="current number of votes">0</div><span id="post-26423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Upgraded from Mountain Lion to Mavericks. Reinstalled XQuartz and then reinstalled Wireshark 1.10.2. Wireshark runs correctly, and in the list of available interfaces it lists them all.</p><p>However only traffic on the WiFi connection (en0) is being detected and captured. Traffic on the ethernets that are connected to my thunderbolt-to-ethernet adapter (en3) or on my Apple Display (en4) is not being detected. When running Mountain Lion prior to the upgrade, traffic was detected correctly on all interfaces.</p><p>Does anyone have any ideas on how to solve the issue? It looks like a permission issue not allowing access to the other interfaces, but I can't find a solution (yet...).</p><p>For the record, the computer is one of the new Macbook 15" with retina display.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-macbook" rel="tag" title="see questions tagged &#39;macbook&#39;">macbook</span> <span class="post-tag tag-link-mavericks" rel="tag" title="see questions tagged &#39;mavericks&#39;">mavericks</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '13, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/f9addddd7821e77072c84629ab21417d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ik8sqi&#39;s gravatar image" /><p><span>ik8sqi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ik8sqi has no accepted answers">0%</span></p></div></div><div id="comments-container-26423" class="comments-container"><span id="26453"></span><div id="comment-26453" class="comment"><div id="post-26453-score" class="comment-score"></div><div class="comment-text"><p>What happens if you try capturing on those interfaces with tcpdump? If that fails in the same fashion, it's a Mavericks bug, not a Wireshark bug.</p></div><div id="comment-26453-info" class="comment-info"><span class="comment-age">(27 Oct '13, 22:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26423" class="comment-tools"></div><div class="clear"></div><div id="comment-26423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26471"></span>

<div id="answer-container-26471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26471-score" class="post-score" title="current number of votes">0</div><span id="post-26471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please run the following command and check if there are any differences regarding the ownership and access rights of those devices.</p><blockquote><p>ls -al /dev/bpf[0-4]</p></blockquote><p>If so, please adjust the other devices to what you see for /dev/bpf0.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26471" class="comments-container"><span id="26492"></span><div id="comment-26492" class="comment"><div id="post-26492-score" class="comment-score"></div><div class="comment-text"><p>Not having permissions to open the BPF devices would prevent you from capturing on <em>any</em> interface. I'll look at the Mavericks XNU source to see if there's anything obvious that would limit access to some but not all interfaces.</p></div><div id="comment-26492-info" class="comment-info"><span class="comment-age">(28 Oct '13, 15:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26471" class="comment-tools"></div><div class="clear"></div><div id="comment-26471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


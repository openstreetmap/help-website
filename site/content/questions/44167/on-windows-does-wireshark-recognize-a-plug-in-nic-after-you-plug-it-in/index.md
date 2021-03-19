+++
type = "question"
title = "On Windows, does Wireshark recognize a plug-in NIC after you plug it in?"
description = '''hi there I have an old HP laptop being used to scan servers on our network . We have recently upgraded to Nexus switches which only communicate on 1gb minimum - the HP laptop only goes up to 100mb. I brought a USB NIC with a 1gb capability - this functions and is recognised by the Win7 OS , but when...'''
date = "2015-07-15T03:41:00Z"
lastmod = "2015-07-16T12:44:00Z"
weight = 44167
keywords = [ "windows", "nic", "pluggable", "wireshark" ]
aliases = [ "/questions/44167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [On Windows, does Wireshark recognize a plug-in NIC after you plug it in?](/questions/44167/on-windows-does-wireshark-recognize-a-plug-in-nic-after-you-plug-it-in)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44167-score" class="post-score" title="current number of votes">0</div><span id="post-44167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi there</p><p>I have an old HP laptop being used to scan servers on our network . We have recently upgraded to Nexus switches which only communicate on 1gb minimum - the HP laptop only goes up to 100mb.</p><p>I brought a USB NIC with a 1gb capability - this functions and is recognised by the Win7 OS , but when I try and sniff traffic with Wireshark(or use NMAP/Nessus,etc) , the interface is not displayed .</p><p>Anyone have an idea where I am going wrong please?</p><p>Many TIA!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-pluggable" rel="tag" title="see questions tagged &#39;pluggable&#39;">pluggable</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/900e2191ced2f2b023fbcdb324a9bddc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresuser&#39;s gravatar image" /><p><span>wiresuser</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresuser has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '15, 17:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44167" class="comments-container"></div><div id="comment-tools-44167" class="comment-tools"></div><div class="clear"></div><div id="comment-44167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44213"></span>

<div id="answer-container-44213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44213-score" class="post-score" title="current number of votes">0</div><span id="post-44213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to reload WinPcap <strong>after</strong> you plugged in the USB interface. In an elevated DOS box (run as administrator), do the following:</p><ul><li>close all Wireshark instances</li><li>run: sc stop npf</li><li>run: sc start npf</li><li>close DOS box</li><li>start Wireshark</li></ul><p>You should now see the interface in Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '15, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44213" class="comments-container"><span id="44216"></span><div id="comment-44216" class="comment"><div id="post-44216-score" class="comment-score"></div><div class="comment-text"><p>Many , many thanks for coming back to me on this . Much appreciated . I will report back .</p></div><div id="comment-44216-info" class="comment-info"><span class="comment-age">(16 Jul '15, 12:14)</span> <span class="comment-user userinfo">wiresuser</span></div></div><span id="44220"></span><div id="comment-44220" class="comment"><div id="post-44220-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-44220-info" class="comment-info"><span class="comment-age">(16 Jul '15, 12:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-44213" class="comment-tools"></div><div class="clear"></div><div id="comment-44213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


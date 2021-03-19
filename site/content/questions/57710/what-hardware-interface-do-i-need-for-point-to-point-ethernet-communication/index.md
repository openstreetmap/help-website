+++
type = "question"
title = "What hardware interface do I need for point-to-point Ethernet communication?"
description = '''This is probably a stupid question, but I am still learning the basics of WireShark. I am trying to set up a platform to test various industrial Ethernet devices. I would like to use a point-to-point connection from my PC to the device in question. Can I simply use my PC&#x27;s onboard Ethernet port? Or ...'''
date = "2016-11-29T10:12:00Z"
lastmod = "2016-11-29T14:31:00Z"
weight = 57710
keywords = [ "ethernet", "industrial-network", "networking", "beginner", "networkinterfaces" ]
aliases = [ "/questions/57710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What hardware interface do I need for point-to-point Ethernet communication?](/questions/57710/what-hardware-interface-do-i-need-for-point-to-point-ethernet-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57710-score" class="post-score" title="current number of votes">0</div><span id="post-57710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is probably a stupid question, but I am still learning the basics of WireShark.</p><p>I am trying to set up a platform to test various industrial Ethernet devices. I would like to use a point-to-point connection from my PC to the device in question. Can I simply use my PC's onboard Ethernet port? Or do I need to use some other type of hardware?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-industrial-network" rel="tag" title="see questions tagged &#39;industrial-network&#39;">industrial-network</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '16, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/1f4b37ff3df6a1460e51c914d0a82844?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cjswish&#39;s gravatar image" /><p><span>cjswish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cjswish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Nov '16, 14:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57710" class="comments-container"></div><div id="comment-tools-57710" class="comment-tools"></div><div class="clear"></div><div id="comment-57710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57712"></span>

<div id="answer-container-57712" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57712-score" class="post-score" title="current number of votes">1</div><span id="post-57712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question can be deemed a Wireshark one only if you try really hard, but anyway - yes, an Ethernet port of your PC can be used to directly connect an Ethernet port of some other equipment using a cable alone (i.e. no need to use a switch or hub between the two), and you can use Wireshark running on your PC to capture that communication. Depending on the capabilities of the two ports, you may need to use a so-called "crossed cable", but for equipment not older than 15 years this should not be an issue, so it is worth trying with a standard patch cable first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '16, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57712" class="comments-container"><span id="57713"></span><div id="comment-57713" class="comment"><div id="post-57713-score" class="comment-score"></div><div class="comment-text"><p><span>@cjswish</span>, the house rules of this site assume that if you find an Answer to your Question useful, you click the checkmark icon, rather than the thumbs up icon, to mark it as such. Doing so highlights the Question in green in the list, informing others coming to ask the same Question that this one has been usefully answered. The checkmark icon is only available to the author of the Question who is the only one to judge whether the answer was helpful or not. The thumbs up are for everyone and their original purpose is to prefer better Answers where more than one Answer is available.</p></div><div id="comment-57713-info" class="comment-info"><span class="comment-age">(29 Nov '16, 14:31)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-57712" class="comment-tools"></div><div class="clear"></div><div id="comment-57712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


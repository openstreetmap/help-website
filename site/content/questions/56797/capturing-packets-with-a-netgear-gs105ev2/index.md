+++
type = "question"
title = "Capturing packets with a Netgear GS105Ev2"
description = '''I have just acquired a Netgear GS105Ev2 managed switch specifically to capture traffic to and from a POS device going out to the internet. So I have my PC, the POS device and a router plugged into this switch, nothing else. I have set the MultiCast snooping port to be that of my PC, and the basic VL...'''
date = "2016-10-28T19:18:00Z"
lastmod = "2016-10-29T02:51:00Z"
weight = 56797
keywords = [ "gs105ev2", "snooping" ]
aliases = [ "/questions/56797" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing packets with a Netgear GS105Ev2](/questions/56797/capturing-packets-with-a-netgear-gs105ev2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56797-score" class="post-score" title="current number of votes">0</div><span id="post-56797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just acquired a Netgear GS105Ev2 managed switch specifically to capture traffic to and from a POS device going out to the internet. So I have my PC, the POS device and a router plugged into this switch, nothing else. I have set the MultiCast snooping port to be that of my PC, and the basic VLAN enabled default options, but still cannot see any traffic going to or from the POS device. Also I have my AVG firewall turned off, and am using Win10 (1607).</p><p>Can anyone confirm the GS150Ev2 settings I need please, and give any other advice to help me.</p><p>Thanks, Graham</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gs105ev2" rel="tag" title="see questions tagged &#39;gs105ev2&#39;">gs105ev2</span> <span class="post-tag tag-link-snooping" rel="tag" title="see questions tagged &#39;snooping&#39;">snooping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '16, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/de963d3ce1f3f0cad75514255a8b00a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graham&#39;s gravatar image" /><p><span>Graham</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graham has one accepted answer">100%</span></p></div></div><div id="comments-container-56797" class="comments-container"></div><div id="comment-tools-56797" class="comment-tools"></div><div class="clear"></div><div id="comment-56797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56798"></span>

<div id="answer-container-56798" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56798-score" class="post-score" title="current number of votes">0</div><span id="post-56798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Graham has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think I can answer my own question! It is not MutliCast I need, but using the ProSAFE Plus utility, select the "System" tab and click the "Monitoring" option on the horizontal bar, then click "Mirroring" on the left hand side below "Port Statistics".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '16, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/de963d3ce1f3f0cad75514255a8b00a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graham&#39;s gravatar image" /><p><span>Graham</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graham has one accepted answer">100%</span></p></div></div><div id="comments-container-56798" class="comments-container"><span id="56804"></span><div id="comment-56804" class="comment"><div id="post-56804-score" class="comment-score"></div><div class="comment-text"><p>Answering your own Question is perfectly fine (except if such Answer would be a mere compilation of other people's Answers). So please take one more step and indicate to others who come to ask the same Question that this one has been answered usefully by Accepting your own Answer by clicking the checkmark icon next to it.</p></div><div id="comment-56804-info" class="comment-info"><span class="comment-age">(29 Oct '16, 02:51)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56798" class="comment-tools"></div><div class="clear"></div><div id="comment-56798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


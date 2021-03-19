+++
type = "question"
title = "Unable to see VLAN tags using Intel 82579LM"
description = '''Hi all My system configuration as follows PC  OS windows 7 ent. 64 bit Switch config monitor session x source interface Gi 0/x monitor session x destination interface fa0/x encapsulation dot1q registry monitormode is 1 i seen vlan information but only STP packet registry monitormode is 0  i dont see...'''
date = "2014-02-05T00:30:00Z"
lastmod = "2014-02-05T02:56:00Z"
weight = 29447
keywords = [ "nic", "vlan", "intel" ]
aliases = [ "/questions/29447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to see VLAN tags using Intel 82579LM](/questions/29447/unable-to-see-vlan-tags-using-intel-82579lm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29447-score" class="post-score" title="current number of votes">0</div><span id="post-29447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>My system configuration as follows</p><p>PC OS windows 7 ent. 64 bit</p><p>Switch config</p><p>monitor session x source interface Gi 0/x</p><p>monitor session x destination interface fa0/x encapsulation dot1q</p><p>registry monitormode is 1 i seen vlan information but only STP packet</p><p>registry monitormode is 0 i dont see vlan information only tcp/ip and more l2 information MAC etc</p><p>check the Print Secreen on attached Pls What is your sugesstion, could you help me pls ? Thank you in advance</p><p>Monitor mode 1 <img src="https://osqa-ask.wireshark.org/upfiles/Monitormode_1.JPG" alt="alt text" /></p><p>Monitor mode 0 <img src="https://osqa-ask.wireshark.org/upfiles/Monitormode_0_6.JPG" alt="alt text" /></p><p>Registry <img src="https://osqa-ask.wireshark.org/upfiles/registry.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-intel" rel="tag" title="see questions tagged &#39;intel&#39;">intel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/5dcfd4c76162deff4e8aac3c17e6db61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alibaltr&#39;s gravatar image" /><p><span>alibaltr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alibaltr has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>05 Feb '14, 02:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-29447" class="comments-container"></div><div id="comment-tools-29447" class="comment-tools"></div><div class="clear"></div><div id="comment-29447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29451"></span>

<div id="answer-container-29451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29451-score" class="post-score" title="current number of votes">0</div><span id="post-29451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a similar question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183">http://ask.wireshark.org/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183</a></p></blockquote><p>additionally: please search the site for 82579.</p><p>BTW: Are you sure your monitored port (Gi 0/x) has vlan tags enabled/configured?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Feb '14, 03:04</strong> </span></p></div></div><div id="comments-container-29451" class="comments-container"></div><div id="comment-tools-29451" class="comment-tools"></div><div class="clear"></div><div id="comment-29451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


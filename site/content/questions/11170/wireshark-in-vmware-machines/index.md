+++
type = "question"
title = "Wireshark in VMWare Machines"
description = '''I am new to Wireshark and would like to learn a lot. Since I&#x27;m a student I have only one Machine(laptop). But, in my laptop, I have installed VMWare Workstation 7. Now my question is...since Wireshark is a network packet analysis tool... Is it possible for me to practice Wireshark in a virtual machi...'''
date = "2012-05-21T04:13:00Z"
lastmod = "2012-05-21T05:53:00Z"
weight = 11170
keywords = [ "practice", "beginner", "vmware", "tutorial", "wireshark" ]
aliases = [ "/questions/11170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark in VMWare Machines](/questions/11170/wireshark-in-vmware-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11170-score" class="post-score" title="current number of votes">0</div><span id="post-11170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark and would like to learn a lot. Since I'm a student I have only one Machine(laptop). But, in my laptop, I have installed VMWare Workstation 7. Now my question is...since Wireshark is a network packet analysis tool... Is it possible for me to practice Wireshark in a virtual machine. I mean, I would like to install a Server OS (basically Windows Server 2003) and 5 Win XP OS as a guest and connect them via NAT in the VMWare itself with the server. If this is not possible, then please anyone guide me as to how can i start learning and experiment Wireshark <strong>on my own</strong>. Any website that has a tutorial on Wireshark. Plzzzzzz Help!!!<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-practice" rel="tag" title="see questions tagged &#39;practice&#39;">practice</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-tutorial" rel="tag" title="see questions tagged &#39;tutorial&#39;">tutorial</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '12, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/6d3ba90ff27994cf837d4d3f442986d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver_rain&#39;s gravatar image" /><p><span>silver_rain</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver_rain has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11170" class="comments-container"></div><div id="comment-tools-11170" class="comment-tools"></div><div class="clear"></div><div id="comment-11170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11171"></span>

<div id="answer-container-11171" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11171-score" class="post-score" title="current number of votes">1</div><span id="post-11171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="silver_rain has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, you can run Wireshark in a VM. You could install as many VMs as you wish and run Wireshark on one of them, capturing the traffic of the others. That works especially well if you connect the VMs by using Host-Only networks, or in bridged mode. NAT might not work so well or give funny results, so for starters I'd recommend creating VMs that have a Host-Only Network to talk to each other. In my tests 3 VMs that have a host only network can see all traffic going back and forth like on a hubbed network, so that would be a nice start.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11171" class="comments-container"><span id="11173"></span><div id="comment-11173" class="comment"><div id="post-11173-score" class="comment-score"></div><div class="comment-text"><p>Thx for the reputation point <span>@silver_rain</span>, but if you really like the answer just accept it (round checkmark button below the tumbs up/down icons) ;-)</p></div><div id="comment-11173-info" class="comment-info"><span class="comment-age">(21 May '12, 05:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-11171" class="comment-tools"></div><div class="clear"></div><div id="comment-11171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


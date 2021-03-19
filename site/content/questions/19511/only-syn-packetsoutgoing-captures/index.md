+++
type = "question"
title = "Only SYN packets(outgoing) captures"
description = '''Hi all, i am using Wireshark 1.8, and the problem is that, i am unable to capture the packets other than SYN. that is i am sure the connectivity is working fine, i can use HTTp web pages also, but while capturing i am only getting the SYN packet. nothing else. i am using 2950 cisco switch. Then i tr...'''
date = "2013-03-14T08:28:00Z"
lastmod = "2013-03-17T22:06:00Z"
weight = 19511
keywords = [ "syn-ack", "configuration", "syn", "oneway" ]
aliases = [ "/questions/19511" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Only SYN packets(outgoing) captures](/questions/19511/only-syn-packetsoutgoing-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19511-score" class="post-score" title="current number of votes">0</div><span id="post-19511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i am using Wireshark 1.8, and the problem is that, i am unable to capture the packets other than SYN. that is i am sure the connectivity is working fine, i can use HTTp web pages also, but while capturing i am only getting the SYN packet. nothing else. i am using 2950 cisco switch. Then i tried to run Wireshark for the interface in my PC, without using monitoring configurations in the switch, then i am able to see all the packets. I am using windows XP, and CA Total defence antivirus is working in the machine. I tried after disabling the anti virus, but still its like the old. Pls help with valuable suggestions..</p><pre><code>SW-1#sh moni
Session 1
---------
Type              : Local Session
Source Ports      :
    Both          : Fa0/24
Destination Ports : Fa0/3
    Encapsulation : Native
          Ingress: Disabled</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn-ack" rel="tag" title="see questions tagged &#39;syn-ack&#39;">syn-ack</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/703cc07b87a263224b3aaec78b67c87b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Unni&#39;s gravatar image" /><p><span>Unni</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Unni has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '13, 08:35</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19511" class="comments-container"></div><div id="comment-tools-19511" class="comment-tools"></div><div class="clear"></div><div id="comment-19511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19596"></span>

<div id="answer-container-19596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19596-score" class="post-score" title="current number of votes">0</div><span id="post-19596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand your question right, this may help.</p><p>Sounds like you need to SPAN the switch port. When you set up the SPAN in the Cisco switch you have to also allow your own computers traffic to traverse the monitor port in the switch by setting the allow traffic option.<br />
</p><p>Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '13, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19596" class="comments-container"></div><div id="comment-tools-19596" class="comment-tools"></div><div class="clear"></div><div id="comment-19596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19602"></span>

<div id="answer-container-19602" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19602-score" class="post-score" title="current number of votes">0</div><span id="post-19602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi..</p><p>i have figured out the issue :) it is because of the anti virus ... i am running CA HIPS in my PC.. after trying with another machine, its working fine,... thanks.. and John, i am already running SPAN in the switch.. the configuration i have given is for SPAN configuration.. thank you ..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '13, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/703cc07b87a263224b3aaec78b67c87b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Unni&#39;s gravatar image" /><p><span>Unni</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Unni has no accepted answers">0%</span></p></div></div><div id="comments-container-19602" class="comments-container"></div><div id="comment-tools-19602" class="comment-tools"></div><div class="clear"></div><div id="comment-19602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


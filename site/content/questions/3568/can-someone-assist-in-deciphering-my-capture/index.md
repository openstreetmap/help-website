+++
type = "question"
title = "Can someone assist in deciphering my capture?"
description = '''I am trying to find out what is going on with our network. At certain times of the day, not always a set time, but at times the network loses connection on random workstations, but it only loses connection on certain parts of the network and not other parts of the network. For example, we still have...'''
date = "2011-04-18T07:56:00Z"
lastmod = "2011-05-07T03:28:00Z"
weight = 3568
keywords = [ "failure", "connection", "network", "loss" ]
aliases = [ "/questions/3568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can someone assist in deciphering my capture?](/questions/3568/can-someone-assist-in-deciphering-my-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3568-score" class="post-score" title="current number of votes">0</div><span id="post-3568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to find out what is going on with our network. At certain times of the day, not always a set time, but at times the network loses connection on random workstations, but it only loses connection on certain parts of the network and not other parts of the network. For example, we still have internet and we can print and view other parts of the network, but not all of it. Also, a reboot of the workstation brings everything back.</p><p>I have been recording during the times of when we are getting failures, but I don't exactly know what I am looking for or at least I don't see anything specific wrong going on.</p><p>Any assistance would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-failure" rel="tag" title="see questions tagged &#39;failure&#39;">failure</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-loss" rel="tag" title="see questions tagged &#39;loss&#39;">loss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/8eda147cdd5fcfa447ceab56af7d3152?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="h4rd2g3t&#39;s gravatar image" /><p><span>h4rd2g3t</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="h4rd2g3t has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '11, 05:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3568" class="comments-container"><span id="3931"></span><div id="comment-3931" class="comment"><div id="post-3931-score" class="comment-score"></div><div class="comment-text"><p>Would you consider making a trace file available for people to look at?</p></div><div id="comment-3931-info" class="comment-info"><span class="comment-age">(04 May '11, 21:17)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-3568" class="comment-tools"></div><div class="clear"></div><div id="comment-3568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3989"></span>

<div id="answer-container-3989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3989-score" class="post-score" title="current number of votes">1</div><span id="post-3989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a little hard to answer you're question, as it doesn't tell much about the network.</p><ul><li><p>Is it a small network with only one subnet and everything directly connected (at L2)? <em>If so, I would look for ARP and ICMP packets and see what they tell you.</em></p></li><li><p>Or do you have a large network with many subnets? <em>Then you might want to look at the routing tables at the time of trouble.</em></p></li><li><p>Are your networking devices redundant? <em>Then you might want to check whether there is asymetric routing going on.</em></p></li></ul><p>It all depends on the situation you are in and the pattern of outage that you have. For instance:</p><ul><li>What is the relationship between the failing devices and how does that compare to the devices that are still reachable</li><li>What is the relationship between the clients that have problems and how does that compare to the clients that do not have the problem).</li></ul><p>All that information helps you to get a grasp of where the problem might be caused.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3989" class="comments-container"></div><div id="comment-tools-3989" class="comment-tools"></div><div class="clear"></div><div id="comment-3989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


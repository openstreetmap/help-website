+++
type = "question"
title = "Measure one way delays between 2 hosts"
description = '''Hi, I would like to plot the variations in One Way Delays (instead of RTTs) of a TCP connection. Assume that I have recorded one pcap on the client and one pcap on the server and that both nodes are perfectly in sync, is there any software that could plot the one way delays ? Regards'''
date = "2016-03-21T05:39:00Z"
lastmod = "2016-03-21T07:03:00Z"
weight = 51061
keywords = [ "owd" ]
aliases = [ "/questions/51061" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Measure one way delays between 2 hosts](/questions/51061/measure-one-way-delays-between-2-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51061-score" class="post-score" title="current number of votes">0</div><span id="post-51061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to plot the variations in One Way Delays (instead of RTTs) of a TCP connection. Assume that I have recorded one pcap on the client and one pcap on the server and that both nodes are <em>perfectly</em> in sync, is there any software that could plot the one way delays ?</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-owd" rel="tag" title="see questions tagged &#39;owd&#39;">owd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '16, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/e2e55c6d8b33c6f22b441b0f39cfa209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teto&#39;s gravatar image" /><p><span>teto</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teto has no accepted answers">0%</span></p></div></div><div id="comments-container-51061" class="comments-container"></div><div id="comment-tools-51061" class="comment-tools"></div><div class="clear"></div><div id="comment-51061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51063"></span>

<div id="answer-container-51063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51063-score" class="post-score" title="current number of votes">0</div><span id="post-51063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From my Point of view the key for success is the exact time stamping during capturing. For that you should specialized capture cards. How to do the analysis in wire sharks itself is described here: <a href="https://blog.packet-foo.com/2015/02/working-with-multi-point-captures/">https://blog.packet-foo.com/2015/02/working-with-multi-point-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-51063" class="comments-container"><span id="51064"></span><div id="comment-51064" class="comment"><div id="post-51064-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I can affirm my nodes are perfectly syncronized because the pcaps are generated by the discrete time simulator ns3 (www.nsnam.org). I am looking for a tool to automate the generation of OWD plots, otherwise I will have to write one myself. From your linked post, they suggest to use proprietary software but I am on linux and it's not clear from their websites if they support the OWD plotting I am looking for.</p></div><div id="comment-51064-info" class="comment-info"><span class="comment-age">(21 Mar '16, 06:39)</span> <span class="comment-user userinfo">teto</span></div></div><span id="51065"></span><div id="comment-51065" class="comment"><div id="post-51065-score" class="comment-score"></div><div class="comment-text"><p>Ok either you use the tools described there at the end of you have write some scripts or merge the pcaps. Maybe the IP.ID could be the key to match the correlating packets.</p></div><div id="comment-51065-info" class="comment-info"><span class="comment-age">(21 Mar '16, 07:03)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-51063" class="comment-tools"></div><div class="clear"></div><div id="comment-51063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


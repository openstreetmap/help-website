+++
type = "question"
title = "Packet captures and Riverbed Appliances"
description = '''Would it be beneficial to capture traffic before and after a Riverbed Steelhead appliance? Is there any tips anyone can provide when reading packets from one of these appliances? Thanks'''
date = "2011-03-02T09:39:00Z"
lastmod = "2011-03-06T09:06:00Z"
weight = 2634
keywords = [ "riverbed", "steelhead", "packet" ]
aliases = [ "/questions/2634" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet captures and Riverbed Appliances](/questions/2634/packet-captures-and-riverbed-appliances)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2634-score" class="post-score" title="current number of votes">0</div><span id="post-2634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would it be beneficial to capture traffic before and after a Riverbed Steelhead appliance?</p><p>Is there any tips anyone can provide when reading packets from one of these appliances?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-riverbed" rel="tag" title="see questions tagged &#39;riverbed&#39;">riverbed</span> <span class="post-tag tag-link-steelhead" rel="tag" title="see questions tagged &#39;steelhead&#39;">steelhead</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '11, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/f6356ebdb200df4ae377d891fee0f69b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scottmildy&#39;s gravatar image" /><p><span>scottmildy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scottmildy has no accepted answers">0%</span></p></div></div><div id="comments-container-2634" class="comments-container"><span id="2681"></span><div id="comment-2681" class="comment"><div id="post-2681-score" class="comment-score"></div><div class="comment-text"><p>scottmildy, are you trying to see how much RB will help or trying to figure out what the "secret sauce" is? Before I get into a long drawn out answer, I wanted to see what you were after.</p></div><div id="comment-2681-info" class="comment-info"><span class="comment-age">(06 Mar '11, 09:06)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-2634" class="comment-tools"></div><div class="clear"></div><div id="comment-2634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2646"></span>

<div id="answer-container-2646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2646-score" class="post-score" title="current number of votes">0</div><span id="post-2646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to capture traffic before and after any appliance if you suspect that the device is responsible for problems in your network. I haven't encountered any Riverbed appliances so far, but I had my share of captures at other traffic management appliances that messed up some network packets really good. One example was a traffic shaper adjusting the TCP window size to ridiculous values that led to total communication breakdown between client and server.</p><p>So if you suspect any appliance to mess up packets you can capture on both sides of the appliance (if it's not a one armed device, otherwise you can only do one capture) and compare traces to see what happens. Comparing traces is a time consuming process, but if you know of a specific communication between two stations that has trouble and you know IP addresses and TCP ports you can find the TCP flows quite easily by looking for those, maybe including the initial TCP sequence number.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '11, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2646" class="comments-container"></div><div id="comment-tools-2646" class="comment-tools"></div><div class="clear"></div><div id="comment-2646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


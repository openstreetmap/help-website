+++
type = "question"
title = "Multiple NOT clauses in a capture filter"
description = '''I just got back from Sharkfest (my first time) and am wicked fired up to try bold new things with Wireshark. As luck would have it, a perfect real-world problem dropped in my lap just this morning. Background: Our customer sends medical imaging data (DICOM) to our load balancer on TCP port 104, whic...'''
date = "2013-06-21T13:23:00Z"
lastmod = "2013-06-21T14:17:00Z"
weight = 22228
keywords = [ "filter", "capture", "not", "multiple" ]
aliases = [ "/questions/22228" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple NOT clauses in a capture filter](/questions/22228/multiple-not-clauses-in-a-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22228-score" class="post-score" title="current number of votes">0</div><span id="post-22228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just got back from Sharkfest (my first time) and am wicked fired up to try bold new things with Wireshark. As luck would have it, a perfect real-world problem dropped in my lap just this morning.</p><p>Background: Our customer sends medical imaging data (DICOM) to our load balancer on TCP port 104, which forwards it to the machine on which I am running dumpcap, and its counterpart, more or less evenly, when things are working correctly. The load balancer strips the original sending device's source IP and substitutes its own.</p><p>The customer may also send DICOM directly to this machine or its counterpart, which is "cheating" and not recommended, as it's a form of "cutting in line" and compromises the integrity of load balancing. My goals are two: (1) Determine how much DICOM the load balancer is sending us over a 24-hour period (we can only process so much, and if they send us more, it backs up in the input queue and the customer complains that the images are not timely visible), and (2) Determine whether the customer is cheating by sending directly to our DICOM processors rather than to the load balancer.</p><p>Unfortunately, this machine also sends DICOM out to port 104 on other machines, and that traffic is not relevant to our present inquiry. I have tried:</p><p>tcp port 104 and not src host [my ip] and not src host [the load balancer's ip]</p><p>and</p><p>tcp port 104 and not (src host [my ip] or src host [the load balancer's ip])</p><p>but neither one works. What should I be doing instead?</p><p>Thank you for your time and consideration.</p><p>Andrew Laurence</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/f787e5c95b6da3426fddb8705401ba7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Laurence&#39;s gravatar image" /><p><span>Andrew Laurence</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Laurence has no accepted answers">0%</span></p></div></div><div id="comments-container-22228" class="comments-container"></div><div id="comment-tools-22228" class="comment-tools"></div><div class="clear"></div><div id="comment-22228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22231"></span>

<div id="answer-container-22231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22231-score" class="post-score" title="current number of votes">0</div><span id="post-22231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap -i &lt;interface&gt; -f "tcp port 104 and (not src host &lt;loadbalancerip&gt; and not src host &lt;urip&gt;)" might be the filter to capture all the traffic coming to or from port 104 with source ip other than your load balancer (or your ip).</p><p>I guess you want to capture the traffic that is not source natted from loadbalancer.</p><p>dumpcap -i &lt;interface&gt; -f "tcp port 104 and src host&lt;clientip&gt;" might also work right?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '13, 14:18</strong> </span></p></div></div><div id="comments-container-22231" class="comments-container"></div><div id="comment-tools-22231" class="comment-tools"></div><div class="clear"></div><div id="comment-22231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


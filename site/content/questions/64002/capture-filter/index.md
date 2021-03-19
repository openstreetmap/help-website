+++
type = "question"
title = "Capture Filter"
description = '''Hi, What is the syntax in the latest Wireshark version to select 2 ip addresses for a capture filter? Thanks. Eric'''
date = "2017-10-18T08:53:00Z"
lastmod = "2017-10-19T16:27:00Z"
weight = 64002
keywords = [ "capture-filter" ]
aliases = [ "/questions/64002" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter](/questions/64002/capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64002-score" class="post-score" title="current number of votes">0</div><span id="post-64002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, What is the syntax in the latest Wireshark version to select 2 ip addresses for a capture filter? Thanks. Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '17, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/d7f8654c07881f7963ce5152ce1a0ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekatow&#39;s gravatar image" /><p><span>ekatow</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekatow has no accepted answers">0%</span></p></div></div><div id="comments-container-64002" class="comments-container"><span id="64003"></span><div id="comment-64003" class="comment"><div id="post-64003-score" class="comment-score"></div><div class="comment-text"><p>The syntax is the same as it's always been as it's BPF syntax as shown <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">here</a>.</p><p>Do you only want packets between the 2 IP addresses or packets to or from either address?</p></div><div id="comment-64003-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="64004"></span><div id="comment-64004" class="comment"><div id="post-64004-score" class="comment-score"></div><div class="comment-text"><p>Traffic to and from either address</p></div><div id="comment-64004-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:12)</span> <span class="comment-user userinfo">ekatow</span></div></div><span id="64005"></span><div id="comment-64005" class="comment"><div id="post-64005-score" class="comment-score"></div><div class="comment-text"><p>For example, you want to see all traffic to or from 192.9.200.1 and all traffic to or from 192.9.200.2, regardless of what host traffic to 192.9.200.{1,2} is coming from and what host traffic from 192.9.200.{1,2} is going to?</p></div><div id="comment-64005-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:25)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="64006"></span><div id="comment-64006" class="comment"><div id="post-64006-score" class="comment-score"></div><div class="comment-text"><p>Ideally, I want to see what is coming from 192.9.200.1 (requests) and what is coming from 192.9.200.2 (responses).</p></div><div id="comment-64006-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:27)</span> <span class="comment-user userinfo">ekatow</span></div></div><span id="64007"></span><div id="comment-64007" class="comment"><div id="post-64007-score" class="comment-score"></div><div class="comment-text"><p>I.e., you want to see <em>all</em> traffic from 192.9.200.1 and <em>all</em> traffic from 192.9.200.2?</p><p>What about traffic <em>to</em> those hosts?</p><p>Or do you only want the traffic <em>between</em> 192.9.200.1 and 192.9.200.2, i.e. packets from 192.9.200.1 to 192.9.200.2 and packets from 192.9.200.2 to 192.9.200.1, and no packets from or to one of those hosts to or from any third host?</p></div><div id="comment-64007-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="64008"></span><div id="comment-64008" class="comment not_top_scorer"><div id="post-64008-score" class="comment-score"></div><div class="comment-text"><p>only want the traffic between 192.9.200.1 and 192.9.200.2, i.e. packets from 192.9.200.1 to 192.9.200.2 and packets from 192.9.200.2 to 192.9.200.1.</p></div><div id="comment-64008-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:31)</span> <span class="comment-user userinfo">ekatow</span></div></div><span id="64009"></span><div id="comment-64009" class="comment not_top_scorer"><div id="post-64009-score" class="comment-score"></div><div class="comment-text"><p>Still unclear to me,the filter doesn't know about requests and responses only source and destination. Given hosts of interest, a &amp; b there can be the following types of traffic:</p><ol><li>a -&gt; b</li><li>b -&gt; a</li><li>a -&gt; somewhere other than b</li><li>somewhere other than b -&gt; a</li><li>b -&gt; somewhere other than a</li><li>somewhere other than a -&gt; b</li><li>somewhere other than a or b -&gt; somewhere other than a or b</li></ol><p>Which of these do you want?</p></div><div id="comment-64009-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="64010"></span><div id="comment-64010" class="comment not_top_scorer"><div id="post-64010-score" class="comment-score"></div><div class="comment-text"><p>1 and 2: From a to b. and what b had to say about what a sent.</p></div><div id="comment-64010-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:37)</span> <span class="comment-user userinfo">ekatow</span></div></div></div><div id="comment-tools-64002" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-64002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64011"></span>

<div id="answer-container-64011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64011-score" class="post-score" title="current number of votes">0</div><span id="post-64011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want "packets from 192.9.200.1 to 192.9.200.2 and packets from 192.9.200.2 to 192.9.200.1.", then the capture filter would be</p><pre><code>(ip src 192.9.200.1 and ip dst 192.9.200.2) or (ip src 192.9.200.2 and ip dst 192.9.200.1)</code></pre><p>You can also use host names, but you'd have to use <code>ip6</code> rather than <code>ip</code> to check for IPv6 packets.</p><p>This will <em>not</em>, however, limit itself to, for example, requests from 192.9.200.1 and responses to those requests from 192.9.200.2; it will include all packets, whether the ones from 192.9.200.1 happen to be requests or not and whether the ones from 192.9.200.2 happen to be responses or not. All that filter looks at are IP addresses in the IPv4 header (or, for <code>ip6</code>, in the IPv6 header).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '17, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-64011" class="comments-container"><span id="64039"></span><div id="comment-64039" class="comment"><div id="post-64039-score" class="comment-score"></div><div class="comment-text"><p>If you want traffic in both directions, you could shorten this to "host 192.9.200.1 and host 192.9.200.2".</p></div><div id="comment-64039-info" class="comment-info"><span class="comment-age">(19 Oct '17, 16:27)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-64011" class="comment-tools"></div><div class="clear"></div><div id="comment-64011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "capture filter with port mirroring"
description = '''I&#x27;ve been using tshark to capture packets coming off of a mirrored port so I can see everything that is coming in and going out of our network. I have the link to our ISP mirrored to a monitoring port where my computer that I use for monitoring is plugged into. I haven&#x27;t had any problems with it whe...'''
date = "2011-04-15T11:28:00Z"
lastmod = "2011-04-19T05:31:00Z"
weight = 3515
keywords = [ "filter", "capture" ]
aliases = [ "/questions/3515" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [capture filter with port mirroring](/questions/3515/capture-filter-with-port-mirroring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3515-score" class="post-score" title="current number of votes">1</div><span id="post-3515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using tshark to capture packets coming off of a mirrored port so I can see everything that is coming in and going out of our network. I have the link to our ISP mirrored to a monitoring port where my computer that I use for monitoring is plugged into. I haven't had any problems with it when I don't have a capture filter. I see the traffic going both ways. However when I put a capture filter of: "tcp port 80" I only get traffic coming into our network, but nothing going out. Is that the way the capture filter is suppose to work? Is it only suppose to capture incoming packets to that port or is it possible to also show outgoing packets to the port as well. I get the same result whether I try the filter in tshark or wireshark. I'm running wireshark/tshark 1.2.8 so I'm going to update to 1.4.4. libpcap is 1.1.1 The box is running OpenSuse 11.3</p><p>Any comments/ideas would be appreciated.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '11, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/fd8f554a9e841a3ced855401f5d6afef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bw447&#39;s gravatar image" /><p><span>bw447</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bw447 has no accepted answers">0%</span></p></div></div><div id="comments-container-3515" class="comments-container"></div><div id="comment-tools-3515" class="comment-tools"></div><div class="clear"></div><div id="comment-3515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3516"></span>

<div id="answer-container-3516" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3516-score" class="post-score" title="current number of votes">1</div><span id="post-3516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bw447 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't use a capture filter, do the incoming and outgoing packets have the same protocol hierarchy? Is there one-way vlan-tagging, pppoe maybe? A capture filter looks at specific offsets in the packet for tcp port numbers. The offset is dependable on the previous protocol layers. So if the protocol layers differ for in the incoming and the outgoing packets, you need to make a capture filter that filters for both of them individually.</p><p>Please check the protocol hierarchy (and vlan tagging) and report so we can help you build a proper filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '11, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3516" class="comments-container"><span id="3555"></span><div id="comment-3555" class="comment"><div id="post-3555-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the questions/comments. I'm going to look into the captures that I have and post what I find.</p><p>Thanks again!</p></div><div id="comment-3555-info" class="comment-info"><span class="comment-age">(18 Apr '11, 05:45)</span> <span class="comment-user userinfo">bw447</span></div></div><span id="3579"></span><div id="comment-3579" class="comment"><div id="post-3579-score" class="comment-score"></div><div class="comment-text"><p>Update I took a look at a regular capture without any filters. Sure enough all traffic leaving our network is tagged with an vlan. However traffic entering our network doesn't have the tag. I'm going to dive into why it's a one way vlan, but I would like to find a filter that will work under this situation. Any ideas?</p><p>Thanks for the help SYNbit.</p></div><div id="comment-3579-info" class="comment-info"><span class="comment-age">(18 Apr '11, 11:19)</span> <span class="comment-user userinfo">bw447</span></div></div><span id="3587"></span><div id="comment-3587" class="comment"><div id="post-3587-score" class="comment-score">1</div><div class="comment-text"><p>You can use a filter like:</p><p>"tcp port 80 or (vlan and tcp port 80)"</p><p>or in more general form:</p><p>"(&lt;original filter&gt;) or (vlan and (&lt;original filter&gt;))"</p><p>(please keep the order in this filter, as the keyword "vlan" shifts all offsets by 4 and would make the filter not work correctly if used first, see also <a href="http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters">http://wiki.wireshark.org/CaptureSetup/VLAN#Capture_filters</a></p></div><div id="comment-3587-info" class="comment-info"><span class="comment-age">(18 Apr '11, 13:49)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3605"></span><div id="comment-3605" class="comment"><div id="post-3605-score" class="comment-score"></div><div class="comment-text"><p>The filter works like a charm. Likes for your help SYNbit!</p></div><div id="comment-3605-info" class="comment-info"><span class="comment-age">(19 Apr '11, 05:31)</span> <span class="comment-user userinfo">bw447</span></div></div></div><div id="comment-tools-3516" class="comment-tools"></div><div class="clear"></div><div id="comment-3516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


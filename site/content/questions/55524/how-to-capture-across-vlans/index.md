+++
type = "question"
title = "How to capture across VLANs?"
description = '''I want to capture all packets on all vlans EXCEPT some port ranges. We have a port mirror in place and are receiving vlan tagged packets as expected. Currently, I&#x27;ve only been able to get capture filters working if we explicitly write &#x27;vlan&#x27; in the filter (see below). Is there a way to apply a captu...'''
date = "2016-09-13T09:19:00Z"
lastmod = "2016-09-14T05:21:00Z"
weight = 55524
keywords = [ "capture-filters", "tagging" ]
aliases = [ "/questions/55524" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture across VLANs?](/questions/55524/how-to-capture-across-vlans)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55524-score" class="post-score" title="current number of votes">0</div><span id="post-55524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture all packets on all vlans EXCEPT some port ranges. We have a port mirror in place and are receiving vlan tagged packets as expected. Currently, I've only been able to get capture filters working if we explicitly write 'vlan' in the filter (see below). Is there a way to apply a capture filter that applies to all vlans?</p><p><strong><em>not ((udp portrange 14336-14600) or (vlan 701 and udp portrange 14336-14600))</em></strong></p><p>The above capture essentially has two statement or'd together, my question is: is it possible to condense this? We have multiple ranges of ports we want to filter, and it gets very cumbersome (and buggy) to string so many together. Is there some syntax to use the udp portrange regardless of any vlan (or without a vlan tag)?</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filters" rel="tag" title="see questions tagged &#39;capture-filters&#39;">capture-filters</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/f7f83d8625167c09404492f2a55db5fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PropellerHead&#39;s gravatar image" /><p><span>PropellerHead</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PropellerHead has no accepted answers">0%</span></p></div></div><div id="comments-container-55524" class="comments-container"><span id="55525"></span><div id="comment-55525" class="comment"><div id="post-55525-score" class="comment-score"></div><div class="comment-text"><p>Followup, here's the filter I'm trying to achieve (which doesn't work). It seems to let some port ranges through that we wouldn't expect.</p><p><strong><em>(not (udp portrange 14336-14600 or udp portrange 319-320 or udp port 9998)) and (not ((vlan 701 and udp portrange 14336-14600) or (vlan 701 and udp portrange 319-320) or (vlan 701 and udp port 9998)) )</em></strong></p></div><div id="comment-55525-info" class="comment-info"><span class="comment-age">(13 Sep '16, 09:33)</span> <span class="comment-user userinfo">PropellerHead</span></div></div></div><div id="comment-tools-55524" class="comment-tools"></div><div class="clear"></div><div id="comment-55524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55528"></span>

<div id="answer-container-55528" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55528-score" class="post-score" title="current number of votes">1</div><span id="post-55528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture traffic for <em>all</em> vlan's, simply omit the optional vlan_id, 701 in this case.</p><p>So, to achieve what you want, I think the following capture filter should work:</p><pre><code>vlan and not (udp portrange 14336-14600 or udp portrange 319-320 or udp port 9998)</code></pre><p>Here you'll notice that I placed the <code>vlan</code> keyword first, since the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter man page</a> indicates that, <em>"Note that the first <strong>vlan</strong> keyword encountered in expression changes the decoding offsets for the remainder of expression on the assumption that the packet is a VLAN packet."</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-55528" class="comments-container"><span id="55531"></span><div id="comment-55531" class="comment"><div id="post-55531-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response.</p><p>Maybe I didn't explain thoroughly enough... some of the packets don't have a vlan tag either. On this particular switch, local traffic doesn't have a vlan tag but anything coming from another switch (fiber trunk) has vlan tag. Can your filter be modified to include non-vlan tagged packets?</p></div><div id="comment-55531-info" class="comment-info"><span class="comment-age">(13 Sep '16, 13:10)</span> <span class="comment-user userinfo">PropellerHead</span></div></div><span id="55532"></span><div id="comment-55532" class="comment"><div id="post-55532-score" class="comment-score"></div><div class="comment-text"><p>In that case, you need to duplicate the UDP port exclusion portion of the capture filter:</p><pre><code>(not (udp portrange 14336-14600 or udp portrange 319-320 or udp port 9998)) or (vlan and not (udp portrange 14336-14600 or udp portrange 319-320 or udp port 9998))</code></pre></div><div id="comment-55532-info" class="comment-info"><span class="comment-age">(13 Sep '16, 13:14)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="55535"></span><div id="comment-55535" class="comment"><div id="post-55535-score" class="comment-score"></div><div class="comment-text"><p>For some reason, tagged and untagged packets from the 14K port range are still showing up in my captures. To be clear, the port ranges are all destination ports.</p></div><div id="comment-55535-info" class="comment-info"><span class="comment-age">(13 Sep '16, 14:22)</span> <span class="comment-user userinfo">PropellerHead</span></div></div><span id="55540"></span><div id="comment-55540" class="comment"><div id="post-55540-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you could post a sample capture to cloudshark (or elsewhere) of the traffic that you're capturing for which you are trying to avoid capturing?</p></div><div id="comment-55540-info" class="comment-info"><span class="comment-age">(13 Sep '16, 16:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="55548"></span><div id="comment-55548" class="comment"><div id="post-55548-score" class="comment-score"></div><div class="comment-text"><blockquote><p>To be clear, the port ranges are all destination ports.</p></blockquote><p>There is yet another set of modifiers, <code>src</code> and <code>dst</code>, which may be used for various types of addresses. So changing <code>udp port[range]</code> to <code>udp dst port[range]</code> should solve your issue.</p></div><div id="comment-55548-info" class="comment-info"><span class="comment-age">(14 Sep '16, 01:45)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55553"></span><div id="comment-55553" class="comment not_top_scorer"><div id="post-55553-score" class="comment-score"></div><div class="comment-text"><p>I don't see how specifying <code>dst</code> is going to help. Without that specifier, the filter will match either the source or destination port[range].</p><p>I would guess that there's some other encapsulation going on for those packets, such as Q-in-Q, but rather than guess, I figured I'd ask for a capture file.</p></div><div id="comment-55553-info" class="comment-info"><span class="comment-age">(14 Sep '16, 05:21)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-55528" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


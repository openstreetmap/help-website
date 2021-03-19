+++
type = "question"
title = "WireShark vs NetShark"
description = '''What doest is mean by &quot;No, really, I have a LOT of traffic&quot; Would like to know in what kind of environment / requirements to chose NetShark? I am planning to use Wireshark for 24x7 packet capture.'''
date = "2016-07-05T01:42:00Z"
lastmod = "2016-07-05T14:43:00Z"
weight = 53824
keywords = [ "question" ]
aliases = [ "/questions/53824" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark vs NetShark](/questions/53824/wireshark-vs-netshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53824-score" class="post-score" title="current number of votes">0</div><span id="post-53824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What doest is mean by "No, really, I have a LOT of traffic"</p><p>Would like to know in what kind of environment / requirements to chose NetShark?</p><p>I am planning to use Wireshark for 24x7 packet capture.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '16, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/d245f0ceec31c05a9420cfff3b2e163d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WYee&#39;s gravatar image" /><p><span>WYee</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WYee has no accepted answers">0%</span></p></div></div><div id="comments-container-53824" class="comments-container"><span id="53827"></span><div id="comment-53827" class="comment"><div id="post-53827-score" class="comment-score"></div><div class="comment-text"><p>I don't really know what NetShark is so I will let others answer you who know more about this product.<br />
</p><p>I can only share that Wireshark is not your tool for 24/7 capture. Due to continuous memory consumption and other risk factors, you won't be happy with long term performance as it will crash. The suggested methods of long term capture are:</p><p>tcpdump (typical for a Unix-like system) windump (Windows system) dumpcap (typical for either system with Wireshark installed)</p><p>I do my background captures with one of these, then analyze with tshark and Wireshark.</p></div><div id="comment-53827-info" class="comment-info"><span class="comment-age">(05 Jul '16, 02:40)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-53824" class="comment-tools"></div><div class="clear"></div><div id="comment-53824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53833"></span>

<div id="answer-container-53833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53833-score" class="post-score" title="current number of votes">0</div><span id="post-53833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be able to get a taste when reading the <a href="http://www.riverbed.com/nl/products/steelcentral/network-performance-management/steelcentral-netshark.html">NetShark</a> pages. Wireshark is a power tool, in its own domain, that is getting to the details of <em>every</em> bit in a packet. That doesn't jive well with prolonged high data rate capture. NetShark is finely tuned to support long term capture, and getting an overview of that traffic, while allowing you to go into depth, when and where needed. More of a top down approach, while Wireshark has more of a bottom up approach, looking at every frame in every detail, then working its way up (to some degree).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '16, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-53833" class="comments-container"><span id="53834"></span><div id="comment-53834" class="comment"><div id="post-53834-score" class="comment-score"></div><div class="comment-text"><p>NetShark is a complete hardware packet capture system, including high-speed disk I/O, leading to a price that is much greater than wireshark.</p></div><div id="comment-53834-info" class="comment-info"><span class="comment-age">(05 Jul '16, 07:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53835"></span><div id="comment-53835" class="comment"><div id="post-53835-score" class="comment-score"></div><div class="comment-text"><p>... Which also means it can handle a lot more traffic without dropping packets.</p><p>If you've got a lot of traffic to capture (large number of packets or bytes per second) then you should do some trials to see if dumpcap or tcpdump can handle the traffic rate with an acceptable (to you) amount of packet drops.</p></div><div id="comment-53835-info" class="comment-info"><span class="comment-age">(05 Jul '16, 07:29)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-53833" class="comment-tools"></div><div class="clear"></div><div id="comment-53833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53846"></span>

<div id="answer-container-53846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53846-score" class="post-score" title="current number of votes">0</div><span id="post-53846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A "poor man's" Netshark, depending on requirements for historical captures, can also be scripted use of Wireshark's command line utilities. For example you can write a very simple bash or perl script that calls "dumpcap" to capture traffic on a given interface for a given time interval and have it save these timed captures into a directory where each capture is timestamped. You can even create a quick-and-dirty retention policy for capture files with bash's "find" command, piped to an "rm" to delete files that exceed a given age.</p><p>From there, many possible (free) bells and whistles can be set up. For example you can do scripted reads against those hourly capture files with tshark -z, to pull all sorts of application-specific counter measurements out of it for analytics.</p><p>Now, this is going to depend on requirements. Such a server needs fast disk I/O, potentially a large amount of storage (depending on what you're capturing), not to mention security/auditing of users accessing the captures. Depending on use it may need more interfaces (depending on how you are physically receiving the packet streams you are capturing).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '16, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-53846" class="comments-container"></div><div id="comment-tools-53846" class="comment-tools"></div><div class="clear"></div><div id="comment-53846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "FIltering out my mobile packets"
description = '''How to filter out traffic that I do with my mobile phone while being on computer? I can filter out other computers but I can&#x27;t do that for phones that are connecting to Internet wirelessly through my router. IPs and MAC are like these: 192.168.1.101 64:A7:69:47:5C:50 192.168.1.119 00:24:1D:91:8D:73 ...'''
date = "2012-07-20T12:13:00Z"
lastmod = "2012-07-21T03:21:00Z"
weight = 12883
keywords = [ "mobile", "filtering", "packets" ]
aliases = [ "/questions/12883" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FIltering out my mobile packets](/questions/12883/filtering-out-my-mobile-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12883-score" class="post-score" title="current number of votes">0</div><span id="post-12883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to filter out traffic that I do with my mobile phone while being on computer? I can filter out other computers but I can't do that for phones that are connecting to Internet wirelessly through my router. IPs and MAC are like these:</p><p>192.168.1.101 64:A7:69:47:5C:50<br />
192.168.1.119 00:24:1D:91:8D:73<br />
192.168.1.103 E4:B0:21:B5:1E:58 - phone<br />
192.168.1.114 00:18:8B:71:16:7E</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '12, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/2b1c3031ecd1917cb35439e5c634bf5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amman&#39;s gravatar image" /><p><span>Amman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amman has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-12883" class="comments-container"></div><div id="comment-tools-12883" class="comment-tools"></div><div class="clear"></div><div id="comment-12883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12893"></span>

<div id="answer-container-12893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12893-score" class="post-score" title="current number of votes">0</div><span id="post-12893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>what do you mean by "filter out"?</p><ol><li>Do you want to see the traffic and it's not in the capture file</li><li>You don't want to see the traffic that's already in the capture file</li></ol><p><strong>Suggestion for 1:</strong></p><p>You will only see that traffic if you captured data at the right place. If your router is also the wirelass AP, you need to capture within the router or on its LAN/WAN interface. If the wireless devices are connected through another AP (access point), you need to capture there.</p><p>See this: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p><strong>Suggestion for 2:</strong></p><p>Use either a capture filter or a display filter</p><p>Capture filter (during capture): not (host 192.168.1.101 or host 192.168.1.119)<br />
Display filter (after capturing): not (ip.addr == 192.168.1.101 or ip.addr == 192.168.1.119)</p><blockquote><p><code>http://wiki.wireshark.org/CaptureFilters</code><br />
<code>http://wiki.wireshark.org/DisplayFilters</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '12, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12893" class="comments-container"></div><div id="comment-tools-12893" class="comment-tools"></div><div class="clear"></div><div id="comment-12893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Identifying packet payload between PLC and CitectSCADA"
description = '''I have a console computer running CitectSCADA connected to a PLC via a managed switch with wireshark monitoring the network. I need to identify which packets in the stream correspond to actions on the user interface on SCADA (i.e. changing a tag value from 0 to 1 and vice versa), but there are hundr...'''
date = "2015-10-22T08:52:00Z"
lastmod = "2015-10-22T12:23:00Z"
weight = 46838
keywords = [ "firewall", "plc", "payload", "beginner", "scada" ]
aliases = [ "/questions/46838" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying packet payload between PLC and CitectSCADA](/questions/46838/identifying-packet-payload-between-plc-and-citectscada)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46838-score" class="post-score" title="current number of votes">0</div><span id="post-46838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a console computer running CitectSCADA connected to a PLC via a managed switch with wireshark monitoring the network. I need to identify which packets in the stream correspond to actions on the user interface on SCADA (i.e. changing a tag value from 0 to 1 and vice versa), but there are hundreds of packets being captured a second. How do I narrow this down to find what I am looking for? The end goal is to identify the payload of the packets for these actions in SCADA to build a firewall for the system.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-plc" rel="tag" title="see questions tagged &#39;plc&#39;">plc</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-scada" rel="tag" title="see questions tagged &#39;scada&#39;">scada</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/5c67bb3d7618d4c81760f222d79d1624?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbaturin&#39;s gravatar image" /><p><span>rbaturin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbaturin has no accepted answers">0%</span></p></div></div><div id="comments-container-46838" class="comments-container"></div><div id="comment-tools-46838" class="comment-tools"></div><div class="clear"></div><div id="comment-46838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46841"></span>

<div id="answer-container-46841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46841-score" class="post-score" title="current number of votes">0</div><span id="post-46841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but there are <strong>hundreds of packets being captured a second</strong>.<br />
<strong>How do I narrow this down</strong> to find what I am looking for?</p></blockquote><p>This sounds like searching the needle in the haystack. So I suggest to reduce the size of the haystack to solve your problem.</p><p>The best way would be: Trigger only one action at a time and monitor that with Wireshark. So you can 'easily' map an action to the content of a network frame. If you can't do that, this is going to become a looooong an tedious reverse engineering task.</p><p>Sorry, no easy way from my point of view, except for what I said: Only one action at a time!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46841" class="comments-container"></div><div id="comment-tools-46841" class="comment-tools"></div><div class="clear"></div><div id="comment-46841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46848"></span>

<div id="answer-container-46848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46848-score" class="post-score" title="current number of votes">0</div><span id="post-46848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most PLC's run a particular protocol, e.g. Modbus, DNP3.0, etc, and these protocols usually run over a single port that is often IANA assigned, although for operational reasons a different port is sometimes used. If the protocol runs over a non-standard port Wireshark won't be able to dissect it unless the protocol has a preference setting for a different port, or supports heuristic detection or you use "Decode As" to specify the correct protocol for the actual port in use.</p><p>Are your firewall requirements to simply restrict the traffic to a particular port\ip address, in which case simple inspection of the traffic (and\or knowledge of the protocol being used) should be sufficient, or are you attempting to actually restrict the protocol data elements in use? The latter will be very difficult to do without knowledge of the actual protocol and PLC configuration as not all data elements may be read or written at any particular time and thus appear in the capture. Think about alarm values, or outputs to set process points. Note that some PLC protocols use a "report by exception" mode where data isn't actually "read" (possibly the full data is only read at SCADA master start-up), only changes in the data are reported by the PLC. Some protocols poll for a "block" of data at regular intervals, regardless of what has changed in the PLC.</p><p>The configuration in CitectSCADA will be able to tell you which I/O driver (aka protocol) is being used and also the data elements in the PLC that are configured. The PLC configuration will definitely tell you what data elements are in use. What is the make and model of the PLC and what is the protocol in use?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46848" class="comments-container"></div><div id="comment-tools-46848" class="comment-tools"></div><div class="clear"></div><div id="comment-46848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


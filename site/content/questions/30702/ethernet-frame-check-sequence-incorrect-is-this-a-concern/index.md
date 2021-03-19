+++
type = "question"
title = "Ethernet Frame Check Sequence Incorrect - Is this a concern?"
description = '''Hello, Fairly new to Wireshark. When I ran this capture on an ip address it has this Ethernet FCS Incorrect event for every ping. I&#x27;m not sure if this is something I need to worry about or not.  I was capturing a Class B network checking for FCS incorrect events and it was alarming.  I don&#x27;t see a w...'''
date = "2014-03-11T18:53:00Z"
lastmod = "2014-03-11T21:04:00Z"
weight = 30702
keywords = [ "fcs" ]
aliases = [ "/questions/30702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet Frame Check Sequence Incorrect - Is this a concern?](/questions/30702/ethernet-frame-check-sequence-incorrect-is-this-a-concern)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30702-score" class="post-score" title="current number of votes">0</div><span id="post-30702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Fairly new to Wireshark. When I ran this capture on an ip address it has this Ethernet FCS Incorrect event for every ping. I'm not sure if this is something I need to worry about or not.</p><p>I was capturing a Class B network checking for FCS incorrect events and it was alarming.</p><p>I don't see a way to add the capture here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/8b3a5f496dccbdfba2e2873875976f5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkme&#39;s gravatar image" /><p><span>sharkme</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkme has no accepted answers">0%</span></p></div></div><div id="comments-container-30702" class="comments-container"></div><div id="comment-tools-30702" class="comment-tools"></div><div class="clear"></div><div id="comment-30702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30704"></span>

<div id="answer-container-30704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30704-score" class="post-score" title="current number of votes">2</div><span id="post-30704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can upload your capture file somewhere else, like www.cloudshark.org, and then include a link to it in your question.</p><p>Usually incorrect Frame Check Sequences are not a problem. Almost all modern network cards do checksum offloading; that is, the FCS is calculated and applied by the NIC instead of by the OS. If you're capturing on one of the endpoints, Wireshark will see frames transmitted by that system before the FCS is calculated and added by the NIC.</p><p>Some signs that incorrect Frame Check Sequences are just due to checksum offloading, and are not really an error:</p><ol><li>The incorrect Frame Check Sequences are only on frames transmitted by the system that you captured on.</li><li>The communication succeeds. In this case, you get a reply to the pings. If the Frame Check Sequences were really incorrect, the frames would be discarded and the communication would fail.</li></ol><p>Its usually better to capture from the wire instead of from either of the endpoints involved in the communication. There are other reasons, besides checksum offloading, why the packets that are transmitted on the wire will be different from packets captured on an endpoint.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 21:04</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-30704" class="comments-container"></div><div id="comment-tools-30704" class="comment-tools"></div><div class="clear"></div><div id="comment-30704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


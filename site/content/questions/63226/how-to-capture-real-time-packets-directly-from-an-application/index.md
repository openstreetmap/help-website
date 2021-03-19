+++
type = "question"
title = "How to capture real-time packets directly from an application"
description = '''Looking for best way to convey my application&#x27;s IPv6 packets in real-time to Wireshark. My application does not Tx/Rx packets on a conventional network or network interface that Wireshark can easily sniff.  It would for example, be great to output my packets to a UDP socket that I can tell Wireshark...'''
date = "2017-07-28T17:19:00Z"
lastmod = "2017-07-28T22:38:00Z"
weight = 63226
keywords = [ "capture", "application", "real-time" ]
aliases = [ "/questions/63226" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture real-time packets directly from an application](/questions/63226/how-to-capture-real-time-packets-directly-from-an-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63226-score" class="post-score" title="current number of votes">0</div><span id="post-63226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking for best way to convey my application's IPv6 packets in real-time to Wireshark. My application does not Tx/Rx packets on a conventional network or network interface that Wireshark can easily sniff. It would for example, be great to output my packets to a UDP socket that I can tell Wireshark to listen on. I feel that so many developers must have had this need, that Wireshark includes built-in support for this in some way.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-real-time" rel="tag" title="see questions tagged &#39;real-time&#39;">real-time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '17, 17:19</strong></p><img src="https://secure.gravatar.com/avatar/99f114b66b6aa43a42ddbe3d8d052aed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikegrobler&#39;s gravatar image" /><p><span>mikegrobler</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikegrobler has no accepted answers">0%</span></p></div></div><div id="comments-container-63226" class="comments-container"></div><div id="comment-tools-63226" class="comment-tools"></div><div class="clear"></div><div id="comment-63226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63229"></span>

<div id="answer-container-63229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63229-score" class="post-score" title="current number of votes">0</div><span id="post-63229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have two basic options:</p><ul><li>on *n*x systems, you can send the UDP packets to the lo inteface and capture there (and if you choose a nice source and destination port and set a corresponding capture filter, you even won't be bothered by other traffic which exists on lo). On Windows, you need to install npcap to be able to capture at lo interface.</li><li>or you can encapsulate the packets in your application as pcap and feed Wireshark through an input pipe. Just remember you have to send the pcap header once, before the very first packet.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jul '17, 22:39</strong> </span></p></div></div><div id="comments-container-63229" class="comments-container"></div><div id="comment-tools-63229" class="comment-tools"></div><div class="clear"></div><div id="comment-63229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


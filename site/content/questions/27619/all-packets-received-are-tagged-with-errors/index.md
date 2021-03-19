+++
type = "question"
title = "All packets received are tagged with errors"
description = '''Hi, I&#x27;m trying to examine packet loss of tcp of wireless. I start a capture and filter the results with the express &quot;ip.addr=={my ip address} and tcp&quot;. This works, but every packet displayed shows some sort of error in it (TCP checksum incorrect, Malformed packet, TCP previous segment not captured, ...'''
date = "2013-12-01T14:42:00Z"
lastmod = "2013-12-02T01:19:00Z"
weight = 27619
keywords = [ "file-format", "filtering", "tcp" ]
aliases = [ "/questions/27619" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [All packets received are tagged with errors](/questions/27619/all-packets-received-are-tagged-with-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27619-score" class="post-score" title="current number of votes">0</div><span id="post-27619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to examine packet loss of tcp of wireless. I start a capture and filter the results with the express "ip.addr=={my ip address} and tcp". This works, but every packet displayed shows some sort of error in it (TCP checksum incorrect, Malformed packet, TCP previous segment not captured, etc). I have yet to see a packet come through with out any of these tags. Am I unknowingly applying some filter that only shows these results? Also, is there a way to see if packets are being dropped due to timeouts or packet reordering?</p><p>I would also like to see packets at the data link layer. Is this possible through wireshark?</p><p>Lastly, I would like to save the results shown in the main panel to a text file to do some parsing (for input into a python program). What format should I be saving the capture as?</p><p>Thanks, Andy</p><p>EDIT: I've included a picture of all what my screen typically looks like when capturing:<img src="https://osqa-ask.wireshark.org/upfiles/WireShark_bad_packets_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-file-format" rel="tag" title="see questions tagged &#39;file-format&#39;">file-format</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '13, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/f130107ebdf13a027e7b36be6bcaa714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolvie964&#39;s gravatar image" /><p><span>wolvie964</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolvie964 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '13, 14:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-27619" class="comments-container"><span id="27620"></span><div id="comment-27620" class="comment"><div id="post-27620-score" class="comment-score"></div><div class="comment-text"><p>I've figured out the saving part. I was doing Save as instead of Export Packet Dissections.</p></div><div id="comment-27620-info" class="comment-info"><span class="comment-age">(01 Dec '13, 15:59)</span> <span class="comment-user userinfo">wolvie964</span></div></div></div><div id="comment-tools-27619" class="comment-tools"></div><div class="clear"></div><div id="comment-27619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27625"></span>

<div id="answer-container-27625" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27625-score" class="post-score" title="current number of votes">1</div><span id="post-27625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wolvie964 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To answer a few of the questions:</p><p>The "bad checksum" error is 99.99999% of the time just a false alarm. Go to Edit &gt; Preferences &gt; Protoocls, and under IPv4 and TCP disable the checksum check to get rid of it. The reason you see that is because Wireshark is seeing the packet before the checksum is actually getting calculated (so you'll see errors on the packets that your own machine is sending, but those errors aren't real).</p><p>Wireshark can dissect at the datalink layer, yes. That's usually the level it goes to, if for example you simply open a live packet capture on an Ethernet interface.</p><p>For the export to text question, yes. Depending on Wireshark version (assuming the latest), that would be File &gt; Export Packet Dissections &gt; as "Plain Text" file, and set the packet range to "Displayed" to push just the packets matching the current display filter to text.</p><p>For the last question on TCP warnings, where you're getting acks for segments not seen in trace file I guess my question is how this packet capture was produced? That error can mean that Wireshark did not receive some of the packets in the TCP stream which actually happened, though out-of-order packets as they're received by the analyzer can cause some of these error types as well.</p><p>For the question on whether it's possible to see whether packets are being dropped due to timeouts, at what layer are you referring?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '13, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-27625" class="comments-container"><span id="27649"></span><div id="comment-27649" class="comment"><div id="post-27649-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response Quadratic. I'm interested in timeouts in the transport layer (retransmission timeout).</p><p>Thanks, Andy</p></div><div id="comment-27649-info" class="comment-info"><span class="comment-age">(02 Dec '13, 01:19)</span> <span class="comment-user userinfo">wolvie964</span></div></div></div><div id="comment-tools-27625" class="comment-tools"></div><div class="clear"></div><div id="comment-27625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Multicast works when wireshark starts"
description = '''Hello all, I have a strange behavior in my lab. I have configure an application server to receive a multicast stream from a camera, but nothing is received. So I started wireshark and magically I received the multicast stream. If I stopped wireshark, I do not receive the stream Multicast. It seems t...'''
date = "2014-01-28T01:56:00Z"
lastmod = "2014-01-28T06:01:00Z"
weight = 29224
keywords = [ "multicast", "wireshark" ]
aliases = [ "/questions/29224" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multicast works when wireshark starts](/questions/29224/multicast-works-when-wireshark-starts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29224-score" class="post-score" title="current number of votes">0</div><span id="post-29224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I have a strange behavior in my lab. I have configure an application server to receive a multicast stream from a camera, but nothing is received. So I started wireshark and magically I received the multicast stream. If I stopped wireshark, I do not receive the stream Multicast.</p><p>It seems that when wireshark listens to the server NIC, this wake up the nic and allow to receive the multicasts. By stopping wireshark to listen to the nic card, then the server also stops receiving the multicast. What wireshark do exactly when listening to the traffic?</p><p>Can someone explain me this behavior?</p><p>Thank you very much</p><p>Alex.O</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '14, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/47a941d4ac771bfe740e22238b482269?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexo&#39;s gravatar image" /><p><span>Alexo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexo has no accepted answers">0%</span></p></div></div><div id="comments-container-29224" class="comments-container"></div><div id="comment-tools-29224" class="comment-tools"></div><div class="clear"></div><div id="comment-29224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29228"></span>

<div id="answer-container-29228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29228-score" class="post-score" title="current number of votes">0</div><span id="post-29228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What wireshark do exactly when listening to the traffic?</p></blockquote><p>It puts the interface in 'promiscuous mode'. In that mode the system will accept all ethernet frames, not just the ones with the MAC address of the NIC (or broadcast or multicast).</p><p>Please check the MAC address of your frames. It is most certainly not the broadcast address (or a multicast address).</p><p>BTW: can you post a sample frame on cloudshark.org ?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '14, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29228" class="comments-container"><span id="29230"></span><div id="comment-29230" class="comment"><div id="post-29230-score" class="comment-score"></div><div class="comment-text"><p>hello Kurt,</p><p>All cameras have multicast mac address beginning by 01:00:5e</p><p>Alex</p></div><div id="comment-29230-info" class="comment-info"><span class="comment-age">(28 Jan '14, 02:58)</span> <span class="comment-user userinfo">Alexo</span></div></div><span id="29234"></span><div id="comment-29234" class="comment"><div id="post-29234-score" class="comment-score"></div><div class="comment-text"><p>Can you please post a sample capture file?</p></div><div id="comment-29234-info" class="comment-info"><span class="comment-age">(28 Jan '14, 03:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29228" class="comment-tools"></div><div class="clear"></div><div id="comment-29228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29238"></span>

<div id="answer-container-29238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29238-score" class="post-score" title="current number of votes">0</div><span id="post-29238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Been there... had that problem...</p><p>Assuming that we're talking IP Multicast (i.e., an IP camera):</p><p>The short answer:</p><p>I would guess that the server application is not configured properly to receive the traffic for the required IP multicast group address matching that being used by the camera.</p><p>The longer answer:</p><p>The multicast listener (server) must exec some code to "join" the desired IP Multicast group. The effect is basically that the group address is translated to a specific ethernet MAC group address and then that address is added to the list of MAC addresses for which the NIC card accepts traffic.</p><p>As Kurt indicated, if the NIC is in promiscuous mode, then all frames are accepted and things work.</p><p>So: (assuming that the server application has the code to do the "join") there's probably a configuration issue (wrong group address ?).</p><p>If the application is homegrown, the code needs to do a "join". (I don't remember if the "join" can be done using a command level tool before running the application).</p><p>(A web search for 'camera "IP multicast"' will find lots of info).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '14, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '14, 08:20</strong> </span></p></div></div><div id="comments-container-29238" class="comments-container"></div><div id="comment-tools-29238" class="comment-tools"></div><div class="clear"></div><div id="comment-29238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


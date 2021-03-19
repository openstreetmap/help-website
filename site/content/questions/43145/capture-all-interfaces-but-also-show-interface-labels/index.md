+++
type = "question"
title = "Capture &#x27;All&#x27; Interfaces, but also show Interface labels"
description = '''I haven&#x27;t found a question on this, however please let me know if there&#x27;s a dupe of this. I have several network interfaces on my system - virtual network interfaces for VMs (vmnet##), Ethernet interface for wired (eth0), and a wireless interface (wlan0), not to mention USB and Localhost interfaces ...'''
date = "2015-06-14T11:03:00Z"
lastmod = "2015-06-15T05:40:00Z"
weight = 43145
keywords = [ "wireshark-1.12", "gui", "multiple-interfaces" ]
aliases = [ "/questions/43145" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture 'All' Interfaces, but also show Interface labels](/questions/43145/capture-all-interfaces-but-also-show-interface-labels)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43145-score" class="post-score" title="current number of votes">0</div><span id="post-43145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I haven't found a question on this, however please let me know if there's a dupe of this.</p><p>I have several network interfaces on my system - virtual network interfaces for VMs (<code>vmnet##</code>), Ethernet interface for wired (<code>eth0</code>), and a wireless interface (<code>wlan0</code>), not to mention USB and Localhost interfaces occasionally.</p><p>In Wireshark (I'm on 1.12.1), I occasionally use the 'Any' capture which captures everything. However, it gets confusing trying to ID the interface it goes out over.</p><p>Is there any way in the Wireshark GUI to identify the network interface as well when using the 'Any' capture that captures on all interfaces, so as being able to see the labels for the given interfaces the traffic is being received/sent through?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark-1.12" rel="tag" title="see questions tagged &#39;wireshark-1.12&#39;">wireshark-1.12</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-multiple-interfaces" rel="tag" title="see questions tagged &#39;multiple-interfaces&#39;">multiple-interfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '15, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/6e70e6cd981e293d57d1f2f0601e3f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teward&#39;s gravatar image" /><p><span>teward</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teward has no accepted answers">0%</span></p></div></div><div id="comments-container-43145" class="comments-container"></div><div id="comment-tools-43145" class="comment-tools"></div><div class="clear"></div><div id="comment-43145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43151"></span>

<div id="answer-container-43151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43151-score" class="post-score" title="current number of votes">1</div><span id="post-43151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there any way in the Wireshark GUI to identify the network interface as well when using the 'Any' capture</p></blockquote><p>Currently, no. The capture code path would have to be changed so that, instead of a single record in the pcap-ng file for the "any" interface, it has a record for all the interfaces it sees, and so that each packet is marked as having come from the interface in question. This is doable, but would require some work on both libpcap and the dumpcap program.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '15, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43151" class="comments-container"><span id="43181"></span><div id="comment-43181" class="comment"><div id="post-43181-score" class="comment-score"></div><div class="comment-text"><p>OK, so that answers that one. Thanks for the prompt response.</p></div><div id="comment-43181-info" class="comment-info"><span class="comment-age">(15 Jun '15, 05:40)</span> <span class="comment-user userinfo">teward</span></div></div></div><div id="comment-tools-43151" class="comment-tools"></div><div class="clear"></div><div id="comment-43151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43146"></span>

<div id="answer-container-43146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43146-score" class="post-score" title="current number of votes">0</div><span id="post-43146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can see in Packet Details in the Frame Section: <img src="https://osqa-ask.wireshark.org/upfiles/Packet.PNG" alt="alt text" /></p><p>The Id you can see in the Interfacelist <img src="https://osqa-ask.wireshark.org/upfiles/Imterfaces.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '15, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-43146" class="comments-container"><span id="43147"></span><div id="comment-43147" class="comment"><div id="post-43147-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but I mean an easier, friendlier method, such as displaying the friendly name in a column or such...</p></div><div id="comment-43147-info" class="comment-info"><span class="comment-age">(14 Jun '15, 12:16)</span> <span class="comment-user userinfo">teward</span></div></div></div><div id="comment-tools-43146" class="comment-tools"></div><div class="clear"></div><div id="comment-43146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


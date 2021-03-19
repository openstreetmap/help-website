+++
type = "question"
title = "Monitoring 2 interfaces on the same machine"
description = '''Hi I wish to use a machine with 2 interfaces, and transmit frames on one interface, to be received on the other interface via a switch. I wish to capture the frames leaving and coming back on the 2 interfaces at the same time. The intention is to compare the two captures to test for jitter and laten...'''
date = "2012-10-09T06:55:00Z"
lastmod = "2012-10-11T07:28:00Z"
weight = 14817
keywords = [ "timing", "interfaces" ]
aliases = [ "/questions/14817" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring 2 interfaces on the same machine](/questions/14817/monitoring-2-interfaces-on-the-same-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14817-score" class="post-score" title="current number of votes">0</div><span id="post-14817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I wish to use a machine with 2 interfaces, and transmit frames on one interface, to be received on the other interface via a switch.</p><p>I wish to capture the frames leaving and coming back on the 2 interfaces at the same time. The intention is to compare the two captures to test for jitter and latency across the switch.</p><p>I can run two instances of Wireshark side by side each monitoring a single interface to achieve this, but I find that when compared, some packets are time stamped as received before they were sent. I fear there is some skewing of data caused by the 2 programs competing for resources.</p><p>I suspect my results would be more stable if I could use one instance of wireshark to view the traffic from both interfaces. I know this is possible in most circumstances but it does not seem to display both sent and received copies of the same frame by default.</p><p>Can anyone help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timing" rel="tag" title="see questions tagged &#39;timing&#39;">timing</span> <span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/60074dc48073fb4204f469af5ca2b439?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Urumiko&#39;s gravatar image" /><p><span>Urumiko</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Urumiko has no accepted answers">0%</span></p></div></div><div id="comments-container-14817" class="comments-container"></div><div id="comment-tools-14817" class="comment-tools"></div><div class="clear"></div><div id="comment-14817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14818"></span>

<div id="answer-container-14818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14818-score" class="post-score" title="current number of votes">0</div><span id="post-14818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I wish to use a machine with 2 interfaces, and transmit frames on one interface, to be received on the other interface via a switch.</p></blockquote><p>The packets will not leave the IP stack (not going to the witch), as the source and destination addresses are on the same machine. That might be the reason for the timestamp issue.</p><p>If you want the packets to leave, you need a second machine with NAT capabilities and or Port Forwarding. Something like this.</p><blockquote><p><code>PC[1:1.1.1.5:45000]  -- [1.1.1.1:8000] PC2 [2.2.2.2:45000] -- PC1[2.2.2.5:8080]</code></p></blockquote><p>Your communication will be:</p><p>PC1 -&gt; PC2:8080<br />
PC2 will NAT/Port Forward the connection back to PC1, but different interface (IP)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14818" class="comments-container"><span id="14854"></span><div id="comment-14854" class="comment"><div id="post-14854-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for your input but my packet generation software is generating raw Ethernet frames with correct MAC addresses. IP addresses are present but invalid. No IP is configured on the interfaces themselves. The frames are still delivered on the strength of the mac address, so I don't think your suggestion is correct?</p></div><div id="comment-14854-info" class="comment-info"><span class="comment-age">(09 Oct '12, 23:33)</span> <span class="comment-user userinfo">Urumiko</span></div></div><span id="14857"></span><div id="comment-14857" class="comment"><div id="post-14857-score" class="comment-score"></div><div class="comment-text"><p>without any further information about your software (how does it actually send the frames) it's impossible to give an advice. Can you please add more details?</p></div><div id="comment-14857-info" class="comment-info"><span class="comment-age">(09 Oct '12, 23:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14818" class="comment-tools"></div><div class="clear"></div><div id="comment-14818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14883"></span>

<div id="answer-container-14883" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14883-score" class="post-score" title="current number of votes">0</div><span id="post-14883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, anyway, if you want to capture on 2 interfaces simultaneously you can use Wireshark 1.8.0+ which allows you to select 1 to N interfaces on which to do simultaneous captures.</p><p>Note, however, that with this method it is still possible for the frames to arrive out of order; actually my experience was that the timestamp was correct but Wireshark had received them out of order (I easily worked around that by sorting the frames by time). This was on Linux.</p><p>Another solution would be to use Linux and use the 'any' pseudodevice (which captures on all interfaces simultaneously).</p><p>But: if you're really interested in high-resolution time stamping, you may want to get a dedicated capture card (like those from Riverbed--Turbocap--or Endace).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-14883" class="comments-container"><span id="14910"></span><div id="comment-14910" class="comment"><div id="post-14910-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff that's pretty helpfull, i'll check it's not just a case of sorting by time-stamp.</p><p>Wow those riverbed devices look ideal, but well out of my price range. Do you know if there's a budget option? I really only need the time stamp down to a resolution of microseconds.</p></div><div id="comment-14910-info" class="comment-info"><span class="comment-age">(10 Oct '12, 23:36)</span> <span class="comment-user userinfo">Urumiko</span></div></div><span id="14930"></span><div id="comment-14930" class="comment"><div id="post-14930-score" class="comment-score"></div><div class="comment-text"><p>Honestly I don't know much about dedicated capture devices. Well, except that I thought that Riverbed's stuff <em>was</em> the budget option--but honestly I don't know.</p></div><div id="comment-14930-info" class="comment-info"><span class="comment-age">(11 Oct '12, 07:28)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-14883" class="comment-tools"></div><div class="clear"></div><div id="comment-14883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


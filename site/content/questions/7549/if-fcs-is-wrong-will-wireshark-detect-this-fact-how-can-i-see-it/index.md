+++
type = "question"
title = "If FCS is wrong, will Wireshark detect this fact? How can I see it?"
description = '''I use Wireshark version 1.4.0; OS: Windows 7 details of problem: I capture UDP stream, and I definitely know, that FCS of all packets is wrong. But all packets are captured and look normally in caprure window (colored blue). Is this possible to differ packets with wrong FCS from packets with correct...'''
date = "2011-11-22T00:01:00Z"
lastmod = "2011-11-22T01:02:00Z"
weight = 7549
keywords = [ "udp", "fcs" ]
aliases = [ "/questions/7549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [If FCS is wrong, will Wireshark detect this fact? How can I see it?](/questions/7549/if-fcs-is-wrong-will-wireshark-detect-this-fact-how-can-i-see-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7549-score" class="post-score" title="current number of votes">0</div><span id="post-7549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use Wireshark version 1.4.0; OS: Windows 7</p><p>details of problem: I capture UDP stream, and I definitely know, that FCS of all packets is wrong. But all packets are captured and look normally in caprure window (colored blue). Is this possible to differ packets with wrong FCS from packets with correct FCS?</p><p>Thank You!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '11, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/8254c5f351b65b722dfcf6cfa648f6ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gistereziz&#39;s gravatar image" /><p><span>Gistereziz</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gistereziz has no accepted answers">0%</span></p></div></div><div id="comments-container-7549" class="comments-container"><span id="7550"></span><div id="comment-7550" class="comment"><div id="post-7550-score" class="comment-score"></div><div class="comment-text"><p>Are you sure that all packets have wrong FCS and why ?</p><p>Normally your NIC will discard every frame with incorrect Layer 2 FCS and so those would never appear in wireshark</p></div><div id="comment-7550-info" class="comment-info"><span class="comment-age">(22 Nov '11, 00:54)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-7549" class="comment-tools"></div><div class="clear"></div><div id="comment-7549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7551"></span>

<div id="answer-container-7551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7551-score" class="post-score" title="current number of votes">2</div><span id="post-7551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer is: "It depends" :-)</p><p>Normally a NIC will drop frames with an incorrect FCS so you will not see the frames at all. But even if the frames are seen by wireshark most NICs (or their drivers) will strip the FCS before passing the packets on. So wireshark will not be able to see whether the FCS was correct or not.</p><p>Then in practice. I used my NetOptics tap in the timestamping mode, which basically uses the FCS field as a timestamp. To my big surprise I was able to see all packets on my ASUS laptop with Realtek NIC. My MacBook did not show any packets (as expected).</p><p>I mailed Realtek whether it was possible to make the NIC/driver *not* strip the FCS, but got a negative response (well, actually I think they did not understand the purpose of my question).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '11, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7551" class="comments-container"></div><div id="comment-tools-7551" class="comment-tools"></div><div class="clear"></div><div id="comment-7551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


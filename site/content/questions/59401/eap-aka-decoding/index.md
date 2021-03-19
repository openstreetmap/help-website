+++
type = "question"
title = "EAP-AKA decoding"
description = '''Hello I am trying to capture some EAP-AKA or EAP-SIM Traffic, and I do not see it decoded: (I see the messages from the AC to the UE, but from the UE to the AC I see IPX or malformed packets - though it is working ok)'''
date = "2017-02-14T04:03:00Z"
lastmod = "2017-02-14T09:53:00Z"
weight = 59401
keywords = [ "eap" ]
aliases = [ "/questions/59401" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [EAP-AKA decoding](/questions/59401/eap-aka-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59401-score" class="post-score" title="current number of votes">0</div><span id="post-59401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I am trying to capture some EAP-AKA or EAP-SIM Traffic, and I do not see it decoded: (I see the messages from the AC to the UE, but from the UE to the AC I see IPX or malformed packets - though it is working ok)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eap" rel="tag" title="see questions tagged &#39;eap&#39;">eap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '17, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/1f517be5ef86c8d961019bd09b5b119b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_PS&#39;s gravatar image" /><p><span>Mike_PS</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_PS has no accepted answers">0%</span></p></div></div><div id="comments-container-59401" class="comments-container"><span id="59402"></span><div id="comment-59402" class="comment"><div id="post-59402-score" class="comment-score"></div><div class="comment-text"><p>Could you share a capture for both EAP-AKA and EAP-SIM exchanges?</p><p>You can place the capture on a shared drive such as Cloudshark or Google drive.</p></div><div id="comment-59402-info" class="comment-info"><span class="comment-age">(14 Feb '17, 06:19)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="59403"></span><div id="comment-59403" class="comment"><div id="post-59403-score" class="comment-score"></div><div class="comment-text"><p>Thanks for quick response, please find it here: <a href="https://we.tl/LbkHnyIPWT">https://we.tl/LbkHnyIPWT</a></p></div><div id="comment-59403-info" class="comment-info"><span class="comment-age">(14 Feb '17, 06:32)</span> <span class="comment-user userinfo">Mike_PS</span></div></div><span id="59404"></span><div id="comment-59404" class="comment"><div id="post-59404-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-59404-info" class="comment-info"><span class="comment-age">(14 Feb '17, 06:37)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-59401" class="comment-tools"></div><div class="clear"></div><div id="comment-59401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59405"></span>

<div id="answer-container-59405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59405-score" class="post-score" title="current number of votes">0</div><span id="post-59405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In these two frames the wlan_mgt.mysterious_olpc_stuff field is not there, or at least the (v2.2.4) dissector thinks so (ignoring the fact that all packets are ethereal). When looking at the raw data its clear the field is there, two bytes further look like the start of LLC (DSAP and SSAP), like in the other packets.</p><p>Looking at the dissector code at this point there is a bit of magic going on</p><pre><code>         So, if the packet doesn&#39;t start with 0xaa 0xaa:
       we first use the same scheme that linux-wlan-ng does to detect
       those encapsulated Ethernet frames, namely looking to see whether
       the frame either starts with 6 octets that match the destination
       address from the 802.11 header or has 6 octets that match the
       source address from the 802.11 header following the first 6 octets,
       and, if so, treat it as an encapsulated Ethernet frame;

       otherwise, we use the same scheme that we use in the Ethernet
       dissector to recognize Netware 802.3 frames, namely checking
       whether the packet starts with 0xff 0xff and, if so, treat it
       as an encapsulated IPX frame, and then check whether the
       packet starts with 0x00 0x00 and, if so, treat it as an OLPC
       frame.</code></pre></pre><p>This should be in a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a>, so it can be further investigated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59405" class="comments-container"><span id="59407"></span><div id="comment-59407" class="comment"><div id="post-59407-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I opened a bug for this. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13411">Bug 13411</a> - EAP AKA not being decoded properly wireshark 2.2.4</p></div><div id="comment-59407-info" class="comment-info"><span class="comment-age">(14 Feb '17, 07:28)</span> <span class="comment-user userinfo">Mike_PS</span></div></div><span id="59412"></span><div id="comment-59412" class="comment"><div id="post-59412-score" class="comment-score"></div><div class="comment-text"><p>Perfect, bug set to confirmed.</p></div><div id="comment-59412-info" class="comment-info"><span class="comment-age">(14 Feb '17, 09:53)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-59405" class="comment-tools"></div><div class="clear"></div><div id="comment-59405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


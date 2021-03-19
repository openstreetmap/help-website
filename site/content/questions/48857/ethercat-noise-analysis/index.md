+++
type = "question"
title = "EtherCAT noise analysis"
description = '''I am trying to analysis EtherCAT packet using WireShark. I could capture EtherCAT packet and the data looks no problem. But, when the EtherCAT packet was destroyed by some reaseon, e.g. noise or cable broken, Can I detect the pacekt was destroyed or not? I can not find any filter to detect disturbed...'''
date = "2016-01-04T22:41:00Z"
lastmod = "2016-01-05T03:31:00Z"
weight = 48857
keywords = [ "noise", "ethercat" ]
aliases = [ "/questions/48857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [EtherCAT noise analysis](/questions/48857/ethercat-noise-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48857-score" class="post-score" title="current number of votes">0</div><span id="post-48857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analysis EtherCAT packet using WireShark.</p><p>I could capture EtherCAT packet and the data looks no problem.</p><p>But, when the EtherCAT packet was destroyed by some reaseon, e.g. noise or cable broken,</p><p>Can I detect the pacekt was destroyed or not?</p><p>I can not find any filter to detect disturbed EtherCAT signal.</p><p>In addition to, How can I detect some EtherCAT packet is loss or not?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-noise" rel="tag" title="see questions tagged &#39;noise&#39;">noise</span> <span class="post-tag tag-link-ethercat" rel="tag" title="see questions tagged &#39;ethercat&#39;">ethercat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '16, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/0abdd994afdaf78486b90fe5fd73622f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hetero98&#39;s gravatar image" /><p><span>hetero98</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hetero98 has no accepted answers">0%</span></p></div></div><div id="comments-container-48857" class="comments-container"><span id="48862"></span><div id="comment-48862" class="comment"><div id="post-48862-score" class="comment-score">1</div><div class="comment-text"><p>I think there are two parts to your question -</p><p>To detect loss, I think you can do a timing analysis. EtherCAT network may produce frames on a given interval (well, never used this protocol but google says process data is cyclic...) so a missing frame will show in the timing. If data is pushed out at a given interval, a lost frame will show as 2x the interval timing. Good display filters and a delta_time column can help with this.</p><p>To actually see the bad frame, you likely need some special hardware. Hilscher makes analysis cards for things like this, but for those challenged to get funding for such equipment, certain Intel NICs have a Linux driver that will pass up all frames, including bad ones, AND which have the CRC intact. These are readable in Wireshark, and sortable by looking at the FCS failure.</p></div><div id="comment-48862-info" class="comment-info"><span class="comment-age">(05 Jan '16, 03:31)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-48857" class="comment-tools"></div><div class="clear"></div><div id="comment-48857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48860"></span>

<div id="answer-container-48860" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48860-score" class="post-score" title="current number of votes">0</div><span id="post-48860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Normally, the network adapter only gives to the upper layers of the software (including Wireshark) frames which have been received properly from the wire, i.e. without any errors detected using the CRC mechanism. You would need a dedicated capturing hardware which would break this rule and hand over all frames, even broken ones, for further processing. Plus, as Wireshark doesn't even get access to the CRC field of the frame, you would need that the capturing software would get it, evaluate it, and set "CRC error" bit in frame information of the pcapng-formatted capture file so that you could display that information in Wireshark. The pcap format doesn't have such fields, it can accommodate only packet contents, no additional information fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '16, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '16, 02:57</strong> </span></p></div></div><div id="comments-container-48860" class="comments-container"></div><div id="comment-tools-48860" class="comment-tools"></div><div class="clear"></div><div id="comment-48860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


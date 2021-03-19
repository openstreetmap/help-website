+++
type = "question"
title = "Multiple time showing same message name for gsm_map message"
description = ''' Hi All, We are capturing a long gsm_map messages segmented and reassembled(XUDT). But for some reason the map messages name is appearing multiple times. Please find the attached pcap trace.  My question is why Wireshark showing the same message name multiple times in Info field? Can anyone please l...'''
date = "2015-07-21T09:21:00Z"
lastmod = "2015-07-22T17:50:00Z"
weight = 44329
keywords = [ "xudt", "segment", "reassembly", "gsm_map" ]
aliases = [ "/questions/44329" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple time showing same message name for gsm\_map message](/questions/44329/multiple-time-showing-same-message-name-for-gsm_map-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44329-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/pic4.png" alt="alt text" /></p><p>Hi All,</p><p>We are capturing a long gsm_map messages segmented and reassembled(XUDT). But for some reason the map messages name is appearing multiple times. Please find the attached pcap trace.</p><p>My question is why Wireshark showing the same message name multiple times in Info field?</p><p>Can anyone please let me know the reason.</p><p>Thanks in advance.</p><p>Regards,</p><p>Iqbal</p></div><div id="question-tags" class="tags-container tags">xudt segment reassembly gsm_map</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '15, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/9367527cd2ebabd1b49cec744a09147e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iqbal&#39;s gravatar image" /><p>iqbal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iqbal has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jul '15, 09:46</p></div></div><div id="comments-container-44329" class="comments-container"></div><div id="comment-tools-44329" class="comment-tools"></div><div class="clear"></div><div id="comment-44329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44399"></span>

<div id="answer-container-44399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44399-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is it showing the duplication only in the info column field, or is it actually showing the messages again and again in the packet details window as well? It's probably a bug. Can you open a bug for this on <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a> and attach a capture file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44399" class="comments-container"><span id="44411"></span><div id="comment-44411" class="comment"><div id="post-44411-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel, thank you so much for your reply. It is showing in Info field as well as in the packets details field. When I highlight those messages in the packet details field it is pointing to the same HEX dump. It seems to be a display bug. As per your advise, I have raised a ticket with Wireshark (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11391">Bug 11391</a>). And also I have uploaded a trace with the above said issue. I will update if there is any update on the ticket. Thanks.</p></div><div id="comment-44411-info" class="comment-info"><span class="comment-age">(23 Jul '15, 03:03)</span> iqbal</div></div><span id="44414"></span><div id="comment-44414" class="comment"><div id="post-44414-score" class="comment-score"></div><div class="comment-text"><p>Got a reply from Wireshark team:</p><p>"Dissection is working fine with master branch, so it looks like the corresponding (maybe too intrusive?) fix did not land in master-1.12 branch. In the meantime you can use Wireshark development builds instead. "</p><p>I did verify this on Dev build and it is displaying correctly. Thanks again Hadriel.</p></div><div id="comment-44414-info" class="comment-info"><span class="comment-age">(23 Jul '15, 04:27)</span> iqbal</div></div></div><div id="comment-tools-44399" class="comment-tools"></div><div class="clear"></div><div id="comment-44399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


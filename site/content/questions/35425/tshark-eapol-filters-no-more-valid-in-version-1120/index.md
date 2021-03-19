+++
type = "question"
title = "Tshark eapol filters no more valid in version 1.12.0"
description = '''Hi, I was previously using eapol filters with Tshark for differentiating between key exchange 1,2,3,4. I have updated my wireshark and apparently these filters don&#x27;t work anymore:  tshark -n -V -r mypcap.pcap -Tfields -e eapol.keydes.key_info.error -e eapol.keydes.key_info.key_mic -e eapol.keydes.ke...'''
date = "2014-08-11T18:03:00Z"
lastmod = "2014-08-12T02:44:00Z"
weight = 35425
keywords = [ "wireshark-1.12", "eapol" ]
aliases = [ "/questions/35425" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark eapol filters no more valid in version 1.12.0](/questions/35425/tshark-eapol-filters-no-more-valid-in-version-1120)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35425-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was previously using eapol filters with Tshark for differentiating between key exchange 1,2,3,4. I have updated my wireshark and apparently these filters don't work anymore:</p><blockquote><p>tshark -n -V -r mypcap.pcap -Tfields -e eapol.keydes.key_info.error -e eapol.keydes.key_info.key_mic -e eapol.keydes.key_info.install -e eapol.keydes.key_info.key_ack -e eapol.keydes.data_len</p></blockquote><p><strong>(process:65567): WARNING</strong> : 'eapol.keydes.key_info.error' isn't a valid field!</p><p><strong>(process:65567): WARNING</strong> : 'eapol.keydes.key_info.key_mic' isn't a valid field!</p><p><strong>(process:65567): WARNING</strong> : 'eapol.keydes.key_info.install' isn't a valid field!</p><p><strong>(process:65567): WARNING</strong> : 'eapol.keydes.key_info.key_ack' isn't a valid field!</p><p><strong>(process:65567): WARNING</strong> : 'eapol.keydes.data_len' isn't a valid field!</p><p>Why? And how to access to Key information with filters on the new version?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">wireshark-1.12 eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '14, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/7d584cd50c24d8e23cca9fed4ac396b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tsharker&#39;s gravatar image" /><p>tsharker<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tsharker has no accepted answers">0%</span></p></div></div><div id="comments-container-35425" class="comments-container"></div><div id="comment-tools-35425" class="comment-tools"></div><div class="clear"></div><div id="comment-35425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35428"></span>

<div id="answer-container-35428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35428-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently, that field has been renamed to</p><blockquote><p>wlan_rsna_eapol.keydes.key_info</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '14, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35428" class="comments-container"><span id="35436"></span><div id="comment-35436" class="comment"><div id="post-35436-score" class="comment-score"></div><div class="comment-text"><p>It works perfectly, thank you!</p><p>Regards, Matt</p></div><div id="comment-35436-info" class="comment-info"><span class="comment-age">(12 Aug '14, 10:05)</span> tsharker</div></div></div><div id="comment-tools-35428" class="comment-tools"></div><div class="clear"></div><div id="comment-35428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Cisco Spectrum Expert (cognio) to Wireshark"
description = '''Is there a way to migrate/convert Cisco (formerly Cognio) Spectrum Expert ccf file format into a file that wireshark can see (ie pcap)...Didn&#x27;t see anything in Cisco&#x27;s guide: http://www.cisco.com/en/US/docs/wireless/spectrum/expert/users/guide/spectrumexpert.pdf  '''
date = "2012-06-26T10:30:00Z"
lastmod = "2012-06-26T12:22:00Z"
weight = 12189
keywords = [ "ccf", "cognio" ]
aliases = [ "/questions/12189" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cisco Spectrum Expert (cognio) to Wireshark](/questions/12189/cisco-spectrum-expert-cognio-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12189-score" class="post-score" title="current number of votes">0</div><span id="post-12189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to migrate/convert Cisco (formerly Cognio) Spectrum Expert ccf file format into a file that wireshark can see (ie pcap)...Didn't see anything in Cisco's guide:</p><p><a href="http://www.cisco.com/en/US/docs/wireless/spectrum/expert/users/guide/spectrumexpert.pdf">http://www.cisco.com/en/US/docs/wireless/spectrum/expert/users/guide/spectrumexpert.pdf</a><br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ccf" rel="tag" title="see questions tagged &#39;ccf&#39;">ccf</span> <span class="post-tag tag-link-cognio" rel="tag" title="see questions tagged &#39;cognio&#39;">cognio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/8fec950383697a689adcac1a87a6f48c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aamercado&#39;s gravatar image" /><p><span>aamercado</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aamercado has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12189" class="comments-container"></div><div id="comment-tools-12189" class="comment-tools"></div><div class="clear"></div><div id="comment-12189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12194"></span>

<div id="answer-container-12194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12194-score" class="post-score" title="current number of votes">0</div><span id="post-12194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the manual:</p><blockquote><p>Cisco Spectrum Expert monitors the RF spectrum used by a variety of wireless network and communications technologies, such as Wi-Fi (802.11) WLANs. Cisco Spectrum Expert consists of a</p></blockquote><p>Cisco Spectrum Expert is a RF signal monitor, so there is nothing to read for Wireshark in the CCF files, as Spectrum Expert does not capture packets, at least not in a way usable for Wireshark. So, it's not a format conversion problem, as there is nothing to convert.</p><p>See also your question in the Cisco forum ;-)</p><p><a href="https://supportforums.cisco.com/thread/2156696">https://supportforums.cisco.com/thread/2156696</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '12, 12:43</strong> </span></p></div></div><div id="comments-container-12194" class="comments-container"></div><div id="comment-tools-12194" class="comment-tools"></div><div class="clear"></div><div id="comment-12194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


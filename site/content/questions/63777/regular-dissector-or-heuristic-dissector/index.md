+++
type = "question"
title = "Regular dissector or heuristic dissector?"
description = '''We have a custom hardware device that uses the IEEE 802.15.4 transport mechanism. To capture these data in WireShark, we are making use this project https://spaces.microchip.com/gf/project/wireshark_cap/frs/?action=&amp;amp;br_pkgrlssort_by=file_size&amp;amp;br_pkgrlssort_order=desc.  When the data is captu...'''
date = "2017-10-09T20:17:00Z"
lastmod = "2017-10-09T20:17:00Z"
weight = 63777
keywords = [ "dissector" ]
aliases = [ "/questions/63777" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Regular dissector or heuristic dissector?](/questions/63777/regular-dissector-or-heuristic-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63777-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a custom hardware device that uses the IEEE 802.15.4 transport mechanism. To capture these data in WireShark, we are making use this project <a href="https://spaces.microchip.com/gf/project/wireshark_cap/frs/?action=&amp;br_pkgrlssort_by=file_size&amp;br_pkgrlssort_order=desc.">https://spaces.microchip.com/gf/project/wireshark_cap/frs/?action=&amp;br_pkgrlssort_by=file_size&amp;br_pkgrlssort_order=desc.</a></p><p>When the data is captured, data transmission packets appear as protocol LwMesh and acknowledgment packets appear as protocol IEEE 802.15.4.</p><p>We want to create a custom dissector, to be applied to all of our packets, to more readily understand the traffic. Based on my reading (and I am brand new to this), it is not clear to me if I should create a regular dissector or a heuristic dissector. In either case, I do not understand why the new dissector would be given preference over the existing one (or, similarly, how to apply a specific dissector to multiple packets).</p><p>Would you please point me int he direction of an answer. Thank you.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '17, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/efb7a1f078cc0924d400ddc530222272?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="groston&#39;s gravatar image" /><p>groston<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="groston has no accepted answers">0%</span></p></div></div><div id="comments-container-63777" class="comments-container"></div><div id="comment-tools-63777" class="comment-tools"></div><div class="clear"></div><div id="comment-63777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


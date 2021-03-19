+++
type = "question"
title = "Adding Absolute Value to I/O Graph"
description = '''I&#x27;m having an issue with trying to graph (realtime) SSI/Noise values from a Monitor Mode capture. The filters &quot;radiotap.dbm_antsignal&quot; and &quot;radiotap.dbm_antnoise&quot; are negative values in the capture and can&#x27;t be graphed in 1.10 of Wireshark. The equipment I&#x27;m running on does not capture the radiotap....'''
date = "2014-04-14T13:27:00Z"
lastmod = "2014-04-14T13:27:00Z"
weight = 31802
keywords = [ "development", "graph" ]
aliases = [ "/questions/31802" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Absolute Value to I/O Graph](/questions/31802/adding-absolute-value-to-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having an issue with trying to graph (realtime) SSI/Noise values from a Monitor Mode capture. The filters "radiotap.dbm_antsignal" and "radiotap.dbm_antnoise" are negative values in the capture and can't be graphed in 1.10 of Wireshark. The equipment I'm running on does not capture the radiotap.db_antsignal/radiotap.db_antnoise values (positive values).</p><p>I'm interested in modifying the source of the latest dev release to try and ensure all values are graphed against an absolute value, but can't figure out where in the code to make this modification.</p><p>Any help is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">development graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/5b11899f6ef8d3994b8bcc4e5c27609f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mire3212&#39;s gravatar image" /><p>mire3212<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mire3212 has no accepted answers">0%</span></p></div></div><div id="comments-container-31802" class="comments-container"><span id="31838"></span><div id="comment-31838" class="comment"><div id="post-31838-score" class="comment-score"></div><div class="comment-text"><p>FWIW there's also a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9985">bug report</a> requesting this.</p></div><div id="comment-31838-info" class="comment-info"><span class="comment-age">(15 Apr '14, 06:12)</span> JeffMorriss ♦</div></div><span id="31839"></span><div id="comment-31839" class="comment"><div id="post-31839-score" class="comment-score"></div><div class="comment-text"><p>Ya, that was me &gt;.&lt;</p><p>But I was hoping I could figure out to address that by modifying the code, but I'm definitely not as experienced as other's on the project. Plus I'm not completely familiar with the overall structure of the source itself, so trying to figure out where to make the modification has proven slightly difficult.</p></div><div id="comment-31839-info" class="comment-info"><span class="comment-age">(15 Apr '14, 06:14)</span> mire3212</div></div></div><div id="comment-tools-31802" class="comment-tools"></div><div class="clear"></div><div id="comment-31802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


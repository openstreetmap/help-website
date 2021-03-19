+++
type = "question"
title = "How the data rate is calculated in prism header?"
description = '''When I send the packet at 6MBps in a 10MHz channel, the prism header shows me a value of 1500. How this is calculated?'''
date = "2017-05-06T01:37:00Z"
lastmod = "2017-05-06T01:37:00Z"
weight = 61265
keywords = [ "datarate" ]
aliases = [ "/questions/61265" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How the data rate is calculated in prism header?](/questions/61265/how-the-data-rate-is-calculated-in-prism-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61265-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I send the packet at 6MBps in a 10MHz channel, the prism header shows me a value of 1500. How this is calculated?</p></div><div id="question-tags" class="tags-container tags">datarate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '17, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/399786f859e6e0634708da7d56bb0604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramana&#39;s gravatar image" /><p>Ramana<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramana has no accepted answers">0%</span></p></div></div><div id="comments-container-61265" class="comments-container"><span id="61281"></span><div id="comment-61281" class="comment"><div id="post-61281-score" class="comment-score"></div><div class="comment-text"><p>I don't know which field you're referring to, but you might want to just examine the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ieee80211-prism.c;h=2a3001c40fdb00948232ce7b4ad1e56e7bec88d1;hb=HEAD">prism source code</a> to see how it works and where the value comes from.</p><p>If you're unable to determine how it's calculated on your own, then I would suggest posting a small packet capture file to somewhere like cloudshark, dropbox, pastebin, etc. so we can see exactly which field you're referring to.</p></div><div id="comment-61281-info" class="comment-info"><span class="comment-age">(08 May '17, 07:53)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-61265" class="comment-tools"></div><div class="clear"></div><div id="comment-61265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "How to scrape packet data?"
description = '''I want to scrape captured http packets for particular data. For example, consider a packet contains an itemID and ItemStatus. I want a quick method of searching and extracting the timestamp, itemID, and ItemStatus from all the captured packets into a csv file for analysis (or whatever). Is there a w...'''
date = "2011-09-25T12:34:00Z"
lastmod = "2011-09-25T12:34:00Z"
weight = 6547
keywords = [ "mining", "data", "packet", "scrape" ]
aliases = [ "/questions/6547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to scrape packet data?](/questions/6547/how-to-scrape-packet-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to scrape captured http packets for particular data. For example, consider a packet contains an itemID and ItemStatus.</p><p>I want a quick method of searching and extracting the timestamp, itemID, and ItemStatus from all the captured packets into a csv file for analysis (or whatever).</p><p>Is there a way to do this?</p><p>Thanks, David</p></div><div id="question-tags" class="tags-container tags">mining data packet scrape</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '11, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/35cccf89cb645f97e05c0043065da775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javaman&#39;s gravatar image" /><p>Javaman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javaman has no accepted answers">0%</span></p></div></div><div id="comments-container-6547" class="comments-container"><span id="6549"></span><div id="comment-6549" class="comment"><div id="post-6549-score" class="comment-score"></div><div class="comment-text"><p>The HTTP protocol has no itemID and itemStatus fields. You'll have to be more specific what these items are.</p></div><div id="comment-6549-info" class="comment-info"><span class="comment-age">(25 Sep '11, 22:54)</span> Jaap ♦</div></div><span id="6550"></span><div id="comment-6550" class="comment"><div id="post-6550-score" class="comment-score">1</div><div class="comment-text"><p>Are you looking for url's that contain certain values?<br />
You can use a display filter to select the packets, that contain a those values:<br />
http contains "itemid" || http contains "itemstatus"<br />
In Packet Details right-click on Request URI and choose "<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayPopUpSection.html#ChWorkColumnHeaderPopUpMenuSection">Apply as Column</a>" from the context menu.<br />
Next select File | Export | File...<br />
Save as type: select CSV<br />
Packet Range: select Displayed<br />
Add a file name and hit OK<br />
</p></div><div id="comment-6550-info" class="comment-info"><span class="comment-age">(26 Sep '11, 00:27)</span> joke</div></div><span id="6551"></span><div id="comment-6551" class="comment"><div id="post-6551-score" class="comment-score"></div><div class="comment-text"><p>You can read more about <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html">exporting data</a> in the wireshark User's Guide.</p></div><div id="comment-6551-info" class="comment-info"><span class="comment-age">(26 Sep '11, 00:31)</span> joke</div></div></div><div id="comment-tools-6547" class="comment-tools"></div><div class="clear"></div><div id="comment-6547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "How to generate a file with specific attributes from a .pcap file?"
description = '''I have a pcap file from which I intend to extract the following features into a text file using tshark:  Frame number  Frame length Source ip Destination ip Source port Destination port Number of packets with this src-&amp;gt;dest pair Number of packets with this dest-&amp;gt;src pair  The first 6 features ...'''
date = "2016-02-11T05:37:00Z"
lastmod = "2016-02-11T05:37:00Z"
weight = 50095
keywords = [ "ip", "filtering", "tshark", "display-filter", "attributes" ]
aliases = [ "/questions/50095" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to generate a file with specific attributes from a .pcap file?](/questions/50095/how-to-generate-a-file-with-specific-attributes-from-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50095-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file from which I intend to extract the following features into a text file using tshark:</p><ol><li>Frame number</li><li>Frame length</li><li>Source ip</li><li>Destination ip</li><li>Source port</li><li>Destination port</li><li>Number of packets with this src-&gt;dest pair</li><li>Number of packets with this dest-&gt;src pair</li></ol><p>The first 6 features can be acquired by using the <strong>-e option</strong>, and the last two fields can be obtained using the <strong>-z conv,ip option</strong>. But I <strong>need to put them together</strong> in a file which has 8 columns, and these <strong>features should stack up side by side.</strong></p><p>Please help. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">ip filtering tshark display-filter attributes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '16, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/88d06c9691e28f6f67accd7364f6b7a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sidsethu&#39;s gravatar image" /><p>sidsethu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sidsethu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '16, 07:34</p></div></div><div id="comments-container-50095" class="comments-container"><span id="50096"></span><div id="comment-50096" class="comment"><div id="post-50096-score" class="comment-score"></div><div class="comment-text"><p>As the first 6 seem to be on a per packet basis and the last 2 are a summary of number of packets, I don't see how they would be printed on the same line.</p><p>Can you give an example of what you want?</p><p>Even so, I don't think tshark will be able to do it as per packet info is printed as the packet is dissected and summary info is printed at the end after all packets have been dissected.</p></div><div id="comment-50096-info" class="comment-info"><span class="comment-age">(11 Feb '16, 06:31)</span> grahamb ♦</div></div><span id="50098"></span><div id="comment-50098" class="comment"><div id="post-50098-score" class="comment-score"></div><div class="comment-text"><p>Have you, by chance, expected that columns 7 an 8 would contain the intermediate summary value for the src and dst socket combination of that packet? I.e. the 15th occurrence of a packet with src socket A and dst socket B in the list would have 15 in column 7?</p></div><div id="comment-50098-info" class="comment-info"><span class="comment-age">(11 Feb '16, 07:20)</span> sindy</div></div><span id="50102"></span><div id="comment-50102" class="comment"><div id="post-50102-score" class="comment-score"></div><div class="comment-text"><p>To @sindy: No, I want all occurrences of a packet with src A and dst B to have 45 as value of column 7, if there are 45 such packets.</p><p>To @grahamb: I do not necessarily want this to happen in one pass, a solution which involves storing in two separate files and then merging to get a tabular form with 8 columns is also welcome.</p></div><div id="comment-50102-info" class="comment-info"><span class="comment-age">(11 Feb '16, 07:40)</span> sidsethu</div></div><span id="50104"></span><div id="comment-50104" class="comment"><div id="post-50104-score" class="comment-score"></div><div class="comment-text"><p>I think you'll have to use the tshark output for the first 6 columns, then post process using your favourite language to add the 7th and 8th, possibly using another run of tshark with the -z,conv option to get tshark to calculate the values for you.</p></div><div id="comment-50104-info" class="comment-info"><span class="comment-age">(11 Feb '16, 08:04)</span> grahamb ♦</div></div></div><div id="comment-tools-50095" class="comment-tools"></div><div class="clear"></div><div id="comment-50095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


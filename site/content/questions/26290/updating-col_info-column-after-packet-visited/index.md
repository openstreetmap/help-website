+++
type = "question"
title = "Updating COL_INFO column after packet visited"
description = '''I am writing a custom protocol dissector for our protocol layered on top of UDP. From the protocol header I can determine various packet attributes which allows me to group the packets into conversations of related data and ack packets.  As part of the protocol header I have a source channel ID whic...'''
date = "2013-10-22T08:32:00Z"
lastmod = "2013-10-24T01:28:00Z"
weight = 26290
keywords = [ "info", "col_info", "update", "cinfo" ]
aliases = [ "/questions/26290" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Updating COL\_INFO column after packet visited](/questions/26290/updating-col_info-column-after-packet-visited)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26290-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a custom protocol dissector for our protocol layered on top of UDP. From the protocol header I can determine various packet attributes which allows me to group the packets into conversations of related data and ack packets.</p><p>As part of the protocol header I have a source channel ID which I extract and store in the conversation. The source channel ID from the first data packet and return ack can be used to create a source / destination channel pair which I want to use in the COL_INFO info column, for example "data packet from 3 &gt; 7", however when the first packet is initially dissected I only know the source channel ID as I have not seen the ack containing the destination ID. This results in the Info column for the first packet only being able to show the source ID and not the destination ID as its unknown at the point the info is constructed, however subsequent packets after the ack is received can be displayed with the full source and destination channel ID data in the info column.</p><p>Is there anyway to go back and update the Info column of a packet, for example when its selected in the GUI and re-dissected, so I can correct the text based on the collected conversation data? I had hoped that the info column would be recreated each time the packet dissector function is run but now I realise that the packets cinfo pointer is NULL on subsequent dissector calls.</p><p>Surely this is not an unusual thing to need to do, i.e. update an Info column text based on information not necessarily available when dissecting an individual packet but amassed as a result of dissecting multiple packets in say a conversation.</p><p>Any help welcome, thanks.</p></div><div id="question-tags" class="tags-container tags">info col_info update cinfo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/6812a2b96d35b55d32826ff02fea6b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20the%20TV&#39;s gravatar image" /><p>Mike the TV<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike the TV has no accepted answers">0%</span></p></div></div><div id="comments-container-26290" class="comments-container"><span id="26351"></span><div id="comment-26351" class="comment"><div id="post-26351-score" class="comment-score"></div><div class="comment-text"><p>Interestingly I notice I get different results depending upon whether the packets are dissected from a live capture or a saved file. From the saved file the final conversation data seems to get used when setting the COL_INFO column so I get the correct packet destination ID.</p><p>That said I have also seen consecutive live captures display the COL_INFO data differently. For example my protocol has an end of message marker which obviously only can be determined once the last packet is received, however for display I was setting the notification that the EOM was missing in the COL_INFO column of all packets in the message. Sometimes the first packet which is dissected in the protocol gets marked with the no EOM tag despite the message having an EOM, but the rest of the packets don't get marked with the no EOM tag, seeming to suggest that the cinfo field only goes NULL after some period of time thereby allowing some of the later packets info field to be updated with the correct error tags once the whole conversation has been processed.</p><p>On other captures however all packets, even the first, get tagged correctly, i.e. no rouge EOM errors.</p><p>At what point in the dissection process does the cinfo field become invalid and the text in the COL_INFO field read-only?</p></div><div id="comment-26351-info" class="comment-info"><span class="comment-age">(24 Oct '13, 01:08)</span> Mike the TV</div></div></div><div id="comment-tools-26290" class="comment-tools"></div><div class="clear"></div><div id="comment-26290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26352"></span>

<div id="answer-container-26352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26352-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packets are only scanned secuentially on the first pass when column info (should) be written, subsequent visits to packets happens when they are vissible in the GUI basing coulmn info on that would be unreliably. Fist you get one info then you scroll down in the list and go back and something different is shown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-26352" class="comments-container"><span id="26353"></span><div id="comment-26353" class="comment"><div id="post-26353-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. So should I not be adding text to the COL_INFO column which can only be determined based on whole conversation data?</p><p>Should the COL_INFO column be limited to just data decoded from the current packet only in isolation?</p><p>How would you therefore alert a user to packets making up a bad conversation if it's not possible to update the COL_INFO column after processing the packets on the first pass, at which time you may not know if the conversation is bad? I know you can add it to the protocol tree pane, and I do also, but having to scroll through each packet to see when a conversation is bad would be a pain, the COL_INFO column seems to naturally provide a nice summary area to indicate this?</p><p>Also why do I sometimes see the correct information in the COL_INFO column which could only be determined from conversation data obtained from later packets if the COL_INFO field is only available for update when dissecting the packet on the first pass?</p><p>It also seems that the processing behaviour is inconsistent when you capture packets live compared to loading a capture from file, does the scanning work differently when loading from a file?</p></div><div id="comment-26353-info" class="comment-info"><span class="comment-age">(24 Oct '13, 02:46)</span> Mike the TV</div></div><span id="26355"></span><div id="comment-26355" class="comment"><div id="post-26355-score" class="comment-score"></div><div class="comment-text"><p>Actually I don't think the packet processing in live captures is as straightforward as you say which may explain why sometime I see it generate the correct COL_INFO text.</p><p>I added some debug to my dissector in my set_info_column_summary() function which I call on every packet after the update_conversation_data() function. This latter function is the one which determines the src and dst channel IDs from my packets, each packet only containing the src channel ID, therefore to get the full src/dst pair the conversation update function must have seen the first and second (ACK) packet in each conversation. This src/dst pair is used to set the channel IDs in the COL_INFO column.</p><p>pkt 5 is the start of a new conversation. From its packet I can determine the src chan as 4, dst chan is unknown -1. Interestingly cinfo pointer is NULL.</p><p>pkt 6 is the ACK reply which gives us the dst chan ID of 0, again the cinfo field is NULL. pkt 5 and 6 then get dissected again with a valid cinfo and by now I know both src and dst channel IDs so the Info field gets set correctly.</p><p>pkts 7-13 then get processed all with cinfo NULL the first time, then again with valid cinfo.</p><p>I am confused as sometimes it works, sometimes it don't?</p><pre><code>Pkt 5: new conversation
Pkt 5: Src chan = 4, dst chan = -1, cinfo = 0x00000000
Pkt 6: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 5: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 6: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 7: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 8: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 9: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 10: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 11: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 12: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 13: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 7: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 8: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 9: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 10: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 11: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 12: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 13: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 12: Src chan = 4, dst chan = 0, cinfo = 0x00000000</code></pre></div><div id="comment-26355-info" class="comment-info"><span class="comment-age">(24 Oct '13, 03:50)</span> Mike the TV</div></div><span id="26356"></span><div id="comment-26356" class="comment"><div id="post-26356-score" class="comment-score"></div><div class="comment-text"><p>OK here's a time when it put unknown for the destination channel ID in the COL_INFO column for the first conversation packet.</p><pre><code>Pkt 27: new conversation
Pkt 27: Src chan = 4, dst chan = -1, cinfo = 0x00000000
Pkt 27: Src chan = 4, dst chan = -1, cinfo = 0x3f9f9138
Pkt 28: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 29: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 30: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 31: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 32: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 33: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 34: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 35: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 36: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 37: Src chan = 4, dst chan = 0, cinfo = 0x00000000
Pkt 28: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 29: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 30: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 31: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 32: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 33: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 34: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 35: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 36: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138
Pkt 37: Src chan = 4, dst chan = 0, cinfo = 0x3f9f9138</code></pre></div><div id="comment-26356-info" class="comment-info"><span class="comment-age">(24 Oct '13, 04:03)</span> Mike the TV</div></div><span id="26358"></span><div id="comment-26358" class="comment"><div id="post-26358-score" class="comment-score"></div><div class="comment-text"><p>I think it's better to ask this type of questions on the developper mailing list</p></div><div id="comment-26358-info" class="comment-info"><span class="comment-age">(24 Oct '13, 05:25)</span> Kurt Knochner ♦</div></div><span id="26364"></span><div id="comment-26364" class="comment"><div id="post-26364-score" class="comment-score"></div><div class="comment-text"><p>I sort of thought this was. I'll go and look for that list instead. Thanks.</p></div><div id="comment-26364-info" class="comment-info"><span class="comment-age">(24 Oct '13, 06:13)</span> Mike the TV</div></div><span id="26366"></span><div id="comment-26366" class="comment not_top_scorer"><div id="post-26366-score" class="comment-score"></div><div class="comment-text"><p>See here:</p><blockquote><p><a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">https://www.wireshark.org/mailman/listinfo/wireshark-dev</a></p></blockquote></div><div id="comment-26366-info" class="comment-info"><span class="comment-age">(24 Oct '13, 06:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26352" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


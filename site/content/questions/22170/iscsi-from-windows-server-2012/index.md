+++
type = "question"
title = "iSCSI from Windows Server 2012"
description = '''Anyone here familiar with iSCSI protocol? I have been sniffing around at some iSCSI traffic and have been working on making a compliant iSCSI server app. Things have been going relatively smoothly until recently. There&#x27;s a LOT of setup required before you can even get to doing your first Read and Wr...'''
date = "2013-06-19T08:23:00Z"
lastmod = "2013-06-19T13:14:00Z"
weight = 22170
keywords = [ "iscsi", "scsi" ]
aliases = [ "/questions/22170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [iSCSI from Windows Server 2012](/questions/22170/iscsi-from-windows-server-2012)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22170-score" class="post-score" title="current number of votes">0</div><span id="post-22170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone here familiar with iSCSI protocol? I have been sniffing around at some iSCSI traffic and have been working on making a compliant iSCSI server app. Things have been going relatively smoothly until recently. There's a LOT of setup required before you can even get to doing your first Read and Write commands. I got through a whole bunch of it, comparing the results of my server against a known SAN device.<br />
</p><p>My problem, however, which I do not necessarily blame on the client, is that the first Write(10) command that comes to my server appears to request that I write 1 Logical Block to the disk, however, the payload for the packet is not existent and the "DataSegmentLength" field is 0. I expected, with 1 logical block being written, that the DataSegmentLength field would be 0x00000200 (512 bytes).<br />
</p><p>I've attached a capture if anyone is so motivated to look at it.... it isn't very long.</p><p><a href="http://files.digitaltundra.com/bad-iscsi.pcapng">Download the Capture of MS iSCSI initiator making bad requests to my iSCSI Development Server</a></p><p>It should also be noted that if I accept this Write(10) request and handle it as defined in the spec, it will continue Sending me 0 length Write requests until the the Initiator reports "Device I/O Error". My server generates no errors.</p><p>Thanks in advance for your time, Jason</p><p>Update: I noticed that ExpCmdSN was looking a little higher than would be expected. I corrected the handling of it. It made no difference in the final outcome however. The attached link reflects the capture BEFORE I made that change.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-scsi" rel="tag" title="see questions tagged &#39;scsi&#39;">scsi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/90b414fbb6c4fa323edd08b76a56a228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evilrobot&#39;s gravatar image" /><p><span>evilrobot</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evilrobot has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '13, 12:00</strong> </span></p></div></div><div id="comments-container-22170" class="comments-container"></div><div id="comment-tools-22170" class="comment-tools"></div><div class="clear"></div><div id="comment-22170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22182"></span>

<div id="answer-container-22182" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22182-score" class="post-score" title="current number of votes">1</div><span id="post-22182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="evilrobot has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At least in the packet capture you uploaded the total packet length displaying is 102 bytes (from initiator for the data write case) which means 14bytes eth header + 20 bytes IP header + 20 bytes TCP Header + 48 bytes ISCSI header. So no data is exactly written to the target and no error responses were seen.Let me know if i am missing anything here...</p><p>If you look at the Login command header(packet.no 23) from initiator the ImmediateData=Yes and InitialR2T=no and if you look at the Login response(packet.no 24)header the Immediatedata=NO and InitialR2T=yes.</p><p>Quoting RFC</p><p>If ImmediateData is set to Yes and InitialR2T is set to No, then the initiator MAY send unsolicited immediate data and/or one unsolicited burst of Data-Out PDUs. Which is your case1(Login request)</p><p>If ImmediateData is set to No and InitialR2T is set to Yes, then the initiator MUST NOT send unsolicited data and the target MUST reject unsolicited data with the corresponding response code. Which is your case2(Login response)</p><p>Is this clue makes sense? Let me know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '13, 12:36</strong> </span></p></div></div><div id="comments-container-22182" class="comments-container"><span id="22184"></span><div id="comment-22184" class="comment"><div id="post-22184-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I am fairly new to this protocol, so you're probably more on top of the rules and specs than I am and I'll look into your suggestion and report back.<br />
</p><p>My login negotiation code is still <em>somewhat</em> of a stub but unless I missed something, it matches the replies of the model I sniffed and therefore the initiation gets exactly what it is accustomed to getting, but it only makes sense to me that the Initiator would send me a 0-byte write request if something in the setup is broken.</p><p>Thanks again.</p></div><div id="comment-22184-info" class="comment-info"><span class="comment-age">(19 Jun '13, 13:01)</span> <span class="comment-user userinfo">evilrobot</span></div></div><span id="22186"></span><div id="comment-22186" class="comment"><div id="post-22186-score" class="comment-score"></div><div class="comment-text"><p>Yes, it appears that the Yes/No values for ImmediateData and InitialR2T were reversed and changing that fixed the Write commands sent from the initiator. I'm still getting I/O errors, but the most obvious problem with the writes appears to be fixed, thankyou!</p></div><div id="comment-22186-info" class="comment-info"><span class="comment-age">(19 Jun '13, 13:14)</span> <span class="comment-user userinfo">evilrobot</span></div></div></div><div id="comment-tools-22182" class="comment-tools"></div><div class="clear"></div><div id="comment-22182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


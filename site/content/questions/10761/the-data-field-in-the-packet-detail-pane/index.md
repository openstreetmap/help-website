+++
type = "question"
title = "the data field in the packet detail pane"
description = '''When I export the packet out to a text file,there are hexadecimal data in the file If there is a data field in the packet detail pane.But if there is not this field,I can not get the data when export the packet out to the text file in spite of it contains many bytes data. The data field Such as the ...'''
date = "2012-05-07T19:10:00Z"
lastmod = "2012-05-10T00:14:00Z"
weight = 10761
keywords = [ "field", "data" ]
aliases = [ "/questions/10761" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [the data field in the packet detail pane](/questions/10761/the-data-field-in-the-packet-detail-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10761-score" class="post-score" title="current number of votes">0</div><span id="post-10761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I export the packet out to a text file,there are hexadecimal data in the file If there is a data field in the packet detail pane.But if there is not this field,I can not get the data when export the packet out to the text file in spite of it contains many bytes data. The data field Such as the following: <img src="http://" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 19:10</strong></p><img src="https://secure.gravatar.com/avatar/feb2695b239215e2418903e11af7035f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yizhibi&#39;s gravatar image" /><p><span>yizhibi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yizhibi has no accepted answers">0%</span></p></img></div></div><div id="comments-container-10761" class="comments-container"></div><div id="comment-tools-10761" class="comment-tools"></div><div class="clear"></div><div id="comment-10761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10782"></span>

<div id="answer-container-10782" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10782-score" class="post-score" title="current number of votes">1</div><span id="post-10782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you select Export-&gt;File from the File menu, take a look at the "Export File" dialog box. On the bottom right of the dialog box, you'll see "Packet Format" options. Here's where you can change the format of the exported data.</p><p>If "Packet details" is set to "As displayed", your text file will look like the Packet Details window; whatever is expanded in that window will be expanded in the text file.</p><p>You can set "Packet details" to "All expanded" to automatically expand every field.</p><p>You can also enable "Packet bytes" to show the full dump of each packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-10782" class="comments-container"><span id="10809"></span><div id="comment-10809" class="comment"><div id="post-10809-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I also want to know why some packet have data,but in the packet detail pane,there is not the data field? Such as: Frame 531: 238 bytes on wire (1904 bits), 238 bytes captured (1904 bits) ... Transmission Control Protocol, Src Port: domain (53), Dst Port: mysql-cluster (1186), Seq: 1, Ack: 1, Len: 184</p><p>But some packet have the data field: Frame 786: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) ... Transmission Control Protocol, Src Port: sms-rcinfo (2701), Dst Port: 51342 (51342), Seq: 1, Ack: 1, Len: 12 Data (12 bytes)</p></div><div id="comment-10809-info" class="comment-info"><span class="comment-age">(09 May '12, 00:43)</span> <span class="comment-user userinfo">yizhibi</span></div></div><span id="10818"></span><div id="comment-10818" class="comment"><div id="post-10818-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if I understand your request. HOWEVER, there is only a 'Data' field in the packet details,</p><p>1.) if there IS data in the packet</p><p>2.) if no dissector exists (or the dissector has been disabled) for that protocol.</p><p>If there is a dissector, there will be no 'Data' field. Instead you will see the information that was added by the dissector ("Hypertext Transfer Protocol", "Secure Sockets Layer", etc.). Maybe that helps.</p><p>Regards<br />
Kurt</p></div><div id="comment-10818-info" class="comment-info"><span class="comment-age">(09 May '12, 02:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10825"></span><div id="comment-10825" class="comment"><div id="post-10825-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response! I means that if there is the data field in the packet details pane, we can get the Hex data when we export the packet to a text file(if it has data).But if there in not the data field,we can not get the Hex data when we export the packet to a text file(although it has data).Why? Wish your response!</p></div><div id="comment-10825-info" class="comment-info"><span class="comment-age">(09 May '12, 05:39)</span> <span class="comment-user userinfo">yizhibi</span></div></div><span id="10829"></span><div id="comment-10829" class="comment"><div id="post-10829-score" class="comment-score"></div><div class="comment-text"><p>Can you please post a sample capture to <strong><a href="http://www.cloudshark.org">http://www.cloudshark.org</a></strong> and post the exported data here, so we can see what you get what you expect to get?</p></div><div id="comment-10829-info" class="comment-info"><span class="comment-age">(09 May '12, 05:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10865"></span><div id="comment-10865" class="comment"><div id="post-10865-score" class="comment-score"></div><div class="comment-text"><p>I upload a packet which have a data field(in the packet detail pane below the "User Datagram Protocol" ).You could export out to a text file,in the file you can see the Hex data which carried by the packet. <a href="http://www.cloudshark.org/captures/4456851016ad">http://www.cloudshark.org/captures/4456851016ad</a> But in the <a href="http://www.cloudshark.org/captures/6b8585a75d34">http://www.cloudshark.org/captures/6b8585a75d34</a> I also upload a packet which have not the data field below the "User Datagram Protocol" (thought the total length is 1179).If you export out to a text file,in the file you can not see the Hex data. Wish you could get!Thanks a lot!</p></div><div id="comment-10865-info" class="comment-info"><span class="comment-age">(09 May '12, 20:47)</span> <span class="comment-user userinfo">yizhibi</span></div></div></div><div id="comment-tools-10782" class="comment-tools"></div><div class="clear"></div><div id="comment-10782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10867"></span>

<div id="answer-container-10867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10867-score" class="post-score" title="current number of votes">1</div><span id="post-10867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the 2nd pcap you've uploaded ("no data field.pcap"), the UDP data is being parsed by the Packet Cable dissector, which parses 3 bytes and consumes the rest of the data (thus hiding the <em>Data</em> field you seek). You can prevent the Packet Cable dissector from eating up your data by disabling the dissector in one of the following ways:</p><ul><li>From the <em>Packet Details</em> pane, right-click the header that shows <strong>PacketCable</strong>, and select <strong>Disable Protocol...</strong> from the context menu. Click <strong>OK</strong> in the subsequent confirmation box.</li></ul><p><em>OR</em></p><ul><li>Open menu <strong>Analyze &gt; Enabled Protocols</strong> (or press <em>SHIFT</em>+<em>CTRL</em>+<em>E</em>), find "PACKETCABLE" in the protocol list, uncheck the <strong>Status</strong> box next to it, and click <strong>OK</strong>.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></div></div><div id="comments-container-10867" class="comments-container"><span id="10870"></span><div id="comment-10870" class="comment"><div id="post-10870-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!I solve this problem which puzzling me for a long time.</p><p>Regards yizhibi</p></div><div id="comment-10870-info" class="comment-info"><span class="comment-age">(10 May '12, 00:14)</span> <span class="comment-user userinfo">yizhibi</span></div></div></div><div id="comment-tools-10867" class="comment-tools"></div><div class="clear"></div><div id="comment-10867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


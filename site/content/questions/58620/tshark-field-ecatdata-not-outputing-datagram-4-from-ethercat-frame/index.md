+++
type = "question"
title = "TShark field ecat.data not outputing datagram 4 from EtherCAT frame"
description = '''Hi, I&#x27;ve just upgraded to wireshark 2.2.3 from 1.6.5 (I think it was). I use the following command to extract information from EtherCAT frames: &quot;C:&#92;Program Files&#92;Wireshark&#92;tshark&quot; -r &quot;myfile&quot; -T fields -e ecat.data -e esl.port -e esl.crcerror -e esl.alignerror -e esl.timestamp  In the previous versi...'''
date = "2017-01-09T20:56:00Z"
lastmod = "2017-01-10T13:58:00Z"
weight = 58620
keywords = [ "ethercat", "tshark" ]
aliases = [ "/questions/58620" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TShark field ecat.data not outputing datagram 4 from EtherCAT frame](/questions/58620/tshark-field-ecatdata-not-outputing-datagram-4-from-ethercat-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58620-score" class="post-score" title="current number of votes">0</div><span id="post-58620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've just upgraded to wireshark 2.2.3 from 1.6.5 (I think it was).</p><p>I use the following command to extract information from EtherCAT frames:</p><pre><code>&quot;C:\Program Files\Wireshark\tshark&quot; -r &quot;myfile&quot; -T fields -e ecat.data -e esl.port -e esl.crcerror -e esl.alignerror -e esl.timestamp</code></pre><p>In the previous version the ecat.data field would output data from all datagrams but in the latest version it is only outputting data from the first three datagrams.<br />
</p><p>My EtherCAT frames generally have either 4 for 5 datagrams.</p><p>If I use -e ecat.sub4.data, no data is output (blank lines). If I use -e ecat.sub5.data then if there is a fifth datagram it is output.</p><p>Here is a summary of a frame with 4 datagrams:</p><pre><code>Frame 41720: 191 bytes on wire (1528 bits), 191 bytes captured (1528 bits)
Ethernet II, Src: MS-NLB-PhysServer-01_05:13:7e:d0 (02:01:05:13:7e:d0), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
EtherCAT frame header
EtherCAT datagram(s): 4 Cmds, &#39;LRD&#39;: len 1, &#39;LRD&#39;: len 68, &#39;LWR&#39;: len 38, &#39;FRMW&#39;: len 4
    EtherCAT datagram: Cmd: &#39;LRD&#39; (10), Len: 1, Addr 0x0, Cnt 1
    EtherCAT datagram: Cmd: &#39;LRD&#39; (10), Len: 68, Addr 0x1, Cnt 2
    EtherCAT datagram: Cmd: &#39;LWR&#39; (11), Len: 38, Addr 0x45, Cnt 2
    EtherCAT datagram: Cmd: &#39;FRMW&#39; (14), Len: 4, Adp 0x3, Ado 0x910, Cnt 6
EtherCAT Switch Link</code></pre><p>Is there any other information I need to supply to help figure out why datagram 4 is not outputting its data?</p><p>Thanks, G.</p><p>A capture file can be found here: <a href="https://1drv.ms/u/s!AoLeUQXl-H0MgQmMddI1ja_Yob95">https://1drv.ms/u/s!AoLeUQXl-H0MgQmMddI1ja_Yob95</a></p><p>Note: the frames with 4 or more datagrams are further down the capture.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethercat" rel="tag" title="see questions tagged &#39;ethercat&#39;">ethercat</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '17, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/ca5d748df219d0e5662b09986ce7e8ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grf&#39;s gravatar image" /><p><span>grf</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grf has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '17, 00:48</strong> </span></p></div></div><div id="comments-container-58620" class="comments-container"><span id="58623"></span><div id="comment-58623" class="comment"><div id="post-58623-score" class="comment-score"></div><div class="comment-text"><p>A sample capture file would be nice.</p></div><div id="comment-58623-info" class="comment-info"><span class="comment-age">(09 Jan '17, 23:35)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58626"></span><div id="comment-58626" class="comment"><div id="post-58626-score" class="comment-score"></div><div class="comment-text"><p>Sorry, couldn't find how to attach a file, can you let me know how? In the meantime I've added a link for one. Thanks, G.</p></div><div id="comment-58626-info" class="comment-info"><span class="comment-age">(10 Jan '17, 00:52)</span> <span class="comment-user userinfo">grf</span></div></div><span id="58628"></span><div id="comment-58628" class="comment"><div id="post-58628-score" class="comment-score"></div><div class="comment-text"><p>A link to the file is fine (and the only way, there's no attachment option here).</p></div><div id="comment-58628-info" class="comment-info"><span class="comment-age">(10 Jan '17, 01:39)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58629"></span><div id="comment-58629" class="comment"><div id="post-58629-score" class="comment-score"></div><div class="comment-text"><p>When I look at the details of the frames in Wireshark (2.2.2), in this case the first one with 4 datagrams, frame 815, I see that there is no field ecat.data in the last datagram, only interpreted timestamps. What data were you expecting?</p></div><div id="comment-58629-info" class="comment-info"><span class="comment-age">(10 Jan '17, 01:44)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58630"></span><div id="comment-58630" class="comment"><div id="post-58630-score" class="comment-score"></div><div class="comment-text"><p>The ones I'm interested are mostly from around frame 2719, before that there's also a whole lot of configuration frames with other datagrams.</p><p>It's the "EtherCAT datagram: Cmd: 'FRMW' (14), Len: 4, Adp 0x3, Ado 0x910, Cnt 4" datagram that I want. This datagram should have 4 bytes of data, which is a 32bit timestamp from an EtherCAT slave.</p><p>Note: I've got "enable disector" checked under the ESL protocol to show the extended EtherCAT Switch Link data at the end of the frame. Otherwise it shows this data as Pad bytes.</p></div><div id="comment-58630-info" class="comment-info"><span class="comment-age">(10 Jan '17, 02:05)</span> <span class="comment-user userinfo">grf</span></div></div><span id="58631"></span><div id="comment-58631" class="comment not_top_scorer"><div id="post-58631-score" class="comment-score"></div><div class="comment-text"><p>Also, looking at frame 815, although its not the one I'm interested in it should still have 24 bytes of data. It is also timestamp related information.</p><p>(EtherCAT datagram: Cmd: 'FPRD' (4), Len: 24, Adp 0x1, Ado 0x910, Cnt 1)</p></div><div id="comment-58631-info" class="comment-info"><span class="comment-age">(10 Jan '17, 02:11)</span> <span class="comment-user userinfo">grf</span></div></div></div><div id="comment-tools-58620" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-58620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58632"></span>

<div id="answer-container-58632" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58632-score" class="post-score" title="current number of votes">1</div><span id="post-58632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="grf has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>ecat.data</code> is a placeholder for data the dissector doesn't understand. With <a href="https://code.wireshark.org/review/#/c/13729/">this change</a> the interpretation of EtherCAT slave controller registers was added to the dissector, replacing the ecat.data placeholders. Adding those field names to the command line should present you with the interpretation of the data you seek.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '17, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58632" class="comments-container"><span id="58633"></span><div id="comment-58633" class="comment"><div id="post-58633-score" class="comment-score"></div><div class="comment-text"><p>I'm away from the computer till tomorrow so will check it out then. Thanks</p></div><div id="comment-58633-info" class="comment-info"><span class="comment-age">(10 Jan '17, 02:37)</span> <span class="comment-user userinfo">grf</span></div></div><span id="58648"></span><div id="comment-58648" class="comment"><div id="post-58648-score" class="comment-score"></div><div class="comment-text"><p>Thanks. The field I needed to use is ecat.reg.dc.systimeL</p></div><div id="comment-58648-info" class="comment-info"><span class="comment-age">(10 Jan '17, 13:58)</span> <span class="comment-user userinfo">grf</span></div></div></div><div id="comment-tools-58632" class="comment-tools"></div><div class="clear"></div><div id="comment-58632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


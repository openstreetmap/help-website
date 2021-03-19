+++
type = "question"
title = "Packet reassemble - FTP-DATA Dissector - FTP - Export Object"
description = '''I am implementing object export for the FTP protocol ( File-&amp;gt; Export Object -&amp;gt; FTP...). I have got to the point of getting the list of files in the ExportObjectDialog window. However in such window I get an entry for each TCP packet used for the trasmission of each FTP packet. If save each ent...'''
date = "2015-01-15T18:48:00Z"
lastmod = "2015-01-15T18:48:00Z"
weight = 39179
keywords = [ "tcp_dissect_pdus", "ftp", "dissector", "reassemble", "tcp" ]
aliases = [ "/questions/39179" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet reassemble - FTP-DATA Dissector - FTP - Export Object](/questions/39179/packet-reassemble-ftp-data-dissector-ftp-export-object)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39179-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am implementing object export for the FTP protocol ( File-&gt; Export Object -&gt; FTP...).</p><p>I have got to the point of getting the list of files in the ExportObjectDialog window. However in such window I get an entry for each TCP packet used for the trasmission of each FTP packet. If save each entry and then join the resulting files in the correct order I get the file I am sopposed to. So I am on the right track but am not doing ftp packet reassembly correctly.</p><p>I have tried two approaches:</p><ol><li><p>The one explainded in section 2.7.2 of README.dissector. You can find the code at <a href="http://pastebin.com/nkxDUhkv">pastebin.com/nkxDUhkv</a>. In order to make reading easier, I have added left several blank lines before and after the reassemble section. I am preatty sure this is the way to go, if this is the case you can skip to the end of the question. However since this approach has not been successful, I am providing details of the second one.</p></li><li><p>I have followed the instructions given at <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html#TcpDissectPdus">https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html#TcpDissectPdus</a> and added some extra code I think necessary, based on implementations I have seen of other dissectors.</p><p>Please note that I think line<br />
</p><p>ftpdatafragmented_handle = create_dissector_handle(dissect_ftpdatafragmented, proto_ftpdatafragmented);</p><p>should go at the end of</p><p>void proto_reg_handoff_ftp(void);</p><p>However for some reason such function is not being called. Therefore I have moved the<br />
ftpdatafragmented_handle to</p><p>dissect_ftpdata(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree *tree).</p><p>Please find the relevant code at <a href="http://pastebin.com/wHR2Q1LY">pastebin.com/wHR2Q1LY</a>. I have upload the whole mofidied FTP dissector code at <a href="http://pastebin.com/jxLUxewm">pastebin.com/jxLUxewm</a>.</p></li></ol><p>Also note that I haven't dealt with conversation and transaction data yet. I will deal with that as soon as I fix packet reassemble.</p><p>What am I doing wrong with packet disassemble? Could somebody please help me?</p><p>Thank you in advance for your time.</p></div><div id="question-tags" class="tags-container tags">tcp_dissect_pdus ftp dissector reassemble tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/5df333830379ff009c6e2243920a5885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyL&#39;s gravatar image" /><p>CrazyL<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyL has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '15, 05:28</p></div></div><div id="comments-container-39179" class="comments-container"></div><div id="comment-tools-39179" class="comment-tools"></div><div class="clear"></div><div id="comment-39179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


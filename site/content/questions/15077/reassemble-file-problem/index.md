+++
type = "question"
title = "Reassemble file problem"
description = '''Hi Forum readers, I obtained a pcap file and wanted to find a pdf file and reassemble it i think i have found the tcp stream for it but when I try to save it the pdf is unreadable. i get refered to chapter 7 of the user manual but that isnt helpful for pdfs. Can anyone help me? If you require any mo...'''
date = "2012-10-18T03:08:00Z"
lastmod = "2012-10-18T04:45:00Z"
weight = 15077
keywords = [ "assemble", "reassembly" ]
aliases = [ "/questions/15077" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Reassemble file problem](/questions/15077/reassemble-file-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15077-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum readers,</p><p>I obtained a pcap file and wanted to find a pdf file and reassemble it i think i have found the tcp stream for it but when I try to save it the pdf is unreadable. i get refered to chapter 7 of the user manual but that isnt helpful for pdfs. Can anyone help me? If you require any more info just let me know</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">assemble reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '12, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/95f9cf574eef517d224c0c3b47449760?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helpMe&#39;s gravatar image" /><p>helpMe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helpMe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '12, 19:41</p></div></div><div id="comments-container-15077" class="comments-container"><span id="15203"></span><div id="comment-15203" class="comment"><div id="post-15203-score" class="comment-score"></div><div class="comment-text"><p>lol Uni SA? im stuck on the same thing</p></div><div id="comment-15203-info" class="comment-info"><span class="comment-age">(23 Oct '12, 16:21)</span> Thor_White</div></div></div><div id="comment-tools-15077" class="comment-tools"></div><div class="clear"></div><div id="comment-15077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15082"></span>

<div id="answer-container-15082" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15082-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it is transfered by either HTTP or SMB you should take a look at the File -&gt; Export Objects menu (you might need to upgrade to 1.8.x to see it if your version is older than that).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '12, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15082" class="comments-container"><span id="15092"></span><div id="comment-15092" class="comment"><div id="post-15092-score" class="comment-score"></div><div class="comment-text"><p>Apparently it's transferred by TCP/FTP if that makes sense?</p></div><div id="comment-15092-info" class="comment-info"><span class="comment-age">(18 Oct '12, 14:05)</span> helpMe</div></div><span id="15094"></span><div id="comment-15094" class="comment"><div id="post-15094-score" class="comment-score">1</div><div class="comment-text"><p>Yeah it does. In that case you should be able to extract the file by using follow TCP stream as you did. Can you upload your file to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the URL so that I can take a look (only if it isn't anything containing sensitve data)?</p></div><div id="comment-15094-info" class="comment-info"><span class="comment-age">(18 Oct '12, 15:39)</span> Jasper ♦♦</div></div><span id="15130"></span><div id="comment-15130" class="comment"><div id="post-15130-score" class="comment-score">1</div><div class="comment-text"><p>Okay, I just extracted the PDF with no problem. This is the recipe:</p><ol><li><p>Select Packet 500, which is the SYN packet for the Data transfer session initiated in the FTP control channel in packets 497-499.</p></li><li><p>Right click, select "Follow TCP Stream". You should get an extra window where the first line contains "%PDF-1.5" in red letters.</p></li><li><p>Make sure the selection box says "Entire conversation (58441 bytes)"</p></li><li><p>Use "save as" to save it as <a href="http://SecretNumber.pdf">SecretNumber.pdf</a></p></li></ol><p>As I said, this just worked fine for me, so it should work for you, too. My guess is you probably tried to export the command channel :-)</p></div><div id="comment-15130-info" class="comment-info"><span class="comment-age">(21 Oct '12, 08:22)</span> Jasper ♦♦</div></div><span id="15135"></span><div id="comment-15135" class="comment"><div id="post-15135-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that Jasper, is there an easy way to tell which SYN packet is initiated in the FTP control channel for future reference</p></div><div id="comment-15135-info" class="comment-info"><span class="comment-age">(21 Oct '12, 13:58)</span> helpMe</div></div><span id="15136"></span><div id="comment-15136" class="comment"><div id="post-15136-score" class="comment-score">1</div><div class="comment-text"><p>Yes, take a look at packet 497, containing the PORT command. Right in there you'll find the IP and port number that the data connection will connect to (unfold the FTP layer and the PORT command in the decode and you'll see it). The SYN packet in packet 500 uses the exact same destination TCP port, so that is how you can match it. It is easier to see if you disable Name Resolution for the transport layer in the View -&gt; Name Resolution menu.</p></div><div id="comment-15136-info" class="comment-info"><span class="comment-age">(21 Oct '12, 15:25)</span> Jasper ♦♦</div></div><span id="15204"></span><div id="comment-15204" class="comment not_top_scorer"><div id="post-15204-score" class="comment-score"></div><div class="comment-text"><p>Thankyou Jasper for yo9ur help on this assignment i was haveing trouple reassembleing the file.</p><p>the way i was trying to do it was with the following steps form</p><p><a href="http://wiki.wireshark.org/TCP_Reassembly">http://wiki.wireshark.org/TCP_Reassembly</a></p><p>but that was for pictures i tried to rename it to a .pdf but that didnt work. so thankyou agian</p></div><div id="comment-15204-info" class="comment-info"><span class="comment-age">(23 Oct '12, 16:23)</span> Thor_White</div></div></div><div id="comment-tools-15082" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-15082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


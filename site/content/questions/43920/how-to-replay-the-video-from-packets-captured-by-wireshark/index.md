+++
type = "question"
title = "how to replay the video from packets captured by wireshark"
description = '''hi all......... i need to know that how can i play video stream from packets received by wireshark... actually this is tiny work of my project .... and i am using wireshark first time so i dont know if anyone can help me to find this out then plzz help..... and if there is any tool to do that than j...'''
date = "2015-07-07T03:05:00Z"
lastmod = "2015-07-07T14:28:00Z"
weight = 43920
keywords = [ "wireshark" ]
aliases = [ "/questions/43920" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to replay the video from packets captured by wireshark](/questions/43920/how-to-replay-the-video-from-packets-captured-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43920-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all......... i need to know that how can i play video stream from packets received by wireshark... actually this is tiny work of my project .... and i am using wireshark first time so i dont know if anyone can help me to find this out then plzz help..... and if there is any tool to do that than just let me know plzz<br />
</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '15, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/a82414c87b0110e7fa0f73b966388420?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anurag&#39;s gravatar image" /><p>anurag<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anurag has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-43920" class="comments-container"></div><div id="comment-tools-43920" class="comment-tools"></div><div class="clear"></div><div id="comment-43920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43941"></span>

<div id="answer-container-43941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43941-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This procedure outlines a method to take a raw Wireshark capture (over the air, or over wire) and reconstruct a video file from the captured UDP packets. Note that this procedure will not work for HDCP 2.0/2.1 protected streams.</p><ol><li>Open the capture in Wireshark.</li><li>If required, decrypt the WiFi traffic.</li><li>Find the UDP port for the video file transfer. In the Filter toolbar, type <strong><em>udp</em></strong> and press enter. This will display only the UDP packets. In the Protocol or Information column, look for some indication for a video transport protocol, for example MPEG-TS. Click on one of the video packet and determine the UDP port. In the Filter toolbar, apply the display filter <strong><em>udp.port==xxxx</em></strong>, where xxxx is the UDP port number.</li><li>From the Main menu, select: Analyze → Decode As... → Select the Transport tab → Ensure the Decode radio button is selected → In the left side of the window, ensure a bidirectional arrow exists between the UDP ports → In the right side of the window, choose RTP → Click OK</li><li>From the Main menu, select: Telephony → RTP → Show All Streams</li><li>Click on the desired stream (usually there should be only one) and click "Analyze" button</li><li>In the newly opened window, click the "Save payload" button</li><li>On the bottom of the window, ensure Format is set to raw and Channel is set to forward</li><li>Save the video stream with an appropriate file extension. For an MPEG transport stream video, use the .ts extension (e.g., video.ts)</li></ol><p>Once the video file is saved, the video file can be viewed using a media player that supports the audio/video compression method and file format.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43941" class="comments-container"><span id="63251"></span><div id="comment-63251" class="comment"><div id="post-63251-score" class="comment-score"></div><div class="comment-text"><p>hi,</p><p>9.Save the video stream with an appropriate file extension. For an MPEG transport stream video, use the .ts extension (e.g., video.ts)</p><p>What should be the video extension for h263 stream from pcap.</p><p>Regards, Venkat ramana</p></div><div id="comment-63251-info" class="comment-info"><span class="comment-age">(31 Jul '17, 00:14)</span> venkatramanasvr</div></div><span id="63252"></span><div id="comment-63252" class="comment"><div id="post-63252-score" class="comment-score"></div><div class="comment-text"><p>The primary purpose of file name extensions is to tell <strong>the operating system</strong> (generally an MS-DOS based one) which application to use to open the file. So if you choose a player capable of handling H.263 and open the file from within the player, the extension should not matter, or you should be able to tell the player what is the format of the file contents. If the application (player) uses extension to identify the format of the file contents, the exact extension required depends on that particular applicaton.</p><p>Other than that, bear in mind that there are several incompatible "flavours" of H.263.</p></div><div id="comment-63252-info" class="comment-info"><span class="comment-age">(31 Jul '17, 00:53)</span> sindy</div></div></div><div id="comment-tools-43941" class="comment-tools"></div><div class="clear"></div><div id="comment-43941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


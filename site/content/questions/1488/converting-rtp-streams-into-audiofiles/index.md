+++
type = "question"
title = "Converting RTP Streams into audiofiles"
description = '''Hi all, I use a router called AVM Fritzbox 7270 with Linux Ubuntu 10.10. The router has a hidden feature to capture network traffic. It allows me to produces .eth files that can be analyzed via wireshark. In order to generate an audio file I use the following procedure:   generate a .eth-file and sa...'''
date = "2010-12-27T06:02:00Z"
lastmod = "2010-12-27T06:02:00Z"
weight = 1488
keywords = [ "telephony", "audio", "streams", "rtp" ]
aliases = [ "/questions/1488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting RTP Streams into audiofiles](/questions/1488/converting-rtp-streams-into-audiofiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I use a router called AVM Fritzbox 7270 with Linux Ubuntu 10.10. The router has a hidden feature to capture network traffic. It allows me to produces .eth files that can be analyzed via wireshark.</p><p>In order to generate an audio file I use the following procedure:</p><ol><li><p>generate a .eth-file and save it to hard drive.</p></li><li><p>Wireshark-&gt;Telephony-&gt;RTP-&gt;Show all Streams</p></li><li><p>Select Stream -&gt; Analyze -&gt; save payload</p></li><li><p>Choose a name of the audio file, set "Format" to ".au", set "Channels" to "both"</p></li></ol><p>In particular the last step does not work to full satisfaction. I get an error message:</p><p><strong>can't save reversed direction in a file: File I/O problem!</strong></p><p>All I can do is to save audio files using "Channel" as "forward". Both, "reversed" and "both" do not work. From a test call I have 2 audio streams available. Both streams have been converted into audio files using "Channel" as "forward". The first audio file covers only what I said, whereas the second audio file covers only what the other person replied. Of course, I would like to have an audio file that contains the telephone call completely.</p><p>I use 2 different DECT telephones, which are only 3 months old:</p><p>Siemens Gigaset E36, Codec G.726. Siemens Gigaset SL400H, Codec G.722, G.726.</p><p>Is it due to the codecs used by the phones? What can I do?</p><p>When looking at Telephony -&gt; VoIPCalls -&gt; Graph there are fat arrows in both directions tagged as "RTP (g711A)" if this helps. Nevertheless, using the "Player" button I can only listen to what the other person said.</p><p>Thank you very much indeed for any help.</p><p>Regards,</p><p>Walter</p></div><div id="question-tags" class="tags-container tags">telephony audio streams rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '10, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/414b770feaa14051e5097e352fe68da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erichm&#39;s gravatar image" /><p>erichm<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erichm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Dec '10, 03:36</p></div></div><div id="comments-container-1488" class="comments-container"><span id="1491"></span><div id="comment-1491" class="comment"><div id="post-1491-score" class="comment-score"></div><div class="comment-text"><p>You never told which version of Wireshark you use, and on what platform.</p></div><div id="comment-1491-info" class="comment-info"><span class="comment-age">(27 Dec '10, 10:39)</span> Jaap ♦</div></div></div><div id="comment-tools-1488" class="comment-tools"></div><div class="clear"></div><div id="comment-1488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


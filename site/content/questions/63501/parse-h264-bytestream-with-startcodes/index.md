+++
type = "question"
title = "Parse h.264 bytestream with startcodes"
description = '''Hi,  I receive a h264 bytestream via rtp. To analyze the stream in wireshark, I set the protocol (rtp) and the decoding options (h264 dynamic payload type to 96). My problem is, that my stream includes h264 startcodes (0x00000001) before nal header types. The fist byte of the startcode wireshark par...'''
date = "2017-08-22T22:01:00Z"
lastmod = "2017-08-23T14:24:00Z"
weight = 63501
keywords = [ "h264", "annexb", "bytestream", "rtp", "startcode" ]
aliases = [ "/questions/63501" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Parse h.264 bytestream with startcodes](/questions/63501/parse-h264-bytestream-with-startcodes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63501-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I receive a h264 bytestream via rtp. To analyze the stream in wireshark, I set the protocol (rtp) and the decoding options (h264 dynamic payload type to 96). My problem is, that my stream includes h264 startcodes (0x00000001) before nal header types. The fist byte of the startcode wireshark parses as nal unit header and of course detects an undefined type.</p><p>Can anyone help me to find out a filter that ignores the first 4 bytes of the h.264 payload or parse the h264 stream correct as byetestream separated with startcodes?</p><p>Thank you, janina</p></div><div id="question-tags" class="tags-container tags">h264 annexb bytestream rtp startcode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '17, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/fb26b6cfcabddb939860316866c94aad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janina&#39;s gravatar image" /><p>janina<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janina has no accepted answers">0%</span></p></div></div><div id="comments-container-63501" class="comments-container"></div><div id="comment-tools-63501" class="comment-tools"></div><div class="clear"></div><div id="comment-63501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63510"></span>

<div id="answer-container-63510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63510-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That looks as if there's either a bug in the H.264 dissector or the byte stream is somehow invalid. Could you file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach a capture that demonstrates the problem?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '17, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63510" class="comments-container"><span id="63512"></span><div id="comment-63512" class="comment"><div id="post-63512-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I don't think that its a bug from wireshark. Rather I didn't quite understand something. Nobody else has a problem like me and I coded the whole video pipeline. I will elucidate my setup. I have written a small programm that gets a video stream from a Logitech C920 webcam and sends it to a server. I get the raw h264 bytestream from the cam and pack the frames into simple 12byte-header rtp packets (without optional extensions). This is the video I'm monitoring.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/spsppsidr_FGtuSGa.PNG" />https://ibb.co/fKQ66k) In the stream you see a sps, pps followed by an idr frame. Is it a regular H264 stream if I send the Bytestream with startcodes via rtp? Or is this format not specified? Should I really write a bug ticket?</p></div><div id="comment-63512-info" class="comment-info"><span class="comment-age">(24 Aug '17, 00:14)</span> janina</div></div><span id="63514"></span><div id="comment-63514" class="comment"><div id="post-63514-score" class="comment-score"></div><div class="comment-text"><p>From the code it seems like when calling the h264 dissector directly it does not take the start code into account. But dissect_h264_nal_unit() does. I'm not sure if your format is "legal" e.g according to RFC specification of H.264 over RTP. If you remove the start code in your script, it should work.</p></div><div id="comment-63514-info" class="comment-info"><span class="comment-age">(24 Aug '17, 04:00)</span> Anders ♦</div></div><span id="63515"></span><div id="comment-63515" class="comment"><div id="post-63515-score" class="comment-score"></div><div class="comment-text"><p>As an alternative it might be possible to write a LUA script to handle your format e.g skip the start code befor calling the h264 decoder.</p></div><div id="comment-63515-info" class="comment-info"><span class="comment-age">(24 Aug '17, 04:02)</span> Anders ♦</div></div></div><div id="comment-tools-63510" class="comment-tools"></div><div class="clear"></div><div id="comment-63510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


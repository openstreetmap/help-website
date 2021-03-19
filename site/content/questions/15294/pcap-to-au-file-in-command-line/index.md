+++
type = "question"
title = "pcap to au-file in command line"
description = '''i wondering to know is there any way to convert a pcap file containing RTP packets to au-file in command line? I know i can do it with wireshark GUI but i m trying to write a script in python so i think i need to do that through command line.'''
date = "2012-10-26T06:32:00Z"
lastmod = "2012-10-27T02:58:00Z"
weight = 15294
keywords = [ "audio", "script" ]
aliases = [ "/questions/15294" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pcap to au-file in command line](/questions/15294/pcap-to-au-file-in-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15294-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i wondering to know is there any way to convert a pcap file containing RTP packets to au-file in command line? I know i can do it with wireshark GUI but i m trying to write a script in python so i think i need to do that through command line.</p></div><div id="question-tags" class="tags-container tags">audio script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '12, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/fb8d994046301235446cac25ccced08d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza&#39;s gravatar image" /><p>reza<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza has no accepted answers">0%</span></p></div></div><div id="comments-container-15294" class="comments-container"></div><div id="comment-tools-15294" class="comment-tools"></div><div class="clear"></div><div id="comment-15294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15311"></span>

<div id="answer-container-15311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15311-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think there is no good way right now, at least not using tshark, which is usually the way to go for scripting. There is a similar question here:</p><p><a href="http://ask.wireshark.org/questions/10493/can-tshark-extract-voice-data-from-an-rtp-stream">http://ask.wireshark.org/questions/10493/can-tshark-extract-voice-data-from-an-rtp-stream</a></p><p>Maybe the answer in that thread can help you, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15311" class="comments-container"><span id="15335"></span><div id="comment-15335" class="comment"><div id="post-15335-score" class="comment-score"></div><div class="comment-text"><p>thanks Jasper, i think Gstreamer might be the answer but the audio quality decreases after i convert the pcap to audio, may be i should change some parameters to get a better quality.</p><p>gst-launch-0.10 -m -v filesrc location=moh.pcap ! pcapparse src-port=40012 \ ! "application/x-rtp, payload=8" ! rtppcmadepay ! alawdec ! audioconvert ! audioresample ! avimux ! filesink location=<a href="http://test1audio2.au">test1audio2.au</a></p><p>(Converted to a comment as per the format of <a href="http://ask.wireshark.org">ask.wireshark.org</a>. Please see the FAQ).</p></div><div id="comment-15335-info" class="comment-info"><span class="comment-age">(29 Oct '12, 05:35)</span> reza</div></div></div><div id="comment-tools-15311" class="comment-tools"></div><div class="clear"></div><div id="comment-15311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


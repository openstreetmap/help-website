+++
type = "question"
title = "How to play Opus, Silk, speed, PCMU, and PCMA codec"
description = '''My application is using Lib function to choose best of below available CODEC opus - 48000 HZ SILK - 16000 Hz speex - 16000 Hz speex - 8000 Hz PCMU - 8000 Hz PCMA - 8000 Hz  I am new to wireshark, How do i play above Codec as i am not able to see any stream under VoIP call window. Kindly help me to p...'''
date = "2015-04-28T23:29:00Z"
lastmod = "2016-01-27T19:26:00Z"
weight = 41935
keywords = [ "voipcalls", "codec", "voip" ]
aliases = [ "/questions/41935" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to play Opus, Silk, speed, PCMU, and PCMA codec](/questions/41935/how-to-play-opus-silk-speed-pcmu-and-pcma-codec)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My application is using Lib function to choose best of below available CODEC</p><pre><code>opus - 48000 HZ
SILK - 16000 Hz
speex - 16000 Hz
speex - 8000 Hz
PCMU - 8000 Hz
PCMA - 8000 Hz</code></pre><p>I am new to wireshark, How do i play above Codec as i am not able to see any stream under VoIP call window.</p><p>Kindly help me to proceed further.</p></div><div id="question-tags" class="tags-container tags">voipcalls codec voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/b580c15e384dd40fe90a253ed90ddd20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandy56&#39;s gravatar image" /><p>Sandy56<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandy56 has no accepted answers">0%</span></p></div></div><div id="comments-container-41935" class="comments-container"></div><div id="comment-tools-41935" class="comment-tools"></div><div class="clear"></div><div id="comment-41935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41939"></span>

<div id="answer-container-41939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41939-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This subject has been addressed multiple times, but here's a quick rundown of the important parts.</p><p>Wireshark needs to see the signalling protocol to show a VoIP call in that window.</p><p>Wireshark needs to see the setup of the media stream (eg. SIP/SDP) to see the RTP stream.</p><p>Wireshark can show RTP streams, by setting the dissector preference 'Try to decode RTP outside conversations'.</p><p>Wireshark can decode/play the media stream as long as it's PCM encoded, other codecs are not supported.</p><p>You can export the RTP contents and use external tools to play the media.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41939" class="comments-container"><span id="41961"></span><div id="comment-41961" class="comment"><div id="post-41961-score" class="comment-score"></div><div class="comment-text"><p>Hi Japp,</p><p>Thanks for your quick response, I tried exporting RTP content in .raw format but after saving the file, when i check the properties of the file its getting displayed as just "File" in Type of file field under properties window,is this how the file will be saved.</p><p>Do i want to convert this file in to .pcm format to play the audio in player like audacity else is there any other player available play this audio</p></div><div id="comment-41961-info" class="comment-info"><span class="comment-age">(30 Apr '15, 00:18)</span> Sandy56</div></div><span id="41962"></span><div id="comment-41962" class="comment"><div id="post-41962-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to convert this file in to .pcm format file</p></div><div id="comment-41962-info" class="comment-info"><span class="comment-age">(30 Apr '15, 00:38)</span> Sandy56</div></div><span id="49567"></span><div id="comment-49567" class="comment"><div id="post-49567-score" class="comment-score"></div><div class="comment-text"><p>@Sandy56, if still interested almost a year later:</p><ol><li><p>look at the difference between "file name extension" and "file internal format", some hints can be found e.g. in Jaap's answer and my comment to <a href="https://ask.wireshark.org/questions/49352/what-is-the-difference-between-pcap-file-the-same-file-opened-by-wireshark-saved-as-txt-file">this question</a>. So the fact that Wireshark does not automatically give the file name any "extension" is your advantage: if your decoder needs a particular "extension" to tell it that the file only contains the raw codec data (i.e. there is no <em>descriptor</em> inside the file, like there is in "wav" and "au" files), you just type that extension to the file name manually (.pcm sounds like a good candidate for files containing PCMA and PCMU raw data, but maybe also L16 raw data). But with such files, the decoder will either ask you for additional information necessary to process the file properly, or make a guess and sometimes play the data improperly.</p></li><li><p>there are two basic categories of audio codecs from the point of view of extraction:</p></li><li><p>for one of them (a typical case is e.g. L16) the byte stream carried as an RTP payload contains all information about its internal structure necessary for the decoder, so <code>Save Payload as -&gt; Raw</code> is enough if you can then tell the decoder some additional parameters (e.g. sample rate). In the example case of L16, you must tell Audacity the sample rate, the number of channels, the order of bytes, and that's it. But even some compressing codecs can be treated like this.</p></li><li><p>for the other one, the RTP payload does not represent a continuous stream, so the decoder needs to know the packet borders and thus <code>Save Payload as -&gt; Raw</code> would cause loss of such information. A typical case here is Opus, see details of how to extract the audio from RTP in Jaap's answer to <a href="https://ask.wireshark.org/questions/42367/understanding-sipsdp-file-in-context-of-opus-codec-cannot-decode-opus">this question</a> and my comments to it. A decoder for Opus is available for free, the script you need to convert tshark packet-by-packet output into an Ogg file is relatively simple.</p></li></ol><p>I'm not sure to which of the two categories SILK and Speex belong, though.</p></div><div id="comment-49567-info" class="comment-info"><span class="comment-age">(27 Jan '16, 23:31)</span> sindy</div></div></div><div id="comment-tools-41939" class="comment-tools"></div><div class="clear"></div><div id="comment-41939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49565"></span>

<div id="answer-container-49565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I also have the need to convert opus music files to mp3.</p><p>then i try many of the software to convert opus files, luckily and finally, i find a step by step guide and a easy-to-use iDealshare VideoGo which can batch convert opus to mp3, wav, wma etc on mac or windows</p><p>Step by step guide at <a href="http://www.idealshare.net/audio-converter/opus-converter.html">http://www.idealshare.net/audio-converter/opus-converter.html</a></p><p>now i like to share it here, hope it also helps for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '16, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/c66106150d151f36791c0e15e0b575e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bestautumnn&#39;s gravatar image" /><p>bestautumnn<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bestautumnn has no accepted answers">0%</span></p></div></div><div id="comments-container-49565" class="comments-container"></div><div id="comment-tools-49565" class="comment-tools"></div><div class="clear"></div><div id="comment-49565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


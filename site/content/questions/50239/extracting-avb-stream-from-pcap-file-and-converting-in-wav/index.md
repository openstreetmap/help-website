+++
type = "question"
title = "Extracting AVB Stream from PCAP file and converting in .wav"
description = '''Hi everybody, I have a .pcap-file with audio AVB streams (IEEE 1722a protocol). I would like to extract the audio data and put it in a .wav-file so that it can be played by a standard player. So I would first need to cut the payload of the AVB streams out of the .pcap-file (I think that should be ea...'''
date = "2016-02-16T06:42:00Z"
lastmod = "2016-02-16T07:20:00Z"
weight = 50239
keywords = [ "pcap", "extract", "avb", "wav" ]
aliases = [ "/questions/50239" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting AVB Stream from PCAP file and converting in .wav](/questions/50239/extracting-avb-stream-from-pcap-file-and-converting-in-wav)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50239-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I have a .pcap-file with audio AVB streams (IEEE 1722a protocol). I would like to extract the audio data and put it in a .wav-file so that it can be played by a standard player. So I would first need to cut the payload of the AVB streams out of the .pcap-file (I think that should be easy as the offsets of these payloads can be calculated), then I have to put the different sequences together to one .wav-file (this should also be possible by adding the right header etc.).</p><p>Is there something like that existing for AVB streams? Which programming language would you use for that purpose?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">pcap extract avb wav</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/adff8d731ffe044e74b218776bff2c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lumi&#39;s gravatar image" /><p>Lumi<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lumi has no accepted answers">0%</span></p></div></div><div id="comments-container-50239" class="comments-container"></div><div id="comment-tools-50239" class="comment-tools"></div><div class="clear"></div><div id="comment-50239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50240"></span>

<div id="answer-container-50240" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50240-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you've stated elsewhere that you've written your own dissector for ieee1722a v14, you should be able to use tshark to dump only the audio data as hex stream, using the appropriate field name as assigned by your dissector both for <code>-Y</code> and <code>-e</code> parameters of tshark (so, if some packets of the aggregated stream carry audio and some don't, you would only dump those with audio). Speculative example as I don't have the details of your dissector:</p><p><code>tshark -r input_file_name -Y my_ieee1722.audiodata -T fields -e my_ieee1722.audiodata &gt; audio_hex</code></p><p>The <code>-e</code> causes <em>all</em> occurrences of the field in the packet to be dumped, separated by comma by default, so for the embedded ieee1722 dissector, <code>-e ieee1722.data.sample.sampledata</code> dumps</p><pre><code>00:00:00,00:00:00,00:00:00,00:00:00,00:00:00,00:00:00</code></pre><p>for each packet containing six 24-bit samples.</p><p>Then, you would use <em>your favourite</em> programming language to post-process that data. Depending on the properties of the audio codec used (block-based or stream-based), it may be enough to compose the output file of a header followed by the data (like <code>wav</code> or <code>au</code> file), or the file may have to be a structured one like <code>ogg</code> if the codec happens to be a block-based one.</p><p>I personally prefer <code>au</code> to <code>wav</code> because with <code>au</code> you don't need to know the total size of the audio data in advance, but as codes for only several codec types are defined for its header, it may not be possible for you to use it.</p><p>The above is enough only if the player you'll use to play the resulting file is able to handle the codec and your only task is to inform it which codec to use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50240" class="comments-container"><span id="50434"></span><div id="comment-50434" class="comment"><div id="post-50434-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy for your answer!</p><p>Finally I got it. For whom it may interest. I used perl for this project. First to read the pcap file and extract the information that I need (number of channels, sample rate, audio data etc.). I didn't use tshark because I wanted my script to be independet from any other tool. In a second step I built the RIFF-Wave-header, attached the audio data and saved the whole to a wav file. And it works :)</p></div><div id="comment-50434-info" class="comment-info"><span class="comment-age">(23 Feb '16, 06:30)</span> Lumi</div></div><span id="50436"></span><div id="comment-50436" class="comment"><div id="post-50436-score" class="comment-score"></div><div class="comment-text"><p>As you've posted the question at <em>Wireshark</em> Q&amp;A site, it seemed obvious that you wanted to let the Wireshark suite do most of the job.</p><p>Therefore, I've changed my original Comment into an Answer. It is up to you whether you consider it useful and so Accept it (using the checkmark) or keep it formally unaccepted.</p></div><div id="comment-50436-info" class="comment-info"><span class="comment-age">(23 Feb '16, 06:46)</span> sindy</div></div></div><div id="comment-tools-50240" class="comment-tools"></div><div class="clear"></div><div id="comment-50240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Can&#x27;t play mp3 track from captured RTP stream"
description = '''I was streaming an mp3 song from server to client while capturing traffic on the client. So I&#x27;ve got a pcap with the only one RTP stream: https://d.pr/Jfah The problem is that I can&#x27;t play it in Wireshark.  Why isn&#x27;t it playable? When I was streaming the audio, I was saving the stream on the client ...'''
date = "2016-11-13T14:39:00Z"
lastmod = "2016-11-14T00:17:00Z"
weight = 57369
keywords = [ "media", "playback", "rtp", "mp3" ]
aliases = [ "/questions/57369" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't play mp3 track from captured RTP stream](/questions/57369/cant-play-mp3-track-from-captured-rtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57369-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was streaming an mp3 song from server to client while capturing traffic on the client. So I've got a pcap with the only one RTP stream: <a href="https://d.pr/Jfah">https://d.pr/Jfah</a> The problem is that I can't play it in Wireshark.</p><p>Why isn't it playable? When I was streaming the audio, I was saving the stream on the client side via VLC - and there's nothing wrong with the file itself, it can be played apart. But Wireshark can't play the same audio from captured pcap...</p></div><div id="question-tags" class="tags-container tags">media playback rtp mp3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '16, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/9d8e7bdd418d0b727f76b47e655bc465?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trixter&#39;s gravatar image" /><p>trixter<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trixter has no accepted answers">0%</span></p></div></div><div id="comments-container-57369" class="comments-container"></div><div id="comment-tools-57369" class="comment-tools"></div><div class="clear"></div><div id="comment-57369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57371"></span>

<div id="answer-container-57371" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57371-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't stream the payload (contents) extracted from RTP to an external player but it plays it on its own, using a sound device as an output. It means that it has to be able to decode the payload, and it currently is able to decode only PCMA and PCMU codecs.</p><p>For any other codec, you have to save the payload to a file and use an external player to play that file. For CBR (constant bit rate) codecs, or for VBR codecs which carry the information about frame boundaries inside the payload, such as MP3, this can be done using <code>Save payload -&gt; raw</code> in Wireshark (so you may stop reading here as you are interested in MP3).</p><p>For those VBR codecs where information about the beginning and end of each packet is not part of the codec payload itself because they expect this information to be conveyed by a generic transport layer, such as Opus, you have to use some other tool to extract both the payload and the information about the packet borders from the capture file and save it in ogg or matroska file format, which both constitute a framework for various VBR codecs. There is <a href="https://ask.wireshark.org/questions/42367/understanding-sipsdp-file-in-context-of-opus-codec-cannot-decode-opus">another Question</a> here which deals with this task in deeper detail.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '16, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '16, 05:39</p></div></div><div id="comments-container-57371" class="comments-container"><span id="57378"></span><div id="comment-57378" class="comment"><div id="post-57378-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it works :) The only weird thing is the resulting file is playable only via QuickTime: VLC and iTunes are not playing it...</p></div><div id="comment-57378-info" class="comment-info"><span class="comment-age">(14 Nov '16, 09:48)</span> trixter</div></div><span id="57379"></span><div id="comment-57379" class="comment"><div id="post-57379-score" class="comment-score"></div><div class="comment-text"><blockquote><p>VLC and iTunes are not playing it...</p></blockquote><p>That sounds weird, as according to the specification, no file header is necessary for the player to handle the mp3 contents.</p><p>Can you compare the original file from the server with the file obtained from the RTP? Maybe the header of the very first frame is lost in transit and the players are unable to synchronize? Besides, I've seen lost packets on your screenshot, so it may be that those players prefer not to play the file with drop-outs so they better don't play it at all...</p></div><div id="comment-57379-info" class="comment-info"><span class="comment-age">(14 Nov '16, 09:58)</span> sindy</div></div></div><div id="comment-tools-57371" class="comment-tools"></div><div class="clear"></div><div id="comment-57371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


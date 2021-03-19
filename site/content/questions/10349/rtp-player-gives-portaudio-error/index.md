+++
type = "question"
title = "RTP player gives portaudio error"
description = '''Hi, I&#x27;m sorry if I missed something. I just installed wireshark on my laptop to practice with. I&#x27;m running Opensuse 12.1 and have to admit I&#x27;m also rather new to Linux! I have a problem when trying to play a RTP stream. I&#x27;m trying to do the following:  Load capture Go to telephony -&amp;gt; rtp -&amp;gt; sh...'''
date = "2012-04-20T07:26:00Z"
lastmod = "2014-07-29T04:00:00Z"
weight = 10349
keywords = [ "player", "portaudio", "rtp" ]
aliases = [ "/questions/10349" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RTP player gives portaudio error](/questions/10349/rtp-player-gives-portaudio-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10349-score" class="post-score" title="current number of votes">0</div><span id="post-10349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm sorry if I missed something. I just installed wireshark on my laptop to practice with. I'm running Opensuse 12.1 and have to admit I'm also rather new to Linux!</p><p>I have a problem when trying to play a RTP stream. I'm trying to do the following:</p><ol><li>Load capture</li><li>Go to telephony -&gt; rtp -&gt; show all streams</li><li>I select the stream I want to listen to and click analyze -&gt; player -&gt; decode and play.</li></ol><p>It then gives me the following error:</p><p>Got this info from PortAudio Library: Default hostApiName: OSS Default devicename: No Device (-1)</p><p>Then when I click ok it gives me another popup:</p><p>Can not Open Stream in PortAudio Library. Error: invalid sample rate</p><p>I can use the "Save Payload" function and save the stream to .au to the file system and play it with VLC.</p><p>I did some searching already on google and found that OSS should be ALSA on Linux, I can't find how to change it within Wireshark however. Also the discussions I find in regards to it don't seem to mention a solution and are usually several years old.</p><p>I also tried updating PortAudio, this did not help.</p><p>Your help is much appreciated!</p><p>Also, system specs:</p><p>ASUS X53e-SX1403V Intel I5 2450M Realtek HD audio</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-player" rel="tag" title="see questions tagged &#39;player&#39;">player</span> <span class="post-tag tag-link-portaudio" rel="tag" title="see questions tagged &#39;portaudio&#39;">portaudio</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '12, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/9837a7785a7c62fc38aa4c7aeb7d1e55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bsanders&#39;s gravatar image" /><p><span>bsanders</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bsanders has no accepted answers">0%</span></p></div></div><div id="comments-container-10349" class="comments-container"></div><div id="comment-tools-10349" class="comment-tools"></div><div class="clear"></div><div id="comment-10349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34965"></span>

<div id="answer-container-34965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34965-score" class="post-score" title="current number of votes">0</div><span id="post-34965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you can see, portaudio is trying to use an OSS audio device which apparently fails. Since you are using PulseAudio, try running Wireshark with <code>padsp</code> which exposes a fake OSS DSP device to PortAudio that actually uses pulseaudio.</p><p>Usage:</p><pre><code>padsp wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '14, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34965" class="comments-container"></div><div id="comment-tools-34965" class="comment-tools"></div><div class="clear"></div><div id="comment-34965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


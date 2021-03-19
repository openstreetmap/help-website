+++
type = "question"
title = "Can not Open Stream in PortAudio Library.  Error: Invalid sample rate"
description = '''Hello, wireshark Version 1.4.2  My system hardware and audio device: HP 210 Mini Fedora 14 2.6.35.10-74.fc14.x86_64  cat /proc/asound/cards  0 [Intel ]: HDA-Intel - HDA Intel  HDA Intel at 0x56200000 irq 46  00:1b.0 Audio device: Intel Corporation N10/ICH 7 Family High Definition Audio Controller (r...'''
date = "2011-01-22T08:05:00Z"
lastmod = "2011-01-26T14:15:00Z"
weight = 1879
keywords = [ "rtp", "wireshark" ]
aliases = [ "/questions/1879" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can not Open Stream in PortAudio Library. Error: Invalid sample rate](/questions/1879/can-not-open-stream-in-portaudio-library-error-invalid-sample-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1879-score" class="post-score" title="current number of votes">0</div><span id="post-1879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><pre><code>wireshark Version 1.4.2</code></pre><p>My system hardware and audio device:</p><pre><code>HP 210 Mini
Fedora 14
2.6.35.10-74.fc14.x86_64
 cat /proc/asound/cards
 0 [Intel          ]: HDA-Intel - HDA Intel
                      HDA Intel at 0x56200000 irq 46

00:1b.0 Audio device: Intel Corporation N10/ICH 7 Family High Definition Audio Controller (rev 02)</code></pre><p>When I try and play back the rtp after making a sip call. I go to VOIP Calls | Player | Decode | Play. I get the following error message.</p><pre><code>Got this info from PortAudio Library:
 Default hostApiName: ALSA
 Default deviceName: HDA Intel: STAC92xx Analog (hw:0,0) (0)</code></pre><p>Can anyone suggest a solution to this problem?</p><p>Many thanks for any advice,</p><p>===== Device info ======</p><pre><code>==============================
Default capture device number: 7
Default playback device number: 7
==============================
Device ID: 0
Device name: ALSA: HDA Intel: STAC92xx Analog (hw:0,0)
Input channels: 2
Output channels: 2
Low Input Latency: 0.011610
Low Output Latency: 0.011610
High Input Latency: 0.046440
High Output Latency: 0.046440
Supported Rates:
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 1
Device name: ALSA: front
Input channels: 0
Output channels: 2
Low Input Latency: -1.000000
Low Output Latency: 0.011610
High Input Latency: -1.000000
High Output Latency: 0.046440
Supported Rates:
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 2
Device name: ALSA: surround40
Input channels: 0
Output channels: 2
Low Input Latency: -1.000000
Low Output Latency: 0.011610
High Input Latency: -1.000000
High Output Latency: 0.046440
Supported Rates:
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 3
Device name: ALSA: surround51
Input channels: 0
Output channels: 2
Low Input Latency: -1.000000
Low Output Latency: 0.011610
High Input Latency: -1.000000
High Output Latency: 0.046440
Supported Rates:
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 4
Device name: ALSA: surround71
Input channels: 0
Output channels: 2
Low Input Latency: -1.000000
Low Output Latency: 0.011610
High Input Latency: -1.000000
High Output Latency: 0.046440
Supported Rates:
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 5
Device name: ALSA: pulse
Input channels: 32
Output channels: 32
Low Input Latency: 0.011610
Low Output Latency: 0.011610
High Input Latency: 0.046440
High Output Latency: 0.046440
Supported Rates:
    8000
    9600
    11025
    12000
    15000
    16000
    22050
    24000
    32000
    44100
    48000
    88200
    96000
    192000
==============================
Device ID: 6
Device name: ALSA: dmix
Input channels: 0
Output channels: 2
Low Input Latency: -1.000000
Low Output Latency: 0.042667
High Input Latency: -1.000000
High Output Latency: 0.042667
Supported Rates:
    48000
==============================
Device ID: 7
Device name: ALSA: default
Input channels: 32
Output channels: 32
Low Input Latency: 0.011610
Low Output Latency: 0.011610
High Input Latency: 0.046440
High Output Latency: 0.046440
Supported Rates:
    8000
    9600
    11025
    12000
    15000
    16000
    22050
    24000
    32000
    44100
    48000
    88200
    96000
    192000
==============================
Selected capture device: 7 - ALSA: default
Selected playback device: 7 - ALSA: default
Supported Rates:
    8000
    9600
    11025
    12000
    15000
    16000
    22050
    24000
    32000
    44100
    48000
    88200
    96000
    192000
Unable to open Portmixer</code></pre><p>======= Edit === After install audacity:</p><pre><code>Got this info from PortAudio Library:
 Default hostApiName: ALSA
 Default deviceName: HDA Intel: STAC92xx Analog (hw:0,0) (0)

Can not Open Stream in PortAudio Library.
 Error: Invalid sample rate</code></pre><p>Audacity installed:</p><pre><code>Name        : audacity
Arch        : x86_64
Version     : 1.3.12
Release     : 0.6.beta.fc14
Size        : 13 M
Repo        : installed
From repo   : updates
Summary     : Multitrack audio editor
URL         : http://audacity.sourceforge.net
License     : GPLv2
Description : ........</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '11, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/9f7667844c54af07fbb1a85592137cd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ant2009&#39;s gravatar image" /><p><span>ant2009</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ant2009 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '11, 07:17</strong> </span></p></div></div><div id="comments-container-1879" class="comments-container"></div><div id="comment-tools-1879" class="comment-tools"></div><div class="clear"></div><div id="comment-1879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1908"></span>

<div id="answer-container-1908" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1908-score" class="post-score" title="current number of votes">1</div><span id="post-1908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ant2009 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Audacity audio device info gives the following picture:</p><ul><li>Wireshark/PortAudio uses the default host api, which is ALSA</li><li>Wireshark/PortAudio uses the default device, which doesn't exists (<a href="http://www.portaudio.com/trac/ticket/49">weird bug</a>)</li><li>Wireshark learns there's no device, starts enumeration.</li><li>Wireshark/PortAudio selects the first host API, ALSA</li><li>Wireshark/PortAudio selects the first device, HDA Intel: STAC92xx Analog (hw:0,0)</li><li>Wireshark/PortAudio opens a stream: Stereo, 16 bit, 8kHz</li><li>As you can see from the Audacity audio device info this device doesn't support rate 8000</li><li>Wireshark gives up</li></ul><p>How to change the ALSA configuration to give you the right device as the first one I don't know.</p><p><strong>The very best way is to put pressure on the PortAudio developers to fix the three years outstanding CRITICAL bug</strong> (*)</p><p>(*) Yeah it's a rant, but it must be solved at the source, not be worked around by all (audio) developers...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '11, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1908" class="comments-container"><span id="1943"></span><div id="comment-1943" class="comment"><div id="post-1943-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help. Just unfortunate that is no final solution.</p></div><div id="comment-1943-info" class="comment-info"><span class="comment-age">(26 Jan '11, 06:51)</span> <span class="comment-user userinfo">ant2009</span></div></div><span id="1955"></span><div id="comment-1955" class="comment"><div id="post-1955-score" class="comment-score"></div><div class="comment-text"><p>Ehm, no, it's not a final solution. What would be is (in order of preference):</p><ol><li>A fixed PortAudio</li><li>An even more exhaustive search by Wireshark for a usable device</li><li>Create a user configuration option</li><li>Have you work on the ALSA/device driver configuration or code</li></ol><p>All of which requires developer cycles.</p></div><div id="comment-1955-info" class="comment-info"><span class="comment-age">(26 Jan '11, 14:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-1908" class="comment-tools"></div><div class="clear"></div><div id="comment-1908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1888"></span>

<div id="answer-container-1888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1888-score" class="post-score" title="current number of votes">1</div><span id="post-1888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's something off with the configuration of your audio system.</p><p>First off, the PortAudio library has some issues finding your default device, on the default host API. That's a PortAudio lib problem by itself, but Wireshark tries to work around it looking for other host API/device configurations.</p><p>It tries to work through the list of host APIs, the first one with devices on them is selected, then the first device on that is selected. An output stream is opened on it, with stereo output, 16 bit samples, 8 kHz sample rate.</p><p>Now, your title says: "Invalid sample rate". That strikes me as odd, because the output configuration is trivial in itself.</p><p>You could investigate further installing Audacity, and checking how it works the output host API/device options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '11, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1888" class="comments-container"><span id="1893"></span><div id="comment-1893" class="comment"><div id="post-1893-score" class="comment-score"></div><div class="comment-text"><p>Hello, thanks for your answer. However, installing audacity didn't work. I installed it and then rebooted. See my edited question of the results. Thanks.</p></div><div id="comment-1893-info" class="comment-info"><span class="comment-age">(23 Jan '11, 08:30)</span> <span class="comment-user userinfo">ant2009</span></div></div><span id="1897"></span><div id="comment-1897" class="comment"><div id="post-1897-score" class="comment-score"></div><div class="comment-text"><p>What does Audacity menu Help|Audio Device Info show ?</p></div><div id="comment-1897-info" class="comment-info"><span class="comment-age">(23 Jan '11, 11:44)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="1905"></span><div id="comment-1905" class="comment"><div id="post-1905-score" class="comment-score"></div><div class="comment-text"><p>Hello Jaap, I have edited my answer with the device info. Thanks.</p></div><div id="comment-1905-info" class="comment-info"><span class="comment-age">(24 Jan '11, 07:16)</span> <span class="comment-user userinfo">ant2009</span></div></div></div><div id="comment-tools-1888" class="comment-tools"></div><div class="clear"></div><div id="comment-1888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


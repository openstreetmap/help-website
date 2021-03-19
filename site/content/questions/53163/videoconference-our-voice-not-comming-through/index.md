+++
type = "question"
title = "Videoconference our voice not comming through"
description = '''Dear everyone,  I have no experience in packet tracing, but since a few months we have a delayed start with specific countries, whereas our office in the US and our office in Japan, with our closer countries Italy and Netherlands offices, we are having no issue in delay. The issue is we can see the ...'''
date = "2016-06-03T01:18:00Z"
lastmod = "2016-06-03T01:18:00Z"
weight = 53163
keywords = [ "videoconference", "connection", "delayed" ]
aliases = [ "/questions/53163" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Videoconference our voice not comming through](/questions/53163/videoconference-our-voice-not-comming-through)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53163-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear everyone,</p><p>I have no experience in packet tracing, but since a few months we have a delayed start with specific countries, whereas our office in the US and our office in Japan, with our closer countries Italy and Netherlands offices, we are having no issue in delay.</p><p>The issue is we can see the opponent side and hear them very well, but they only start to hear us after 5 till 15 minutes, as very sometimes it is connected instantly.</p><p>I traced the session with wireshark, but don't know which packets to really look for.</p><p>Kind regards, Sven</p></div><div id="question-tags" class="tags-container tags">videoconference connection delayed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/b8f0b08e0d3337e5bc247de201b2fa41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SvenSub&#39;s gravatar image" /><p>SvenSub<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SvenSub has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jun '16, 01:21</p></div></div><div id="comments-container-53163" class="comments-container"><span id="53165"></span><div id="comment-53165" class="comment"><div id="post-53165-score" class="comment-score"></div><div class="comment-text"><p>The first thing to do would be to capture simultaneously at both ends in order to exclude obvious things like packets getting somewhere in the sea.</p><p>For any advice from here you'd either have to specify what videoconferencing equipment you use so that people eventually knowing that equipment could advise you what exactly to look at in the capture (but don't expect too much from this approach), or you'd have to capture a "dry run" of the conference where the issue would show up but the conference itself would not contain any sensitive information, and publish the capture somewhere at publicly accessible file sharing service (Cloudshark is the most task-specific one but you can use Google drive, Dropbox, ...) and edit your Question with links to the files from both ends. This approach allows general network specialists to find how your videoconferencing works without knowledge of your particular solution, and either tell you what to look for or even directly tell you what the issue is. Needless to say that such captures would have to last until the remote party starts hearing your audio.</p><p>It is not excluded that everything is fine at network level and the root cause of your issue is in the videoconferencing application.</p></div><div id="comment-53165-info" class="comment-info"><span class="comment-age">(03 Jun '16, 01:33)</span> sindy</div></div></div><div id="comment-tools-53163" class="comment-tools"></div><div class="clear"></div><div id="comment-53163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


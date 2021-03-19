+++
type = "question"
title = "Help me track down origin of random computer sound"
description = '''For the past three months, the same specific sound has occurred randomly on any computer (I have tested 3) attached to my wired network. I have pretty much eliminated that the cause is hardware (either replaced or swapped everything) or Windows. It has been suggested that this sound must be somethin...'''
date = "2017-07-04T16:31:00Z"
lastmod = "2017-07-04T16:31:00Z"
weight = 62505
keywords = [ "sound" ]
aliases = [ "/questions/62505" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help me track down origin of random computer sound](/questions/62505/help-me-track-down-origin-of-random-computer-sound)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62505-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For the past three months, the same specific sound has occurred randomly on any computer (I have tested 3) attached to my wired network. I have pretty much eliminated that the cause is hardware (either replaced or swapped everything) or Windows. It has been suggested that this sound must be something passing through the network and that I should use Wireshark to scope out its origin.</p><p>I have run Wireshark twice when the sound occurred. Can someone please give me some advice at what sort of event to look for in the saved log entries.</p><p>Here is a recording of the sound: <a href="https://soundcloud.com/finvarra/nuc-sound-2">https://soundcloud.com/finvarra/nuc-sound-2</a></p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">sound</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '17, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/caf9557fe865a4761f33579c3748eb11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="finvarra&#39;s gravatar image" /><p>finvarra<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="finvarra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '17, 16:32</p></div></div><div id="comments-container-62505" class="comments-container"><span id="62510"></span><div id="comment-62510" class="comment"><div id="post-62510-score" class="comment-score"></div><div class="comment-text"><p>You have eliminated Windows? Not sure, but this sounds like some confirmation sound of an event. Go look for that in the configuration settings. Then you'll know the related event.</p></div><div id="comment-62510-info" class="comment-info"><span class="comment-age">(04 Jul '17, 23:38)</span> Jaap ♦</div></div><span id="62520"></span><div id="comment-62520" class="comment"><div id="post-62520-score" class="comment-score"></div><div class="comment-text"><p>I've eliminated Windows because I've turned off all Windows system sounds and hooked up 3 different machines to the same network (1 running Win10, the others Win7) with only kb/mouse and heard the exact sound. In fact, one of the machines I tested was a friend's.</p></div><div id="comment-62520-info" class="comment-info"><span class="comment-age">(05 Jul '17, 07:22)</span> finvarra</div></div><span id="62525"></span><div id="comment-62525" class="comment"><div id="post-62525-score" class="comment-score"></div><div class="comment-text"><p>The chance that the sound itself is transmitted in the form of audio data over the network each time you can hear it, and as such it could be found in data captured using Wireshark, is quite small (leaving aside the issue of way too many codecs which could be used and thus the complexity of finding a sound pattern rather than a byte pattern).</p><p>It is much more likely that the sound is pre-loaded at your machine along with some application which plays it whenever a particular network event happens. So if you've got two capture files from the times when the sound occurred, you should identify those data flows in each of them which were ongoing at the moment the sound has occurred and slightly before, and then identify each single one of them, and also one-time events like DHCP address assignment or so. If two of them match by the remote IP address between the two capture files while others don't, it could be a hint. But I'd rather think of chat applications, softphones etc. first.</p></div><div id="comment-62525-info" class="comment-info"><span class="comment-age">(05 Jul '17, 07:55)</span> sindy</div></div></div><div id="comment-tools-62505" class="comment-tools"></div><div class="clear"></div><div id="comment-62505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


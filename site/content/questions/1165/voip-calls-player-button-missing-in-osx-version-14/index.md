+++
type = "question"
title = "Voip calls Player button missing in OSX version 1.4"
description = '''Where has the Player function gone in the Wireshark 1.4.x version for OSX ? I am running OSX 10.6.5 Snow Leopard and the older 32-bit versions do not run as fast as the 64-bit version, but the 1.4 version has no function to play RTP streams. This is indeed a problem. '''
date = "2010-11-29T14:02:00Z"
lastmod = "2010-12-10T04:45:00Z"
weight = 1165
keywords = [ "1.4", "player", "rtp", "voip", "decode" ]
aliases = [ "/questions/1165" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Voip calls Player button missing in OSX version 1.4](/questions/1165/voip-calls-player-button-missing-in-osx-version-14)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Where has the Player function gone in the Wireshark 1.4.x version for OSX ? I am running OSX 10.6.5 Snow Leopard and the older 32-bit versions do not run as fast as the 64-bit version, but the 1.4 version has no function to play RTP streams. This is indeed a problem.</p></div><div id="question-tags" class="tags-container tags">1.4 player rtp voip decode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '10, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/2ca47d309b460016dc465847663c319a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ladf&#39;s gravatar image" /><p>ladf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ladf has no accepted answers">0%</span></p></div></div><div id="comments-container-1165" class="comments-container"></div><div id="comment-tools-1165" class="comment-tools"></div><div class="clear"></div><div id="comment-1165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1291"></span>

<div id="answer-container-1291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have the same experience. The player button is there on windows, but disapeared in the 1.4 version for OS X. really nasty if you want to use Wireshark for voip debugging.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '10, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/95b9a8eeb20cdb0ef0f1d24d835f6688?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvds&#39;s gravatar image" /><p>pvds<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvds has no accepted answers">0%</span></p></div></div><div id="comments-container-1291" class="comments-container"></div><div id="comment-tools-1291" class="comment-tools"></div><div class="clear"></div><div id="comment-1291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1313"></span>

<div id="answer-container-1313" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1313-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't compare 'older 32 bit versions' with '1.4' and say they're different. These are different aspects of the Wireshark builds.</p><p>You have Wireshark versions build for 32 bit systems and 64 bit systems respectively, that's one angle.</p><p>You have stable release 1.0, 1.2 and now 1.4 versions, that's another angle.</p><p>What you probably noticed is that the 1.2 release, build as 32 bit version did have a Player button, while the 1.4 release, build as 64 bit version does not.</p><p>If you check the About Wireshark dialog box look for <em>PortAudio</em>. If that library is included you'll have the Player button, otherwise not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '10, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1313" class="comments-container"></div><div id="comment-tools-1313" class="comment-tools"></div><div class="clear"></div><div id="comment-1313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


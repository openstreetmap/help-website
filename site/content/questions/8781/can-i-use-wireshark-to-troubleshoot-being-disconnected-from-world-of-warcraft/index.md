+++
type = "question"
title = "Can I use Wireshark to troubleshoot being disconnected from World of Warcraft?"
description = '''My girlfriend and I (on same wired cable connection) are constantly getting disconnected simultaneously when we play World of Warcraft. Will Wireshark help us identify the issue and whether the disconnects are initiated on our side or the server end?'''
date = "2012-02-02T10:05:00Z"
lastmod = "2012-02-03T20:56:00Z"
weight = 8781
keywords = [ "troubleshooting" ]
aliases = [ "/questions/8781" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use Wireshark to troubleshoot being disconnected from World of Warcraft?](/questions/8781/can-i-use-wireshark-to-troubleshoot-being-disconnected-from-world-of-warcraft)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8781-score" class="post-score" title="current number of votes">0</div><span id="post-8781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My girlfriend and I (on same wired cable connection) are constantly getting disconnected simultaneously when we play World of Warcraft. Will Wireshark help us identify the issue and whether the disconnects are initiated on our side or the server end?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '12, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/0e93c276d6ec3fe06b46236b5341217a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paraella&#39;s gravatar image" /><p><span>paraella</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paraella has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '12, 15:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8781" class="comments-container"></div><div id="comment-tools-8781" class="comment-tools"></div><div class="clear"></div><div id="comment-8781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8804"></span>

<div id="answer-container-8804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8804-score" class="post-score" title="current number of votes">0</div><span id="post-8804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might be able to determine if it is a connection abort coming in from the server, or if it is your client(s) that do this. You'll have to capture your traffic either on your PC (while WoW is running) or somewhere down the line, maybe on or at your router (some have diagnostic options to write network packets to files, but there may be a size limitation).</p><p>I have no idea what kind of protocol WoW uses, but I guess it is a UDP based protocol like most online games use. In that case you'll not have Reset packets and other "nice" indicators of network problems that TCP would offer, but maybe you can tell from the content of the game packets what happened - for example, you might see content in a packet from the server that looks similar right before your connection gets dropped, and that both of your PCs receive.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8804" class="comments-container"></div><div id="comment-tools-8804" class="comment-tools"></div><div class="clear"></div><div id="comment-8804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8818"></span>

<div id="answer-container-8818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8818-score" class="post-score" title="current number of votes">0</div><span id="post-8818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From what I can find documented (<a href="http://eu.battle.net/support/en/article/configuring-your-router-for-use-with-world-of-warcraft-and-the-blizzard-downloader-101707">http://eu.battle.net/support/en/article/configuring-your-router-for-use-with-world-of-warcraft-and-the-blizzard-downloader-101707</a>):</p><ul><li>WoW uses tcp/1119 and tcp/3724</li><li>Blizzard Downloader uses tcp/6881-tcp/6999 (the full range)</li><li>WoW Voice Chat uses udp/3724</li><li>Battle.net service uses tcp/1120</li></ul><p>I'd pay attention to connections on tcp/1119 and tcp/3724, but you want to make sure that all of those ports are available and/or properly forwarded through your router.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '12, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-8818" class="comments-container"></div><div id="comment-tools-8818" class="comment-tools"></div><div class="clear"></div><div id="comment-8818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


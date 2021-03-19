+++
type = "question"
title = "1.99.1, OS X, and Multiple Windows"
description = '''I was going to download 1.12.2 64bit for OS X and I noticed the pretty little note that read &quot;OS X users might want to try the development release below&quot;...so I did. The interface is certainly polished and more OS X&#x27;y (sounds like OS Sexy when I saw it out load...HA!). Anyway - I can&#x27;t find a way to...'''
date = "2014-12-15T06:50:00Z"
lastmod = "2014-12-15T09:09:00Z"
weight = 38570
keywords = [ "interface", "osx", "1.99.1" ]
aliases = [ "/questions/38570" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [1.99.1, OS X, and Multiple Windows](/questions/38570/1991-os-x-and-multiple-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38570-score" class="post-score" title="current number of votes">0</div><span id="post-38570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was going to download 1.12.2 64bit for OS X and I noticed the pretty little note that read "OS X users might want to try the development release below"...so I did.</p><p>The interface is certainly polished and more OS X'y (sounds like OS Sexy when I saw it out load...HA!). Anyway - I can't find a way to open two captures for viewing simultaneously. I've looked through the Wiki and the mailing lists but I didn't see anything that addressed the issue. Is this a known limitation of the QT interface on OS X? I did grab the 64bit version and I do have a retina display - but I'm not sure that information is relevant to my question. The new interface is snazzy and all, but I'll be back on the X11 boat for now because I need the ability to view multiple captures simultaneously. Thanks for the great work!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-1.99.1" rel="tag" title="see questions tagged &#39;1.99.1&#39;">1.99.1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '14, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-38570" class="comments-container"></div><div id="comment-tools-38570" class="comment-tools"></div><div class="clear"></div><div id="comment-38570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38581"></span>

<div id="answer-container-38581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38581-score" class="post-score" title="current number of votes">1</div><span id="post-38581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark assumes that each process has one and only one main window. This isn't a problem on Windows or X11 since you can just create another process. It is a problem when run as an OS X application bundle, as you've discovered. Adding multiple main windows per process would be a huge development effort and I'm not sure if or when it will be done. In the mean time you can work around the problem using <code>open -n /Applications/Wireshark.app</code>. This isn't optimal in that it adds a Wireshark icon to the dock for each instance but it works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-38581" class="comments-container"></div><div id="comment-tools-38581" class="comment-tools"></div><div class="clear"></div><div id="comment-38581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38571"></span>

<div id="answer-container-38571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38571-score" class="post-score" title="current number of votes">0</div><span id="post-38571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can only load one file at a time (always has, so this is not specific to the QT build), so you'll have to start multiple instances to display more than one file. I'm not familiar with OSX, but I guess you should be able to position two Wireshark instances next to each other.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38571" class="comments-container"><span id="38575"></span><div id="comment-38575" class="comment"><div id="post-38575-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response. I don't see a way (an easy way) to force multiple instances with the new version. With all previous versions Wireshark would automatically open captures in new windows - automatically generating a second instance. I can force a second instance to launch by running "wireshark" from the CLI - but this is rather clunky and makes it more work to open captures from VMs that I have running in the background. There isn't an "Open new window" in the File menu, nor do I see an open in the Preferences to force new instances/windows.</p></div><div id="comment-38575-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:20)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="38576"></span><div id="comment-38576" class="comment"><div id="post-38576-score" class="comment-score">1</div><div class="comment-text"><p>You might want to add a bug report at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> for this, and either declare it a bug or feature request ;-)</p></div><div id="comment-38576-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="38577"></span><div id="comment-38577" class="comment"><div id="post-38577-score" class="comment-score"></div><div class="comment-text"><p>Feature request 10778 added. Thanks Jasper!</p></div><div id="comment-38577-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:35)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-38571" class="comment-tools"></div><div class="clear"></div><div id="comment-38571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


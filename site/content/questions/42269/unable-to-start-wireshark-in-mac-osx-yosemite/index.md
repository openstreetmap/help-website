+++
type = "question"
title = "Unable to start wireshark in Mac OSX Yosemite"
description = '''Hi,  I&#x27;m unable to start wireshark on my mac. wireshark version is 1.12.4. I&#x27;m currently using mac osx 10.10 yosemite, when I start wireshark(both 64bit and 32 bit version),it will just quit immediately after showing icon in th dock. When I start it in the terminal, I face the following errors: jinx...'''
date = "2015-05-09T21:48:00Z"
lastmod = "2015-06-04T12:51:00Z"
weight = 42269
keywords = [ "macosx", "yosemite" ]
aliases = [ "/questions/42269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to start wireshark in Mac OSX Yosemite](/questions/42269/unable-to-start-wireshark-in-mac-osx-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42269-score" class="post-score" title="current number of votes">0</div><span id="post-42269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm unable to start wireshark on my mac. wireshark version is 1.12.4.</p><p>I'm currently using mac osx 10.10 yosemite, when I start wireshark(both 64bit and 32 bit version),it will just quit immediately after showing icon in th dock. When I start it in the terminal, I face the following errors:</p><pre><code>jinxuans-MacBook-Air:~ jinxuanw$ wireshark 
2015-05-09 21:42:06.953 defaults[56605:372907] 
The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2015-05-09 21:42:06.965 defaults[56606:372913] 
The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist
./sync_osx_look.sh: line 38: gtkrc: Permission denied
cp: /Applications/Wireshark.app/Contents/Resources/etc/pango/pangox.aliases: No such file or directory

(wireshark-bin:56595): Gtk-WARNING **: Locale not supported by C library.
    Using the fallback &#39;C&#39; locale.

(wireshark-bin:56595): Gtk-WARNING **: cannot open display:</code></pre><p>Any suggestion to solve this issue?</p><p>Addition: I have tried to reinstall xquartz and create symbolic link in /usr/X11. Xquartz version is 2.7.7</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-yosemite" rel="tag" title="see questions tagged &#39;yosemite&#39;">yosemite</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '15, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/06c5082297e2fba41adedb26dd747334?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jinxuan%20wu&#39;s gravatar image" /><p><span>jinxuan wu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jinxuan wu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '15, 21:52</strong> </span></p></div></div><div id="comments-container-42269" class="comments-container"><span id="42274"></span><div id="comment-42274" class="comment"><div id="post-42274-score" class="comment-score">1</div><div class="comment-text"><p>Maybe try the developer version 1.99, which uses QT?</p></div><div id="comment-42274-info" class="comment-info"><span class="comment-age">(10 May '15, 02:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42281"></span><div id="comment-42281" class="comment"><div id="post-42281-score" class="comment-score"></div><div class="comment-text"><p>I just tried 1.99 64bit version, by start with wireshark -withqt it worked. Thank you for your advice.</p></div><div id="comment-42281-info" class="comment-info"><span class="comment-age">(10 May '15, 10:30)</span> <span class="comment-user userinfo">jinxuan wu</span></div></div><span id="42286"></span><div id="comment-42286" class="comment"><div id="post-42286-score" class="comment-score"></div><div class="comment-text"><p>What happens if you type "xterm" as a command?</p></div><div id="comment-42286-info" class="comment-info"><span class="comment-age">(10 May '15, 15:07)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="42896"></span><div id="comment-42896" class="comment"><div id="post-42896-score" class="comment-score"></div><div class="comment-text"><p>Did you reboot after creating the symlink?</p></div><div id="comment-42896-info" class="comment-info"><span class="comment-age">(04 Jun '15, 12:51)</span> <span class="comment-user userinfo">Joe C</span></div></div></div><div id="comment-tools-42269" class="comment-tools"></div><div class="clear"></div><div id="comment-42269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42382"></span>

<div id="answer-container-42382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42382-score" class="post-score" title="current number of votes">0</div><span id="post-42382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you have to install XQuartz and wireshark. once installed start X11 (located in /Application/Utilities/X11). you have to wait a few minutes the first time and then try to start wireshark. you may get an error prompt or the begining wireshark prompt will disapper with opening the dashboard (the dashboard can take a few seconds to appear). you have to work at it the first time as it runs a bit clunky. once you get it going the first time, subsequent times are not difficult.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/eda96ad10feffdbe22faa88ad508d969?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johannes&#39;s gravatar image" /><p><span>johannes</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johannes has no accepted answers">0%</span></p></div></div><div id="comments-container-42382" class="comments-container"></div><div id="comment-tools-42382" class="comment-tools"></div><div class="clear"></div><div id="comment-42382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


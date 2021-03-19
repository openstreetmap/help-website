+++
type = "question"
title = "Mac os x 10.6 Wireshark won&#x27;t start.."
description = '''I get  While WS is open, its windows can be displayed or hidden by displaying or hiding the X11 app. The first time this version of WS is run it may take several mins before the main window is displayed while font caches are built.  I get that message. but it never starts up.  MBP OS X snow lep. 10....'''
date = "2011-02-11T16:52:00Z"
lastmod = "2012-01-02T10:13:00Z"
weight = 2290
keywords = [ "osx", "mac", "startup" ]
aliases = [ "/questions/2290" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mac os x 10.6 Wireshark won't start..](/questions/2290/mac-os-x-106-wireshark-wont-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2290-score" class="post-score" title="current number of votes">0</div><span id="post-2290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I get</p><p>While WS is open, its windows can be displayed or hidden by displaying or hiding the X11 app. The first time this version of WS is run it may take several mins before the main window is displayed while font caches are built.</p><p>I get that message. but it never starts up.</p><p>MBP OS X snow lep. 10.6</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '11, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/0e6e8bf0cd06ab091822c8cd5e06d213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avant_guard3&#39;s gravatar image" /><p><span>avant_guard3</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avant_guard3 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Feb '12, 19:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-2290" class="comments-container"></div><div id="comment-tools-2290" class="comment-tools"></div><div class="clear"></div><div id="comment-2290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2295"></span>

<div id="answer-container-2295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2295-score" class="post-score" title="current number of votes">0</div><span id="post-2295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ditto.</p><p>Running it from the command line</p><p>bash-3.2# /Applications/Wireshark.app/Contents/MacOS/Wireshark</p><p>2011-02-13 02:42:32.400 defaults[77170:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist</p><p>2011-02-13 02:42:32.420 defaults[77171:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist</p><p>dyld: Library not loaded: /usr/X11/lib/libpng12.0.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: Incompatible library version: wireshark-bin requires version 45.0.0 or later, but libpng12.0.dylib provides version 42.0.0 bash-3.2#</p><p>I've got current Xcode and X11 XQuartz 2.3.5 installed on my machine. port upgrade libpng on macports is at 1.2.40.</p><p>wireshark seems to be looking for a libpng with an entirely different numbering convention.</p><p>Whuzzup?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/ed2ddfe3ce5e547c20fafa0c82b3e970?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SGBotsford&#39;s gravatar image" /><p><span>SGBotsford</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SGBotsford has no accepted answers">0%</span></p></div></div><div id="comments-container-2295" class="comments-container"><span id="2320"></span><div id="comment-2320" class="comment"><div id="post-2320-score" class="comment-score"></div><div class="comment-text"><p>Ok. I've got a working wireshark. Did the macport version.</p><p>Comment to the developers: If you want portable code, do not write to the lastest version of the library unless you need a feature from that newer version.</p></div><div id="comment-2320-info" class="comment-info"><span class="comment-age">(13 Feb '11, 23:27)</span> <span class="comment-user userinfo">SGBotsford</span></div></div><span id="2325"></span><div id="comment-2325" class="comment"><div id="post-2325-score" class="comment-score"></div><div class="comment-text"><p>If "the developers" means the Wireshark developers, we don't write to libpng <em>at all</em>, we write to GTK+ (and not the latest version); GTK+ builds with libpng. The problem is the version with which GTK+ is built; the build procedure for GTK+ is oriented towards building with the version installed on the machine, not with the version in, for OS X, an SDK.</p></div><div id="comment-2325-info" class="comment-info"><span class="comment-age">(14 Feb '11, 10:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2295" class="comment-tools"></div><div class="clear"></div><div id="comment-2295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8191"></span>

<div id="answer-container-8191" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8191-score" class="post-score" title="current number of votes">0</div><span id="post-8191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open the ChmodBPF script, which is located in /Library/StartupItems/ChmodBPF/ChmodBPF, in a text editor. Add a chown line so that the file looks like this: ... chgrp admin /dev/bpf <em>chmod g+rw /dev/bpf</em> chown foobar:admin /dev/bpf* } ... But replace foobar here with the user you want to run Wireshark under. Save the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '12, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/e1c72a1a7eb7efcb090b9f5fcec01d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Lucas&#39;s gravatar image" /><p><span>Michael Lucas</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Lucas has no accepted answers">0%</span></p></div></div><div id="comments-container-8191" class="comments-container"></div><div id="comment-tools-8191" class="comment-tools"></div><div class="clear"></div><div id="comment-8191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


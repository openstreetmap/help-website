+++
type = "question"
title = "MAC OSX 10.6.3 - When I Open Wireshark it shows on dock then closes"
description = '''When I open Wireshark, it just shows on the dock as if it opened, then it closes itself, why is this? When I run it using terminal it says: The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib  Refere...'''
date = "2011-05-01T23:32:00Z"
lastmod = "2011-06-14T19:00:00Z"
weight = 3868
keywords = [ "crash", "osx", "mac", "installation" ]
aliases = [ "/questions/3868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC OSX 10.6.3 - When I Open Wireshark it shows on dock then closes](/questions/3868/mac-osx-1063-when-i-open-wireshark-it-shows-on-dock-then-closes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3868-score" class="post-score" title="current number of votes">1</div><span id="post-3868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I open Wireshark, it just shows on the dock as if it opened, then it closes itself, why is this?</p><p>When I run it using terminal it says: The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: Incompatible library version: wireshark-bin requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0</p><p>What does this mean?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/7d2a20ea20f40a93c53120360ca9ba9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Nethers&#39;s gravatar image" /><p><span>Tim Nethers</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Nethers has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>14 Jun '11, 19:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-3868" class="comments-container"></div><div id="comment-tools-3868" class="comment-tools"></div><div class="clear"></div><div id="comment-3868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3877"></span>

<div id="answer-container-3877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3877-score" class="post-score" title="current number of votes">1</div><span id="post-3877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently, the libfreetype you're using is incompatible with Wireshark. Others have had similar problems (<a href="https://trac.macports.org/ticket/25016">here</a> and <a href="http://octave.1599824.n4.nabble.com/Mac-OSX-10-6-5-update-td3041761.html">here</a>), and it seems to be related to a foul <code>DYLD_LIBRARY_PATH</code>. The second <a href="http://octave.1599824.n4.nabble.com/Mac-OSX-10-6-5-update-td3041761.html">link</a> (referring to gnuplot but same problem here) provides a temporary(?) workaround:</p><ol><li>Open the folder /Applications in the finder</li><li>Right-click on Wireshark.app and select "Show package contents"</li><li>Navigate to /Applications/Wireshark.app/Contents/Resources/bin</li><li>Right-click on the file "wireshark" and select "Open with -&gt; Other ... -&gt; TextEdit.app"</li><li>Change the line:</li></ol><p>from: <code>DYLD_LIBRARY_PATH="${ROOT}/lib:${DYLD_LIBRARY_PATH}"</code><br />
to: <code>DYLD_LIBRARY_PATH="${ROOT}/lib"</code></p><p>and</p><p>from: <code>DYLD_FRAMEWORK_PATH</code><br />
to: <code>DYLD_FRAMEWORK_PATH="${ROOT}/lib"</code></p><p><strong>EDIT</strong>: If the workaround above doesn't work for you, try re-installing freetype [from <a href="http://www.macports.org/">MacPorts</a>].</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '11, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '11, 12:14</strong> </span></p></div></div><div id="comments-container-3877" class="comments-container"><span id="3879"></span><div id="comment-3879" class="comment"><div id="post-3879-score" class="comment-score"></div><div class="comment-text"><p>The first one already existed with $TOP in place of ${ROOT} The second did not exist.</p></div><div id="comment-3879-info" class="comment-info"><span class="comment-age">(02 May '11, 09:25)</span> <span class="comment-user userinfo">Tim Nethers</span></div></div><span id="4567"></span><div id="comment-4567" class="comment"><div id="post-4567-score" class="comment-score"></div><div class="comment-text"><p>Someone else had a similar <a href="http://ask.wireshark.org/questions/4528/wireshark-does-not-run">problem</a> with libfreetype recently and resolved it by performing a system update.</p></div><div id="comment-4567-info" class="comment-info"><span class="comment-age">(14 Jun '11, 19:00)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-3877" class="comment-tools"></div><div class="clear"></div><div id="comment-3877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Wireshark not opening after OS X 10.10.3 update"
description = '''I am new to this forum but I am looking for a little help here. Ever since updating to OS X Yosemite 10.10.3 Wireshark will not open. I was originally running Wireshark 1.12.3 I have also tried upgrading to 1.12.4. It bounces on my dock then closes there is no error code. Console however puts out: 4...'''
date = "2015-04-15T18:09:00Z"
lastmod = "2015-04-16T17:13:00Z"
weight = 41468
keywords = [ "osx", "10.10.3" ]
aliases = [ "/questions/41468" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not opening after OS X 10.10.3 update](/questions/41468/wireshark-not-opening-after-os-x-10103-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41468-score" class="post-score" title="current number of votes">0</div><span id="post-41468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to this forum but I am looking for a little help here. Ever since updating to OS X Yosemite 10.10.3 Wireshark will not open. I was originally running Wireshark 1.12.3 I have also tried upgrading to 1.12.4. It bounces on my dock then closes there is no error code.</p><p>Console however puts out:</p><pre><code>4/15/15 8:42:26.299 PM cloudd[245]: Failed to create dir at /Users/USER/Library/Containers/com.apple.TextEdit/*/Assets: Error Domain=NSCocoaErrorDomain Code=513 &quot;You don’t have permission to save the file “Assets” in the folder “CloudKit”.&quot; UserInfo=0x7fd5a9830890 {NSFilePath=/Users/Bubba1/Library/Containers/com.apple.TextEdit/Data/Library/Caches/CloudKit/Assets, NSUnderlyingError=0x7fd5a982f370 &quot;The operation couldn’t be completed. Operation not permitted&quot;}

4/15/15 8:42:26.306 PM sandboxd[273]: ([245]) cloudd(245) deny file-write-create /Users/Bubba1/Library/Containers/com.apple.TextEdit/Data/Library/Caches</code></pre><p>These errors persist after permissions repair as well.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-10.10.3" rel="tag" title="see questions tagged &#39;10.10.3&#39;">10.10.3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 18:09</strong></p><img src="https://secure.gravatar.com/avatar/8851005fc4ea73e64de2c2328e45aa4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dawstinger&#39;s gravatar image" /><p><span>dawstinger</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dawstinger has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '15, 05:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41468" class="comments-container"><span id="41473"></span><div id="comment-41473" class="comment"><div id="post-41473-score" class="comment-score"></div><div class="comment-text"><p>That error is probably something unrelated to Wireshark - it sounds like an error with iCloud Drive and TextEdit.</p></div><div id="comment-41473-info" class="comment-info"><span class="comment-age">(15 Apr '15, 21:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41501"></span><div id="comment-41501" class="comment"><div id="post-41501-score" class="comment-score"></div><div class="comment-text"><p>What did you upgrade from? An earlier version of Yosemite, or a version prior to Yosemite?</p><p>What does <code>ls -ld /opt/X11 /usr/X11</code> print?</p></div><div id="comment-41501-info" class="comment-info"><span class="comment-age">(16 Apr '15, 13:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41502"></span><div id="comment-41502" class="comment"><div id="post-41502-score" class="comment-score"></div><div class="comment-text"><p>lrwxr-xr-x 1 root wheel 8 Feb 2 09:11 /usr/X11 -&gt; /opt/X11</p><pre><code>/opt/X11:
total 8
lrwxr-xr-x    1 root  wheel     8 Apr 16 16:37 X11 -&gt; /opt/X11
drwxr-xr-x  125 root  wheel  4250 Feb  2 09:06 bin
drwxr-xr-x    3 root  wheel   102 Mar  5  2012 etc
drwxr-xr-x   17 root  wheel   578 Feb  2 09:06 include
drwxr-xr-x  194 root  wheel  6596 Feb  2 09:06 lib
drwxr-xr-x   14 root  wheel   476 Aug 11  2014 share
drwxr-xr-x    5 root  wheel   170 Aug 11  2014 var</code></pre></div><div id="comment-41502-info" class="comment-info"><span class="comment-age">(16 Apr '15, 13:50)</span> <span class="comment-user userinfo">dawstinger</span></div></div><span id="41503"></span><div id="comment-41503" class="comment"><div id="post-41503-score" class="comment-score"></div><div class="comment-text"><p>and that is after running the other command sudo ln -s /opt/X11 /usr/X11 and Wireshark still doesn't run. And when I try to open X11 by itself I do get an error 'An error occurred while starting the X11 server: "Cannot establish any listening sockets - Make sure an X server isn't already running"</p><p>Click Quit to quit X11. Click Report to see more details or send a report to Apple.'</p></div><div id="comment-41503-info" class="comment-info"><span class="comment-age">(16 Apr '15, 13:52)</span> <span class="comment-user userinfo">dawstinger</span></div></div><span id="41504"></span><div id="comment-41504" class="comment"><div id="post-41504-score" class="comment-score"></div><div class="comment-text"><p>OK, so there's an underlying problem with X11. What does <code>ps -ef | egrep -i quartz</code> print?</p></div><div id="comment-41504-info" class="comment-info"><span class="comment-age">(16 Apr '15, 14:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41505"></span><div id="comment-41505" class="comment not_top_scorer"><div id="post-41505-score" class="comment-score"></div><div class="comment-text"><p>502 846 842 0 5:20PM ttys000 0:00.00 egrep -i quartz</p></div><div id="comment-41505-info" class="comment-info"><span class="comment-age">(16 Apr '15, 14:20)</span> <span class="comment-user userinfo">dawstinger</span></div></div><span id="41506"></span><div id="comment-41506" class="comment not_top_scorer"><div id="post-41506-score" class="comment-score"></div><div class="comment-text"><p>So what does <code>ps -ef | egrep -i x11</code> print?</p></div><div id="comment-41506-info" class="comment-info"><span class="comment-age">(16 Apr '15, 14:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41508"></span><div id="comment-41508" class="comment not_top_scorer"><div id="post-41508-score" class="comment-score"></div><div class="comment-text"><p>502 893 889 0 6:51PM ttys000 0:00.00 egrep -i x11</p></div><div id="comment-41508-info" class="comment-info"><span class="comment-age">(16 Apr '15, 15:52)</span> <span class="comment-user userinfo">dawstinger</span></div></div></div><div id="comment-tools-41468" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-41468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41510"></span>

<div id="answer-container-41510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41510-score" class="post-score" title="current number of votes">1</div><span id="post-41510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, no obvious X11 server running (i.e., it appears that there <em>isn't</em> "an X server ... already running", so <em>that's</em> probably not the issue), and the required symlink is present (so the usual fix for X11-on-Yosemite issues isn't relevant here).</p><p>Try uninstalling XQuartz, using the "Uninstall (Snow Leopard or Later)" instructions in <a href="http://xquartz.macosforge.org/trac/wiki/X11-UsersFAQ">the XQuartz X11-Users FAQ</a>. Then download the latest version of XQuartz and install it, and see whether you can launch X11 by itself. If not, try rebooting, and try again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '15, 16:06</strong> </span></p></div></div><div id="comments-container-41510" class="comments-container"><span id="41512"></span><div id="comment-41512" class="comment"><div id="post-41512-score" class="comment-score"></div><div class="comment-text"><p>Thank every one for the help. Uninstall of Quartz(X11) and reinstall corrected the issue.</p></div><div id="comment-41512-info" class="comment-info"><span class="comment-age">(16 Apr '15, 17:13)</span> <span class="comment-user userinfo">dawstinger</span></div></div></div><div id="comment-tools-41510" class="comment-tools"></div><div class="clear"></div><div id="comment-41510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41500"></span>

<div id="answer-container-41500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41500-score" class="post-score" title="current number of votes">0</div><span id="post-41500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answer in this topic helped me (version 1.12.4) <a href="https://ask.wireshark.org/questions/36367/wireshark-doesnt-start-after-upgrading-to-mac-os-x-yosemite">https://ask.wireshark.org/questions/36367/wireshark-doesnt-start-after-upgrading-to-mac-os-x-yosemite</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/4754a7c0383f725ed718963f598f1580?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexRoslyakov&#39;s gravatar image" /><p><span>AlexRoslyakov</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexRoslyakov has no accepted answers">0%</span></p></div></div><div id="comments-container-41500" class="comments-container"></div><div id="comment-tools-41500" class="comment-tools"></div><div class="clear"></div><div id="comment-41500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Mac OS X 10.6 Installation problem"
description = '''I previously had Wireshark 1.4.6 Intel 64 installed on Mac OS X 10.6. I installed Wireshark 1.8.1 Intel 64 over it by executing the installer package. The installation claimed to be successful. When I tried to launch it, I got the error message Couldn&#x27;t load module /Applications/Wireshark.app/Conten...'''
date = "2012-08-01T19:22:00Z"
lastmod = "2012-08-01T23:17:00Z"
weight = 13305
keywords = [ "quits", "macosx", "installation", "error", "10.6" ]
aliases = [ "/questions/13305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS X 10.6 Installation problem](/questions/13305/mac-os-x-106-installation-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13305-score" class="post-score" title="current number of votes">0</div><span id="post-13305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I previously had Wireshark 1.4.6 Intel 64 installed on Mac OS X 10.6. I installed Wireshark 1.8.1 Intel 64 over it by executing the installer package. The installation claimed to be successful. When I tried to launch it, I got the error message</p><p>Couldn't load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: _dissector_get_port_handle Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so Expected in: flat namespace in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so</p><p>I clicked the OK button to acknowledge that message and I got another error message</p><p>Couldn't load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so, 10): Symbol not found: _dissector_add Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so Expected in: flat namespace in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so</p><p>I clicked the OK button to acknowledge that message and Wireshark quit.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-quits" rel="tag" title="see questions tagged &#39;quits&#39;">quits</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-10.6" rel="tag" title="see questions tagged &#39;10.6&#39;">10.6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/ab8e5acfd8eaac0d74707bbcabb400e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rosenberg&#39;s gravatar image" /><p><span>Rosenberg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rosenberg has no accepted answers">0%</span></p></div></div><div id="comments-container-13305" class="comments-container"><span id="13306"></span><div id="comment-13306" class="comment"><div id="post-13306-score" class="comment-score"></div><div class="comment-text"><p>When I did the installation, I was running under an unprivileged account, and when prompted during the installation process, I entered the password for the Administrator account. As reported above, the installation reported it was successful, but Wireshark won't run. I then removed Wireshark, logged in as the Administrator and re-installed Wireshark. Whatever the problem was, this seems to have fixed it. Wireshark no longer quits when run under either the Administrator account or the unprivileged account.</p></div><div id="comment-13306-info" class="comment-info"><span class="comment-age">(01 Aug '12, 21:22)</span> <span class="comment-user userinfo">Rosenberg</span></div></div></div><div id="comment-tools-13305" class="comment-tools"></div><div class="clear"></div><div id="comment-13305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13308"></span>

<div id="answer-container-13308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13308-score" class="post-score" title="current number of votes">1</div><span id="post-13308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I previously had Wireshark 1.4.6 Intel 64 installed on Mac OS X 10.6. I installed Wireshark 1.8.1 Intel 64 over it ...</p><pre><code>Couldn&#39;t load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: _dissector_get_port_handle Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so Expected in: flat namespace in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so</code></pre></blockquote><p>Sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7401">bug 7401</a>. Removing Wireshark removed the stale plugin (it's a built-in dissector in 1.8.x, so, instead of replacing the plugin with an updated version, the installer just left the un-updated version behind).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '12, 23:20</strong> </span></p></div></div><div id="comments-container-13308" class="comments-container"></div><div id="comment-tools-13308" class="comment-tools"></div><div class="clear"></div><div id="comment-13308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


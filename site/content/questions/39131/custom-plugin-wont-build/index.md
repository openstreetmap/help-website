+++
type = "question"
title = "Custom Plugin won&#x27;t Build"
description = '''I&#x27;m currently attempting to add a custom plugin to the Wireshark that I built from source for Windows 7. Everything&#x27;s gone okay so far, but when I try to build with the plugin added (following the README.plugin instructions) I am getting a long series of errors from wireshark&#92;epan&#92;proto.h. Just befo...'''
date = "2015-01-14T11:05:00Z"
lastmod = "2015-01-16T11:55:00Z"
weight = 39131
keywords = [ "windows", "wireshark", "plugins" ]
aliases = [ "/questions/39131" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Plugin won't Build](/questions/39131/custom-plugin-wont-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39131-score" class="post-score" title="current number of votes">0</div><span id="post-39131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently attempting to add a custom plugin to the Wireshark that I built from source for Windows 7. Everything's gone okay so far, but when I try to build with the plugin added (following the README.plugin instructions) I am getting a long series of errors from wireshark\epan\proto.h. Just before these start, I'm seeing several warnings from Visual Studio\VC\INCLUDE\stdarg.h, where no object file is generated and it talks about macro redefinitions. What could be causing this?</p><p>Edit: Looking at the Linux version of Wireshark that successfully uses this plugin, I noticed that there is a reference to the plugin directory in the file "configure.in." I'm not seeing configure.in in my version of Wireshark at all. Is this just a difference between the Windows and Linux versions, or am I missing a file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '15, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p><span>mehubb985</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '15, 12:09</strong> </span></p></div></div><div id="comments-container-39131" class="comments-container"><span id="39133"></span><div id="comment-39133" class="comment"><div id="post-39133-score" class="comment-score"></div><div class="comment-text"><p>We'll need to see the errors to work out what's failing. How are you adding the plugin to the build, as an custom extension or a permanent one?</p></div><div id="comment-39133-info" class="comment-info"><span class="comment-age">(14 Jan '15, 13:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="39219"></span><div id="comment-39219" class="comment"><div id="post-39219-score" class="comment-score"></div><div class="comment-text"><p>I was trying to do a permanent extension, but have since switched to custom for simplicity. I undid all the changes I had made to the basic Wireshark and rebuilt to make sure everything was working, and it was fine. I then copied the Custom.m4, Custom.make, and Custon.nmake files into the plugins directory, replacing foo with my plugin name. Now I'm getting a bunch of errors in the epan subdirectory.</p><p>As for the specific errors, there are all sorts of syntax errors in epan\proto.h. Like, missing parenthesis and expected constant expression kind of stuff. I have no idea what could be causing it, but it's the same error I had when trying to do a permanent plugin.</p></div><div id="comment-39219-info" class="comment-info"><span class="comment-age">(16 Jan '15, 10:58)</span> <span class="comment-user userinfo">mehubb985</span></div></div><span id="39220"></span><div id="comment-39220" class="comment"><div id="post-39220-score" class="comment-score"></div><div class="comment-text"><p>To minimise the output, you could just run nmake in the plugin directory.</p><p>It sounds as though there's something wrong in the code before proto.h is included.</p></div><div id="comment-39220-info" class="comment-info"><span class="comment-age">(16 Jan '15, 11:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-39131" class="comment-tools"></div><div class="clear"></div><div id="comment-39131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


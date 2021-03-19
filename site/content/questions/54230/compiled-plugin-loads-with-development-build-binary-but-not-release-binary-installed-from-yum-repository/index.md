+++
type = "question"
title = "Compiled plugin loads with development build binary, but not release binary installed from yum repository"
description = '''I&#x27;m new to Wireshark development and I&#x27;m having trouble loading my custom Wireshark plugin in a production environment. I&#x27;ve developed and compiled a custom plugin for Linux (CentOS) following the steps in the Wireshark README files. The Wireshark development binary (version 1.10.14) will load the p...'''
date = "2016-07-21T13:10:00Z"
lastmod = "2016-07-28T09:24:00Z"
weight = 54230
keywords = [ "compile", "plugin", "linux" ]
aliases = [ "/questions/54230" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Compiled plugin loads with development build binary, but not release binary installed from yum repository](/questions/54230/compiled-plugin-loads-with-development-build-binary-but-not-release-binary-installed-from-yum-repository)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54230-score" class="post-score" title="current number of votes">0</div><span id="post-54230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark development and I'm having trouble loading my custom Wireshark plugin in a production environment. I've developed and compiled a custom plugin for Linux (CentOS) following the steps in the Wireshark README files. The Wireshark development binary (version 1.10.14) will load the plugin, however, if I copy the plugin to a production machine running Wireshark 1.10.14, it fails to load. I receive a message that tvb_length is not defined. I've tried setting/creating a "LD_LIBRARY_PATH" environment variable, running "ldconfig" command, installing wireshark-devel package, etc....with the same results. How do I compile the plugin so I can drop it in a machine running Wireshark 1.10.14 and get it to successfully load and find the necessary symbols. Do I need to configure the build using the command "./configure --enable-static"?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '16, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/c8d9b99aa59ee95888e89a41b5e55453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emucker&#39;s gravatar image" /><p><span>emucker</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emucker has no accepted answers">0%</span></p></div></div><div id="comments-container-54230" class="comments-container"></div><div id="comment-tools-54230" class="comment-tools"></div><div class="clear"></div><div id="comment-54230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54243"></span>

<div id="answer-container-54243" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54243-score" class="post-score" title="current number of votes">1</div><span id="post-54243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="emucker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you really, really sure your deployment system is running a 1.10 release?</p><p>In 1.10 <code>tvb_length()</code> was a function. Starting in 1.12 it became a macro and starting in 2.0 it went away completely.</p><p>The symptoms you're describing make it sound like you're compiling against 1.10.x (so your plugin is expecting a symbol with that name) but running against 1.12.y (where the symbol has been renamed).</p><p>One thing to check is what tvb*length functions your production libwireshark provides. Try:</p><pre><code>nm -D /path/to/libwireshark.so.* | grep tvb | grep length</code></pre><p>If you don't see <code>tvb_length</code> defined and it is 1.10.x then maybe CentOS picked up the patch that turned <code>tvb_length()</code> into a macro (IOW CentOS's 1.10.14 may not be exactly the same as ours--you'd have to check the source RPM to know for sure).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '16, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54243" class="comments-container"><span id="54304"></span><div id="comment-54304" class="comment"><div id="post-54304-score" class="comment-score"></div><div class="comment-text"><p>Thank you. This was the problem. Although the Wireshark version installed on CentOS 7 reports version 1.10.14, the actual call in the library is tvb_captured_length. Now that I know what is going on, I should be able to resolve it pretty quickly.</p></div><div id="comment-54304-info" class="comment-info"><span class="comment-age">(25 Jul '16, 08:54)</span> <span class="comment-user userinfo">emucker</span></div></div><span id="54406"></span><div id="comment-54406" class="comment"><div id="post-54406-score" class="comment-score"></div><div class="comment-text"><p>For supplemental information. To correct the problem I had to:</p><ol><li>Download the CentOS 7.2 sources rpm for wireshark 1.10.14</li><li>Extract patch files from the sources rpm</li><li>Apply the patches using the order specified in the wireshark.spec file included in the sources rpm</li><li>Rebuild wireshark and plugin with the patched code</li><li>Copied the plugin to the wireshark plugin directory and it successfully loaded.</li></ol></div><div id="comment-54406-info" class="comment-info"><span class="comment-age">(28 Jul '16, 09:24)</span> <span class="comment-user userinfo">emucker</span></div></div></div><div id="comment-tools-54243" class="comment-tools"></div><div class="clear"></div><div id="comment-54243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


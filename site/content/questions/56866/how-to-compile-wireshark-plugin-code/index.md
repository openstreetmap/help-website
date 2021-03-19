+++
type = "question"
title = "How to compile wireshark plugin code"
description = '''I am sorry for posting this very Basic question. I am totally new in wireshark developmet(actually Software development in General)... So far I have been succesfully following wireshark developers guide and have been able to build wireshark for both 32bit and 64bit(wireshark developers guide 2.2). N...'''
date = "2016-10-31T07:14:00Z"
lastmod = "2016-10-31T09:23:00Z"
weight = 56866
keywords = [ "compile", "windows", "dissector", "linux", "plugin" ]
aliases = [ "/questions/56866" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to compile wireshark plugin code](/questions/56866/how-to-compile-wireshark-plugin-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56866-score" class="post-score" title="current number of votes">0</div><span id="post-56866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sorry for posting this very Basic question. I am totally new in wireshark developmet(actually Software development in General)...</p><p>So far I have been succesfully following wireshark developers guide and have been able to build wireshark for both 32bit and 64bit(wireshark developers guide 2.2).</p><p>Now I'd like compile plugin from .c files and use them on wireshark. I have some source codes for custom plugin. But I couldn't find any direction in the developers guide about compiling them. For example - in which Directory to put the source code and which commands to use to compile them? where will I find my .dll plugin anfter compilation? where to put the .dll file to use it in wireshark?</p><p>Also, how do I compile the plugin source code in Ubunut, as later I have to compile it under Ubuntu and get the .so files.</p><p>Right now I have no Idea what to do with the code. I'd really appreciate the help.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '16, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-56866" class="comments-container"></div><div id="comment-tools-56866" class="comment-tools"></div><div class="clear"></div><div id="comment-56866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56868"></span>

<div id="answer-container-56868" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56868-score" class="post-score" title="current number of votes">1</div><span id="post-56868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The reference doc for plugins is in the source tree docs\README.plugins.</p><p>Note that if the plugin source code is from an older version then you'll have some work to do to modify the plugin to conform to the latest plugin and Wireshark interface standards. The best way to work out what needs to be done is to look at the source code of one of the "standard" plugins from the version your plugin was created for, e.g. 1.10, and then look at the current version of that same plugin.</p><p>When compiling on Ubuntu the instructions are much sparser, and I prefer using CMake rather than autotools as mentioned in the Dev Guide. I've successfully built using CMake, by running <code>sudo apt-get build-dep wireshark-dev</code> to pull in all the required libraries, then git clone the source and then run a CMake generation step, this time not specifying the generator (so it defaults to <code>make</code>), and then running <code>make</code> to build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '16, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56868" class="comments-container"><span id="56869"></span><div id="comment-56869" class="comment"><div id="post-56869-score" class="comment-score"></div><div class="comment-text"><p>Thanks as always. What is the specific command for CMake Generation step?</p></div><div id="comment-56869-info" class="comment-info"><span class="comment-age">(31 Oct '16, 08:42)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="56871"></span><div id="comment-56871" class="comment"><div id="post-56871-score" class="comment-score">1</div><div class="comment-text"><p>IT's been a while since I've done that, so don't have it direct to hand. but the one used on the Ubuntu build-bot is:</p><pre><code>cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_SYSCONFDIR=/etc -DCMAKE_INSTALL_LOCALSTATEDIR=/var -DENABLE_HTML_GUIDES=ON -DCMAKE_INSTALL_LIBDIR=/usr/lib/x86_64-linux-gnu -DBUILD_wireshark_gtk=ON</code></pre><p>This is in a build directly under the top-level source directory, I prefer to move the build out of the source tree, so the first argument to cmake should be the relative path to the sources.</p></div><div id="comment-56871-info" class="comment-info"><span class="comment-age">(31 Oct '16, 09:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56868" class="comment-tools"></div><div class="clear"></div><div id="comment-56868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


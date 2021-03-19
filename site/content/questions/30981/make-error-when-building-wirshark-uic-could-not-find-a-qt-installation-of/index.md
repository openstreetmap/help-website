+++
type = "question"
title = "Make error when building Wirshark : uic: could not find a Qt installation of &#x27;&#x27;"
description = '''Hi,  I am trying to build wireshark on ubuntu 12.04. I ran ./autogen.sh and ./configure. ./configure complained about uninstalled packages and I ran the following commands to get it work  pkg-config --libs --cflags Qt5Core  sudo apt-get install qt5-default qttools5-dev-tools  sudo apt-get install qt...'''
date = "2014-03-20T00:03:00Z"
lastmod = "2014-03-20T07:12:00Z"
weight = 30981
keywords = [ "qt", "wireshark" ]
aliases = [ "/questions/30981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Make error when building Wirshark : uic: could not find a Qt installation of ''](/questions/30981/make-error-when-building-wirshark-uic-could-not-find-a-qt-installation-of)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30981-score" class="post-score" title="current number of votes">0</div><span id="post-30981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to build wireshark on ubuntu 12.04.</p><p>I ran ./autogen.sh and ./configure.</p><p>./configure complained about uninstalled packages and I ran the following commands to get it work</p><pre><code> pkg-config --libs --cflags Qt5Core
 sudo apt-get install qt5-default qttools5-dev-tools
 sudo apt-get install qtdeclarative5-dev
 sudo aptitude install build-essential automake autoconf libgtk2.0-dev libglib2.0-dev libpcap0.8-dev flex bison
 sudo apt-get install build-essential automake autoconf libgtk2.0-dev libglib2.0-dev libpcap0.8-dev flex bison</code></pre><p>I then did a make and I am seeing this error:</p><p>uic: could not find a Qt installation of ''</p><p>Do I have to set any environment variables?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '14, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p><span>niks3089</span><br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-30981" class="comments-container"></div><div id="comment-tools-30981" class="comment-tools"></div><div class="clear"></div><div id="comment-30981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30989"></span>

<div id="answer-container-30989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30989-score" class="post-score" title="current number of votes">0</div><span id="post-30989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I ran into that problem last year. See: <a href="http://www.wireshark.org/lists/wireshark-dev/201306/msg00186.html">http://www.wireshark.org/lists/wireshark-dev/201306/msg00186.html</a></p><p>Give this a try:</p><pre><code>sudo apt-get install qt-devel</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-30989" class="comments-container"></div><div id="comment-tools-30989" class="comment-tools"></div><div class="clear"></div><div id="comment-30989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


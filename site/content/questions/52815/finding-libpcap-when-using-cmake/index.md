+++
type = "question"
title = "Finding libpcap when using CMake"
description = '''Hi,  I&#x27;m compiling from source on ARM based ubuntu (14.04) system similar to Raspberry Pi. I&#x27;ve hit the: tshark: This version of TShark was not built with support for capturing packets message and I&#x27;ve read that I must &quot;use --with-pcap option in your configure.&quot; I see the following files at the top ...'''
date = "2016-05-21T15:33:00Z"
lastmod = "2016-05-31T12:43:00Z"
weight = 52815
keywords = [ "cmake", "pcap" ]
aliases = [ "/questions/52815" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding libpcap when using CMake](/questions/52815/finding-libpcap-when-using-cmake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52815-score" class="post-score" title="current number of votes">0</div><span id="post-52815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm compiling from source on ARM based ubuntu (14.04) system similar to Raspberry Pi. I've hit the: tshark: This version of TShark was not built with support for capturing packets message and I've read that I must "use --with-pcap option in your configure."</p><p>I see the following files at the top level:</p><pre><code>$ ls -1 *conf*
INSTALL.configure
cmakeconfig.h.in
config.guess
config.h
config.h.win32
config.nmake
config.sub
configure.ac</code></pre><p>Where should I enable the use of pcap? Please be as specific as possible. Do I need to apt-get any other library for pcap?</p><p>I'm compiling by: cmake . &amp;&amp; make</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '16, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/02ff570891314a58db5b17db2cfb9d1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kupylin&#39;s gravatar image" /><p><span>kupylin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kupylin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '16, 15:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-52815" class="comments-container"><span id="52816"></span><div id="comment-52816" class="comment"><div id="post-52816-score" class="comment-score"></div><div class="comment-text"><p>Where did you read the statement that you must "use --with-pcap option in your configure."? That statement needs to be updated to handle CMake as well as autoconf; <code>--with-pcap</code> is an autoconf option, and doesn't apply if you're using CMake.</p></div><div id="comment-52816-info" class="comment-info"><span class="comment-age">(21 May '16, 15:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="52817"></span><div id="comment-52817" class="comment"><div id="post-52817-score" class="comment-score"></div><div class="comment-text"><p>Are you compiling <em>on</em> the ARM-based system to build a program to run on the same system, or are you compiling on some <em>other</em> system to produce a program to run on the ARM-based system, i.e. are you cross-compiling?</p></div><div id="comment-52817-info" class="comment-info"><span class="comment-age">(21 May '16, 15:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="53084"></span><div id="comment-53084" class="comment"><div id="post-53084-score" class="comment-score"></div><div class="comment-text"><p>Hi, I'm doing a native compilation on the ARM based system that I intend to run. My installed compiler is gcc 4.8.x. I'll get back to you on where the message to use cap came from.</p></div><div id="comment-53084-info" class="comment-info"><span class="comment-age">(31 May '16, 12:43)</span> <span class="comment-user userinfo">kupylin</span></div></div></div><div id="comment-tools-52815" class="comment-tools"></div><div class="clear"></div><div id="comment-52815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52818"></span>

<div id="answer-container-52818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52818-score" class="post-score" title="current number of votes">0</div><span id="post-52818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should get the libpcap development package libpcap0.8-dev. That provides you with the <strong>development</strong> files you need to compile using --with-pcap (which cmake should be able to find just fine actually).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '16, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '16, 16:00</strong> </span></p></div></div><div id="comments-container-52818" class="comments-container"><span id="52819"></span><div id="comment-52819" class="comment"><div id="post-52819-score" class="comment-score"></div><div class="comment-text"><p>At least if this is doing a native compile. The package might have some other name if they're cross-compiling.</p></div><div id="comment-52819-info" class="comment-info"><span class="comment-age">(21 May '16, 16:10)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="52820"></span><div id="comment-52820" class="comment"><div id="post-52820-score" class="comment-score"></div><div class="comment-text"><blockquote><p>That provides you with the development files you need to compile using --with-pcap (which cmake should be able to find just fine actually).</p></blockquote><p>Both CMake and autotools should find libpcap without any help if the development package is installed; no need for <code>--with-pcap=</code> with autotools or <code>-DCMAKE_PREFIX_PATH=</code> with CMake.</p></div><div id="comment-52820-info" class="comment-info"><span class="comment-age">(21 May '16, 16:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-52818" class="comment-tools"></div><div class="clear"></div><div id="comment-52818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


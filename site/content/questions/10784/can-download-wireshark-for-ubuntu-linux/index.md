+++
type = "question"
title = "Can Download Wireshark for Ubuntu Linux?"
description = '''Hi everyone! I use Ubuntu Linux and would like to download Wireshark. But in the list of Third-Party Packages, the link to download it for Ubuntu takes me to a page that says that Wireshark software does not exist for Ubuntu. (Here&#x27;s the link: http://packages.ubuntu.com/search?suite=all&amp;amp;searchon...'''
date = "2012-05-08T10:34:00Z"
lastmod = "2012-09-08T03:56:00Z"
weight = 10784
keywords = [ "linux", "ubuntu" ]
aliases = [ "/questions/10784" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can Download Wireshark for Ubuntu Linux?](/questions/10784/can-download-wireshark-for-ubuntu-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10784-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone! I use Ubuntu Linux and would like to download Wireshark. But in the list of Third-Party Packages, the link to download it for Ubuntu takes me to a page that says that Wireshark software does not exist for Ubuntu. (Here's the link: <a href="http://packages.ubuntu.com/search?suite=all&amp;searchon=names&amp;keywords=wireshark)">http://packages.ubuntu.com/search?suite=all&amp;searchon=names&amp;keywords=wireshark)</a></p><p>So does that mean it's not possible for me to download it for my computer? Or is there some other way?</p><p>Please note my knowledge of computers is only basic. Thank you so much to anyone who is willing to help me! :)</p><p>Stephanie.</p></div><div id="question-tags" class="tags-container tags">linux ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/5832ea5ef206ea8ca1258b4c6cd59963?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephanie&#39;s gravatar image" /><p>stephanie<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephanie has no accepted answers">0%</span></p></div></div><div id="comments-container-10784" class="comments-container"></div><div id="comment-tools-10784" class="comment-tools"></div><div class="clear"></div><div id="comment-10784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10785"></span>

<div id="answer-container-10785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10785-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>$ sudo apt-get install wireshark</code></pre><p>should download and install Wireshark for you*. The search page you give also fails to find other packages that I know to exist for Ubuntu (e.g. <code>build-essential</code>), so I would not believe it to be accurate at this time.</p><p>*It will probably not be the latest version, since the package repositories tend to lag behind a few releases, but if you absolutely <em>need</em> the latest version, you're better off building it yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-10785" class="comments-container"></div><div id="comment-tools-10785" class="comment-tools"></div><div class="clear"></div><div id="comment-10785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14135"></span>

<div id="answer-container-14135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14135-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I used to build Wireshark 1.8.2 from source. The version in the Ubuntu repository is ancient. Wireshark 1.8.2 has dissectors for MMS, GOOSE and Sampled Values.</p><p>1) Install GTK 2:</p><pre><code>apt-get install libgtk2.0-dev</code></pre><p><br />
2) Download the libpcap source<br />
3) In the source directory:</p><pre><code> ./configure
 make
 make install</code></pre><p>4) Download the wireshark source<br />
5) In the source directory:</p><pre><code> ./configure
 make
 make check
 make install</code></pre><p>6) Root privilege is needed to run wireshark - it needs access to network devices<br />
7) To run Wireshark from the Ubuntu application menu:</p><pre><code>  gksu wireshark</code></pre><p>8) To run wireshark from the command line:</p><pre><code> sudo wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '12, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/ecb2e988c82f65a83dd521fe9d90ede5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Neil%20Higgins&#39;s gravatar image" /><p>Neil Higgins<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Neil Higgins has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '12, 10:35</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-14135" class="comments-container"><span id="14141"></span><div id="comment-14141" class="comment"><div id="post-14141-score" class="comment-score"></div><div class="comment-text"><p>Running Wireshark as root is <strong>not</strong> recommended. Following the steps from another <a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">question</a>, you can setup your Ubuntu machine so that Wireshark properly lists the network devices without resorting to <code>sudo</code>.</p></div><div id="comment-14141-info" class="comment-info"><span class="comment-age">(08 Sep '12, 10:43)</span> helloworld</div></div><span id="18342"></span><div id="comment-18342" class="comment"><div id="post-18342-score" class="comment-score"></div><div class="comment-text"><p>(Sorry, I accidentally deleted the comment listing some other packages required to build from source, rather than my comment.)</p><p><em>If</em> you're going to build Wireshark from source, in order to get a newer version than 1.6.x, you'll also need:</p><p>flex, bison, autoconf, and possibly python</p><p>and you might also want:</p><p>zlib-devel, gnutls-devel, krb5-devel, libsmi-devel, GeoIP-devel, portaudio-devel, and lua-devel</p><p>to get to use all the features.</p><p><code>apt-get build-dep wireshark</code> might be a good way to get what you need (that'd be for 1.6.x, but that should work for 1.8.x).</p></div><div id="comment-18342-info" class="comment-info"><span class="comment-age">(05 Feb '13, 17:29)</span> Guy Harris ♦♦</div></div><span id="18343"></span><div id="comment-18343" class="comment"><div id="post-18343-score" class="comment-score"></div><div class="comment-text"><p>The only reason to download libpcap source is to build the latest libpcap or to link it with libnl (if linked with libnl, it should do a better job of handling monitor mode; it's not linked with libnl in the binary packages that come with Debian/Ubuntu/etc.).</p></div><div id="comment-18343-info" class="comment-info"><span class="comment-age">(05 Feb '13, 17:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14135" class="comment-tools"></div><div class="clear"></div><div id="comment-14135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10907"></span>

<div id="answer-container-10907" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10907-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use Synaptic Package Manager to find and install Wireshark - just search for "wireshark" in the search box.</p><p><a href="http://packages.ubuntu.com/search?suite=all&amp;searchon=names&amp;keywords=wireshark">The search package link</a> shows a number of packages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 15:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-10907" class="comments-container"></div><div id="comment-tools-10907" class="comment-tools"></div><div class="clear"></div><div id="comment-10907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


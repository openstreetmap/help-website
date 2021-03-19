+++
type = "question"
title = "can ./autogen.sh be skipped in wireshark build process"
description = '''Hi, I am trying to build wireshark 2.2.4 in linux Environment(cent os 6.3), the commands are:-./autogen.sh ./configure ./make to install:-make install I took source code directly from wireshark site. Now, My question is could i skip to execute ./autogen.sh. (because my build machine is having autoco...'''
date = "2017-04-25T03:11:00Z"
lastmod = "2017-05-03T04:46:00Z"
weight = 61030
keywords = [ "autoconf", "build", "autogen.sh" ]
aliases = [ "/questions/61030" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [can ./autogen.sh be skipped in wireshark build process](/questions/61030/can-autogensh-be-skipped-in-wireshark-build-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61030-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to build wireshark 2.2.4 in linux Environment(cent os 6.3), the commands are:-</p><pre><code>./autogen.sh
./configure
./make</code></pre>to install:-<pre><code>make install</code></pre>I took source code directly from wireshark site. Now, My question is could i skip to execute ./autogen.sh. (because my build machine is having autoconf 2.63, whereas to build wireshark2.2.4 ,autoconf 2.64 or later is needed and currently the autoconf cannot be changed as it's used many other modules)</div><div id="question-tags" class="tags-container tags">autoconf build autogen.sh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '17, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p>Abhisek<br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '17, 04:54</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-61030" class="comments-container"><span id="61033"></span><div id="comment-61033" class="comment"><div id="post-61033-score" class="comment-score"></div><div class="comment-text"><p>What source code did you take? git clone? From where, and which branch? tarball? Other?</p></div><div id="comment-61033-info" class="comment-info"><span class="comment-age">(25 Apr '17, 04:55)</span> Jaap ♦</div></div><span id="61085"></span><div id="comment-61085" class="comment"><div id="post-61085-score" class="comment-score"></div><div class="comment-text"><p>it's a tarball (wireshark-2.2.4.tar.bz2).</p></div><div id="comment-61085-info" class="comment-info"><span class="comment-age">(27 Apr '17, 23:29)</span> Abhisek</div></div></div><div id="comment-tools-61030" class="comment-tools"></div><div class="clear"></div><div id="comment-61030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61040"></span>

<div id="answer-container-61040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61040-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As hinted at by Jaap's comment, it is possible to avoid running ./autogen.sh: the way to do it is to download Wireshark's source code as a tarball (e.g., from <a href="https://www.wireshark.org/download/src/">here</a>). Those source tarballs have already had ./autogen.sh run on them (it's part of the <code>make dist</code> process in the world of autofoo).</p><p>Note that this won't work, however, if you need to modify Wireshark in certain ways (e.g., to add dissectors).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '17, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-61040" class="comments-container"><span id="61086"></span><div id="comment-61086" class="comment"><div id="post-61086-score" class="comment-score"></div><div class="comment-text"><p>I actually tried without ./autogen.sh and build is successful. Thanks. But, If i want to add dissectors in epan/dissectors directory and update that directory makefile accordingly, then why i need autogen.sh in build process?</p></div><div id="comment-61086-info" class="comment-info"><span class="comment-age">(27 Apr '17, 23:32)</span> Abhisek</div></div><span id="61091"></span><div id="comment-61091" class="comment"><div id="post-61091-score" class="comment-score"></div><div class="comment-text"><p>You may get away with that. Note that because Makefile is generated from Makefile.am you should make sure to add them there as well.</p></div><div id="comment-61091-info" class="comment-info"><span class="comment-age">(28 Apr '17, 01:47)</span> Jaap ♦</div></div><span id="61188"></span><div id="comment-61188" class="comment"><div id="post-61188-score" class="comment-score"></div><div class="comment-text"><p>I tried to skip ./autogen.sh step by ./configure ./make ./make clean ./make install</p><p>but getting error when i am modifying makefile.am and that time geeting error in make clean &amp; make failied ( error missing automake &lt;version&gt;).</p><p>Any alternatives so that i can change makefile.am and ./autogen.sh is not needed.</p><p>Please help.</p></div><div id="comment-61188-info" class="comment-info"><span class="comment-age">(03 May '17, 03:55)</span> Abhisek</div></div><span id="61190"></span><div id="comment-61190" class="comment not_top_scorer"><div id="post-61190-score" class="comment-score"></div><div class="comment-text"><p>"currently the autoconf cannot be changed as it's used many other modules)" would changing it really affect the other modules adversely?</p></div><div id="comment-61190-info" class="comment-info"><span class="comment-age">(03 May '17, 03:59)</span> Anders ♦</div></div><span id="61194"></span><div id="comment-61194" class="comment not_top_scorer"><div id="post-61194-score" class="comment-score"></div><div class="comment-text"><p>Ok basically the machine is having wireshark 1.10.6, wireshark 1.12.8 also. Current autoconf version 2.63. This autoconf is good enough for WS1.10.6 and WS 1.12.8, but not for 2.2.4. So if we change autoconf to 2.64 or later, does it affect WS1.10.6 and WS1.12.8 build process?</p></div><div id="comment-61194-info" class="comment-info"><span class="comment-age">(03 May '17, 04:38)</span> Abhisek</div></div><span id="61197"></span><div id="comment-61197" class="comment"><div id="post-61197-score" class="comment-score">1</div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/22953/abhisek">@Abhisek</a> You can upgrade to autoconf 2.64 without issues, 1.10.z and 1.12.z should continue to work with that newer version.</p></div><div id="comment-61197-info" class="comment-info"><span class="comment-age">(03 May '17, 04:58)</span> Lekensteyn</div></div><span id="61214"></span><div id="comment-61214" class="comment"><div id="post-61214-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>getting error when i am modifying makefile.am ... make failied ( error missing automake &lt;version&gt;).</p></blockquote><p>If you modify Makefile.am, you <em>must</em> have automake (that's the program that turns Makefile.am into Makefile.in) and you <em>must</em> run automake to rebuild Makefile.in. You're best advised to run ./autogen.sh, because it runs automaker and autoconf for you.</p></div><div id="comment-61214-info" class="comment-info"><span class="comment-age">(03 May '17, 11:49)</span> Guy Harris ♦♦</div></div><span id="61249"></span><div id="comment-61249" class="comment not_top_scorer"><div id="post-61249-score" class="comment-score"></div><div class="comment-text"><p>autoconf 2.69 is installed.So now ./autogen.sh is being executed. Now build for 2.2.4 is done as well as 1.10.x &amp; 1.12.y. So no problem with autoconf latest version. Thanks all.</p></div><div id="comment-61249-info" class="comment-info"><span class="comment-age">(05 May '17, 02:49)</span> Abhisek</div></div></div><div id="comment-tools-61040" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-61040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61195"></span>

<div id="answer-container-61195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61195-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As alternative to autotools, you can try CMake. CentOS 6 includes CMake 2.8.12.2 while the current minimum required CMake version is 2.8.8.</p><p>No "autogen.sh" step is needed for CMake. Here are the recommended steps (assuming you are in the Wireshark source tree):</p><pre><code>mkdir build
cd build
cmake ..
make
make install</code></pre><p>For more information, see the README.cmake file in the top of the source tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-61195" class="comments-container"><span id="61196"></span><div id="comment-61196" class="comment"><div id="post-61196-score" class="comment-score"></div><div class="comment-text"><p>Ok basically the machine is having wireshark 1.10.6, wireshark 1.12.8 also. Current autoconf version 2.63. This autoconf is good enough for WS1.10.6 and WS 1.12.8, but not for 2.2.4. So if we change autoconf to 2.64 or later, does it affect WS1.10.6 and WS1.12.8 build process?</p></div><div id="comment-61196-info" class="comment-info"><span class="comment-age">(03 May '17, 04:55)</span> Abhisek</div></div><span id="61198"></span><div id="comment-61198" class="comment"><div id="post-61198-score" class="comment-score"></div><div class="comment-text"><p>(Replied to the other post; if you use CMake then the autoconf version is totally irrelevant as it is not used.)</p></div><div id="comment-61198-info" class="comment-info"><span class="comment-age">(03 May '17, 04:59)</span> Lekensteyn</div></div><span id="61199"></span><div id="comment-61199" class="comment"><div id="post-61199-score" class="comment-score"></div><div class="comment-text"><p>But Cmake will use Qt, whereas we need gtk3 only. Please correct me if i am wrong.</p></div><div id="comment-61199-info" class="comment-info"><span class="comment-age">(03 May '17, 05:16)</span> Abhisek</div></div><span id="61200"></span><div id="comment-61200" class="comment"><div id="post-61200-score" class="comment-score"></div><div class="comment-text"><p>Both CMake and autotools try to enable Qt, but if you prefer GTK+ 3 only (not recommended), use <code>cmake -DBUILD_wireshark=0 -DBUILD_wireshark_gtk=1 -DENABLE_GTK3=1</code>. You can see all available options using the <code>ccmake .</code> command in the build directory or <code>cmake-gui .</code> (for a graphical window).</p></div><div id="comment-61200-info" class="comment-info"><span class="comment-age">(03 May '17, 05:22)</span> Lekensteyn</div></div></div><div id="comment-tools-61195" class="comment-tools"></div><div class="clear"></div><div id="comment-61195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


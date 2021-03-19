+++
type = "question"
title = "Not Able to launch Wireshark on Yosemite"
description = '''Hi, I was using Mavericks on my mac machine and wireshark was running fine on it. Now i updated mavericks to it to Yosemite 10.10. but after updating OS i am not able to launch Wireshark.  I tried both GUI way as well as terminal way but the result is same, Wireshark icon flashes in dock and then go...'''
date = "2014-09-03T23:10:00Z"
lastmod = "2014-09-16T10:04:00Z"
weight = 35986
keywords = [ "yosemite" ]
aliases = [ "/questions/35986" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Not Able to launch Wireshark on Yosemite](/questions/35986/not-able-to-launch-wireshark-on-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was using Mavericks on my mac machine and wireshark was running fine on it. Now i updated mavericks to it to Yosemite 10.10. but after updating OS i am not able to launch Wireshark.</p><p>I tried both GUI way as well as terminal way but the result is same, Wireshark icon flashes in dock and then goes away.</p><p>Please help if any one has launched wireshark on Yosemite.</p><p>I removed Wireshark and then re-installed latest version (1.12.0) but no success.</p><p>Thanks in Advance :)</p></div><div id="question-tags" class="tags-container tags">yosemite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '14, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/0d7e788bbafa60b56ea3a534b74db1de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amit1010&#39;s gravatar image" /><p>Amit1010<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amit1010 has no accepted answers">0%</span></p></div></div><div id="comments-container-35986" class="comments-container"><span id="36034"></span><div id="comment-36034" class="comment"><div id="post-36034-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem.</p></div><div id="comment-36034-info" class="comment-info"><span class="comment-age">(05 Sep '14, 12:46)</span> THN</div></div></div><div id="comment-tools-35986" class="comment-tools"></div><div class="clear"></div><div id="comment-35986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36046"></span>

<div id="answer-container-36046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36046-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Xquartz reinstalation has solved the problem for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '14, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/6c6309e8188537cc34e15025030ed93d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="THN&#39;s gravatar image" /><p>THN<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="THN has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '14, 14:31</p></div></div><div id="comments-container-36046" class="comments-container"></div><div id="comment-tools-36046" class="comment-tools"></div><div class="clear"></div><div id="comment-36046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36369"></span>

<div id="answer-container-36369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like as part of the Yosemite install; its installer moves all "foreign" files from /usr to /opt - so you end up with X11 in /opt/X11 rather than /usr/X11. I've just reinstalled X11 and it is working now; but it may be that simply a move of /opt/X11 to /usr/X11 will resolve the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/17a32b94d7481cc6918620428350c5cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OddParityBit&#39;s gravatar image" /><p>OddParityBit<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OddParityBit has no accepted answers">0%</span></p></div></div><div id="comments-container-36369" class="comments-container"><span id="36382"></span><div id="comment-36382" class="comment"><div id="post-36382-score" class="comment-score"></div><div class="comment-text"><p>The standard location for Xquartz is under <code>/opt</code>; it's not under <code>/usr</code> because it's not a component of OS X, it's a third-party component (although the "third party" in this case happens to be Apple Inc.). Starting with Mountain Lion, Apple didn't ship X11 as a standard OS component; instead, they offered it through Mac OS Forge. <code>/usr/X11</code>, on Mountain Lion and later, should be a symbolic link to <code>/opt/X11</code>, and Xquartz should be installed in <code>/opt/X11</code>.</p></div><div id="comment-36382-info" class="comment-info"><span class="comment-age">(16 Sep '14, 17:44)</span> Guy Harris ♦♦</div></div><span id="36392"></span><div id="comment-36392" class="comment"><div id="post-36392-score" class="comment-score">1</div><div class="comment-text"><p>Ar, OK. So, the Yosemite installer deleted the symlink between /opt/X11 and /usr/X11; which my re-install of Xquartz restored.</p><p>So, the post-Yosemite fix is likely just "ln -s /opt/X11 /usr/X11"...</p></div><div id="comment-36392-info" class="comment-info"><span class="comment-age">(16 Sep '14, 22:22)</span> OddParityBit</div></div><span id="37375"></span><div id="comment-37375" class="comment"><div id="post-37375-score" class="comment-score">1</div><div class="comment-text"><p>@OddParityBit this worked for me: <code>ln -s /opt/X11 /usr/X11</code>. I didn't reinstall</p></div><div id="comment-37375-info" class="comment-info"><span class="comment-age">(27 Oct '14, 12:41)</span> bhaveshpatel</div></div><span id="37379"></span><div id="comment-37379" class="comment"><div id="post-37379-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, the Yosemite installer deleted the symlink between /opt/X11 and /usr/X11</p></blockquote><p>Probably. I guess it discards <code>/usr</code> and installs the Yosemite version in its place, although <a href="https://jimlindley.com/blog/yosemite-upgrade-homebrew-tips/">supposedly it at least preserves <em>some</em> stuff under <code>/usr</code></a>; perhaps <code>/usr/X11</code> isn't something it preserves. (Just <code>/usr/local</code>?)</p></div><div id="comment-37379-info" class="comment-info"><span class="comment-age">(27 Oct '14, 14:28)</span> Guy Harris ♦♦</div></div><span id="39755"></span><div id="comment-39755" class="comment"><div id="post-39755-score" class="comment-score"></div><div class="comment-text"><p>i have try everything you said and write without sucess. Can anyone help me:</p><p>I have instaled Xquartz, and wireshark. The wireshark ask me to find the X11, i do that, and the only thing that happens, is the X11 terminal that open.</p><p>Thanks in advance. alfredo Almeida</p></div><div id="comment-39755-info" class="comment-info"><span class="comment-age">(10 Feb '15, 03:08)</span> Introvertido</div></div><span id="42122"></span><div id="comment-42122" class="comment not_top_scorer"><div id="post-42122-score" class="comment-score"></div><div class="comment-text"><p>I am having the same problem, reinstalled both X11 and wireshark as the link didn't work, still unable to load wireshark after several attempts.</p><p>If I run from command line I get this -</p><pre><code>2015-05-06 11:09:18.801 defaults[1551:7511] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2015-05-06 11:09:18.809 defaults[1552:7516] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist
dyld: Library not loaded: /usr/X11/lib/libcairo.2.dylib
  Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
  Reason: image not found
Trace/BPT trap: 5</code></pre><p>any further suggestions??</p></div><div id="comment-42122-info" class="comment-info"><span class="comment-age">(06 May '15, 03:22)</span> dalbone</div></div><span id="42149"></span><div id="comment-42149" class="comment not_top_scorer"><div id="post-42149-score" class="comment-score"></div><div class="comment-text"><p>If <code>/opt/X11</code> doesn't exist, the X11 installation didn't work.</p><p>If <code>/opt/X11</code> does exist, but <code>/usr/X11</code> doesn't exist, do <code>sudo ln -s /opt/X11 /usr/X11</code>.</p><p>If <code>/opt/X11</code> does exist, and <code>/usr/X11</code> is a symbolic link to it (<code>ls -l /usr/X11</code> reports it as a symlink to <code>/opt/X11</code>), then do <code>ls -l /opt/X11/lib/libcairo*</code> and report what it says.</p><p>If <code>/opt/X11</code> does exist, and <code>/usr/X11</code> exists but is <em>not</em> a symbolic link to <code>/opt/X11</code>, try removing it with <code>sudo rm -rf /usr/X11</code> and then doing <code>sudo ln -s /opt/X11 /usr/X11</code>.</p></div><div id="comment-42149-info" class="comment-info"><span class="comment-age">(06 May '15, 10:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36369" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-36369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


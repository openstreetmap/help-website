+++
type = "question"
title = "How to install CSG2 plugin"
description = '''Hi, I would like to know how to add or install plugin for CSG2 in my wireshark. Below are my wireshark version. Thanks. Version 1.6.4 (SVN Rev 39941 from /trunk-1.6) Copyright 1998-2011 Gerald Combs gerald@wireshark.org and contributors. This is free software; see the source for copying conditions. ...'''
date = "2012-05-29T18:34:00Z"
lastmod = "2012-05-29T22:47:00Z"
weight = 11456
keywords = [ "development", "mac", "plugin" ]
aliases = [ "/questions/11456" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to install CSG2 plugin](/questions/11456/how-to-install-csg2-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know how to add or install plugin for CSG2 in my wireshark. Below are my wireshark version. Thanks.</p><p>Version 1.6.4 (SVN Rev 39941 from /trunk-1.6)</p><p>Copyright 1998-2011 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.5, with GLib 2.29.8, with libpcap 1.1.1, with libz 1.2.3, without POSIX capabilities, without libpcre, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS 2.12.7, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Sep 30 2011 11:17:29), without AirPcap.</p><p>Running on Mac OS 10.7.4 (Darwin 11.4.0), with libpcap version 1.1.1, with libz 1.2.5, GnuTLS 2.12.7, Gcrypt 1.4.6.</p><p>Built using gcc 4.2.1 (Apple Inc. build 5666) (dot 3).</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p></div><div id="question-tags" class="tags-container tags">development mac plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/bd37a6c0f1e16ceb70a1e9c8ca5b6f23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunn&#39;s gravatar image" /><p>sunn<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 May '12, 20:16</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11456" class="comments-container"></div><div id="comment-tools-11456" class="comment-tools"></div><div class="clear"></div><div id="comment-11456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11459"></span>

<div id="answer-container-11459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11459-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html#id36146034">developer's guide</a>, <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/doc/README.developer?revision=37146&amp;view=markup">README.developer</a>, <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/doc/README.plugins?revision=37146&amp;view=markup">README.plugins</a> and <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/README.macos?revision=37146&amp;view=markup">README.macos</a> should get you started, and there are plenty of <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/plugins/">existing plugins</a> available to help you as well, not to mention <a href="http://ask.wireshark.org/">this</a> site and the Wireshark developer's <a href="http://www.wireshark.org/lists/">mailing list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11459" class="comments-container"><span id="11484"></span><div id="comment-11484" class="comment"><div id="post-11484-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys!!!</p></div><div id="comment-11484-info" class="comment-info"><span class="comment-age">(31 May '12, 00:45)</span> sunn</div></div></div><div id="comment-tools-11459" class="comment-tools"></div><div class="clear"></div><div id="comment-11459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11462"></span>

<div id="answer-container-11462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11462-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is an open bug request for CSG2. Plugin/Dissector code exists, however it is not yet included into the official code, as some requirements did not match and have never been resolved !?!</p><blockquote><p><code>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6153</code></p></blockquote><p>So, no CSG2 support, until that patch get's included.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11462" class="comments-container"></div><div id="comment-tools-11462" class="comment-tools"></div><div class="clear"></div><div id="comment-11462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


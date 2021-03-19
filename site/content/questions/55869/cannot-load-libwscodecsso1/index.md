+++
type = "question"
title = "cannot load libwscodecs.so.1"
description = '''I just linstalled wireshark 2.2 for linux and now get the following message when trying to run wireshark as any user, including root.  Wireshark: error while loading shared libraries: libwscodecs.so.1: cannot open shared object file: no such file or directory.  I ran ./confirure, make and make insta...'''
date = "2016-09-26T11:23:00Z"
lastmod = "2016-09-26T11:23:00Z"
weight = 55869
keywords = [ "libraries", "linux" ]
aliases = [ "/questions/55869" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot load libwscodecs.so.1](/questions/55869/cannot-load-libwscodecsso1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55869-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just linstalled wireshark 2.2 for linux and now get the following message when trying to run wireshark as any user, including root.</p><p>Wireshark: error while loading shared libraries: libwscodecs.so.1: cannot open shared object file: no such file or directory.</p><p>I ran ./confirure, make and make install without any errors.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">libraries linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/c55a2415a2e26ce60bcc15bda115362b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanHicks76&#39;s gravatar image" /><p>DanHicks76<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanHicks76 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '16, 13:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55869" class="comments-container"><span id="55876"></span><div id="comment-55876" class="comment"><div id="post-55876-score" class="comment-score"></div><div class="comment-text"><p>"Installed" as in "downloaded the source and ran ./configure, make, and make install", rather than "installed" as in "installed my Linux distribution's binary package"?</p></div><div id="comment-55876-info" class="comment-info"><span class="comment-age">(26 Sep '16, 13:40)</span> Guy Harris ♦♦</div></div><span id="55879"></span><div id="comment-55879" class="comment"><div id="post-55879-score" class="comment-score"></div><div class="comment-text"><p>I downloaded and untared the linux wireshark-2.2.0.tar.bz2 file than ran 'sudo ./configure &amp;&amp; make &amp;&amp; make install'</p></div><div id="comment-55879-info" class="comment-info"><span class="comment-age">(26 Sep '16, 13:57)</span> DanHicks76</div></div><span id="55880"></span><div id="comment-55880" class="comment"><div id="post-55880-score" class="comment-score"></div><div class="comment-text"><p>So you're running the installed Wireshark, either from the command line (<code>/usr/local/bin/wireshark</code>) or by launching it from the GUI?</p><p>What happens if you run <code>sudo /sbin/ldconfig</code> and then try running Wireshark?</p></div><div id="comment-55880-info" class="comment-info"><span class="comment-age">(26 Sep '16, 14:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-55869" class="comment-tools"></div><div class="clear"></div><div id="comment-55869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


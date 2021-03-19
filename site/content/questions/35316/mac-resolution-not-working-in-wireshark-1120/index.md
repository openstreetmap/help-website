+++
type = "question"
title = "MAC resolution not working in Wireshark 1.12.0"
description = '''Under Ubuntu 14.04, MAC manufacturer resolution (e.g. mapping 00:09:5b:01:02:03 → Netgear_01:02:03) works fine when using the version from the repositories. However, I wanted to use the latest wireshark version so installed from source. Configure options are: ./configure --enable-dumpcap --enable-se...'''
date = "2014-08-07T17:50:00Z"
lastmod = "2014-08-22T06:19:00Z"
weight = 35316
keywords = [ "manuf", "mac", "resolution", "install", "wireshark" ]
aliases = [ "/questions/35316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC resolution not working in Wireshark 1.12.0](/questions/35316/mac-resolution-not-working-in-wireshark-1120)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35316-score" class="post-score" title="current number of votes">0</div><span id="post-35316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under Ubuntu 14.04, MAC manufacturer resolution (e.g. mapping 00:09:5b:01:02:03 → Netgear_01:02:03) works fine when using the version from the repositories.</p><p>However, I wanted to use the latest wireshark version so installed from source. Configure options are:</p><pre><code>./configure --enable-dumpcap --enable-setcap-install --with-dumpcap-group=wireshark --prefix=/usr --sysconfdir=/etc</code></pre><p>But following installation, MAC resolution does not work despite being enabled. Build is fine and presents in both Wireshark (QT5, GTK3 build) and TShark.</p><p>This is true for both normal MAC fields (e.g. wlan.sa) as well as those with the new "_resolved" extension (wlan.sa_resolved). My manuf file (as provided from the wireshark website) is located in <em>/etc/</em>. The problem still persists even if I try alternative locations including <em>/usr/share/wireshark/</em>, <em>/usr/local/share/wirshsark/</em> or <em>~/.wireshark/</em>.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-manuf" rel="tag" title="see questions tagged &#39;manuf&#39;">manuf</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '14, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/0e31e8af1a1ab93b4fedfd17a1bbb48d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ebafaux&#39;s gravatar image" /><p><span>ebafaux</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ebafaux has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '14, 16:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35316" class="comments-container"><span id="35670"></span><div id="comment-35670" class="comment"><div id="post-35670-score" class="comment-score"></div><div class="comment-text"><p>Was using 1.12.0 and noticed Layer 2 captures were no longer showing name resolution either. Removed 1.12.0 and went back to 1.10.9 and everything's fine again. BOO! :-)</p></div><div id="comment-35670-info" class="comment-info"><span class="comment-age">(22 Aug '14, 06:19)</span> <span class="comment-user userinfo">obgmugen</span></div></div></div><div id="comment-tools-35316" class="comment-tools"></div><div class="clear"></div><div id="comment-35316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35322"></span>

<div id="answer-container-35322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35322-score" class="post-score" title="current number of votes">0</div><span id="post-35322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open the Wireshark Help dialog and look in the "Folders" tab for the locations of the "Personal Configuration" and "Global Configuration" folders. The file "manuf" should be in one of those locations to work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '14, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35322" class="comments-container"><span id="35376"></span><div id="comment-35376" class="comment"><div id="post-35376-score" class="comment-score"></div><div class="comment-text"><p>I just installed wireshark 1.12.0 on win7 and mac resolution doesn't work anymore, reverted back to 1.10.9 everything is ok. Did not modify the existing manuf that comes with the installation ...</p></div><div id="comment-35376-info" class="comment-info"><span class="comment-age">(10 Aug '14, 07:38)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="35377"></span><div id="comment-35377" class="comment"><div id="post-35377-score" class="comment-score"></div><div class="comment-text"><p>I can confirm that for Version 1.12.0-rc2-125-g8a47b3a</p></div><div id="comment-35377-info" class="comment-info"><span class="comment-age">(10 Aug '14, 07:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35378"></span><div id="comment-35378" class="comment"><div id="post-35378-score" class="comment-score">2</div><div class="comment-text"><p>I believe this bug (regression) was very recently fixed...</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10344">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10344</a></p><p><a href="https://code.wireshark.org/review/#/c/3522/">https://code.wireshark.org/review/#/c/3522/</a></p></div><div id="comment-35378-info" class="comment-info"><span class="comment-age">(10 Aug '14, 08:11)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-35322" class="comment-tools"></div><div class="clear"></div><div id="comment-35322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


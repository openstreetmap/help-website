+++
type = "question"
title = "Owner of /Library/Application Support/Wireshark is not root"
description = '''I&#x27;ve noticed that on both of my Macs, user of &quot;/Library/Application Support/Wireshark&quot; is user 504. ls -als /Library/Application&#92; Support/ 0 drwx------ 4 504 wheel 136 Sep 24 18:45 Wireshark  Is it a normal behavior or it should be root? Can it interfere when the plist &quot;/Library/LaunchDaemons/org.wi...'''
date = "2015-11-12T03:35:00Z"
lastmod = "2015-11-12T03:35:00Z"
weight = 47541
keywords = [ "osx", "chmodbpf", "permission" ]
aliases = [ "/questions/47541" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Owner of /Library/Application Support/Wireshark is not root](/questions/47541/owner-of-libraryapplication-supportwireshark-is-not-root)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47541-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've noticed that on both of my Macs, user of "/Library/Application Support/Wireshark" is user 504.</p><pre><code>ls -als /Library/Application\ Support/
0 drwx------   4 504   wheel   136 Sep 24 18:45 Wireshark</code></pre><p>Is it a normal behavior or it should be root?</p><p>Can it interfere when the plist "/Library/LaunchDaemons/org.wireshark.ChmodBPF.plist" wants to launch "/Library/Application Support/Wireshark/ChmodBPF/ChmodBPF" on startup?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">osx chmodbpf permission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '15, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-47541" class="comments-container"></div><div id="comment-tools-47541" class="comment-tools"></div><div class="clear"></div><div id="comment-47541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "Can I limit name resolution to only use Wireshark&#x27;s own hosts file?"
description = '''I would like to enable network name resolution but only allow Wireshark to use its hosts file in %WIRESHARK%&#92;hosts, or %APPDATA%&#92;Wireshark&#92;hostsdisable. It appears that when I enable network name resolution in preferences then it enables name reslution using, DNS, the windows hosts file, and the Wir...'''
date = "2010-09-14T22:11:00Z"
lastmod = "2010-09-15T00:07:00Z"
weight = 78
keywords = [ "name-resolving", "dns" ]
aliases = [ "/questions/78" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I limit name resolution to only use Wireshark's own hosts file?](/questions/78/can-i-limit-name-resolution-to-only-use-wiresharks-own-hosts-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-78-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to enable network name resolution but only allow Wireshark to use its hosts file in %WIRESHARK%\hosts, or %APPDATA%\Wireshark\hostsdisable. It appears that when I enable network name resolution in preferences then it enables name reslution using, DNS, the windows hosts file, and the Wireshark hosts file. I often analyze very large captures from a private network while I'm attached to my corporate network, I do have a large wireshark hosts file but there are many addresses for which I do not have an entry, Wireshark resorts to DNS to attempt to resolve these names and it takes a very long time since many are not reachable and result in a timeout before proceeding. Dos anyone know if there is a way to disable DNS network name resolution while at the same time allowing network name resolution using the Wireshark hosts file?</p><p>Thanks for any help!!</p></div><div id="question-tags" class="tags-container tags">name-resolving dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '10, 22:11</strong></p><img src="https://secure.gravatar.com/avatar/2a5329d1ad6dae528190cad17e273fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saninim&#39;s gravatar image" /><p>Saninim<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saninim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '12, 18:35</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-78" class="comments-container"></div><div id="comment-tools-78" class="comment-tools"></div><div class="clear"></div><div id="comment-78-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="80"></span>

<div id="answer-container-80" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-80-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you want isn't possible, currently, but shouldn't be required. If you check <em>Enable concurrent DNS name resolution</em> in the name resolution preferences the DNS name resolving takes place without blocking further operation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-80" class="comments-container"><span id="87"></span><div id="comment-87" class="comment"><div id="post-87-score" class="comment-score"></div><div class="comment-text"><p>According to <a href="http://c-ares.haxx.se/ares_init.html">http://c-ares.haxx.se/ares_init.html</a> we can force the use of the local hosts file using <code>ARES_OPT_LOOKUPS</code>. Unfortunately there doesn't seem to be a way to get there. The code that parses the <code>RES_OPTIONS</code> environment variable doesn't provide an option for this, and we don't provide a way to set the flags within Wireshark. This should probably be a <a href="http://wiki.wireshark.org/WishList#Name_resolution">wishlist</a> item in Bugzilla.</p></div><div id="comment-87-info" class="comment-info"><span class="comment-age">(15 Sep '10, 10:36)</span> Gerald Combs ♦♦</div></div><span id="12040"></span><div id="comment-12040" class="comment"><div id="post-12040-score" class="comment-score"></div><div class="comment-text"><p>I added it to the wishlist.</p></div><div id="comment-12040-info" class="comment-info"><span class="comment-age">(18 Jun '12, 21:03)</span> cmaynard ♦♦</div></div><span id="12049"></span><div id="comment-12049" class="comment"><div id="post-12049-score" class="comment-score"></div><div class="comment-text"><p>I added a Bug report :-) <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380</a></p></div><div id="comment-12049-info" class="comment-info"><span class="comment-age">(19 Jun '12, 01:42)</span> Anders ♦</div></div><span id="12562"></span><div id="comment-12562" class="comment"><div id="post-12562-score" class="comment-score">2</div><div class="comment-text"><p>For the record, the bug is pretty much implemented (although the bug is still open). I also moved the WishList item to the Done section.</p></div><div id="comment-12562-info" class="comment-info"><span class="comment-age">(10 Jul '12, 08:25)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-80" class="comment-tools"></div><div class="clear"></div><div id="comment-80-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


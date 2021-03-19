+++
type = "question"
title = "Wireshark for Solaris Issue: g_int64_hash"
description = '''I installed wireshark and all of its dependencies for Solaris 10. However, when I try to open it, I get the following error: ld.so.1: wireshark: fatal: relocation error: file /opt/csw/lib/sparcv8/libwireshark.so.5: symbol g_int64_hash: referenced symbol not found Do you know the cause of this issue?...'''
date = "2017-02-10T13:24:00Z"
lastmod = "2017-02-19T13:58:00Z"
weight = 59338
keywords = [ "glib", "g_int64_hash", "solaris" ]
aliases = [ "/questions/59338" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark for Solaris Issue: g\_int64\_hash](/questions/59338/wireshark-for-solaris-issue-g_int64_hash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59338-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed wireshark and all of its dependencies for Solaris 10. However, when I try to open it, I get the following error:</p><p>ld.so.1: wireshark: fatal: relocation error: file /opt/csw/lib/sparcv8/libwireshark.so.5: symbol g_int64_hash: referenced symbol not found</p><p>Do you know the cause of this issue? Is this related to glib? Other sites mentioned updating glib to version 2.22 or later, where this installation appears to be 2.0. If so, is that package available for download?</p></div><div id="question-tags" class="tags-container tags">glib g_int64_hash solaris</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '17, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/8dc6b4c7ebe76f59681e830e6b1c691a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sewalters&#39;s gravatar image" /><p>sewalters<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sewalters has no accepted answers">0%</span></p></div></div><div id="comments-container-59338" class="comments-container"></div><div id="comment-tools-59338" class="comment-tools"></div><div class="clear"></div><div id="comment-59338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59339"></span>

<div id="answer-container-59339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59339-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you <a href="https://developer.gnome.org/glib/stable/glib-Hash-Tables.html#g-int64-hash">look here</a> you'll see they are correct; this function requires Glib version 2.22.</p><p>I've found a reference <a href="https://www.opencsw.org/package/glib2/">here</a> but I'm no expert on Solaris, so this may not be the right one for you. At least it tell's there are suitable packages/libraries out there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '17, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59339" class="comments-container"><span id="59392"></span><div id="comment-59392" class="comment"><div id="post-59392-score" class="comment-score"></div><div class="comment-text"><p>Based on <a href="https://wiki.wireshark.org/Development/Support_library_version_tracking,">https://wiki.wireshark.org/Development/Support_library_version_tracking,</a> Wireshark 2.0 and 2.2 should still work with GLib 2.14. For older versions, the files epan/g_int64_hash_routines.c (and .h) were introduced in v1.99.3rc0-165-gcfb1bc3bb4. If not, then it is likely a bug. @sewalters what Wireshark version were you trying to build?</p></div><div id="comment-59392-info" class="comment-info"><span class="comment-age">(13 Feb '17, 17:02)</span> Lekensteyn</div></div></div><div id="comment-tools-59339" class="comment-tools"></div><div class="clear"></div><div id="comment-59339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59541"></span>

<div id="answer-container-59541" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59541-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Updating Glib to version 2.22 successfully fixed my issue. I was able to retrieve the file from the link provided (OpenCSW). I was confusing Glib with libglib (thinking they were the same), which contributed to my problem! Thanks for the assistance!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '17, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/8dc6b4c7ebe76f59681e830e6b1c691a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sewalters&#39;s gravatar image" /><p>sewalters<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sewalters has no accepted answers">0%</span></p></div></div><div id="comments-container-59541" class="comments-container"></div><div id="comment-tools-59541" class="comment-tools"></div><div class="clear"></div><div id="comment-59541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


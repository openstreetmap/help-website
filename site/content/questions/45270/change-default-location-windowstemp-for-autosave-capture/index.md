+++
type = "question"
title = "Change default location windows/temp for autosave capture"
description = '''How do you change the wireshark default location of Windows/Temp to another folder (or drive for that matter)? The wireshark machine has a small harddrive and it is desired to capture the file to a network or USB drive with a much larger capacity.'''
date = "2015-08-20T08:48:00Z"
lastmod = "2015-08-20T14:16:00Z"
weight = 45270
keywords = [ "autosavetemp" ]
aliases = [ "/questions/45270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Change default location windows/temp for autosave capture](/questions/45270/change-default-location-windowstemp-for-autosave-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do you change the wireshark default location of Windows/Temp to another folder (or drive for that matter)? The wireshark machine has a small harddrive and it is desired to capture the file to a network or USB drive with a much larger capacity.</p></div><div id="question-tags" class="tags-container tags">autosavetemp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '15, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/adbd78d2a52a45bf6921c77dcbb19df8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guydub&#39;s gravatar image" /><p>guydub<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guydub has no accepted answers">0%</span></p></div></div><div id="comments-container-45270" class="comments-container"></div><div id="comment-tools-45270" class="comment-tools"></div><div class="clear"></div><div id="comment-45270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45281"></span>

<div id="answer-container-45281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45281-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at this blog post:</p><p><a href="https://blog.packet-foo.com/2014/07/wireshark-file-storage/">https://blog.packet-foo.com/2014/07/wireshark-file-storage/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '15, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45281" class="comments-container"><span id="45283"></span><div id="comment-45283" class="comment"><div id="post-45283-score" class="comment-score"></div><div class="comment-text"><p>It might be nice for the <a href="https://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a> to mention the Windows <code>TEMP</code> environment variable like it does the *nix <a href="https://en.wikipedia.org/wiki/TMPDIR"><code>TMPDIR</code></a> environment variable. Speaking of <code>TMPDIR</code> though, it appears that this isn't always the correct environment variable which defines the temporary file directory. On my RHEL6 system, for example, the relevant environment variable is <code>TMP</code>, not <code>TMPDIR</code>, despite what <a href="http://www.gtk.org/api/2.6/glib/glib-Miscellaneous-Utility-Functions.html#g-get-tmp-dir"><code>g_get_tmp_dir()</code></a> claims, which is what <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=dumpcap.c;h=de683346e6201aac1ebf8f74e6056a0bedf04d0a;hb=HEAD#l3417"><code>dumpcap</code></a> calls via <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=wsutil/tempfile.c;h=93bd66fe7aade147e06ddce9692e026abc7d7621;hb=HEAD#l206"><code>create_tempfile()</code></a> to find the temporary file directory. RHEL6 is installed with glib2-2.26.1-3.el6.x86_64 and examining <a href="http://ftp.gnome.org/pub/GNOME/sources/glib/2.26/">glib2.26.1 sources</a> seems to indicate that <code>TMPDIR</code> should work, but it doesn't.</p></div><div id="comment-45283-info" class="comment-info"><span class="comment-age">(20 Aug '15, 18:49)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-45281" class="comment-tools"></div><div class="clear"></div><div id="comment-45281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


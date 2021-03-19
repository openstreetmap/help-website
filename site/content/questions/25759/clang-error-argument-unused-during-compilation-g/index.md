+++
type = "question"
title = "clang: error: argument unused during compilation: &#x27;-g&#x27;"
description = '''I am on FreeBSD 6.3 using clang 3.1 to build wireshark 1.11.0-SVN-52370. gmake[3]: Entering directory /usr/home/timpr/workspace/wireshark-1.11.0-SVN-52370/epan/wmem&#x27;  CCLD wmem_test clang: error: argument unused during compilation: &#x27;-g&#x27; gmake[3]: *** [wmem_test] Error 1 gmake[3]: Leaving directory/u...'''
date = "2013-10-08T13:14:00Z"
lastmod = "2013-10-08T13:14:00Z"
weight = 25759
keywords = [ "clang" ]
aliases = [ "/questions/25759" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [clang: error: argument unused during compilation: '-g'](/questions/25759/clang-error-argument-unused-during-compilation-g)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am on FreeBSD 6.3 using clang 3.1 to build wireshark 1.11.0-SVN-52370.</p><p>gmake[3]: Entering directory <code>/usr/home/timpr/workspace/wireshark-1.11.0-SVN-52370/epan/wmem'   CCLD   wmem_test clang: error: argument unused during compilation: '-g' gmake[3]: *** [wmem_test] Error 1 gmake[3]: Leaving directory</code>/usr/home/timpr/workspace/wireshark-1.11.0-SVN-52370/epan/wmem'</p><p>I assume the root cause of the problem is how LINK is defined, using a couple CFLAGS. Removing them resolves that problem.</p><p>LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \ $(LIBTOOLFLAGS) --mode=link $(CCLD) $(AM_CFLAGS) $(CFLAGS) \ $(AM_LDFLAGS) $(LDFLAGS) -o [email protected]</p></div><div id="question-tags" class="tags-container tags">clang</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/97221de68e381abf9fede7efbe80e7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tdprime&#39;s gravatar image" /><p>tdprime<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tdprime has no accepted answers">0%</span></p></div></div><div id="comments-container-25759" class="comments-container"><span id="25837"></span><div id="comment-25837" class="comment"><div id="post-25837-score" class="comment-score"></div><div class="comment-text"><p>Silly question, perhaps, but are you using configure? There's a specific test that checks whether the compiler accepts -g that should have run.</p></div><div id="comment-25837-info" class="comment-info"><span class="comment-age">(09 Oct '13, 08:47)</span> beroset</div></div></div><div id="comment-tools-25759" class="comment-tools"></div><div class="clear"></div><div id="comment-25759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


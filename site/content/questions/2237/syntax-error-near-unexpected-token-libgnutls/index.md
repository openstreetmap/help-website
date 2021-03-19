+++
type = "question"
title = "syntax error near unexpected token `LIBGNUTLS,&#x27;"
description = '''So over all of yesterday I spent fixing issues I was having with ./autogen.sh and I was overjoyed when I finally got it to pass. But now when I run ./configure I end up with this error: &amp;gt;./configure: line 15463: syntax error near unexpected token `LIBGNUTLS,&#x27; &amp;gt;./configure: line 15463: ` PKG_CH...'''
date = "2011-02-08T10:59:00Z"
lastmod = "2011-02-08T10:59:00Z"
weight = 2237
keywords = [ "error", "syntax", "configure", "libgnutls" ]
aliases = [ "/questions/2237" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [syntax error near unexpected token \`LIBGNUTLS,'](/questions/2237/syntax-error-near-unexpected-token-libgnutls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2237-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So over all of yesterday I spent fixing issues I was having with ./autogen.sh and I was overjoyed when I finally got it to pass.</p><p>But now when I run ./configure I end up with this error:</p><pre><code>&gt;./configure: line 15463: syntax error near unexpected token `LIBGNUTLS,&#39;
&gt;./configure: line 15463: `  PKG_CHECK_MODULES(LIBGNUTLS, gnutls &gt;= 1.2.0,&#39;</code></pre><p>I tried googling it. It's hard to follow some of the threads but I attempted some of the fixes that were suggested; reinstalling glib for example.</p><p>The part in the file that invokes the error is an if block that does the LIBGNUTLS check. So I tried running it with --with-gnutls=no to no avail.</p><p>I can get it to pass if I erase that block completely and but when I do a "make" I get yet another error. I forgot to get the exact text but it was related to LIBGNUTLS...</p><p>Any ideas or nudges in the right direction would be appreciated. =]</p></div><div id="question-tags" class="tags-container tags">error syntax configure libgnutls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p>Rodayo<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2237" class="comments-container"><span id="2238"></span><div id="comment-2238" class="comment"><div id="post-2238-score" class="comment-score"></div><div class="comment-text"><p>Could you provide some version numbers?</p></div><div id="comment-2238-info" class="comment-info"><span class="comment-age">(08 Feb '11, 12:49)</span> Jaap ♦</div></div></div><div id="comment-tools-2237" class="comment-tools"></div><div class="clear"></div><div id="comment-2237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


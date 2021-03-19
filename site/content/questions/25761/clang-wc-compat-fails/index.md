+++
type = "question"
title = "clang: -Wc++-compat fails"
description = '''I am on FreeBSD 6.3, using clang 3.1 to build wireshark. I am getting the following error during compile. The question is, what purpose is -Wc++-compat playing? Should it really be turned on here? I am actually tempted to remove &quot;#ifndef __GNUC__&quot; from smi.h.  CC libwireshark_la-epan.lo In file incl...'''
date = "2013-10-08T13:25:00Z"
lastmod = "2013-10-17T14:19:00Z"
weight = 25761
keywords = [ "clang" ]
aliases = [ "/questions/25761" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [clang: -Wc++-compat fails](/questions/25761/clang-wc-compat-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25761-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am on FreeBSD 6.3, using clang 3.1 to build wireshark.</p><p>I am getting the following error during compile. The question is, what purpose is -Wc++-compat playing? Should it really be turned on here?</p><p>I am actually tempted to remove "<code>#ifndef __GNUC__</code>" from smi.h.</p><pre><code>  CC     libwireshark_la-epan.lo
In file included from epan.c:31:
In file included from ../wsutil/wsgcrypt.h:63:
...
In file included from epan.c:63:
/usr/local/include/smi.h:319:1: error: empty struct has size 0 in C, size 1 in
      C++ [-Werror,-Wc++-compat]
} SmiElement;
^
6 warnings and 1 error generated.
gmake[3]: *** [libwireshark_la-epan.lo] Error 1</code></pre></div><div id="question-tags" class="tags-container tags">clang</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/97221de68e381abf9fede7efbe80e7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tdprime&#39;s gravatar image" /><p>tdprime<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tdprime has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '13, 16:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-25761" class="comments-container"><span id="29248"></span><div id="comment-29248" class="comment"><div id="post-29248-score" class="comment-score"></div><div class="comment-text"><p>I have forwarded the following fix to the people of the libsmi project:</p><p><code>  / SmiElement -- an item in a list (row index column, notification object)   /  typedef struct SmiElement { +#ifdef clang +    char dummy;         / CLANG complains about this with -WC++-compat / +#endif  #ifndef GNUC      char dummy;         / many compilers are unhappy with empty structures.  /  #endif      / no visible attributes /  } SmiElement;</code></p><p>(I give up on formatting this.....)</p></div><div id="comment-29248-info" class="comment-info"><span class="comment-age">(28 Jan '14, 13:04)</span> MavEtJu</div></div></div><div id="comment-tools-25761" class="comment-tools"></div><div class="clear"></div><div id="comment-25761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25762"></span>

<div id="answer-container-25762" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25762-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The purpose behind having that flag turned on was to allow C++ compilers to be used to compile Wireshark. During the initial cleanup to make that possible, a number of latent bugs were also discovered and fixed. The flag was then turned on to avoid re-introducing incompatibilities. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8416">Wireshark bug #8416</a> for more details on the why and how. In your case, it looks as though you have a C++ incompatible system file. You could either modify that file (or perhaps see if there is a newer version that someone else has already fixed?) or temporarily remove the flag from your compilation. If you think this is an issue that will affect other FreeBSD users, you might consider filing a bug report in bugzilla.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-25762" class="comments-container"></div><div id="comment-tools-25762" class="comment-tools"></div><div class="clear"></div><div id="comment-25762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26147"></span>

<div id="answer-container-26147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I ran into this as well. I worked around it by removing <code>#ifndef __GNUC__</code> from smi.h. Passing <code>--disable-warnings-as-errors</code> to configure would probably have worked as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '13, 16:14</p></div></div><div id="comments-container-26147" class="comments-container"></div><div id="comment-tools-26147" class="comment-tools"></div><div class="clear"></div><div id="comment-26147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


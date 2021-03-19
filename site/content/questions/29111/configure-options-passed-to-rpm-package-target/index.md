+++
type = "question"
title = "./configure options passed to rpm-package target?"
description = '''I just noticed that the RPM spec file has its own set of ./configure options. This made me question whether support for different options that I run prior to running &quot;make&quot; and &quot;make rpm-package&quot; aren&#x27;t being passed to the RPM build process. I tried to add the same &quot;--with-XXXX&quot; options to the file ...'''
date = "2014-01-22T13:05:00Z"
lastmod = "2014-01-22T13:12:00Z"
weight = 29111
keywords = [ "rpm", "redhat" ]
aliases = [ "/questions/29111" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [./configure options passed to rpm-package target?](/questions/29111/configure-options-passed-to-rpm-package-target)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29111-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just noticed that the RPM spec file has its own set of ./configure options. This made me question whether support for different options that I run prior to running "make" and "make rpm-package" aren't being passed to the RPM build process.</p><p>I tried to add the same "--with-XXXX" options to the file in its ./configure section manually, but the build process ended prematurely because it said the options were not recognized options.</p><p>Any insight?</p></div><div id="question-tags" class="tags-container tags">rpm redhat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/34ab7b09251ce1194b33bb66c2b32d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorwex&#39;s gravatar image" /><p>jorwex<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorwex has no accepted answers">0%</span></p></div></div><div id="comments-container-29111" class="comments-container"></div><div id="comment-tools-29111" class="comment-tools"></div><div class="clear"></div><div id="comment-29111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29112"></span>

<div id="answer-container-29112" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29112-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm interesting must have been something I did wrong.</p><p>This worked:</p><pre><code>%configure \
  --with-gnu-ld \
%if %{with_c_ares}
  --with-c-ares \
%endif
%if %{with_adns}
  --with-adns \
%endif
%if %{with_lua}
  --with-lua \
%endif
%if %{with_portaudio}
  --with-portaudio \
%endif
%if %{with_gtk3}
  --with-gtk3 \
%endif
  --without-zlib --disable-warnings-as-errors</code></pre>This didn't:<pre><code>%configure \
  --with-gnu-ld \
  --without-zlib \ 
%if %{with_c_ares}
  --with-c-ares \
%endif
%if %{with_adns}
  --with-adns \
%endif
%if %{with_lua}
  --with-lua \
%endif
%if %{with_portaudio}
  --with-portaudio \
%endif
%if %{with_gtk3}
  --with-gtk3 \
%endif
  --disable-warnings-as-errors</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/34ab7b09251ce1194b33bb66c2b32d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorwex&#39;s gravatar image" /><p>jorwex<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorwex has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '14, 14:34</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-29112" class="comments-container"></div><div id="comment-tools-29112" class="comment-tools"></div><div class="clear"></div><div id="comment-29112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


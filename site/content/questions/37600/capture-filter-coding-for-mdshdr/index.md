+++
type = "question"
title = "Capture filter coding for MDSHDR"
description = '''Hi All, I am trying to code capture filters for packets based on the mds header.  The BPF opcode generated to filter the Dst Index is as follows. { 0x20, 0, 0, 0x00000013 }, { 0x54, 0, 0, 0x0ffc0000 }, { 0x15, 0, 1, 0x01000000 }, { 0x6, 0, 0, 0x0000ffff }, { 0x6, 0, 0, 0x00000000 },  the filter not ...'''
date = "2014-11-05T20:25:00Z"
lastmod = "2014-11-05T20:25:00Z"
weight = 37600
keywords = [ "capture-filter", "bpf" ]
aliases = [ "/questions/37600" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter coding for MDSHDR](/questions/37600/capture-filter-coding-for-mdshdr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37600-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am trying to code capture filters for packets based on the mds header. The BPF opcode generated to filter the Dst Index is as follows.</p><pre><code>{ 0x20, 0, 0, 0x00000013 },
{ 0x54, 0, 0, 0x0ffc0000 },
{ 0x15, 0, 1, 0x01000000 },
{ 0x6, 0, 0, 0x0000ffff },
{ 0x6, 0, 0, 0x00000000 },</code></pre><p>the filter not only filters packets with Dst Index 0x40 but also 0x3c0</p><p>the packets look like</p><pre><code>0       0       0       0       0       bc      6b      6b      6b      6b      6b      6b      fc      fc      80      8
0       46      fe      71      0       1       0       0       c9      ef      0       0       1e      e7      2       ff
ff      fd      0       ff      ff      fd      22      38      0       0       6c      0       0       0       51      13
ff      ff      0       0       0       0       14      0       0       0       2       0       0       0       0       0
0       c8      0       0       0       0       0       0       0       0       0       0       0       0       0       0
0       14      0       0       0       50      0       0       0       d0      0       1       4       2f      3       0
0       0       57      d5</code></pre><p>and</p><pre><code>0       0       0       0       ee      0       0       0       0       0       0       a       fc      fc      91      6
0       e2      ff      7f      0       40      0       1       0       0       0       10      1       0       20      ff
fa      4       0       ff      fa      4       1       0       0       2       0       0       0       0       ff      ff
ff      ff      0       0       0       0       0       0       0       0       0       0       0       13      0       0
0       5       9       5c      84      18      0       0       0       0       0       0       0       0       0       0
0       0       0       0       0       0       0       ff      fa      4       0       ff      fa      4       0       0
c       37      0       0       0       0       0       0       0       0       0       0       0       1       0       0
0       0       6       8       20      0       6       8       20      0       0       7a      49      0       8       b9
52      7c      74      d3      2b      7f      2b      d6      6e      8f      bd      17      a4      9a      1c      76
dd      84      3b      39      d4      9f      2b      ba      6c      88      db      67      aa      e3      21      fd
60      95      d0      8b      14      fb      61      83      8b      1f      9a      2f      b9      b6      a5      96
3a      e0      cf      e       7f      fa      c8      ec      83      a3      53      2d      86      74      2a      e6
a       fa      71      1e      f6      d3      a1      81      f2      3b      b0      ab      f1      56      41      2b
36      10      39      b6      a       1       a2      8d      a4      f5      bb      2b      6a      e5      11      74</code></pre><p>It is kind of strange that the BPF code matched 1000000 and f000000 at the same time.</p><p>Could you kindly help me out? May be I am missing something basic.</p><p>Thanks and Regards, Aparna N</p></div><div id="question-tags" class="tags-container tags">capture-filter bpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '14, 20:25</strong></p><img src="https://secure.gravatar.com/avatar/b605d47d2e423a49d4a281eb597b9fba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aparna&#39;s gravatar image" /><p>Aparna<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aparna has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '14, 01:58</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37600" class="comments-container"></div><div id="comment-tools-37600" class="comment-tools"></div><div class="clear"></div><div id="comment-37600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


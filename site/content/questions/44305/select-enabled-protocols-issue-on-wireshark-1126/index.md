+++
type = "question"
title = "Select enabled protocols issue on wireshark 1.12.6"
description = '''Hello, When I updated wireshark from 1.12.5 to 1.12.6, the entry Enabled protocols has suddenly disappeared from the menu Analyze. Even if I press SHIFT+CTRL+E nothing happens. My personal protocol name is correctly displayed in the capture window, but the dissector action is shown as Data field onl...'''
date = "2015-07-19T17:35:00Z"
lastmod = "2015-07-20T11:41:00Z"
weight = 44305
keywords = [ "enabled", "protocols" ]
aliases = [ "/questions/44305" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Select enabled protocols issue on wireshark 1.12.6](/questions/44305/select-enabled-protocols-issue-on-wireshark-1126)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When I updated wireshark from 1.12.5 to 1.12.6, the entry Enabled protocols has suddenly disappeared from the menu Analyze.</p><p>Even if I press SHIFT+CTRL+E nothing happens.</p><p>My personal protocol name is correctly displayed in the capture window, but the dissector action is shown as Data field only.</p><p>In what condition the Analyze/Enabled protocols entry could disappear ?</p><p>Other items disappeared as well: Analyze/User Specified decodes Analyze/Expert info Analyze/Expert info Composite Analyze/Conversation Filter</p><p>My actual config:</p><p>Mageia5 Linux 64bits</p><p>wireshark 1.12.6 64bits</p><p>Thank you</p><p>BB</p></div><div id="question-tags" class="tags-container tags">enabled protocols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '15, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/81c7622b6d74193675e96174992d830d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="biba_paris&#39;s gravatar image" /><p>biba_paris<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="biba_paris has no accepted answers">0%</span></p></div></div><div id="comments-container-44305" class="comments-container"></div><div id="comment-tools-44305" class="comment-tools"></div><div class="clear"></div><div id="comment-44305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44313"></span>

<div id="answer-container-44313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44313-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>By any chance did you build /install the Qt GUI instead of the GTK based one?</p><p>Nothing changed in Wireshark 1.12.6 wrt those features, unless you launched the incomplete and buggy (in this branch) Qt GUI that did not have them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '15, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-44313" class="comments-container"><span id="44314"></span><div id="comment-44314" class="comment"><div id="post-44314-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your fast reply.</p><p>Your answer reminded me that I have seen some qt packages update on Mageia5 these days.</p><p>But how to know if I'm using QT or Gtk gui ?</p><p>Here are some console messages when I launch wireshark:</p><pre><code>QMetaObject::connectSlotsByName: No matching signal for on_bStart_clicked()
QMetaObject::connectSlotsByName: No matching signal for on_bStop_clicked()
FIX: packet list heading menu sensitivity
01:15:52.367  Dbg  FIX: timestamp types should be set elsewhere
01:15:52.367 Main Info fill_in_local_interfaces() starts
01:15:52.368 Capture Msg  Capture Interface List ...
01:15:52.368 Capture Dbg  sync_interface_list_open
01:15:52.368 Capture Dbg  sync_pipe_open_command
01:15:52.439 Capture Dbg  read 14 indicator: S empty value
01:15:52.439 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
01:15:52.439 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
01:15:52.439 Capture Msg  Capture Interface Capabilities ...
01:15:52.439 Capture Dbg  sync_if_capabilities_open
01:15:52.439 Capture Dbg  sync_pipe_open_command
01:15:52.482 Capture Dbg  read 14 indicator: S empty value
01:15:52.482 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
01:15:52.482 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
01:15:52.483 Capture Msg  Capture Interface Capabilities ...
01:15:52.483 Capture Dbg  sync_if_capabilities_open
01:15:52.483 Capture Dbg  sync_pipe_open_command
01:15:52.512 Capture Dbg  read 14 indicator: S empty value
01:15:52.512 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
01:15:52.512 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
01:15:52.584 Capture Msg  Capture Interface Capabilities failed!
01:15:52.584 Capture Msg  Capture Interface Capabilities ...</code></pre><p>etc...</p></div><div id="comment-44314-info" class="comment-info"><span class="comment-age">(20 Jul '15, 16:34)</span> biba_paris</div></div><span id="44315"></span><div id="comment-44315" class="comment"><div id="post-44315-score" class="comment-score">1</div><div class="comment-text"><p>That output means you're using the Qt-based GUI.</p></div><div id="comment-44315-info" class="comment-info"><span class="comment-age">(20 Jul '15, 17:16)</span> Hadriel</div></div><span id="44319"></span><div id="comment-44319" class="comment"><div id="post-44319-score" class="comment-score"></div><div class="comment-text"><p>Thank you Hadriel, you are right.</p><p>In the description of the Mageia package, QT GUI is used.</p><p>If I understand, something happened to wireshark, after last lib64qt5core update.</p><p>I tried to reinstall qt5, but it has a huge number of Apps in its dependance tree.</p><p>I returned to my debian Jessie version (1.12.1) under GTK, until a solution is found for Mageia5 QT version.</p></div><div id="comment-44319-info" class="comment-info"><span class="comment-age">(20 Jul '15, 23:35)</span> biba_paris</div></div><span id="44321"></span><div id="comment-44321" class="comment"><div id="post-44321-score" class="comment-score">1</div><div class="comment-text"><p>Linux distro should not package a Wireshark 1.12.x version with Qt GUI: in this branch this graphical front-end is more a proof of concept than anything else and is not ready for production. It will be part of Wireshark 2.0.</p></div><div id="comment-44321-info" class="comment-info"><span class="comment-age">(21 Jul '15, 03:51)</span> Pascal Quantin</div></div><span id="44324"></span><div id="comment-44324" class="comment"><div id="post-44324-score" class="comment-score"></div><div class="comment-text"><p>Thank you Pascal for your info.</p><p>Linux distros are time crunchers with their policies.</p><p>For example: As I told you, I launched wireshark 1.12.1 GTK under debian jessie.</p><p>Now, I'm facing a new problem:</p><p>The generic dissector plugin (<a href="http://wsgd.free.fr/)">http://wsgd.free.fr/)</a> stopped working.</p><p>I had created a desc/wsgd files for a personnal protocol</p><p>The reason displayed is that glibc &lt; 2.14 in debian jessie.</p><p>And no way to upgrade jessie (8.1)</p><p>Do I have to add a new os (like ubuntu) to overtake this issue ?</p><p>I'm wasting my time with os problems !!!</p></div><div id="comment-44324-info" class="comment-info"><span class="comment-age">(21 Jul '15, 05:59)</span> biba_paris</div></div><span id="44325"></span><div id="comment-44325" class="comment not_top_scorer"><div id="post-44325-score" class="comment-score"></div><div class="comment-text"><p>@biba_paris</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-44325-info" class="comment-info"><span class="comment-age">(21 Jul '15, 06:11)</span> grahamb ♦</div></div></div><div id="comment-tools-44313" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


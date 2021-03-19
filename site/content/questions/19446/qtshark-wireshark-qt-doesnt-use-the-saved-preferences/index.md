+++
type = "question"
title = "QtShark (wireshark-qt) doesn&#x27;t use the saved preferences"
description = '''QtShark doesn&#x27;t use the preferences I set. The preferences file gets altered when using the preferences gui, but the values are completely ignored. Manually editing the file doesn&#x27;t work either. xxx@xxx:~$ qtshark FIX: packet list heading menu sensitivity  /usr/local/lib/libwireshark.so.0: undefined...'''
date = "2013-03-13T06:29:00Z"
lastmod = "2013-03-13T10:35:00Z"
weight = 19446
keywords = [ "qtshark", "preferences", "settings" ]
aliases = [ "/questions/19446" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [QtShark (wireshark-qt) doesn't use the saved preferences](/questions/19446/qtshark-wireshark-qt-doesnt-use-the-saved-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>QtShark doesn't use the preferences I set.</p><p>The preferences file gets altered when using the preferences gui, but the values are completely ignored.</p><p>Manually editing the file doesn't work either.</p><pre><code>[email protected]:~$ qtshark
FIX: packet list heading menu sensitivity 
/usr/local/lib/libwireshark.so.0: undefined symbol: py_create_dissector_handle      
14:25:21.435  Dbg  plugin_dir: /usr/local/lib/wireshark/plugins/1.9.2-SVN-48274     
14:25:21.473  Dbg  FIX: timestamp types should be set elsewhere                     
14:25:21.473 Capture Msg  Capture Interface List ...                                
14:25:21.473 Capture Dbg  sync_interface_list_open                                  
14:25:21.473 Capture Dbg  sync_pipe_open_command                                    
14:25:21.500 Capture Dbg  read 9 indicator: S empty value
14:25:21.501 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.501 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.501 Capture Msg  Capture Interface Capabilities ...
14:25:21.501 Capture Dbg  sync_linktype_list_open
14:25:21.501 Capture Dbg  sync_pipe_open_command
14:25:21.536 Capture Dbg  read 9 indicator: S empty value
14:25:21.536 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.536 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.536 Capture Msg  Capture Interface Capabilities ...
14:25:21.536 Capture Dbg  sync_linktype_list_open
14:25:21.536 Capture Dbg  sync_pipe_open_command
14:25:21.565 Capture Dbg  read 9 indicator: S empty value
14:25:21.566 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.566 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.566 Capture Msg  Capture Interface Capabilities ...
14:25:21.566 Capture Dbg  sync_linktype_list_open
14:25:21.566 Capture Dbg  sync_pipe_open_command
14:25:21.597 Capture Dbg  read 9 indicator: S empty value
14:25:21.598 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.598 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.598 Capture Msg  Capture Interface Capabilities ...
14:25:21.598 Capture Dbg  sync_linktype_list_open
14:25:21.598 Capture Dbg  sync_pipe_open_command
14:25:21.651 Capture Dbg  read 9 indicator: S empty value
14:25:21.652 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.652 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.652 Capture Msg  Capture Interface Capabilities ...
14:25:21.652 Capture Dbg  sync_linktype_list_open
14:25:21.652 Capture Dbg  sync_pipe_open_command
14:25:21.689 Capture Dbg  read 9 indicator: S empty value
14:25:21.690 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.690 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.690 Capture Msg  Capture Interface Capabilities ...
14:25:21.690 Capture Dbg  sync_linktype_list_open
14:25:21.690 Capture Dbg  sync_pipe_open_command
14:25:21.729 Capture Dbg  read 9 indicator: S empty value
14:25:21.729 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.730 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.730 Capture Msg  Capture Interface Capabilities ...
14:25:21.730 Capture Dbg  sync_linktype_list_open
14:25:21.730 Capture Dbg  sync_pipe_open_command
14:25:21.778 Capture Dbg  read 9 indicator: S empty value
14:25:21.779 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.779 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.779 Capture Msg  Capture Interface Capabilities ...
14:25:21.780 Capture Dbg  sync_linktype_list_open
14:25:21.780 Capture Dbg  sync_pipe_open_command
14:25:21.825 Capture Dbg  read 9 indicator: S empty value
14:25:21.826 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.826 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.826 Capture Msg  Capture Interface Capabilities ...
14:25:21.826 Capture Dbg  sync_linktype_list_open
14:25:21.826 Capture Dbg  sync_pipe_open_command
14:25:21.863 Capture Dbg  read 9 indicator: S empty value
14:25:21.864 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.864 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.864 Capture Msg  Capture Interface Capabilities ...
14:25:21.864 Capture Dbg  sync_linktype_list_open
14:25:21.864 Capture Dbg  sync_pipe_open_command
14:25:21.914 Capture Dbg  read 9 indicator: S empty value
14:25:21.915 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.915 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.915 Capture Msg  Capture Interface Capabilities ...
14:25:21.915 Capture Dbg  sync_linktype_list_open
14:25:21.915 Capture Dbg  sync_pipe_open_command
14:25:21.985 Capture Dbg  read 9 indicator: S empty value
14:25:21.986 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:21.986 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:21.986  Dbg  FIX: fetch recent color settings
14:25:21.988 Capture Msg  Capture Interface List ...
14:25:21.989 Capture Dbg  sync_interface_list_open
14:25:21.989 Capture Dbg  sync_pipe_open_command
14:25:22.026 Capture Dbg  read 9 indicator: S empty value
14:25:22.027 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
14:25:22.027 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.000s
14:25:22.031 Capture Dbg  sync_interface_stats_open
14:25:22.031 Capture Dbg  sync_pipe_open_command
14:25:22.169 Capture Dbg  read 9 indicator: S empty value
14:25:22.171 Main Info Wireshark is up and ready to go</code></pre><p>What goes wrong?</p></div><div id="question-tags" class="tags-container tags">qtshark preferences settings</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/c6a3ebfd6e3ccbcb4abdd4b4bdf1b7b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ghost16&#39;s gravatar image" /><p>Ghost16<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ghost16 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '13, 07:12</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19446" class="comments-container"></div><div id="comment-tools-19446" class="comment-tools"></div><div class="clear"></div><div id="comment-19446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19461"></span>

<div id="answer-container-19461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19461-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Qt version of Wireshark is a work in progress, so there are a number of things that don't work at all or that don't work as well as they do in the GTK+ version; you should file a bug on this on the <a href="http://bugs.wireshark.org">Wireshark Bugzilla</a> to get it investigated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19461" class="comments-container"></div><div id="comment-tools-19461" class="comment-tools"></div><div class="clear"></div><div id="comment-19461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


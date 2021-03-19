+++
type = "question"
title = "Interaction between Plugin and GUI"
description = '''How to know which packet is selected in packet list? Maybe there is a flag in pinfo? I&#x27;ve found a plugin_if_register_gui_cb in plugin_if.h. If I understand it right, this registered callback is callled only when somebody calls plugin_if_goto_frame and not when UI hitted. What is the appropriate way ...'''
date = "2016-06-03T04:53:00Z"
lastmod = "2016-06-03T04:53:00Z"
weight = 53175
keywords = [ "gui", "api", "plugin" ]
aliases = [ "/questions/53175" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interaction between Plugin and GUI](/questions/53175/interaction-between-plugin-and-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to know which packet is selected in packet list? Maybe there is a flag in pinfo?</p><p>I've found a <code>plugin_if_register_gui_cb</code> in <code>plugin_if.h</code>. If I understand it right, this registered callback is callled only when somebody calls <code>plugin_if_goto_frame</code> and not when UI hitted.</p><p>What is the appropriate way to do some additional GUI as plugin in wireshark?</p><p>Thank you!</p><p><strong>edit:</strong> Well, I can use <code>plugin_if_get_ws_info</code>, but it only works on files and when capturing is done. Any method to do this live?</p></div><div id="question-tags" class="tags-container tags">gui api plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/2de9a43ced32f93c1c5d30166d8a0090?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Siarhei%20Rak&#39;s gravatar image" /><p>Siarhei Rak<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Siarhei Rak has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jun '16, 06:46</p></div></div><div id="comments-container-53175" class="comments-container"></div><div id="comment-tools-53175" class="comment-tools"></div><div class="clear"></div><div id="comment-53175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


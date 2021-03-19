+++
type = "question"
title = "Message Box from Dissector Plugin"
description = '''Hi, is there a possibility to create / open a message box from my own wireshark plugin?'''
date = "2012-02-06T07:41:00Z"
lastmod = "2012-02-06T09:03:00Z"
weight = 8848
keywords = [ "box", "message", "dissector", "plugin" ]
aliases = [ "/questions/8848" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Message Box from Dissector Plugin](/questions/8848/message-box-from-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8848-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is there a possibility to create / open a message box from my own wireshark plugin?</p></div><div id="question-tags" class="tags-container tags">box message dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '12, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/ce79034142dc613a1a30949664b84723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic&#39;s gravatar image" /><p>Nic<br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic has no accepted answers">0%</span></p></div></div><div id="comments-container-8848" class="comments-container"></div><div id="comment-tools-8848" class="comment-tools"></div><div class="clear"></div><div id="comment-8848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8851"></span>

<div id="answer-container-8851" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8851-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a possibility to report an error that, <em>IF</em> your dissector is running in Wireshark, will appear as a message box. If it's running in TShark, it will appear as text on the standard output.</p><p>The following functions are declared in <code>epan/report_err.h</code>:</p><p>To report an arbitrary message, call</p><pre><code>report_failure(const char *msg_format, ...);</code></pre><p>It takes, as arguments, a printf-style format string and arguments.</p><p>To report an error from an attempt to open a file, call</p><pre><code>report_open_failure(const char *filename, int err, gboolean for_writing);</code></pre><p>It takes, as arguments:</p><ul><li>the pathname of the file being opened</li><li>an <code>errno</code> value</li><li>a Boolean that's <code>TRUE</code> if the failed attempt was to was open the file for writing and <code>FALSE</code> if it was to open the file for reading</li></ul><p>To report an error from an attempt to open a file for reading, call</p><pre><code>report_read_failure(const char *filename, int err);</code></pre><p>It takes the pathname of the file and an <code>errno</code> value as arguments.</p><p>To report an error from an attempt to open a file for writing, call</p><pre><code>report_write_failure(const char *filename, int err);</code></pre><p>It takes the pathname of the file and an <code>errno</code> value as arguments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '12, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8851" class="comments-container"><span id="8855"></span><div id="comment-8855" class="comment"><div id="post-8855-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>thank you for your answer. This works fine. But is there a possibility to add a dialog with some labels and checkboxes? I tried to use the GtkWidget but this has errors while compiling.</p></div><div id="comment-8855-info" class="comment-info"><span class="comment-age">(06 Feb '12, 09:43)</span> Nic</div></div><span id="8856"></span><div id="comment-8856" class="comment"><div id="post-8856-score" class="comment-score"></div><div class="comment-text"><p>That's a different question, and the answer to it is "no". We do not, and never will, support GUI functions in dissectors, as dissectors can run in command-line programs or Web servers or....</p><p>If you want the user to be able to configure options for a dissector, you can register a dissector preference; a checkbox sounds like a Boolean preference, which will show up in the entry for a dissector in the Preferences dialog box as a checkbox. They can also be set from the command line with the "-o" flag.</p></div><div id="comment-8856-info" class="comment-info"><span class="comment-age">(06 Feb '12, 09:54)</span> Guy Harris ♦♦</div></div><span id="8858"></span><div id="comment-8858" class="comment"><div id="post-8858-score" class="comment-score"></div><div class="comment-text"><p>It's actually possible to open a <a href="http://wiki.wireshark.org/LuaAPI/GUI#new_dialog.28title.2C_action.2C_field1_.5B.2Cfield2_....5D.29">dialog</a> from a Lua dissector, but IMO dialogs should be spawned from <strong>outside</strong> a dissector (or postdissector or tap) to avoid bugs like repeatedly opening a dialog based on a trigger that occurs multiple times in a pcap.</p></div><div id="comment-8858-info" class="comment-info"><span class="comment-age">(06 Feb '12, 10:38)</span> bstn</div></div><span id="8859"></span><div id="comment-8859" class="comment"><div id="post-8859-score" class="comment-score"></div><div class="comment-text"><p>One would hope that people aren't opening dialogs in dissectors to provide an option better implemented as a preference.</p></div><div id="comment-8859-info" class="comment-info"><span class="comment-age">(06 Feb '12, 11:06)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8851" class="comment-tools"></div><div class="clear"></div><div id="comment-8851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


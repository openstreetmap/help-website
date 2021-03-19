+++
type = "question"
title = "enhancing dissector"
description = '''Hello, I need to enhance wireshark for some proprietary information. I need to use this function dissector_try_uint_new present in packet.c. It checks the value in a given uint dissector table and, if found, call the dissector with the arguments supplied.  Is there any example of adding a function p...'''
date = "2011-04-06T13:48:00Z"
lastmod = "2011-04-07T10:52:00Z"
weight = 3380
keywords = [ "dissector" ]
aliases = [ "/questions/3380" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [enhancing dissector](/questions/3380/enhancing-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to enhance wireshark for some proprietary information. I need to use this function dissector_try_uint_new present in packet.c. It checks the value in a given uint dissector table and, if found, call the dissector with the arguments supplied.</p><p>Is there any example of adding a function pointer in table passed to this function? I know that this is very specific question and i am sorry for asking this. If there is an example of definition, it will help me.</p><p>Thanks, Dhanashree</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '11, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p>dsprabhu4<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3380" class="comments-container"></div><div id="comment-tools-3380" class="comment-tools"></div><div class="clear"></div><div id="comment-3380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3391"></span>

<div id="answer-container-3391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3391-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to add a call to <code>dissector_add</code> in your <code>proto_reg_handoff_</code> function as so:</p><pre><code>void proto_reg_handoff_PROTOABBREV(void)
{
//...
dissector_add(&quot;tablename&quot;,         //the dissector table you are registering to
              1000,                //your uint
              PROTOABBREV_handle); //your dissector handle
//...
}</code></pre><p>Usually, dissector tables are named like <code>"protocol.field"</code> (e.g. <code>"tcp.port"</code>). Your comment to Jaap indicates you want to do this for the bacapp dissector, but I do not see the bacapp dissector registering a dissector table for you to register against. Unless you have already done so, you will need to add that functionality to the bacapp dissector yourself in <code>epan/packet-bacapp.c</code>. Note also that if you add a dissector table to a dissector, you will also need to add (at least) a call to <code>dissector_try_uint_new</code> (or similar) within that dissector as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '11, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3391" class="comments-container"><span id="3392"></span><div id="comment-3392" class="comment"><div id="post-3392-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. I got one example from cip packet and your mail has verified this information. I was able to add a function and debug code.</p></div><div id="comment-3392-info" class="comment-info"><span class="comment-age">(07 Apr '11, 12:37)</span> dsprabhu4</div></div><span id="3393"></span><div id="comment-3393" class="comment"><div id="post-3393-score" class="comment-score"></div><div class="comment-text"><p>I get following fatal errors for some tool when i compile using VS 2008 EE.</p><p>12&gt;'C:Program' is not recognized as an internal or external command, 12&gt;operable program or batch file. 12&gt;NMAKE : fatal error U1077: '"C:Program FilesNSISmakensis.exe' : return code '0x1' 12&gt;Stop. 12&gt;NMAKE : fatal error U1077: '"C:Program FilesMicrosoft Visual Studio 9.0VCbinnmake.exe"' : return code '0x2' 12&gt;Stop. 12&gt;Project : error PRJ0019: A tool returned an error code from "Performing Makefile project actions" 12&gt;Build log was saved at "file://c:wiresharkPortableAppsBuildLog.htm"</p><p>Any idea??</p></div><div id="comment-3393-info" class="comment-info"><span class="comment-age">(07 Apr '11, 12:38)</span> dsprabhu4</div></div><span id="3394"></span><div id="comment-3394" class="comment"><div id="post-3394-score" class="comment-score"></div><div class="comment-text"><p>It looks like NSIS failed to build your installer package. You should check the build log that the error mentions.</p></div><div id="comment-3394-info" class="comment-info"><span class="comment-age">(07 Apr '11, 13:28)</span> multipleinte...</div></div></div><div id="comment-tools-3391" class="comment-tools"></div><div class="clear"></div><div id="comment-3391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3385"></span>

<div id="answer-container-3385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3385-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does <a href="http://developer.gnome.org/glib/unstable/glib-Type-Conversion-Macros.html#GPOINTER-TO-UINT:CAPS">GPOINTER_TO_UINT</a> help here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '11, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3385" class="comments-container"><span id="3387"></span><div id="comment-3387" class="comment"><div id="post-3387-score" class="comment-score"></div><div class="comment-text"><p>I need an example of how to define dissector_try_uint_new function pointer and how to add it in bacapp_dissector_table table. This is vendor specific code used in one of the protocol.</p></div><div id="comment-3387-info" class="comment-info"><span class="comment-age">(07 Apr '11, 07:53)</span> dsprabhu4</div></div><span id="3464"></span><div id="comment-3464" class="comment"><div id="post-3464-score" class="comment-score"></div><div class="comment-text"><p>Need some more help on this dissector question again<br />
</p><p>I have added a dissector for some proprietary message decoding in exising protocol. That dissector function (actual implmentation) needs to be in a different c file for maintenance. This is an enhancement for a standard protocol. but i need to add this dissector in proto_reg_handoff_PROTOABBREV of exising standard protocol. Is there any way to do this? I am facing problem with compilation.</p></div><div id="comment-3464-info" class="comment-info"><span class="comment-age">(12 Apr '11, 07:33)</span> dsprabhu4</div></div></div><div id="comment-tools-3385" class="comment-tools"></div><div class="clear"></div><div id="comment-3385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Functions involved in the Dissecting Process [Header files and examples]"
description = '''According to the book pg 468 (reader) / pg 440 (book), under the title of &quot; The Dissection Process&quot; I was unable to locate which header files that some of the functions belongs to:  dissect_frame() dissect_try_port()  May i know to which header files that these functions belong to? Is there any tuto...'''
date = "2011-07-27T20:09:00Z"
lastmod = "2011-07-28T01:28:00Z"
weight = 5334
keywords = [ "dissector", "epan", "wireshark" ]
aliases = [ "/questions/5334" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Functions involved in the Dissecting Process \[Header files and examples\]](/questions/5334/functions-involved-in-the-dissecting-process-header-files-and-examples)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5334-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>According to the <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf1.2.2.">book</a> pg 468 (reader) / pg 440 (book), under the title of " The Dissection Process" I was unable to locate which header files that some of the functions belongs to:</p><ol><li><code>dissect_frame()</code></li><li><code>dissect_try_port()</code></li></ol><p>May i know to which header files that these functions belong to?</p><p>Is there any tutorials or guidelines out there on how to use the functions? If you could, please provide me a simple example of using the functions in the dissectors (<code>epan_dissector_run()</code>, <code>dissect_packet</code>,<code>dissect_frame()</code>, <code>dissect_try_port()</code>). I do really appreciate that. Thanks</p><p>Regards, Eddie Choo</p></div><div id="question-tags" class="tags-container tags">dissector epan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p>eddie choo<br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div></div><div id="comments-container-5334" class="comments-container"></div><div id="comment-tools-5334" class="comment-tools"></div><div class="clear"></div><div id="comment-5334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5338"></span>

<div id="answer-container-5338" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5338-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your link to "the book" is dead for me, so I'm not sure what you are referencing.</p><ol><li><code>dissect_frame()</code> isn't in any header file. The function is found in epan\dissectors\frame.c. It is called from epan\packet.c in function <code>dissect_packet()</code> via <code>call_dissector()</code> using the handle to the frame dissector located by the <code>packet_init()</code> function.</li><li>I think you mean <code>dissector_try_port()</code> which doesn't exist any more. It was renamed to <code>dissector_try_uint()</code> in revision 35224 with the following reason for the change:</li></ol><blockquote><p>Rename the routines that handle dissector tables with unsigned integer keys to have _uint in their names, to match the routines that handle dissector tables with string keys. (Using _port can confuse people into thinking they're intended solely for use with TCP/UDP/etc. ports when, in fact, they work better for things such as Ethernet types, where the binding of particular values to particular protocols are a lot stronger.)</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '11, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '11, 02:08</p></div></div><div id="comments-container-5338" class="comments-container"><span id="5340"></span><div id="comment-5340" class="comment"><div id="post-5340-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham, thanks for your reply. I am sorry that i submitted the wrong link. <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf">This is the correct one</a></p></div><div id="comment-5340-info" class="comment-info"><span class="comment-age">(28 Jul '11, 01:52)</span> eddie choo</div></div></div><div id="comment-tools-5338" class="comment-tools"></div><div class="clear"></div><div id="comment-5338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


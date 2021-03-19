+++
type = "question"
title = "How can I filter streams that contain file downloads?"
description = '''What filter can I use to obtain the streams associated to the objects that are listed when doing the following in Wireshark?  - File/Export/Objects/HTTP Thank you in advance!'''
date = "2011-08-09T14:49:00Z"
lastmod = "2011-08-09T14:59:00Z"
weight = 5601
keywords = [ "filter", "http", "streams" ]
aliases = [ "/questions/5601" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I filter streams that contain file downloads?](/questions/5601/how-can-i-filter-streams-that-contain-file-downloads)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What filter can I use to obtain the streams associated to the objects that are listed when doing the following in Wireshark? - File/Export/Objects/HTTP</p><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags">filter http streams</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/458fd48b7df19117cba8bab4942dc562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Migdalia&#39;s gravatar image" /><p>Migdalia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Migdalia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 19:13</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-5601" class="comments-container"></div><div id="comment-tools-5601" class="comment-tools"></div><div class="clear"></div><div id="comment-5601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5602"></span>

<div id="answer-container-5602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter "http" will be a good start :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '11, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5602" class="comments-container"><span id="5603"></span><div id="comment-5603" class="comment"><div id="post-5603-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response! ... I am adding more details:</p><p>My trace file has hundred of streams to the same server, but not all the streams have an object (file download). I would like to filter the complete conversations (TCP and http packets)for the streams that have objects. I get a good filter when I do the following:</p><blockquote><p>File/Export/Objects/HTTP</p></blockquote><p>With this output, I identify the streams that have objects, and manually create a filter like: (tcp.stream == 25) || (tcp.stream == 49) || (tcp.stream == 70) || (tcp.stream == 77) || (tcp.stream == 83)</p><p>This works for trace files with few objects, but not when the list is long. I would like something like: "tcp.stream contains &lt;filename&gt;", but "contains" cannot be used as an operator with tcp.stream Is there an easy way to accomplish this? Thank you.</p></div><div id="comment-5603-info" class="comment-info"><span class="comment-age">(09 Aug '11, 16:14)</span> Migdalia</div></div><span id="5614"></span><div id="comment-5614" class="comment"><div id="post-5614-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ for details)</p><p>The filtering mechanism is currently only able to select frames that match a particular pattern. It is not capable of selecting a whole session (tcp stream) based on something in the stream.</p><p>The way I work around this is to use some scripting around tshark. Please see the <a href="http://sharkfest.wireshark.org/sharkfest.11/presentations/A-2_Blok-Using_Wireshark_Command_Line_Tools_&amp;_Scripting.pdf">presentation I gave at Sharkfest</a> for more info on how to do that.</p></div><div id="comment-5614-info" class="comment-info"><span class="comment-age">(10 Aug '11, 00:38)</span> SYN-bit ♦♦</div></div><span id="5615"></span><div id="comment-5615" class="comment"><div id="post-5615-score" class="comment-score"></div><div class="comment-text"><p>An other way would be to use <a href="http://wiki.wireshark.org/Mate">MATE</a> or <a href="http://wiki.wireshark.org/Lua">LUA</a>, but I have not used them enough myself to explain how to use them.</p></div><div id="comment-5615-info" class="comment-info"><span class="comment-age">(10 Aug '11, 00:53)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5602" class="comment-tools"></div><div class="clear"></div><div id="comment-5602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


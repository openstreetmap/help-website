+++
type = "question"
title = "How to display HTTP Header Length in bytes as a column?"
description = '''How can I do this in Wireshark?'''
date = "2011-04-18T09:32:00Z"
lastmod = "2011-04-18T13:43:00Z"
weight = 3574
keywords = [ "display" ]
aliases = [ "/questions/3574" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to display HTTP Header Length in bytes as a column?](/questions/3574/how-to-display-http-header-length-in-bytes-as-a-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3574-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I do this in Wireshark?</p></div><div id="question-tags" class="tags-container tags">display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/e26c7ebb23eae3f6b8a22c85915807f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce&#39;s gravatar image" /><p>Bruce<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce has no accepted answers">0%</span></p></div></div><div id="comments-container-3574" class="comments-container"></div><div id="comment-tools-3574" class="comment-tools"></div><div class="clear"></div><div id="comment-3574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3585"></span>

<div id="answer-container-3585" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3585-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you want to add the HTTP header "Content-Length" as a column? You can achieve that by rightclicking on the "Content-Length" header in the packet details pane. Then you can choose "Apply as Column". If you are using a version lower than 1.4.0, you can do it by opening the column preferences and then add a custom column with the field name "http.content_length_header".</p><p>(There is no field in wireshark that shows you the length of the HTTP headers, so if that was your question, it is not possible currently)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3585" class="comments-container"><span id="3597"></span><div id="comment-3597" class="comment"><div id="post-3597-score" class="comment-score"></div><div class="comment-text"><p>@SYNbit: Can I write a plugin or something to do that? Once I get access to the raw data its easy to find out the header length. Will wireshark allow me to do this?</p></div><div id="comment-3597-info" class="comment-info"><span class="comment-age">(18 Apr '11, 21:55)</span> Bruce</div></div><span id="3601"></span><div id="comment-3601" class="comment"><div id="post-3601-score" class="comment-score">1</div><div class="comment-text"><p>You might be able to write a LUA script that does what you need. You can also write a plugin, but that would replace the HTTP dissector which might not be what you want. The easiest though, would be to add this functionality to the existing http dissector (epan/dissectors/packet-http.c).</p></div><div id="comment-3601-info" class="comment-info"><span class="comment-age">(18 Apr '11, 23:56)</span> SYN-bit ♦♦</div></div><span id="3602"></span><div id="comment-3602" class="comment"><div id="post-3602-score" class="comment-score"></div><div class="comment-text"><p>If you do add fields for the HTTP header length, I would suggest using http.request.header_length and http.response.header_length.</p><p>It would be great if you can submit your patch to the wireshark repository for others to use as well. You can add it at https://bugs.wireshark.org :-)</p></div><div id="comment-3602-info" class="comment-info"><span class="comment-age">(19 Apr '11, 03:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3585" class="comment-tools"></div><div class="clear"></div><div id="comment-3585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


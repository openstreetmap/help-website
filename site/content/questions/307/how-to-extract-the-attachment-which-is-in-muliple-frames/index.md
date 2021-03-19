+++
type = "question"
title = "How to extract the attachment which is in muliple frames ?"
description = '''How to extract the attachment which is in multiple frames ? for eg a doc file'''
date = "2010-09-23T21:49:00Z"
lastmod = "2010-09-24T00:41:00Z"
weight = 307
keywords = [ "doc", "attachment", "file" ]
aliases = [ "/questions/307" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract the attachment which is in muliple frames ?](/questions/307/how-to-extract-the-attachment-which-is-in-muliple-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-307-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to extract the attachment which is in multiple frames ? for eg a doc file</p></div><div id="question-tags" class="tags-container tags">doc attachment file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '10, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/4382893663cabf8a4a0e2ca272e7bdc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethaliasathanar&#39;s gravatar image" /><p>sethaliasath...<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethaliasathanar has no accepted answers">0%</span></p></div></div><div id="comments-container-307" class="comments-container"></div><div id="comment-tools-307" class="comment-tools"></div><div class="clear"></div><div id="comment-307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="308"></span>

<div id="answer-container-308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-308-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on the protocol that was used to transfer the "attachment". For some protocols (HTTP, DICOM and SMB at the moment) Wireshark can export the objects through "File -&gt; Export -&gt; Objects -&gt; &lt;proto&gt;".</p><p>If the attachment you are interested in is not transferred using one of those, your best bet is to do a "Follow TCP/UDP stream" and save the raw data (it's best to only save the data in one direction).</p><p>Then you have to use a (hex) editor to delete all the unnecessary data around your attachment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '10, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-308" class="comments-container"><span id="439"></span><div id="comment-439" class="comment"><div id="post-439-score" class="comment-score"></div><div class="comment-text"><p>Laura has a GREAT demo for this in one of her wireshark training books. I don't remember if is in the new one or one of her older revs but I did it and it blew me away. There might even be a demo on youtube. I used the hex process the SYNbit refers to. It is well worth digging into to learn. You will be amazed at you find :)</p></div><div id="comment-439-info" class="comment-info"><span class="comment-age">(06 Oct '10, 07:05)</span> blacknight</div></div></div><div id="comment-tools-308" class="comment-tools"></div><div class="clear"></div><div id="comment-308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


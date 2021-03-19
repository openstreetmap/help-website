+++
type = "question"
title = "Why are options missing on File Save As menu in v1.12.2?"
description = '''I just upgraded to v1.12.2, and when I do a File-&amp;gt;Save As it just looks like a normal Windows file save dialogue, with no options to save Displayed packets, Marked packets, etc. Is this a known issue, and is there a published resolution?'''
date = "2014-12-30T07:33:00Z"
lastmod = "2014-12-30T07:46:00Z"
weight = 38796
keywords = [ "filtered", "save", "packets" ]
aliases = [ "/questions/38796" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why are options missing on File Save As menu in v1.12.2?](/questions/38796/why-are-options-missing-on-file-save-as-menu-in-v1122)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38796-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just upgraded to v1.12.2, and when I do a File-&gt;Save As it just looks like a normal Windows file save dialogue, with no options to save Displayed packets, Marked packets, etc. Is this a known issue, and is there a published resolution?</p></div><div id="question-tags" class="tags-container tags">filtered save packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/3692efbae740e7e090820d147c0f5e98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulS&#39;s gravatar image" /><p>PaulS<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulS has no accepted answers">0%</span></p></div></div><div id="comments-container-38796" class="comments-container"></div><div id="comment-tools-38796" class="comment-tools"></div><div class="clear"></div><div id="comment-38796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38797"></span>

<div id="answer-container-38797" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38797-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Never mind, I see they have moved it to an option under the File-&gt;Export section. Why the h.. would the developers make a needless, arbitrary change like that to something that's been in the product for many years under the File-&gt;Save As menu? (rhetorical question, no need to answer)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/3692efbae740e7e090820d147c0f5e98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulS&#39;s gravatar image" /><p>PaulS<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulS has no accepted answers">0%</span></p></div></div><div id="comments-container-38797" class="comments-container"><span id="38798"></span><div id="comment-38798" class="comment"><div id="post-38798-score" class="comment-score"></div><div class="comment-text"><p>IIRC it was discussed a fair bit by the devs, the aim is to separate the notions of changing the capture file format (Save As) and exporting particular parts of the capture (Export ...).</p><p>You question has brought to attention the fact that the User Guide sections for Save As and Export ... require some work.</p></div><div id="comment-38798-info" class="comment-info"><span class="comment-age">(30 Dec '14, 08:02)</span> grahamb ♦</div></div><span id="38837"></span><div id="comment-38837" class="comment"><div id="post-38837-score" class="comment-score"></div><div class="comment-text"><p>Because "Save as", in 99 44/100% of the applications out there, means "save the whole thing to a new file and make that the current file", and "Save" means "save the whole thing in the current file".</p><p>Given that 1.12 added editing capabilities, by allowing comments to be added, changed, and removed, "Save" now became a much more important option. "Save as"'s old behavior was confusing to some - see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6640">bug 6640</a>, for example.</p><p>So Wireshark, as of 1.12, works the same way other applications work, even if it doesn't work the same way that older versions of Wireshark worked. The change wasn't arbitrary and, given 1) the confusion that the old behavior had (where "Save as" worked differently depending on whether you saved all packets or not), 2) the need for a "Save" operation that saves everything, and 3) the fact that "Save as" in Wireshark didn't mean the same thing as it does in other applications (another source of confusion), it wasn't unnecessary, either.</p></div><div id="comment-38837-info" class="comment-info"><span class="comment-age">(31 Dec '14, 16:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-38797" class="comment-tools"></div><div class="clear"></div><div id="comment-38797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


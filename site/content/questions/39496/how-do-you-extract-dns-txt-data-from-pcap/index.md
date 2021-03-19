+++
type = "question"
title = "How do you extract DNS TXT data from pcap"
description = '''Is there a way to use TShark to extract DNS TXT data from DNS responses to a text file? I tried using... tshark -r &amp;lt;pcapname&amp;gt; -T fields -e &quot;dns.txt&quot; &amp;gt; &amp;lt;filename&amp;gt;.txt It seems to run but the file is blank when I read it. Thanks in advance!'''
date = "2015-01-30T05:13:00Z"
lastmod = "2015-01-30T05:25:00Z"
weight = 39496
keywords = [ "dns.txt", "dns" ]
aliases = [ "/questions/39496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you extract DNS TXT data from pcap](/questions/39496/how-do-you-extract-dns-txt-data-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39496-score" class="post-score" title="current number of votes">0</div><span id="post-39496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to use TShark to extract DNS TXT data from DNS responses to a text file? I tried using...</p><p>tshark -r &lt;pcapname&gt; -T fields -e "dns.txt" &gt; &lt;filename&gt;.txt</p><p>It seems to run but the file is blank when I read it.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns.txt" rel="tag" title="see questions tagged &#39;dns.txt&#39;">dns.txt</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/d10ae2f20defde4863f706842c20ccf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spotlight&#39;s gravatar image" /><p><span>spotlight</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spotlight has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '15, 05:13</strong> </span></p></div></div><div id="comments-container-39496" class="comments-container"></div><div id="comment-tools-39496" class="comment-tools"></div><div class="clear"></div><div id="comment-39496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39497"></span>

<div id="answer-container-39497" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39497-score" class="post-score" title="current number of votes">0</div><span id="post-39497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's no txt field in the DNS dissection. Which part of the DNS response do you need?</p><p>Hint, you can find field names by clicking on the item in the protocol tree and looking at the status bar where the field name is shown in parentheses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39497" class="comments-container"></div><div id="comment-tools-39497" class="comment-tools"></div><div class="clear"></div><div id="comment-39497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


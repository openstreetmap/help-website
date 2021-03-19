+++
type = "question"
title = "Display filter works in Wireshark but not in TShark - Special Characters Issue?"
description = '''I am trying to write a tshark read filter to match a wireshark display filter that works fine. However it seems that even using quotation marks (which works in Wireshark), I get a variety of errors, based on the contents.  Seems to be the same for both frame contains and tcp.data contains -R frame c...'''
date = "2011-06-22T15:50:00Z"
lastmod = "2011-06-24T01:33:00Z"
weight = 4682
keywords = [ "special", "tshark", "characters" ]
aliases = [ "/questions/4682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter works in Wireshark but not in TShark - Special Characters Issue?](/questions/4682/display-filter-works-in-wireshark-but-not-in-tshark-special-characters-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4682-score" class="post-score" title="current number of votes">0</div><span id="post-4682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a tshark read filter to match a wireshark display filter that works fine. However it seems that even using quotation marks (which works in Wireshark), I get a variety of errors, based on the contents. Seems to be the same for both frame contains and tcp.data contains</p><p>-R frame contains "something="<br />
returns: = not expected in this context</p><p>-R frame contains "2134 error"<br />
returns: error expected in this context<br />
</p><p>-R frame contains "txt" returns: not expected in this context</p><p>-R frame contains "(test" returns: syntaxt error</p><p>-R frame contains ":text" returns: not valid byte string</p><p>I am stumped because these work fine to find the strings in wireshark. I have successfully written ones with plain text letters that work fine across both TShark and Wireshark, and all I have changed is the read filter strings. Please advise!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-special" rel="tag" title="see questions tagged &#39;special&#39;">special</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-characters" rel="tag" title="see questions tagged &#39;characters&#39;">characters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/5416b98569b7f47d3b9ce3c5e0fde005?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erub&#39;s gravatar image" /><p><span>erub</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erub has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '11, 15:50</strong> </span></p></div></div><div id="comments-container-4682" class="comments-container"></div><div id="comment-tools-4682" class="comment-tools"></div><div class="clear"></div><div id="comment-4682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4683"></span>

<div id="answer-container-4683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4683-score" class="post-score" title="current number of votes">0</div><span id="post-4683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On the commandline the whole filter should be one string, ie the whole display filter should be in quotes (or contain no spaces). You might want to try the following:</p><pre><code>-R &#39;frame contains &quot;something=&quot;&#39;</code></pre><p>(I believe this does not work on Windows, but I know there are ways on windows, even though I don't know them :-))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-4683" class="comments-container"><span id="4695"></span><div id="comment-4695" class="comment"><div id="post-4695-score" class="comment-score"></div><div class="comment-text"><p>I actually found the answer to this question (for windows) in another thread:</p><p>frame contains " blah blah error crazy characters #&amp;%#($# " works fine. Thanks for the reply!</p></div><div id="comment-4695-info" class="comment-info"><span class="comment-age">(23 Jun '11, 09:55)</span> <span class="comment-user userinfo">erub</span></div></div><span id="4717"></span><div id="comment-4717" class="comment"><div id="post-4717-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", see the FAQ)</p></div><div id="comment-4717-info" class="comment-info"><span class="comment-age">(24 Jun '11, 01:33)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4683" class="comment-tools"></div><div class="clear"></div><div id="comment-4683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "pdml files are very large ..."
description = '''Could wireshark use the import facility of XML or some king of entity relationship so that pdml files do not become unordinately big? ~   I think tcpflow works that way. It only keeps active open connections and close the file with the particular data once the connection is closed. ~   Thank you  lb...'''
date = "2011-10-21T06:26:00Z"
lastmod = "2011-10-29T11:18:00Z"
weight = 7022
keywords = [ "pdml", "file", "size" ]
aliases = [ "/questions/7022" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pdml files are very large ...](/questions/7022/pdml-files-are-very-large)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7022-score" class="post-score" title="current number of votes">0</div><span id="post-7022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could wireshark use the import facility of XML or some king of entity relationship so that pdml files do not become unordinately big? ~ I think tcpflow works that way. It only keeps active open connections and close the file with the particular data once the connection is closed. ~ Thank you lbrtchx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '11, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/8092334bd5317ea0b2526599f06750de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Albretch%20Mueller&#39;s gravatar image" /><p><span>Albretch Mue...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Albretch Mueller has no accepted answers">0%</span></p></div></div><div id="comments-container-7022" class="comments-container"></div><div id="comment-tools-7022" class="comment-tools"></div><div class="clear"></div><div id="comment-7022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7026"></span>

<div id="answer-container-7026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7026-score" class="post-score" title="current number of votes">1</div><span id="post-7026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is where Wireshark and tcpflow differ. While tcpflow just concerned with TCP flows, Wireshark goes beyond that and works on <em>every</em> frame seen on the network. You may want to limit your output by filter ing your capture before saving it as PDML.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7026" class="comments-container"><span id="7143"></span><div id="comment-7143" class="comment"><div id="post-7143-score" class="comment-score"></div><div class="comment-text"><p>Well, "beyond" you say?</p><p>~</p><p>How is it that your answer relate to my question?</p>~<p>I see that wireshark is more like a network traffic viewer (using the output sniffed by tcpdump), but it would be nice if it would somehow craft PDML files in a way that, even while working on "every frame seen on the network" it would, in a more orthodox MVC way, let users easily only -open- and view what they want</p>~<p>I think the functionality is there (it is like -opening for viewing- only what you need instead of "working on every packet" and then letting users "select" what they need to view). Probably a few changes in the code would achieve this. This is how it would functional stack up:</p>~<p>1) tcpdum sniffs network traffic</p>~<p>2) &gt; &gt; a la tcpflow, files and their metadata would be separately captured &lt; &lt;</p>~<p>3) wireshark would use (2)'s metadata to select and only view what one needs</p>~<p>I could reword my initial question: How do people do if they need to keep a viewer open for long periods of time to only watch certain packets without making the capture files prohibitively large?</p>~<p>lbrtchx</p></div><div id="comment-7143-info" class="comment-info"><span class="comment-age">(29 Oct '11, 07:21)</span> <span class="comment-user userinfo">Albretch Mue...</span></div></div><span id="7146"></span><div id="comment-7146" class="comment"><div id="post-7146-score" class="comment-score"></div><div class="comment-text"><p>There are <a href="http://www.riverbed.com/us/products/cascade/cascade_pilot_personal_edition.php">other tools</a> for that.</p></div><div id="comment-7146-info" class="comment-info"><span class="comment-age">(29 Oct '11, 11:18)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-7026" class="comment-tools"></div><div class="clear"></div><div id="comment-7026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


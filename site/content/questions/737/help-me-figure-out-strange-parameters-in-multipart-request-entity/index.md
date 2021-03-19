+++
type = "question"
title = "Help me figure out strange parameters in Multipart Request Entity"
description = '''I am trying to analyse file uploading in FileDude.com  When i upload a file, a post request is sent with a multipart request entity which contains 3 parts. The first one is &quot;Filedata&quot; which contains the file data and the others are named &quot;x&quot; and &quot;y&quot; with some values. These values differ each time I ...'''
date = "2010-10-28T23:42:00Z"
lastmod = "2010-10-29T00:38:00Z"
weight = 737
keywords = [ "request", "multipart", "entity" ]
aliases = [ "/questions/737" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help me figure out strange parameters in Multipart Request Entity](/questions/737/help-me-figure-out-strange-parameters-in-multipart-request-entity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-737-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyse file uploading in FileDude.com</p><p>When i upload a file, a post request is sent with a multipart request entity which contains 3 parts. The first one is "Filedata" which contains the file data and the others are named "x" and "y" with some values. These values differ each time I upload a file(even if it is same file). X is like 77, 100, 47 and Y is like 11, 10, 13.. I don't know how these values are being calculated. Can anyone figure this out?</p></div><div id="question-tags" class="tags-container tags">request multipart entity</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '10, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/b6895d0627be12c4d0afe83cc06e9120?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vigneshwaran&#39;s gravatar image" /><p>Vigneshwaran<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vigneshwaran has no accepted answers">0%</span></p></div></div><div id="comments-container-737" class="comments-container"></div><div id="comment-tools-737" class="comment-tools"></div><div class="clear"></div><div id="comment-737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="738"></span>

<div id="answer-container-738" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-738-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The page is using a form with an image as "submit" button:</p><pre><code>    &lt;form action=&quot;http://srv4.nl1.filedude.com/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
        &lt;input name=&quot;Filedata&quot; type=&quot;file&quot; size=&quot;45&quot;&gt;&lt;br/&gt;&lt;br/&gt;
        &lt;input type=&quot;image&quot; src=&quot;http://static.filedude.com/templates/normal/img_en/upload.png&quot; /&gt;&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;
    &lt;/form&gt;</code></pre><p>The X and Y values are the coordinates of the location where the user clicked in the "submit" image.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '10, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-738" class="comments-container"></div><div id="comment-tools-738" class="comment-tools"></div><div class="clear"></div><div id="comment-738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "How can I search for Notes with a keyword?"
description = '''Hi - I&#x27;d like to search for OSM Notes with the keyword &quot;solar&quot; in the text. How can I do that please? (There&#x27;s no hint of it in the wiki page about Notes, even in the Advanced Use. It seems to me I can&#x27;t be the first person wanting to do this)'''
date = "2019-07-31T09:10:00Z"
lastmod = "2019-11-07T22:05:00Z"
weight = 70249
keywords = [ "notes-api", "notes", "search" ]
aliases = [ "/questions/70249" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I search for Notes with a keyword?](/questions/70249/how-can-i-search-for-notes-with-a-keyword)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70249-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I'd like to search for OSM Notes with the keyword "solar" in the text. How can I do that please?</p>
<p>(There's no hint of it in the <a href="https://wiki.openstreetmap.org/wiki/Notes">wiki page about Notes</a>, even in the Advanced Use. It seems to me I can't be the first person wanting to do this)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notes-api" rel="tag" title="see questions tagged &#39;notes-api&#39;">notes-api</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '19, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/cb99b2abaa73502ace0175863ca12b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcld&#39;s gravatar image" />
<p><span>mcld</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '19, 09:11</strong> </span></p>
</div>
</div>
<div id="comments-container-70249" class="comments-container">
&#10;</div>
<div id="comment-tools-70249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70249-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="70250"></span>

<div id="answer-container-70250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70250-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-70250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A nice web interface to search in the note text is here: <a href="https://ent8r.github.io/NotesReview/">https://ent8r.github.io/NotesReview/</a> and if you want to just access the API and get back an XML document, you can fire off a query like <a href="https://api.openstreetmap.org/api/0.6/notes/search?q=%22search+term+here%22&amp;closed=0">https://api.openstreetmap.org/api/0.6/notes/search?q=%22search+term+here%22&amp;closed=0</a> (details about the API are in <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API">https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '19, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '19, 09:19</strong> </span></p>
</div>
</div>
<div id="comments-container-70250" class="comments-container">
<span id="70251"></span>
<div id="comment-70251" class="comment">
<div id="post-70251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. The web interface didn't work for me (I filed an <a href="https://github.com/ENT8R/NotesReview/issues/34">issue here</a>) but I look forward to it working. The raw search is good to know. I wish it also had a bbox parameter! ... But then, that wasn't my question to you.</p>
</div>
<div id="comment-70251-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 09:55)</span> <span class="comment-user userinfo">mcld</span>
</div>
</div>
<span id="71526"></span>
<div id="comment-71526" class="comment">
<div id="post-71526-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks! Now on wiki: <a href="https://wiki.openstreetmap.org/wiki/Notes/Advanced_use#Search_for_Notes_with_a_keyword">https://wiki.openstreetmap.org/wiki/Notes/Advanced_use#Search_for_Notes_with_a_keyword</a></p>
</div>
<div id="comment-71526-info" class="comment-info">
<span class="comment-age">(07 Nov '19, 22:05)</span> <span class="comment-user userinfo">iriman</span>
</div>
</div>
</div>
<div id="comment-tools-70250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70250-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


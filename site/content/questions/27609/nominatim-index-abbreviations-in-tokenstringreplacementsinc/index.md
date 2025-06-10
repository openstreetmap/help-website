+++
type = "question"
title = "nominatim index abbreviations in tokenstringreplacements.inc"
description = '''Hi all I installed nominatim in a server..., in this route: /module/tokenstringreplacements.inc, I index a new abbreviations, a sample: str_replace(buffer, &amp;amp;len, &amp;amp;changes, &quot; diagonal &quot;, 10, &quot; diag &quot;, 6, 0); str_replace(buffer, &amp;amp;len, &amp;amp;changes, &quot; diagonal &quot;, 10, &quot; dg &quot;, 6, 0); str_repl...'''
date = "2013-10-29T01:33:00Z"
lastmod = "2013-10-29T17:09:00Z"
weight = 27609
keywords = [ "abbreviations", "nominatim", "name" ]
aliases = [ "/questions/27609" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nominatim index abbreviations in tokenstringreplacements.inc](/questions/27609/nominatim-index-abbreviations-in-tokenstringreplacementsinc)

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
<span id="post-27609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27609-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I installed nominatim in a server..., in this route: /module/tokenstringreplacements.inc, I index a new abbreviations, a sample:</p>
<p>str_replace(buffer, &amp;len, &amp;changes, " diagonal ", 10, " diag ", 6, 0); str_replace(buffer, &amp;len, &amp;changes, " diagonal ", 10, " dg ", 6, 0); str_replace(buffer, &amp;len, &amp;changes, " diagonal ", 10, " dig ", 6, 0);</p>
<p>I search by diagonal and diag in results OK, but a search a new created abbreviations "dg" and "dig" and NOT search...</p>
<p>is a /tokenstringreplacements.inc the data of abbreviations in search, or any other archive editet for the index abbreviations?</p>
<p>thanks</p>
<p>Alveniz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-abbreviations" rel="tag" title="see questions tagged &#39;abbreviations&#39;">abbreviations</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '13, 01:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8151a2cd9f1041f10b62d8ca446d3b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alveniz&#39;s gravatar image" />
<p><span>alveniz</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alveniz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27609" class="comments-container">
&#10;</div>
<div id="comment-tools-27609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27609-form-container" class="comment-form-container">
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

<span id="27616"></span>

<div id="answer-container-27616" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27616-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alveniz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>tokenstringreplacements.inc</code> is the right place for abbreviations but it is working in the opposite than what you seem to expect. What it does is to replace all unabbreviated terms with their short version. This way, only abbreviated versions of the names are saved in the database and equally the search terms are abbreviated before matching.</p>
<p>If in your case you want to be able to find "foo diagonal" also by typing "foo diag", "foo dig", and "foo dg", then all four terms have to be replaced with the same thing, so that they match. You should use the most ambiguous abbreviation as the common term, in this case "dg". So the replacements should be:</p>
<pre><code>str_replace(buffer, &amp;len, &amp;changes, &quot; diagonal &quot;, 10, &quot; dg &quot;, 4, 0); 
str_replace(buffer, &amp;len, &amp;changes, &quot; diag &quot;, 6, &quot; dg &quot;, 4, 0);
str_replace(buffer, &amp;len, &amp;changes, &quot; dig &quot;, 5, &quot; dg &quot;, 4, 0);</code></pre>
<p>Note that these changes have to be done before the import, as the normalization needs to be applied to the names in the imported OSM data as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '13, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27616" class="comments-container">
<span id="27636"></span>
<div id="comment-27636" class="comment">
<div id="post-27636-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Amigo muchas Gracias, Works...</p>
<p>Alveniz</p>
</div>
<div id="comment-27636-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 17:09)</span> <span class="comment-user userinfo">alveniz</span>
</div>
</div>
</div>
<div id="comment-tools-27616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27616-form-container" class="comment-form-container">
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


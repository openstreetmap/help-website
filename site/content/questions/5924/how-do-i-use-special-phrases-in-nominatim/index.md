+++
type = "question"
title = "How do I use special phrases in Nominatim?"
description = '''The Nominatim wiki page links to a page of special phrases that apparently can be used as part of a query. It doesn&#x27;t clearly explain how to use these phrases. So how would I for example search for JFK airport, or search for an address in a specific county with these special phrases?'''
date = "2011-06-21T13:51:00Z"
lastmod = "2011-06-22T11:34:00Z"
weight = 5924
keywords = [ "special-phrases", "nominatim" ]
aliases = [ "/questions/5924" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use special phrases in Nominatim?](/questions/5924/how-do-i-use-special-phrases-in-nominatim)

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
<span id="post-5924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5924-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim wiki page</a> links to a page of <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">special phrases</a> that apparently can be used as part of a query. It doesn't clearly explain how to use these phrases. So how would I for example search for JFK airport, or search for an address in a specific county with these special phrases?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-special-phrases" rel="tag" title="see questions tagged &#39;special-phrases&#39;">special-phrases</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '11, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/735a05084346db68dff750870654da3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Dearing&#39;s gravatar image" />
<p><span>Justin Dearing</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Dearing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5924" class="comments-container">
&#10;</div>
<div id="comment-tools-5924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5924-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="5927"></span>

<div id="answer-container-5927" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5927-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The phrases are used to search for other tags then the <em>name</em> tag. If you search for "airports in New York" you would get JFK, LaGuardia and Albany because they are airports (<em>amenity=airport</em>) in New York. It is used to better understand search terms and allows you to find e.g. "Hospitals near Central Park, New York" and get results even though none of them have the term "Hospital" in the name.</p>
<p>It also allows for multilingual search.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '11, 17:21</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-5927" class="comments-container">
<span id="5929"></span>
<div id="comment-5929" class="comment">
<div id="post-5929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So for address lookup input, you enter the values of the phrases freeform, like you do for regular address elements? Is their a methodology outside of the nominatim api where you can query a special phrases more specifically?</p>
</div>
<div id="comment-5929-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 17:42)</span> <span class="comment-user userinfo">Justin Dearing</span>
</div>
</div>
<span id="5933"></span>
<div id="comment-5933" class="comment">
<div id="post-5933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The nominatim special phrases are for better interaction with humens. What you want is probably more in the lines of the <a href="http://wiki.openstreetmap.org/wiki/Xapi">Xapi</a>.</p>
</div>
<div id="comment-5933-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 21:20)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5927-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5946"></span>

<div id="answer-container-5946" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5946-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "special phrases" described on the page you link are meant for manually entering queries (either on the Nominatim main page itself, or on the main OSM page, which also uses Nominatim).</p>
<p>They can be used to find objects of certain types (by searching for certain tags). Without them, you could only search objects by name, which does not allow things like searching for all hospitals or churches in a city.</p>
<blockquote>
<p>So how would I for example search for JFK airport, or search for an address in a specific county with these special phrases?</p>
</blockquote>
<p>Not at all :-). If you are looking for one specific objects, and you know its name, you don't need special phrases. Just use a normal search, which will automatically search by name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '11, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-5946" class="comments-container">
&#10;</div>
<div id="comment-tools-5946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5946-form-container" class="comment-form-container">
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


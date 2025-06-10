+++
type = "question"
title = "Wrong country boundaries"
description = '''If I tried to get Germany or France admin_level=2 (country boundaries) I got for Germany also Nederland.  For France I got also Italy and Nederland. Is it wrong data or my query is wrong? Check this under link: https://overpass-turbo.eu/s/1GCA Or there is the whole query you can try on: https://over...'''
date = "2024-01-30T09:48:00Z"
lastmod = "2024-02-01T14:45:00Z"
weight = 88216
keywords = [ "boundaries", "admin_level", "administrative", "query" ]
aliases = [ "/questions/88216" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wrong country boundaries](/questions/88216/wrong-country-boundaries)

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
<span id="post-88216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88216-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I tried to get Germany or France admin_level=2 (country boundaries) I got for Germany also Nederland. For France I got also Italy and Nederland. Is it wrong data or my query is wrong?</p>
<p>Check this under link: <a href="https://overpass-turbo.eu/s/1GCA">https://overpass-turbo.eu/s/1GCA</a></p>
<p>Or there is the whole query you can try on: <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a></p>
<p>Query:</p>
<pre><code>   [out:json][timeout:180];
   {{geocodeArea:Germany}}-&gt;.searchArea;
   (
       relation[admin_level=2][boundary=administrative][name](area.searchArea);
   );
   out geom;
   &gt;;
   out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '24, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/fb327fa88f2e7d6fefa4e6b418fecfa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0602Petr&#39;s gravatar image" />
<p><span>0602Petr</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0602Petr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88216" class="comments-container">
&#10;</div>
<div id="comment-tools-88216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88216-form-container" class="comment-form-container">
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

<span id="88220"></span>

<div id="answer-container-88220" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88220-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-88220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="0602Petr has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is expected. You are asking for boundaries partly or completely within the German boundary. Germany has a dispute with the Netherlands at the Dollard about the boundary. For that reason, in the OSM data a section of the Netherland's boundary is within German borders.</p>
<p>I expect a similar effect wrt France and Italy somewhere at the Montblanc. France and Netherlands is a surprise pair because the two countries only border in the Carribean (Saint Martin/Sint Maarten), and borders there are expected to be fitting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '24, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-88220" class="comments-container">
<span id="88221"></span>
<div id="comment-88221" class="comment">
<div id="post-88221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand , but is there a way (how to change the query) to get only Germany boundary?</p>
</div>
<div id="comment-88221-info" class="comment-info">
<span class="comment-age">(31 Jan '24, 10:08)</span> <span class="comment-user userinfo">0602Petr</span>
</div>
</div>
<span id="88224"></span>
<div id="comment-88224" class="comment">
<div id="post-88224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just query by name "Deutschland"? With tthe other criteria, you should get just <a href="https://www.openstreetmap.org/relation/51477">https://www.openstreetmap.org/relation/51477</a> .</p>
<p>I'm not sure why you were searching for "countries within Germany" - were you expecting to look elsewhere and search for enclaves, maybe?</p>
</div>
<div id="comment-88224-info" class="comment-info">
<span class="comment-age">(31 Jan '24, 14:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="88226"></span>
<div id="comment-88226" class="comment">
<div id="post-88226-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My goal is to find all regions and districts in Germany so I am trying to search all relations (with admin_level=4(6)) in Germany area. But I also get regions and districts from Nederland because of dispute boundary. The better way would be to search relations by tag (like: ['ISO3166-1'='DE']) but this tag is not represent on relations.</p>
</div>
<div id="comment-88226-info" class="comment-info">
<span class="comment-age">(01 Feb '24, 08:50)</span> <span class="comment-user userinfo">0602Petr</span>
</div>
</div>
</div>
<div id="comment-tools-88220" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88220-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88227"></span>

<div id="answer-container-88227" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have already found the solution how to query regions of Germany:</p>
<pre><code>[out:json][timeout:180];
area[&quot;ISO3166-1&quot;=&quot;DE&quot;]-&gt;.searchArea;
(
   relation[&quot;ISO3166-2&quot;~&quot;DE&quot;][admin_level=4][boundary=administrative][name](area.searchArea);
);
out geom;</code></pre>
<p>and than for each region relation I can query districts of that region:</p>
<pre><code>[out:json][timeout:180];
rel(28322); // relation id for &#39;Mecklenburg-Vorpommern&#39; region
map_to_area -&gt; .searchArea;  // map_to_area is mapping relation into area
(
   relation[admin_level=6][boundary=administrative][name](area.searchArea);
);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '24, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/fb327fa88f2e7d6fefa4e6b418fecfa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0602Petr&#39;s gravatar image" />
<p><span>0602Petr</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0602Petr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '24, 18:46</strong> </span></p>
</div>
</div>
<div id="comments-container-88227" class="comments-container">
&#10;</div>
<div id="comment-tools-88227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88227-form-container" class="comment-form-container">
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


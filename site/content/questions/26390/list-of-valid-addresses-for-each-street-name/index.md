+++
type = "question"
title = "list of valid addresses for each street name"
description = '''I&#x27;d like to list of valid addresses for each street name. Entering the street name and city would return a list of valid addresses. (abandoned/unused building are still valid and returned in the list). As an alternative option I&#x27;d like to enter street name,addresse and city and return true/false if ...'''
date = "2013-09-16T16:28:00Z"
lastmod = "2013-09-16T19:12:00Z"
weight = 26390
keywords = [ "source" ]
aliases = [ "/questions/26390" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [list of valid addresses for each street name](/questions/26390/list-of-valid-addresses-for-each-street-name)

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
<span id="post-26390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26390-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to list of valid addresses for each street name. Entering the street name and city would return a list of valid addresses. (abandoned/unused building are still valid and returned in the list).</p>
<p>As an alternative option I'd like to enter street name,addresse and city and return true/false if the addresse if valid/invalid</p>
<p>Thx :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '13, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e2905869cc2064b47c77d62d0ef48b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc0&#39;s gravatar image" />
<p><span>Marc0</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26390" class="comments-container">
&#10;</div>
<div id="comment-tools-26390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26390-form-container" class="comment-form-container">
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

<span id="26404"></span>

<div id="answer-container-26404" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26404-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a local copy of the OSM database, you can list all addresses by street name (and limited by a bounding box) using some quite simple queries, directly on the database. You can create your own local copy of the database using data from a country extract, or even the whole planet data.</p>
<p>I don't think there is any kind of support for this type of search in the standard API, and I believe there won't be any time soon.</p>
<p>However, even if you had the whole database loaded, most places do not have any street numbering information, and the places that have, only have the starting and ending street numbers for a street or street segment. That said, I believe OSM isn't suitable for this kind of search yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '13, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-26404" class="comments-container">
<span id="26406"></span>
<div id="comment-26406" class="comment">
<div id="post-26406-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, there is absolutely no guarantee that the addresses are really valid, since anyone can upload incorrect/incomplete/outdated information or make mistakes (minor and catastrophic as well).</p>
</div>
<div id="comment-26406-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 18:43)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-26404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26404-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26407"></span>

<div id="answer-container-26407" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26407-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> to query for all addresses of a given street an a given city. See this example query for all addresses in the street <em>Wartburgstraße</em> and city <em>Dresden</em>:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
  &lt;union&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;addr:city&quot; v=&quot;Dresden&quot;/&gt;
      &lt;has-kv k=&quot;addr:street&quot; v=&quot;Wartburgstraße&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;addr:city&quot; v=&quot;Dresden&quot;/&gt;
      &lt;has-kv k=&quot;addr:street&quot; v=&quot;Wartburgstraße&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;relation&quot;&gt;
      &lt;has-kv k=&quot;addr:city&quot; v=&quot;Dresden&quot;/&gt;
      &lt;has-kv k=&quot;addr:street&quot; v=&quot;Wartburgstraße&quot;/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>You can view a <a href="http://overpass-turbo.eu/s/13H">visualized result</a> using <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">overpass turbo</a>.</p>
<p>The Overpass API supports both JSON and XML as output formats. See the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">Overpass API language guide</a> for more information.</p>
<p>As already mentioned by MCPicoli: This result reflects only the addresses contained in OSM's database and doesn't have to be complete.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '13, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '13, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-26407" class="comments-container">
<span id="26409"></span>
<div id="comment-26409" class="comment">
<div id="post-26409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It would be great if São Paulo, Brazil had 10% of the data that Berlin has. Thanks for the tip on the Overpass API. I will try to install it on my local server and do some experimentation...</p>
</div>
<div id="comment-26409-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 19:12)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-26407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26407-form-container" class="comment-form-container">
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


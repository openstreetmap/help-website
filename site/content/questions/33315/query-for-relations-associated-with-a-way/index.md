+++
type = "question"
title = "Query for Relations Associated with A Way"
description = '''Hi OSM community, I am new here and would be grateful if you could help me with the following. Background I am developing an android app that uses OSM maps. (Using Nutiteq SDK) Question I would like to know how to query for the bus services (relations) associated with a way id. Example: With a way i...'''
date = "2014-05-20T10:51:00Z"
lastmod = "2014-06-16T20:00:00Z"
weight = 33315
keywords = [ "query" ]
aliases = [ "/questions/33315" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query for Relations Associated with A Way](/questions/33315/query-for-relations-associated-with-a-way)

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
<span id="post-33315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33315-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM community,</p>
<p>I am new here and would be grateful if you could help me with the following.</p>
<p><strong>Background</strong></p>
<p>I am developing an android app that uses OSM maps. (Using Nutiteq SDK)</p>
<p><strong>Question</strong></p>
<p>I would like to know how to query for the bus services (relations) associated with a way id.<br />
Example: With a way id, for example <em>157561015</em>, realize that bus services <em>170, 171, 184, ...</em> are associated with this way.</p>
<p><strong>Suggestions</strong></p>
<ol>
<li><p>I noticed that openstreetmap.org has the capability to perform such a query. See <a href="http://www.openstreetmap.org/way/157561015">http://www.openstreetmap.org/way/157561015</a> . Scroll down the "side-bar" to see relations</p></li>
<li><p>Convert OSM map data into a form that can be used to create a database. Is there an easy way of doing this? (for e.g. Spatialite?)</p></li>
</ol>
<p>Thank you for reading.</p>
<p>Regards, David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '14, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6226e9fe1bfbf1d10a7a17f59a84a659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidleejy&#39;s gravatar image" />
<p><span>davidleejy</span><br />
<span class="score" title="24 reputation points">24</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidleejy has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-33315" class="comments-container">
&#10;</div>
<div id="comment-tools-33315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33315-form-container" class="comment-form-container">
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

<span id="33322"></span>

<div id="answer-container-33322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33322-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ad 1.</p>
<p>The website obviously has access to the main database. For external apps that are not editors, we prefer (strongly) that you use the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">overpass-api</a>. You can use <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass turbo</a> to test your queries. <a href="http://overpass-turbo.eu/s/3sT">These are all the bus routes using way 157561015</a>.</p>
<p>If later your app becomes wildly successful, we actually prefer you setup your own database. ;)</p>
<p>ad 2.</p>
<p>I think you answered your own question: <a href="https://www.gaia-gis.it/fossil/spatialite-tools/wiki?name=spatialite_osm_raw">spatialite osm raw</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '14, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '14, 13:04</strong> </span></p>
</div>
</div>
<div id="comments-container-33322" class="comments-container">
<span id="33417"></span>
<div id="comment-33417" class="comment">
<div id="post-33417-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you cartinus.</p>
<p>A "relation" node in the response has "member role" elements like so:</p>
<p>¶</p>
<p>¶</p>
<p>&lt;relation id="1147131"&gt;</p>
<p>&lt;member role="" ref="174286674" type="way"/&gt;</p>
<p>&lt;member role="" ref="175840093" type="way"/&gt;</p>
<p>■</p>
<p>■</p>
<p>■</p>
<p>&lt;member role="stop" ref="410484491" type="node"/&gt;</p>
<p>&lt;tag v="WOODLANDS REG INT" k="from"/&gt;</p>
<p>&lt;tag v="Svc 961" k="name"/&gt;</p>
<p>&lt;tag v="SMRT" k="network"/&gt;</p>
<p>&lt;tag v="961" k="ref"/&gt;</p>
<p>&lt;tag v="bus" k="route"/&gt;</p>
<p>&lt;tag v="LORONG 1 GEYLANG TER" k="to"/&gt;</p>
<p>&lt;tag v="route" k="type"/&gt;</p>
<p>&lt;/relation&gt;</p>
<p>¶</p>
<p>¶</p>
<p>¶</p>
<p>Might you also know how to shorten the response by leaving out "member role" elements?</p>
</div>
<div id="comment-33417-info" class="comment-info">
<span class="comment-age">(23 May '14, 14:09)</span> <span class="comment-user userinfo">davidleejy</span>
</div>
</div>
<span id="34012"></span>
<div id="comment-34012" class="comment">
<div id="post-34012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is now a new feature in Overpass that gives you the relations without the members.</p>
<p>In stead of:</p>
<pre><code>(
  way(157561015);
  &lt;;
);
rel._[route=bus];
out;</code></pre>
<p>write:</p>
<pre><code>(
  way(157561015);
  &lt;;
);
rel._[route=bus];
out tags;</code></pre>
<p>The only change is the last word.</p>
</div>
<div id="comment-34012-info" class="comment-info">
<span class="comment-age">(16 Jun '14, 20:00)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33322-form-container" class="comment-form-container">
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


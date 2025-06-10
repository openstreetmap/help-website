+++
type = "question"
title = "Can i exclude the district borders extending on ocean in admin_level 5?"
description = '''Remove the extending border line on to the ocean  https://www.openstreetmap.org/#map=10/19.0751/84.7726&amp;amp;layers=N This is how i form layer  &amp;lt;Layer name=&quot;admin-5678&quot; status=&quot;on&quot; srs=&quot;&amp;amp;osm2pgsql_projection;&quot;&amp;gt;  &amp;lt;StyleName&amp;gt;admin-5678&amp;lt;/StyleName&amp;gt;  &amp;lt;Datasource&amp;gt;  &amp;lt;Paramete...'''
date = "2016-06-22T08:43:00Z"
lastmod = "2016-07-06T19:54:00Z"
weight = 50367
keywords = [ "openstreetmap", "mapnik" ]
aliases = [ "/questions/50367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can i exclude the district borders extending on ocean in admin_level 5?](/questions/50367/can-i-exclude-the-district-borders-extending-on-ocean-in-admin_level-5)

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
<span id="post-50367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50367-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-50367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Remove the extending border line on to the ocean</p>
<p><a href="https://www.openstreetmap.org/#map=10/19.0751/84.7726&amp;layers=N">https://www.openstreetmap.org/#map=10/19.0751/84.7726&amp;layers=N</a></p>
<p>This is how i form layer</p>
<pre><code>&lt;Layer name=&quot;admin-5678&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;admin-5678&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,admin_level
       from &amp;prefix;_roads
       where &quot;boundary&quot;=&#39;administrative&#39;
         and admin_level=&#39;5&#39;
       ) as admin&lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '16, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a497617ea77bb7f45521e5d4a97e8082?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZMapTeam&#39;s gravatar image" />
<p><span>ZMapTeam</span><br />
<span class="score" title="34 reputation points">34</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZMapTeam has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '16, 13:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-50367" class="comments-container">
<span id="50369"></span>
<div id="comment-50369" class="comment">
<div id="post-50369-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Is this a question, a suggestion, or...?</p>
</div>
<div id="comment-50369-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 09:01)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="50376"></span>
<div id="comment-50376" class="comment">
<div id="post-50376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Question ...presently facing issue</p>
</div>
<div id="comment-50376-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 10:26)</span> <span class="comment-user userinfo">ZMapTeam</span>
</div>
</div>
<span id="50377"></span>
<div id="comment-50377" class="comment">
<div id="post-50377-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to use more words explaining what the problem is, then. Is the map <em>data</em> wrong, or are you just asking about how it appears on a map, the <em>rendering</em> of it?</p>
</div>
<div id="comment-50377-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 10:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50380"></span>
<div id="comment-50380" class="comment not_top_scorer">
<div id="post-50380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ya sure.. When ever i set zoom to 7 in my map i could see the district borders extending on ocean.. U could see that clearly here - <a href="http://www.openstreetmap.org/#map=11/15.6799/80.6688">http://www.openstreetmap.org/#map=11/15.6799/80.6688</a> (lines with purple color)</p>
</div>
<div id="comment-50380-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 11:41)</span> <span class="comment-user userinfo">ZMapTeam</span>
</div>
</div>
<span id="50382"></span>
<div id="comment-50382" class="comment">
<div id="post-50382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You still need to use more words explaining what the problem is. You've included a "layer" definition in the question now, but what is that used with? How does (whatever that is) get its data? Is it something that you've downloaded, and if so what and from where?</p>
</div>
<div id="comment-50382-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 14:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50689"></span>
<div id="comment-50689" class="comment">
<div id="post-50689-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Related question: <a href="https://gis.stackexchange.com/questions/201120/i-want-to-remove-the-maritime-border-in-higher-admin-levels-4-using-carto-bo">https://gis.stackexchange.com/questions/201120/i-want-to-remove-the-maritime-border-in-higher-admin-levels-4-using-carto-bo</a></p>
</div>
<div id="comment-50689-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 19:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50367" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50367-form-container" class="comment-form-container">
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

<span id="50386"></span>

<div id="answer-container-50386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50386-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need to rewrite your stylesheet to either:</p>
<ul>
<li>Filter out borders with <code>boundary_type=territorial_waters</code> and <code>maritime=yes</code>, or</li>
<li>Render ocean areas <em>above</em> boundaries, not below them.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '16, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50386" class="comments-container">
<span id="50663"></span>
<div id="comment-50663" class="comment">
<div id="post-50663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i dont have a key called boundary_type and maritime in my planet_osm_roads table.</p>
</div>
<div id="comment-50663-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 11:13)</span> <span class="comment-user userinfo">ZMapTeam</span>
</div>
</div>
<span id="50668"></span>
<div id="comment-50668" class="comment">
<div id="post-50668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Richard's referring to values in the OSM data here, not in the imported rendering database. One option you have is to use lua tag transforms with osm2pgsql to convert values or remove things that you don't want to see:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md</a></p>
<p>Here, for example is how I remove all admin boundaries for use in a map style that I created for my own use:</p>
<p><a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L359">https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L359</a></p>
<p>Of course, you'd need to look at the data in OSM to make sure that it has tags that you can use for filtering.</p>
</div>
<div id="comment-50668-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 11:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50386-form-container" class="comment-form-container">
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


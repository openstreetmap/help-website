+++
type = "question"
title = "How to Render OSM Map tiles without text (osm2pgsql, mapnik, apache, mod_tile) ?"
description = '''Hello, I have setup a rendering stack (osm2pgsql, mapnik, apache, mod_tile) and am able to create a map for region specified by gps co-ordinates using render_list_geo.pl The maps look great! I used openstreetmap-carto style to render my map tiles.  Though I was interested to customize it by removing...'''
date = "2022-05-19T12:36:00Z"
lastmod = "2022-05-30T12:28:00Z"
weight = 84525
keywords = [ "xml", "text", "mapnik" ]
aliases = [ "/questions/84525" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to Render OSM Map tiles without text (osm2pgsql, mapnik, apache, mod_tile) ?](/questions/84525/how-to-render-osm-map-tiles-without-text-osm2pgsql-mapnik-apache-mod_tile)

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
<span id="post-84525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84525-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have setup a rendering stack (osm2pgsql, mapnik, apache, mod_tile) and am able to create a map for region specified by gps co-ordinates using render_list_geo.pl The maps look great! I used openstreetmap-carto style to render my map tiles.</p>
<p>Though I was interested to customize it by removing all text labels (street names, building names, park names, landmark names, all types of text). I have the XML files with me that go as input to Mapnik, though I am not sure what should I edit in them to disable the text completely.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '22, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d561310552086ae83097f8a3b8394be7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="royrod&#39;s gravatar image" />
<p><span>royrod</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="royrod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84525" class="comments-container">
&#10;</div>
<div id="comment-tools-84525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84525-form-container" class="comment-form-container">
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

<span id="84526"></span>

<div id="answer-container-84526" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="royrod has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have a couple of options:</p>
<ol>
<li>Remove the places where names are rendered from the .mss and .mml files (there will be quite a lot of these)</li>
<li>Edit the .lua file used when loading the database to rewrite the "name" and "ref" etc. with an empty string or delete those tags.</li>
</ol>
<p>The <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua#L63">OSM Carto lua</a> has a "delete tags" section; it might be as simple as adding "name" and "ref" to that list. If for any reason that does not work adding the code to change those tags to <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua#L285">filter_tags_generic</a> would.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '22, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '22, 12:58</strong> </span></p>
</div>
</div>
<div id="comments-container-84526" class="comments-container">
<span id="84529"></span>
<div id="comment-84529" class="comment">
<div id="post-84529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I followed step 2 and edited the Lua file. Then I ran osm2pgsql and used render_list_geo.pl Still my tiles have text labels at all places. Did I miss something ?</p>
</div>
<div id="comment-84529-info" class="comment-info">
<span class="comment-age">(19 May '22, 15:19)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
<span id="84544"></span>
<div id="comment-84544" class="comment">
<div id="post-84544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to be absolutely clear, you'll need to make sure you're not looking at cached information.</p>
<ul>
<li>after a change to the .lua you'll need to reload the data</li>
<li>you'll want to restart apache2 and renderd to make sure that you're serving fresh files</li>
<li>you'll want to delete existing meta tiles from below e.g. /var/lib/mod_tile/yourstylename</li>
<li>you'll want to make requests from an incognito browser and watch the server as it renders your new tile (hopefully without names)</li>
</ul>
</div>
<div id="comment-84544-info" class="comment-info">
<span class="comment-age">(20 May '22, 09:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84623"></span>
<div id="comment-84623" class="comment">
<div id="post-84623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This made it clear, thankyou for listing it down.</p>
</div>
<div id="comment-84623-info" class="comment-info">
<span class="comment-age">(30 May '22, 12:28)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
</div>
<div id="comment-tools-84526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84526-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84530"></span>

<div id="answer-container-84530" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84530-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My approach would have been to take the project.xml you have generated and - with a text editor - comment out all the occurrences of &lt;textsymbolizer ...=""&gt;. That is certainly a hack but should work nicely.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '22, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '22, 15:50</strong> </span></p>
</div>
</div>
<div id="comments-container-84530" class="comments-container">
<span id="84539"></span>
<div id="comment-84539" class="comment">
<div id="post-84539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to remove the lines corresponding to &lt;textsymbolizer ...=""&gt; in the XML file, after that I ran, render_list_geo.pl there were no changes in the rendered files.</p>
<p>I cleared all previous tiles from memory. Is there a way to apply the changes that were made.</p>
</div>
<div id="comment-84539-info" class="comment-info">
<span class="comment-age">(20 May '22, 01:57)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
<span id="84545"></span>
<div id="comment-84545" class="comment">
<div id="post-84545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How did you "clear all previous tiles from memory"? Try the list from the "Just to be absolutely clear" list in the other comment.</p>
</div>
<div id="comment-84545-info" class="comment-info">
<span class="comment-age">(20 May '22, 09:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84622"></span>
<div id="comment-84622" class="comment">
<div id="post-84622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This solution also worked for me thankyou for answering it</p>
</div>
<div id="comment-84622-info" class="comment-info">
<span class="comment-age">(30 May '22, 12:28)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
</div>
<div id="comment-tools-84530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84530-form-container" class="comment-form-container">
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


+++
type = "question"
title = "What does a Mapnik stylesheet rule look like?"
description = '''Can someone give an example? I am missing any OSM-specific docs around... I know I can download the real OpenStreetMap style but I do not really understand it. I am looking for a simpler example.'''
date = "2012-03-22T19:47:00Z"
lastmod = "2012-03-22T21:00:00Z"
weight = 11431
keywords = [ "rendering", "stylesheet", "mapnik" ]
aliases = [ "/questions/11431" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does a Mapnik stylesheet rule look like?](/questions/11431/what-does-a-mapnik-stylesheet-rule-look-like)

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
<span id="post-11431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11431-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can someone give an example? I am missing any OSM-specific docs around... I know I can download the real OpenStreetMap style but I do not really understand it. I am looking for a simpler example.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '12, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '12, 20:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-11431" class="comments-container">
&#10;</div>
<div id="comment-tools-11431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11431-form-container" class="comment-form-container">
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

<span id="11448"></span>

<div id="answer-container-11448" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11448-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-11448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is a simple example that I have taken from Jochen Topf's and my book, "OpenStreetMap - Using and Enhancing the Free Map of the World".</p>
<p>Suppose you have imported data with osm2pgsql, and you want to draw all roads (no matter what type of road) as a grey line. You would make a style like this:</p>
<pre><code>&lt;Style name=&quot;roads&quot;&gt;
  &lt;Rule&gt;
    &lt;LineSymbolizer&gt;
      &lt;CssParameter name=&quot;stroke&quot;&gt;#aaa&lt;/CssParameter&gt;
      &lt;CssParameter name=&quot;stroke-width&quot;&gt;0.4&lt;/CssParameter&gt;
    &lt;/LineSymbolizer&gt;
  &lt;/Rule&gt;
&lt;/Style&gt;</code></pre>
<p>You will need a layer definition to go with that:</p>
<pre><code>&lt;Layer name=&quot;roads&quot; status=&quot;on&quot; srs=&quot;+init=epsg:4326&quot;&gt;
  &lt;StyleName&gt;roads&lt;/StyleName&gt;
  &lt;Datasource&gt;
    &lt;Parameter name=&quot;table&quot;&gt;
    (select way from planet_osm_line where highway is not null) as road
    &lt;/Parameter&gt;
    &lt;Parameter name=&quot;type&quot;&gt;postgis&lt;/Parameter&gt;
    &lt;Parameter name=&quot;port&quot;&gt;5432&lt;/Parameter&gt;
    &lt;Parameter name=&quot;user&quot;&gt;osm&lt;/Parameter&gt;
    &lt;Parameter name=&quot;dbname&quot;&gt;osm&lt;/Parameter&gt;
    &lt;Parameter name=&quot;estimate_extent&quot;&gt;false&lt;/Parameter&gt;
    &lt;Parameter name=&quot;extent&quot;&gt;-180,-85,180,85&lt;/Parameter&gt;
  &lt;/Datasource&gt;
&lt;/Layer&gt;</code></pre>
<p>This assumes that there is a database called “osm” on the local PostGIS server, that the user “osm” has access to it, and that it has a table named planet_osm_line, populated with geometry data in the EPSG:4326 projection, from which we can load information about roads. This is exactly what Osm2pgsql produces when you run it with the --latlong option.</p>
<p>The next thing you will want to do is of course have different rules for different types of roads (probably using the &lt;filter&gt; element), and maybe different rules styles for different zoom levels (using the &lt;maxscaledenominator&gt; and &lt;minscaledenominator&gt; elements).</p>
<p>See the Mapnik documentation at <a href="https://github.com/mapnik/mapnik/wiki/">https://github.com/mapnik/mapnik/wiki/</a> for further details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '12, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11448" class="comments-container">
&#10;</div>
<div id="comment-tools-11448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11448-form-container" class="comment-form-container">
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


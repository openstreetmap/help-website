+++
type = "question"
title = "Polygons not getting rendered on my setup"
description = '''I have been building a tile server from scratch based on the instructions here: https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ Renderd runs, and the rendering process renders roads, streets names, etc., but it looks like all the polygons are missing (no forests, lakes, etc):  Rend...'''
date = "2019-09-25T15:59:00Z"
lastmod = "2019-10-15T08:03:00Z"
weight = 70916
keywords = [ "rendering", "renderd", "polygons", "osm2pgsql" ]
aliases = [ "/questions/70916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Polygons not getting rendered on my setup](/questions/70916/polygons-not-getting-rendered-on-my-setup)

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
<span id="post-70916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70916-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been building a tile server from scratch based on the instructions here: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Renderd runs, and the rendering process renders roads, streets names, etc., but it looks like all the polygons are missing (no forests, lakes, etc): <img src="/upfiles/MissingPolygons.png" alt="alt text" /></p>
<p>Renderd is not reporting any errors, and the osm2pgsql process likewise ran without issue. I used the following command for the import, with the standard OSM stylesheet:</p>
<pre><code>osm2pgsql -d gis --create --slim --hstore --tag-transform-script src/openstreetmap-carto/openstreetmap-carto.lua --flat-nodes planetnodes.bin -C 30000 --number-processes 8 -S src/openstreetmap-carto/openstreetmap-carto.style planet-latest.osm.pbf</code></pre>
<p>I'm not quite sure where I should start looking, since I'm not seeing any error messages. I may have made a stupid mistake somewhere, or maybe I got unlucky and grabbed a 'bad' version of one of the repositories?</p>
<p>I intend to make some tests soon, with a smaller import before I restart the entire import again (if that is indeed necessary). But if anyone has some idea of what may have gone wrong, I would appreciate the help!</p>
<p>(Edit) What I am looking for an answer to, as someone who is not an expert on the rendering process, which is more likely in this case? Is the import itself broken, or is something the rendering process (renderd) broken, or set up incorrectly</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '19, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ee79584621b1de369a8406f63f4842c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="praabjerg&#39;s gravatar image" />
<p><span>praabjerg</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="praabjerg has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '19, 17:13</strong> </span></p>
</div>
</div>
<div id="comments-container-70916" class="comments-container">
<span id="70917"></span>
<div id="comment-70917" class="comment">
<div id="post-70917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where did you get the data from? I would start with exact dataset from the tutorial to test it on something smaller than the whole world.</p>
</div>
<div id="comment-70917-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 16:39)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="70919"></span>
<div id="comment-70919" class="comment">
<div id="post-70919-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A hint - you don't have to drop the whole planet database in order to test another set of data, it's enough to temporary rename the database. I use a simple gis-swap.sh script which looks like this (I could use multiple names like planet/standard/small etc and name them as gis, but most of the time simple swapping two databases is enough for me):</p>
<pre><code>#!/bin/bash
&#10;sudo service postgresql restart
sudo -u postgres -H -- psql -c &quot;alter database gis rename to temp;&quot;
sudo -u postgres -H -- psql -c &quot;alter database gis2 rename to gis;&quot;
sudo -u postgres -H -- psql -c &quot;alter database temp rename to gis2;&quot;</code></pre>
</div>
<div id="comment-70919-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 17:06)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="70920"></span>
<div id="comment-70920" class="comment">
<div id="post-70920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's simply the Planet PBF file from <a href="https://planet.openstreetmap.org">https://planet.openstreetmap.org</a> And yes, I'm going to test with a smaller dataset when I can find the time for it. But I think what I'm looking for here, more specifically, is what this behaviour might indicate to someone experienced: Is this more likely to be an issue with the import itself, or the rendering process? I will add this to the question, for clarity.</p>
</div>
<div id="comment-70920-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 17:08)</span> <span class="comment-user userinfo">praabjerg</span>
</div>
</div>
<span id="70921"></span>
<div id="comment-70921" class="comment">
<div id="post-70921-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And that's definitely helpful! Thanks! It's such a simple thing, but I hadn't actually considered that you can just rename the database to test other imports.</p>
</div>
<div id="comment-70921-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 17:34)</span> <span class="comment-user userinfo">praabjerg</span>
</div>
</div>
<span id="70974"></span>
<div id="comment-70974" class="comment">
<div id="post-70974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What was the outcome? Does it look the same with some other data?</p>
</div>
<div id="comment-70974-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 17:52)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="70984"></span>
<div id="comment-70984" class="comment not_top_scorer">
<div id="post-70984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried importing Iceland, and now it looks like it should! But I ended up doing this on a more recent openstreetmap-carto pull. I realized too late that I should have used the same conditions for the test import, because now I don't remember the exact commit I used earlier for the full import. But as it turned out, I wasn't using an official release, just the latest commit. So maybe the lesson is that I really <em>should</em> just use the releases when doing this. I think I'm going to start another full import later today, then we shall have to see how that works out in a couple of days.</p>
</div>
<div id="comment-70984-info" class="comment-info">
<span class="comment-age">(01 Oct '19, 07:28)</span> <span class="comment-user userinfo">praabjerg</span>
</div>
</div>
</div>
<div id="comment-tools-70916" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70916-form-container" class="comment-form-container">
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

<span id="71178"></span>

<div id="answer-container-71178" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71178-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So, I ended up rerunning the entire import twice with a stable release of openstreetmap-carto. After the first rerun, tiles took <em>far</em> too long to render. I discovered that osm2pgsql seemed to have missed generating some of the indices. And generating them manually after the fact did not seem to fix rendering performance. On the 2nd rerun, I made absolutely sure that there would be space for everything, including the indices, on the disk. And now everything works!</p>
<p>So I think the reason for the polygons not rendering could be either</p>
<ul>
<li>that I had a development version of openstreetmap-carto from the repository that somehow broke the rendering process, or</li>
<li>that some of the indices were missing, and renderd hit a timeout on queries for the polygons, or something to that effect. Though that seems strange, as renderd didn't time out on the database generated from the 1st rerun, even when queries took a <em>long</em> time.</li>
</ul>
<p>In any case, this problem has been resolved now, and the rendering times are now reasonable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '19, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ee79584621b1de369a8406f63f4842c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="praabjerg&#39;s gravatar image" />
<p><span>praabjerg</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="praabjerg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71178" class="comments-container">
&#10;</div>
<div id="comment-tools-71178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71178-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Can&#x27;t get local OSM API server to return any map data"
description = '''I&#x27;m trying to set up my own Rails Port OSM API server as my application needs to make a very large number of map queries. I finally have everything looking like it should work but when I query a region of the map that has been populated from a .osm file using osm2pgsql I just get the wrapper nodes w...'''
date = "2016-08-06T01:45:00Z"
lastmod = "2016-08-08T21:02:00Z"
weight = 51272
keywords = [ "api", "local", "empty", "server" ]
aliases = [ "/questions/51272" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get local OSM API server to return any map data](/questions/51272/cant-get-local-osm-api-server-to-return-any-map-data)

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
<span id="post-51272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51272-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to set up my own Rails Port OSM API server as my application needs to make a very large number of map queries.</p>
<p>I finally have everything looking like it should work but when I query a region of the map that has been populated from a .osm file using osm2pgsql I just get the wrapper nodes with no actual content returned. It's as though the region I'm querying has not been populated with data.</p>
<p>The details:</p>
<p>I'm using an Ubuntu 16.04 running on a Virtual Machine.</p>
<p>I followed all steps described here: <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> . But I had to change a few things due to version and package name changes. So I ended up installing these:</p>
<pre><code>sudo apt-get install ruby libruby ruby-dev \
                 libmagickwand-dev libxml2-dev libxslt1-dev nodejs \
                 apache2 apache2-dev build-essential git-core \
                 postgresql postgresql-contrib libpq-dev postgresql-server-dev-all \
                 libsasl2-dev imagemagick
sudo gem install bundler</code></pre>
<p>I got error messages later on in the process regarding not having svgo installed, so I also ended up installing this to get rid of the errors:</p>
<pre><code>sudo apt-get install npm
sudo npm install -g svgo
&#10;# and due to https://github.com/nodejs/node-v0.x-archive/issues/3911 :
sudo ln -s /usr/bin/nodejs /usr/bin/node</code></pre>
<p>To fix some other errors I got when trying to run osm2pgsql I found I had to add PostGIS support to database:</p>
<pre><code>psql -U &lt;user&gt; &lt;database&gt;
e.g. psql -U myusername openstreetmap
at prompt type:
    CREATE EXTENSION postgis;
    \q      // to exit</code></pre>
<p>I got hold of the Bonn, Germany .osm.bz2 file from mapzen.com/data/metro-extracts/</p>
<p>I populated this into the database:</p>
<pre><code>osm2pgsql -s -U myusername -d openstreetmap bonn_germany.osm.bz2</code></pre>
<p>I carefully examined the log generated and there were no errors and the import seemed to be successful.</p>
<p>I started the Rails Port webserver: bundle exec rails server</p>
<p>From a webpage on the same PC I did a REST query for a small region that is inside Bonn:</p>
<pre><code>localhost:3000/api/0.6/map?bbox=7.0974,50.7321,7.0982,50.7325</code></pre>
<p>I got a response so I know the server is running, but the response just contained the following:</p>
<pre><code>   &lt;osm version=&quot;0.6&quot; generator=&quot;OpenStreetMap server&quot; copyright=&quot;OpenStreetMap and contributors&quot; attribution=&quot;http://www.openstreetmap.org/copyright&quot; license=&quot;http://opendatacommons.org/licenses/odbl/1-0/&quot;&gt;
&#10;        &lt;bounds minlat=&quot;50.7321&quot; minlon=&quot;7.0974&quot; maxlat=&quot;50.7325&quot; maxlon=&quot;7.0982&quot;&gt;
&#10;    &lt;/osm&gt;</code></pre>
<p>So I'm just getting the wrapper nodes with no data for the region inside the bounding box.</p>
<p>If I make the same query to the public server:</p>
<pre><code>www.openstreetmap.com/api/0.6/map?bbox=7.0974,50.7321,7.0982,50.7325</code></pre>
<p>Then I get a long list of nodes and ways from inside the bounding box as expected.</p>
<p>Any idea what I am doing wrong?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '16, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1f7eee70781fe255c6080ea67ac5e216?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techtonic&#39;s gravatar image" />
<p><span>techtonic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techtonic has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '16, 01:54</strong> </span></p>
</div>
</div>
<div id="comments-container-51272" class="comments-container">
<span id="51275"></span>
<div id="comment-51275" class="comment">
<div id="post-51275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Setting up a rails port just for a number of map calls seems to be quite a lot of overhead to me. I would possibly suggest to set up your own Overpass API instance and use the <a href="https://github.com/drolbr/Overpass-API/blob/master/src/cgi-bin/map">map call</a> available there. I may be a bit biased, though... Can you shed some light on how many calls you're planning to run per minute and what your coverage area looks like?</p>
</div>
<div id="comment-51275-info" class="comment-info">
<span class="comment-age">(06 Aug '16, 08:14)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51288"></span>
<div id="comment-51288" class="comment">
<div id="post-51288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> I need to perform a map query to get the nodes and ways (not interested in image tiles) on an array of approx 2km x 2km tiles covering most of central Europe. Plus we need to edit the database locally using other GIS tools in ways that would not be beneficial to the OSM community, so it would not be right to do it to the public copy. I am definitely looking at Overpass as a possibility for reading the finished map in a more efficient manner. I'm kinda new to OSM so still trying to figure out what is possible.</p>
</div>
<div id="comment-51288-info" class="comment-info">
<span class="comment-age">(07 Aug '16, 07:16)</span> <span class="comment-user userinfo">techtonic</span>
</div>
</div>
</div>
<div id="comment-tools-51272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51272-form-container" class="comment-form-container">
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

<span id="51286"></span>

<div id="answer-container-51286" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51286-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The rails port uses a database schema that is different from osm2pgsql's, hence osm2pgsql is the wrong tool to use if you want to populate a database for use with the rails port. You must use osmosis with the "APIDB" schema instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '16, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51286" class="comments-container">
<span id="51289"></span>
<div id="comment-51289" class="comment">
<div id="post-51289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I was not aware of that and it sounds like a probable cause of my problem. I did try using Osmosis to import a few times but had trouble getting it to connect to the postgresql database. I will try again when I get back to work next week.</p>
</div>
<div id="comment-51289-info" class="comment-info">
<span class="comment-age">(07 Aug '16, 07:20)</span> <span class="comment-user userinfo">techtonic</span>
</div>
</div>
<span id="51309"></span>
<div id="comment-51309" class="comment">
<div id="post-51309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I finally got osmosis to connect to database by removing password requirement from pg_hba.conf. Importing the same .osm file with osmosis works and now I am getting valid data returned :) Thanks for the help!</p>
</div>
<div id="comment-51309-info" class="comment-info">
<span class="comment-age">(08 Aug '16, 21:02)</span> <span class="comment-user userinfo">techtonic</span>
</div>
</div>
</div>
<div id="comment-tools-51286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51286-form-container" class="comment-form-container">
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


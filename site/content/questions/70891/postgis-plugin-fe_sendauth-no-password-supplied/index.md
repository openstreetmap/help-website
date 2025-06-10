+++
type = "question"
title = "Postgis Plugin: fe_sendauth: no password supplied"
description = '''Hello, I am using the instructions found at https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ to setup a OSM mapping server. If the ubuntu user matches the postgresql user ( i.e. renderaccount) everything works without any problems. However, I would like to get stuff to work where th...'''
date = "2019-09-23T13:07:00Z"
lastmod = "2019-09-23T20:48:00Z"
weight = 70891
keywords = [ "renderd", "postgresql", "postgis" ]
aliases = [ "/questions/70891" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Postgis Plugin: fe_sendauth: no password supplied](/questions/70891/postgis-plugin-fe_sendauth-no-password-supplied)

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
<span id="post-70891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70891-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am using the instructions found at <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> to setup a OSM mapping server. If the ubuntu user matches the postgresql user ( i.e. renderaccount) everything works without any problems.</p>
<p>However, I would like to get stuff to work where the ubuntu user is XXX and the postgresql user remains renderaccount.</p>
<p>I can get past most issues by:</p>
<ol>
<li><p>changing pg_hba.conf so:</p>
<pre><code>local   all             all                                     peer</code></pre>
<p>looks like:</p>
<pre><code>local   all             all                                     md5</code></pre></li>
<li><p>Setting the PGUSER environment variable to renderaccount</p></li>
<li><p>adding <em>:</em>:gis:renderaccount:&lt;password&gt; to ~/.pgpass</p></li>
</ol>
<p>However, when I am ready to startup the renderer by doing:</p>
<p>renderd -f -c /usr/local/etc/renderd.conf</p>
<p>I am presented with the errors:</p>
<pre><code>renderd[47532]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: fe_sendauth: no password supplied
Connection string: &#39; dbname=gis connect_timeout=4&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 765 of &#39;/home/lander/src/openstreetmap-carto-de/osm.xml&#39;
renderd[47532]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: fe_sendauth: no password supplied
Connection string: &#39; dbname=gis connect_timeout=4&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 765 of &#39;/home/lander/src/openstreetmap-carto-de/osm.xml&#39;
renderd[47532]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: fe_sendauth: no password supplied
Connection string: &#39; dbname=gis connect_timeout=4&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 765 of &#39;/home/lander/src/openstreetmap-carto-de/osm.xml&#39;
renderd[47532]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: fe_sendauth: no password supplied
Connection string: &#39; dbname=gis connect_timeout=4&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 765 of &#39;/home/lander/src/openstreetmap-carto-de/osm.xml&#39;</code></pre>
<p>I am assuming what is going on is that it is trying to talk to the database using the renderaccount user, but because there is a password, it cannot and does not try to look at the .pgpass file.</p>
<p>This seems to be an issue with postgis...</p>
<p>What might I need to change so the rendering system can use the specific user I specify?</p>
<p>Regards, Willie</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '19, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a9b35f68139efb13b1b91d5c7f012a1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Willie_H&#39;s gravatar image" />
<p><span>Willie_H</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Willie_H has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70891" class="comments-container">
&#10;</div>
<div id="comment-tools-70891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70891-form-container" class="comment-form-container">
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

<span id="70894"></span>

<div id="answer-container-70894" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Willie_H has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might have to add the username and password to the XML style that is processed my mapnik/renderd, or if you prefer add it to the project.mml file before you execute the "carto" command to process that into an XML file. There's a "osm2pgsql" section near the start of the mml file that has database access information:</p>
<pre><code>osm2pgsql: &amp;osm2pgsql
    type: &quot;postgis&quot;
    dbname: &quot;gis&quot;
    key_field: &quot;&quot;
    geometry_field: &quot;way&quot;
    user: &quot;renderaccount&quot;
    password: &quot;password&quot;
    extent: &quot;-20037508,-20037508,20037508,20037508&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '19, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '19, 19:43</strong> </span></p>
</div>
</div>
<div id="comments-container-70894" class="comments-container">
<span id="70895"></span>
<div id="comment-70895" class="comment">
<div id="post-70895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is what that section currently looks like in the project.mml I am using...</p>
<pre><code>osm2pgsql: &amp;osm2pgsql
    type: &quot;postgis&quot;
    dbname: &quot;gis&quot;
    key_field: &quot;&quot;
    geometry_field: &quot;way&quot;
    extent: &quot;-20037508,-20037508,20037508,20037508&quot;</code></pre>
<p>where is this section documented? I am not certain what the keys should be.</p>
</div>
<div id="comment-70895-info" class="comment-info">
<span class="comment-age">(23 Sep '19, 15:48)</span> <span class="comment-user userinfo">Willie_H</span>
</div>
</div>
<span id="70896"></span>
<div id="comment-70896" class="comment">
<div id="post-70896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. I was able to find the keys that one needed to use:</p>
<pre><code>osm2pgsql: &amp;osm2pgsql
    type: &quot;postgis&quot;
    dbname: &quot;gis&quot;
    key_field: &quot;&quot;
    geometry_field: &quot;way&quot;
    user: &quot;renderaccount&quot;
    password: &quot;password&quot;
    extent: &quot;-20037508,-20037508,20037508,20037508&quot;</code></pre>
<p>If you wanted to add this to your answer to make it complete, I will mark it as the answer.</p>
</div>
<div id="comment-70896-info" class="comment-info">
<span class="comment-age">(23 Sep '19, 16:10)</span> <span class="comment-user userinfo">Willie_H</span>
</div>
</div>
<span id="70898"></span>
<div id="comment-70898" class="comment">
<div id="post-70898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry for being imprecise, and glad you found it.</p>
</div>
<div id="comment-70898-info" class="comment-info">
<span class="comment-age">(23 Sep '19, 19:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70899"></span>
<div id="comment-70899" class="comment">
<div id="post-70899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Need one more detail. As it turns out, /etc/postgresql/10/main/pg_hba.conf needs to be edited as well to say:</p>
<pre><code>local   all             all                                     trust</code></pre>
<p>(Although, I am not quite sure why this is necessary and it may mean (checked at the moment) that the password entry in the osm2pgsql section is unnecessary.</p>
<p>Can you add that to your answer as well?</p>
</div>
<div id="comment-70899-info" class="comment-info">
<span class="comment-age">(23 Sep '19, 20:48)</span> <span class="comment-user userinfo">Willie_H</span>
</div>
</div>
</div>
<div id="comment-tools-70894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70894-form-container" class="comment-form-container">
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


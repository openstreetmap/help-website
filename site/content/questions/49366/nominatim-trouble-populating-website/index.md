+++
type = "question"
title = "Nominatim: Trouble populating website"
description = '''Hi all, I am encountering an annoying error while trying to populate the website (at http://localhost/nominatim). I followed all the instructions listed at link text but, at the moment I call ./utils/setup.php --create-website &amp;lt;Apache document root&amp;gt;/nominatim  I got the following error  WARNIN...'''
date = "2016-04-22T16:06:00Z"
lastmod = "2016-04-25T15:22:00Z"
weight = 49366
keywords = [ "setup", "warning", "localhost", "nominatim" ]
aliases = [ "/questions/49366" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim: Trouble populating website](/questions/49366/nominatim-trouble-populating-website)

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
<span id="post-49366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49366-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am encountering an annoying error while trying to populate the website (at <a href="http://localhost/nominatim).">http://localhost/nominatim).</a></p>
<p>I followed all the instructions listed at <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">link text</a> but, at the moment I call</p>
<pre><code>./utils/setup.php --create-website &lt;Apache document root&gt;/nominatim</code></pre>
<p>I got the following error</p>
<pre><code>WARNING: resetting threads to 1
Symlinks created
&#10;WARNING: Unable to access the website at http://localhost/nominatim/
You may want to update settings/local.php with @define(&#39;CONST_Website_BaseURL&#39;, &#39;http://[HOST]/[PATH]/&#39;);
Setup finished.</code></pre>
<p>I see that some files are generated, but not the tiles (i.e. tiles.js is not present).</p>
<p>My entry for this in apache2.conf is (I also tried to insert this into my 000-default.conf , but nothing has changed)</p>
<pre><code>    &lt; Directory /var/www/html/nominatim/&gt;
          Options MultiViews Indexes FollowSymLinks Includes ExecCGI
          AllowOverride AuthConfig FileInfo
          AddType text/html .php
          Require all granted
    &lt; /Directory&gt;</code></pre>
<p>While my local.php is</p>
<pre><code>// Paths
@define(&#39;CONST_Postgresql_Version&#39;, &#39;9.3&#39;);
@define(&#39;CONST_Postgis_Version&#39;, &#39;2.1&#39;);
&#10;// Website settings
@define(&#39;CONST_Website_BaseURL&#39;, &#39;http://localhost/nominatim/&#39;);</code></pre>
<p>Any hints about something else that I can check ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '16, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/dc400b116300e713442e10b6d3c1dfe4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GabBurnout&#39;s gravatar image" />
<p><span>GabBurnout</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GabBurnout has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '16, 08:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-49366" class="comments-container">
&#10;</div>
<div id="comment-tools-49366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49366-form-container" class="comment-form-container">
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

<span id="49380"></span>

<div id="answer-container-49380" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49380-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is a search engine only and not a tile server. Hence it does not generate tiles. A typical local installation of a Nominatim server will load search results from your own server, but map tiles from OpenStreetMap over the web.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '16, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49380" class="comments-container">
<span id="49405"></span>
<div id="comment-49405" class="comment">
<div id="post-49405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer,</p>
<p>I just followed step by step the installation guide where, in the <strong>Import and index OSM data</strong> section indicates to run the command the import of the osm file.</p>
<p>Then, into the <strong>Set up the website</strong> section, the command for populating the website is explained.</p>
<p>Is this the command supposed to be executed in order to import the tiles into the website folder ? Or the first ?</p>
<p>Thanks again,</p>
<p>Cheers</p>
</div>
<div id="comment-49405-info" class="comment-info">
<span class="comment-age">(25 Apr '16, 12:07)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
<span id="49406"></span>
<div id="comment-49406" class="comment">
<div id="post-49406-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim does not include tiles, and the setup-website command only creates a couple of symlinks so that you can use the search through a web browser and your local Apache web server.</p>
</div>
<div id="comment-49406-info" class="comment-info">
<span class="comment-age">(25 Apr '16, 12:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="49411"></span>
<div id="comment-49411" class="comment">
<div id="post-49411-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looking into the setup.php file, I can notice that, for the website population, a check for the presence of the file js/tiles.js is performed. In my case, it's the root of my problems (I think) because I don't have this one.</p>
<p>Am I supposed to install a map server (like <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">in here</a> for instance) to have it ?</p>
<p>Cheers,</p>
<p>G.</p>
</div>
<div id="comment-49411-info" class="comment-info">
<span class="comment-age">(25 Apr '16, 15:07)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
<span id="49412"></span>
<div id="comment-49412" class="comment">
<div id="post-49412-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I see. It appears that something has been recently changed in Nominatim and the check whether --setup-website has succeeded still looks for a tiles.js file which doesn't exist anymore. I recommend you raise this issue on the <a href="https://github.com/twain47/Nominatim/issues">Nominatim bug tracker.</a></p>
</div>
<div id="comment-49412-info" class="comment-info">
<span class="comment-age">(25 Apr '16, 15:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49380-form-container" class="comment-form-container">
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


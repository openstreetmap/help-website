+++
type = "question"
title = "How do I configure renderd and mod_tile for postgresql running on non default socket?"
description = '''I have a tile server I&#x27;ve built on Ubuntu 18.04LTS using steps/sources from here.  Here is where I differed. I added a postgres cluster on another filesystem, and added the service on port 5433. Using a global environment variable, I set PGPORT to 5433; issuing psql loads up the correct database. Os...'''
date = "2018-06-15T16:35:00Z"
lastmod = "2018-06-16T15:56:00Z"
weight = 64223
keywords = [ "manual", "renderd", "config", "postgresql" ]
aliases = [ "/questions/64223" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I configure renderd and mod_tile for postgresql running on non default socket?](/questions/64223/how-do-i-configure-renderd-and-mod_tile-for-postgresql-running-on-non-default-socket)

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
<span id="post-64223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64223-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a tile server I've built on Ubuntu 18.04LTS using steps/sources from <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#mod_tile_and_renderd">here</a>.</p>
<p>Here is where I differed. I added a postgres cluster on another filesystem, and added the service on port 5433. Using a global environment variable, I set PGPORT to 5433; issuing <code>psql</code> loads up the correct database. <code>Osm2pgsql</code> and subsequent database updates appear to be working fine.</p>
<p>However, <code>renderd</code> does not like my setup:</p>
<pre><code>An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: FATAL:  role &quot;tile_server&quot; does not exist
                                      Connection string: &#39; dbname=gis connect_timeout=4&#39;
                                        encountered during parsing of layer &#39;landcover&#39; in Layer at line 1026 of &#39;/home/tile_server/src/openstreetmap-carto-AJT/mapnik.xml&#39;</code></pre>
<p>I figured this error is occurring because <code>renderd</code> has accessed the default postgresql database.</p>
<p>I grep'd source code looking for a hardcoded port, but it didn't jump out at me.</p>
<p>So, I started looking for <code>renderd.conf</code> options. I'm trying to find man page <code>renderd.conf</code> but no luck so far.</p>
<p>Specifically:</p>
<ol>
<li>Do you see a different explanation for my error that I should be researching?</li>
<li>Is there a <code>renderd.conf</code> option to specify the postgres port?</li>
<li>Ummm, where do I find the man page for <code>renderd.conf</code>?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-manual" rel="tag" title="see questions tagged &#39;manual&#39;">manual</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-config" rel="tag" title="see questions tagged &#39;config&#39;">config</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '18, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-64223" class="comments-container">
&#10;</div>
<div id="comment-tools-64223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64223-form-container" class="comment-form-container">
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

<span id="64225"></span>

<div id="answer-container-64225" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64225-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tim_rohrer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a <code>renderd</code> issue; <code>renderd</code> doesn't know what PostgreSQL even is. The code responsible for connecting to PostgreSQL is in the mapnik rendering library, and controlled by your style file (mapnik.xml). You can configure a port in the <code>&lt;Datasource&gt;</code> section of your style file, as per the documentation here: <a href="https://github.com/mapnik/mapnik/wiki/PostGIS">https://github.com/mapnik/mapnik/wiki/PostGIS</a></p>
<p>If your XML is generated from a .mml/.yml file using the carto compiler, then you have to set the port in your .mml/.yml file accordingly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '18, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64225" class="comments-container">
<span id="64227"></span>
<div id="comment-64227" class="comment">
<div id="post-64227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My XML is generated from the <code>project.mml</code> provided in <code>openstreetmap-carto-AJT</code>.</p>
<p>From my read of the link, in the Layer section of the MML, I should add attributes for the Datasource.</p>
<p>Do I have to add <code>"port": "5433",</code> in every single section for which there is a Datasource of type postgis? Or is there a way to do this globally?</p>
<p>And thank you for helping me understand the dependencies!</p>
</div>
<div id="comment-64227-info" class="comment-info">
<span class="comment-age">(16 Jun '18, 04:02)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="64228"></span>
<div id="comment-64228" class="comment">
<div id="post-64228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Never tried it, but a quick web search finds <a href="/questions/54587/how-to-use-xml-file-generated-by-openstreetmap-carto-with-mapnik-and-postgis">this</a> which has a syntax for "port" in a project.mml.</p>
</div>
<div id="comment-64228-info" class="comment-info">
<span class="comment-age">(16 Jun '18, 10:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64229"></span>
<div id="comment-64229" class="comment">
<div id="post-64229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. I promise I had been doing a lot of web searching when I wrote the comment. :-) That post had not come up. Interestingly, I had tried to add some lines to the JSON, but carto wasn't liking what I was doing.</p>
<p>Then I came across (this)[<a href="https://cartocss.readthedocs.io/en/latest/mml.html%5D">https://cartocss.readthedocs.io/en/latest/mml.html]</a> which seemed to suggest the file needed to be in yaml to have global-like settings. I converted the project.mml to yaml, but haven't tested it with carto yet.</p>
<p>I did do a global replace to add the port settings after the type line (70 replacements), and that seems to have worked. Not very elegant :-) If I come up with a better process, I'll come back here an post a complete answer for future searchers.</p>
</div>
<div id="comment-64229-info" class="comment-info">
<span class="comment-age">(16 Jun '18, 15:56)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-64225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64225-form-container" class="comment-form-container">
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


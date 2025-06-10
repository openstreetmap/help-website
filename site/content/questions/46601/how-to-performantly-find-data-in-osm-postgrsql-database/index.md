+++
type = "question"
title = "How to performantly find data in osm postgrsql database?"
description = '''Hello everyone. In case that on the way to the select something went wront, here are the steps i used to populate my database: 1) I downloaded the germany-latest.osm from geofabrik and used osmfilter on it, to reduce the amount of data. Because less data can&#x27;t be bad, right? The used command is: osm...'''
date = "2015-11-15T20:57:00Z"
lastmod = "2015-11-16T20:05:00Z"
weight = 46601
keywords = [ "postgresql", "postgis", "sql" ]
aliases = [ "/questions/46601" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to performantly find data in osm postgrsql database?](/questions/46601/how-to-performantly-find-data-in-osm-postgrsql-database)

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
<span id="post-46601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>In case that on the way to the select something went wront, here are the steps i used to populate my database:</p>
<p>1) I downloaded the germany-latest.osm from geofabrik and used osmfilter on it, to reduce the amount of data. Because less data can't be bad, right? The used command is:</p>
<pre><code>osmfilter D:\osm\germany-latest.osm --keep= --keep-ways=&quot;water= or waterway= or natural= or leisure= or landuse= or landcover=&quot; --keep-relations=&quot;water= or natural= or leisure= or landuse= or landcover= or waterway=&quot; -o=D:\osm\germany-filtered.osm</code></pre>
<p>2) I importet the data into a default installation of postgrsql + postgis with cygwin. The used command, which didn't show any errors is:</p>
<pre><code>osm2pgsql.exe d:\osm\germany-filtered.osm -d osm -U postgres -P 5432 -S d:\osm\default.style --hstore --keep-coastlines --host localhost</code></pre>
<p>Now i have, as far as i can tell by looking into it with pgAdmin, a database with all the data i want to use. But accessing those data is terrible slow and i have no idea why. Is it that I'm not using an ssd? Is something wrong with my SQL command? Either way, it takes 48-50s to get data, no matter how often i've executed it before. Shouldn't some form of caching kick in when i fire the same request repeadetly? On the good side, after a bit of playing around the data aquired by that sql command seems to be correct :-).</p>
<pre><code>Select * from planet_osm_polygon z where ST_DWITHIN(Geography(ST_Transform(z.way,4326)), T_GeographyFromText(&#39;POINT(7.46362209 51.47892401)&#39;),500);</code></pre>
<p>What I'm trying to get is "everything within 500m of coordinate" and i would like to get this kinda faster than those 48-50s... especially since theres going to be more than 1 concurrent request at a time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '15, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-46601" class="comments-container">
<span id="46606"></span>
<div id="comment-46606" class="comment">
<div id="post-46606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could likely skip the "osmfilter" step by writing a good style file for the osm2pgsql import.</p>
</div>
<div id="comment-46606-info" class="comment-info">
<span class="comment-age">(15 Nov '15, 22:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46601-form-container" class="comment-form-container">
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

<span id="46605"></span>

<div id="answer-container-46605" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46605-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="EinFreierNick has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>PostGIS will normally use spatial indexes to speed up these types of queries. These indexes have been created by osm2pgsql but your query is formulated in a way that renders them ineffective. Hence PostGIS must actually compute the difference between your point and every single polygon in the database.</p>
<p>Your database is in Mercator metres since you haven't specified "-l" on import. Therefore, do</p>
<pre><code>SELECT * FROM planet_osm_polygon 
WHERE ST_DWITHIN(way, 
   ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(7.46362209,51.47892401),4326),3857), 500);</code></pre>
<p>to utilize the index. If you are worried about the discrepancy between Mercator metres and real metres, you can still use a more precise calculation based on ST_DWITHIN or ST_DISTANCE with geography data types, but only <em>after</em> you have filtered out the candidate objects with the index - i.e. you might use a distance of 1000 in the query above, and then add your WHERE condition at the end.</p>
<p>Use the <code>EXPLAIN</code> command to have PostGIS tell you whether it can use an index. EXPLAIN is a science unto itself but as a rule of thumb, anything that says "sequential scan" in there means slowness.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '15, 22:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46605" class="comments-container">
<span id="46620"></span>
<div id="comment-46620" class="comment">
<div id="post-46620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>executing that commands give me the following error message:</p>
<p>ERROR: Operation on mixed SRID geometries <strong><em>*</em></strong> <strong><em>Error</em></strong> <strong><em>*</em></strong></p>
<p>ERROR: Operation on mixed SRID geometries SQL state: XX000</p>
</div>
<div id="comment-46620-info" class="comment-info">
<span class="comment-age">(16 Nov '15, 16:50)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
<span id="46622"></span>
<div id="comment-46622" class="comment">
<div id="post-46622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if i switch positions for 4326 and 3857, the query executes - but delivers no results no matter how high i set the meteres</p>
</div>
<div id="comment-46622-info" class="comment-info">
<span class="comment-age">(16 Nov '15, 17:45)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
<span id="46626"></span>
<div id="comment-46626" class="comment">
<div id="post-46626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might have imported your database in 900913 not 3857 - try switching 3857 in my example to 900913. Both are equal but PostGIS doesn't know.</p>
</div>
<div id="comment-46626-info" class="comment-info">
<span class="comment-age">(16 Nov '15, 19:02)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46629"></span>
<div id="comment-46629" class="comment">
<div id="post-46629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah :) This works. Execution time for the first execution was 72ms. Every execution afterwards was 23-25ms. That is a time that allows me to go further :) THANK YOU.</p>
</div>
<div id="comment-46629-info" class="comment-info">
<span class="comment-age">(16 Nov '15, 20:05)</span> <span class="comment-user userinfo">EinFreierNick</span>
</div>
</div>
</div>
<div id="comment-tools-46605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46605-form-container" class="comment-form-container">
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


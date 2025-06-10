+++
type = "question"
title = "nominatim setup problem"
description = '''Hi everyone. I tried to install nominatim using ./utils/setup.php --osm-file &amp;lt;your planet=&quot;&quot; file=&quot;&quot;&amp;gt; --all I changed CONST pathes to(where all except osmosis are located)   @define(&#x27;CONST_Postgresql_Version&#x27;, &#x27;8.4&#x27;);  @define(&#x27;CONST_Path_Postgresql_Contrib&#x27;, &#x27;/usr/share/postgresql/&#x27;.CONST_Pos...'''
date = "2012-04-11T14:02:00Z"
lastmod = "2012-04-12T07:43:00Z"
weight = 11898
keywords = [ "nominatim", "planet_osm" ]
aliases = [ "/questions/11898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim setup problem](/questions/11898/nominatim-setup-problem)

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
<span id="post-11898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11898-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>I tried to install nominatim using ./utils/setup.php --osm-file &lt;your planet="" file=""&gt; --all I changed CONST pathes to(where all except osmosis are located)</p>
<pre><code> @define(&#39;CONST_Postgresql_Version&#39;, &#39;8.4&#39;);
    @define(&#39;CONST_Path_Postgresql_Contrib&#39;, &#39;/usr/share/postgresql/&#39;.CONST_Postgresql_Version.&#39;/contr$
    @define(&#39;CONST_Path_Postgresql_Postgis&#39;, CONST_Path_Postgresql_Contrib.&#39;&#39;);
    @define(&#39;CONST_Osm2pgsql_Binary&#39;,&#39;/bin/osm2pgsql/osm2pgsql&#39;);
    @define(&#39;CONST_Osmosis_Binary&#39;, CONST_BasePath.&#39;/osmosis-0.38/bin/osmosis&#39;);</code></pre>
<p>And got strange answer from nominatim</p>
<pre><code>.........
SET
CREATE TABLE
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
Import
Using projection SRS 4326 (Latlong)
NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Out of memory for dense node cache, reduce --cache size
Error occurred, cleaning up
osm2pgsql SVN version 0.80.0 (32bit id space)
&#10;ERROR: No Data</code></pre>
<p>Also for planet_osm db I used to have 900913 projection. How can I manage with this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '12, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/04a50c0f1ba0dbf4a36e948646b8f47d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzzzteph&#39;s gravatar image" />
<p><span>zzzzteph</span><br />
<span class="score" title="30 reputation points">30</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzzzteph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11898" class="comments-container">
&#10;</div>
<div id="comment-tools-11898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11898-form-container" class="comment-form-container">
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

<span id="11922"></span>

<div id="answer-container-11922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11922-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That error has two possible causes:</p>
<ol>
<li>You are running out of physical memory. Supply more swap space. When importing the planet, RAM + swap should amount to at least 30GB. If you are importing something smaller, you might try to reduce osm2pgsql's cache. In the most recent version of Nominatim, you can add the <code>--osm2pgsql-cache</code> parameter when calling setup.php. The default is 15000 (MB), try something smaller.</li>
<li>You have compiled osm2pgsql in 32-bit mode and now you are running out of virtual memory. Check the output of: <code>file osm2pgsql</code>. If it says <code>ELF 32-bit</code>, you need to recompile osm2pgsql.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '12, 07:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-11922" class="comments-container">
&#10;</div>
<div id="comment-tools-11922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11922-form-container" class="comment-form-container">
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


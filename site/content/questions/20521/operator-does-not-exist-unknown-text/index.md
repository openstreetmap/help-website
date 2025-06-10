+++
type = "question"
title = "operator does not exist: unknown =&gt; text"
description = '''Hi for all. When I run: $ ./setup.php --osm-file poland.osm.bz2 --all script is running until: ... Strict Standards: Non-static method DB::isError() should not be called statically in /usr/share/php/DB.php on line 557 PHP Strict Standards: Non-static method PEAR::isError() should not be called stati...'''
date = "2013-03-06T09:59:00Z"
lastmod = "2013-03-06T13:10:00Z"
weight = 20521
keywords = [ "operator", "nominatim", "postcode", "pg_query", "name" ]
aliases = [ "/questions/20521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [operator does not exist: unknown =\> text](/questions/20521/operator-does-not-exist-unknown-text)

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
<span id="post-20521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi for all. When I run:</p>
<p>$ ./setup.php --osm-file poland.osm.bz2 --all</p>
<p>script is running until:</p>
<p>...</p>
<p>Strict Standards: Non-static method DB::isError() should not be called statically in /usr/share/php/DB.php on line 557 PHP Strict Standards: Non-static method PEAR::isError() should not be called statically in /home/nominatim/lib/db.php on line 8</p>
<p>Strict Standards: Non-static method PEAR::isError() should not be called statically in /home/nominatim/lib/db.php on line 8 PHP Strict Standards: Non-static method DB::isManip() should not be called statically, assuming $this from incompatible context in /usr/share/php/DB/common.php on line 2200</p>
<p>Strict Standards: Non-static method DB::isManip() should not be called statically, assuming $this from incompatible context in /usr/share/php/DB/common.php on line 2200</p>
<p>PHP Strict Standards: Non-static method DB::isManip() should not be called statically, assuming $this from incompatible context in /usr/share/php/DB/common.php on line 2200</p>
<p>Strict Standards: Non-static method DB::isManip() should not be called statically, assuming $this from incompatible context in /usr/share/php/DB/common.php on line 2200</p>
<p><strong>PHP Warning: pg_query(): Query failed: ERROR: operator does not exist: unknown =&gt; text LINE 1: SELECT 'ref'=&gt;NEW.postcode</strong></p>
<pre><code>    ^</code></pre>
<p>HINT: No operator matches the given name and argument type(s). You might need to add explicit type casts. QUERY: SELECT 'ref'=&gt;NEW.postcode CONTEXT: PL/pgSQL function placex_insert() line 84 at assignment in /home/nominatim/utils/setup.php on line 455</p>
<p><strong>Warning: pg_query(): Query failed: ERROR: operator does not exist: unknown =&gt; text LINE 1: SELECT 'ref'=&gt;NEW.postcode</strong></p>
<pre><code>   ^</code></pre>
<p>HINT: No operator matches the given name and argument type(s). You might need to add explicit type casts. QUERY: SELECT 'ref'=&gt;NEW.postcode CONTEXT: PL/pgSQL function placex_insert() line 84 at assignment in /home/nominatim/utils/setup.php on line 455 ERROR: ERROR: operator does not exist: unknown =&gt; text LINE 1: SELECT 'ref'=&gt;NEW.postcode ^</p>
<p>HINT: No operator matches the given name and argument type(s). You might need to add explicit type casts. QUERY: SELECT 'ref'=&gt;NEW.postcode CONTEXT: PL/pgSQL function placex_insert() line 84 at assignment ERROR: operator does not exist: unknown =&gt; text LINE 1: SELECT 'ref'=&gt;NEW.postcode ^</p>
<p>HINT: No operator matches the given name and argument type(s). You might need to add explicit type casts. QUERY: SELECT 'ref'=&gt;NEW.postcode CONTEXT: PL/pgSQL function placex_insert() line 84 at assignment</p>
<p>END OF LOGS</p>
<p>From setup.php I can see that it is breaking down somewhere in --load-data function. Earlier tasks run just fine.</p>
<p>I also found in nominatim/sql/functions.sql, in line 982:</p>
<p>NEW.name := 'ref'=&gt;NEW.postcode;</p>
<p>My software (system is gentoo):</p>
<p>mapnik-2.1.0</p>
<p>postgis-2.0.2-r2</p>
<p>osm2pgsql version from <a href="http://svn.openstreetmap.org/applications/utils/export/osm2pgsql/" title="title">svn sources</a> (tried with and without --64bit-ids support compiled in, same result)</p>
<p>postgres-9.2</p>
<p>geos-3.3.3</p>
<p>libxml2-2.9.0-r2</p>
<p>pear-1.9.4</p>
<p>PEAR-DB-1.7.14</p>
<p>PEAR-MDB2_Driver_pgsql-1.5.0_beta3</p>
<p>php-5.4.8</p>
<p><strong>What is wrong?</strong></p>
<p>In nominatim sources I have made a change:</p>
<ol>
<li>Using sed: www-data -&gt; osmuser but this shouldn't break anything.</li>
</ol>
<p>Also in postgres, in pg_operator table I <strong>can't find</strong> '=&gt;' operator but I didn't modify anything there. Any help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-operator" rel="tag" title="see questions tagged &#39;operator&#39;">operator</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-pg_query" rel="tag" title="see questions tagged &#39;pg_query&#39;">pg_query</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '13, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/dac1e1598195ef62ce74c782c0bbe536?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myvupln&#39;s gravatar image" />
<p><span>myvupln</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myvupln has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20521" class="comments-container">
&#10;</div>
<div id="comment-tools-20521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20521-form-container" class="comment-form-container">
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

<span id="20522"></span>

<div id="answer-container-20522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20522-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Support for postgresql versions &gt;= 9.2 and postgis &gt;= 2.0 has only been recently added to Nominatim. Please try the latest development version from github.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '13, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-20522" class="comments-container">
<span id="20526"></span>
<div id="comment-20526" class="comment">
<div id="post-20526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks for quick response.</p>
<p>I had Nominatim from <span>git://github.com/twain47/Nominatim.git.</span></p>
<p>I used version: Nominatim-2.0.0 (from tag).</p>
<p>After checkout to master (so now I am using the latest commit):</p>
<p>ERROR: PostGIS version is not correct. Expected 1.5 found 2.0</p>
<p>So currently I need to switch to postgis-1.5.3 from postgis-2.0.0 :(</p>
<p>Thanks for Your help.</p>
</div>
<div id="comment-20526-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 13:01)</span> <span class="comment-user userinfo">myvupln</span>
</div>
</div>
<span id="20527"></span>
<div id="comment-20527" class="comment">
<div id="post-20527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I thought. This requires also downgrade of whole postgresql-server to version 9.1.x due to postgis dependency and so on, and so on...</p>
</div>
<div id="comment-20527-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 13:09)</span> <span class="comment-user userinfo">myvupln</span>
</div>
</div>
<span id="20528"></span>
<div id="comment-20528" class="comment">
<div id="post-20528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to change the postgis version in your settings/local.php. Just copy the relevant line from settings/settings.php and change the version to 2.0.</p>
</div>
<div id="comment-20528-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 13:10)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-20522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20522-form-container" class="comment-form-container">
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


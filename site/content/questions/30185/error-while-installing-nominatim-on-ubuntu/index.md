+++
type = "question"
title = "Error while installing Nominatim on ubuntu"
description = '''Using projection SRS 4326 (Latlong) NOTICE: table &quot;place&quot; does not exist, skipping NOTICE: type &quot;keyvalue&quot; does not exist, skipping NOTICE: type &quot;wordscore&quot; does not exist, skipping NOTICE: type &quot;stringlanguagetype&quot; does not exist, skipping NOTICE: type &quot;keyvaluetype&quot; does not exist, skipping NOTICE...'''
date = "2014-01-24T13:59:00Z"
lastmod = "2014-01-25T06:49:00Z"
weight = 30185
keywords = [ "nominatim", "ubuntu" ]
aliases = [ "/questions/30185" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while installing Nominatim on ubuntu](/questions/30185/error-while-installing-nominatim-on-ubuntu)

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
<span id="post-30185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using projection SRS 4326 (Latlong)</p>
<pre><code>NOTICE:  table &quot;place&quot; does not exist, skipping
NOTICE:  type &quot;keyvalue&quot; does not exist, skipping
NOTICE:  type &quot;wordscore&quot; does not exist, skipping
NOTICE:  type &quot;stringlanguagetype&quot; does not exist, skipping
NOTICE:  type &quot;keyvaluetype&quot; does not exist, skipping
NOTICE:  function get_connected_ways(pg_catalog.int4[]) does not exist, skipping
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Out of memory for dense node cache, reduce --cache size
Error occurred, cleaning up
ERROR: Error executing external command: /home/nominatim/Nominatim/osm2pgsql/osm2pgsql -lsc -O 
gazetteer --hstore -C 4664 -P 5432 -d nominatim /home/nominatim/Nominatim/data/europe/andorra-latest.osm.pbf
Symlinks created
WARNING: Unable to access the website at http://nominatim.localhost/
You may want to update settings/local.php with @define(&#39;CONST_Website_BaseURL&#39;, &#39;http://[HOST]/[PATH]/&#39;);
ERROR: Site 400-nominatim does not exist!</code></pre>
<p>In Browser url(<a href="http://localhost/nominatim/)">http://localhost/nominatim/)</a> shows like</p>
<pre><code>string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#2 (8) { [&quot;error_message_prefix&quot;]=&gt; string(0) &quot;&quot; [&quot;mode&quot;]=&gt; int(1) [&quot;level&quot;]=&gt; int(1024) [&quot;code&quot;]=&gt; int(-25) [&quot;message&quot;]=&gt; string(29) &quot;DB Error: extension not found&quot; [&quot;userinfo&quot;]=&gt; string(55) &quot; [DB Error: extension not found] ** pgsql://@/nominatim&quot; [&quot;backtrace&quot;]=&gt; array(7) { [0]=&gt; array(6) { [&quot;file&quot;]=&gt; string(21) &quot;/usr/share/php/DB.php&quot; [&quot;line&quot;]=&gt; int(966) [&quot;function&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;class&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(5) { [0]=&gt; string(29) &quot;DB Error: extension not found&quot; [1]=&gt; int(-25) [2]=&gt; int(1) [3]=&gt; int(1024) ...
...
...
[&quot;_default_error_mode&quot;]=&gt; NULL [&quot;_default_error_options&quot;]=&gt; NULL [&quot;_default_error_handler&quot;]=&gt; string(0) &quot;&quot; [&quot;_error_class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;_expected_errors&quot;]=&gt; array(0) { } } [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(2) { [0]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(0) &quot;&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [1]=&gt; bool(false) } } [5]=&gt; array(6) { [&quot;file&quot;]=&gt; string(36) &quot;/home/nominatim/Nominatim/lib/db.php&quot; [&quot;line&quot;]=&gt; int(7) [&quot;function&quot;]=&gt; string(7) &quot;connect&quot; [&quot;class&quot;]=&gt; string(2) &quot;DB&quot; [&quot;type&quot;]=&gt; string(2) &quot;::&quot; [&quot;args&quot;]=&gt; array(2) { [0]=&gt; string(19) &quot;pgsql://@/nominatim&quot; [1]=&gt; bool(false) } } [6]=&gt; array(4) { [&quot;file&quot;]=&gt; string(44) &quot;/home/nominatim/Nominatim/website/search.php&quot; [&quot;line&quot;]=&gt; int(10) [&quot;function&quot;]=&gt; string(5) &quot;getDB&quot; [&quot;args&quot;]=&gt; array(0) { } } } [&quot;callback&quot;]=&gt; NULL } DB Error: extension not found</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '14, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>25 Jan '14, 06:50</strong> </span></p>
</div>
</div>
<div id="comments-container-30185" class="comments-container">
<span id="30186"></span>
<div id="comment-30186" class="comment">
<div id="post-30186-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please write your question on top of all that log stuff.</p>
</div>
<div id="comment-30186-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 14:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30187"></span>
<div id="comment-30187" class="comment">
<div id="post-30187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The title says install, but you are talking about the import and indexing, right?</p>
</div>
<div id="comment-30187-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 15:25)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30189"></span>
<div id="comment-30189" class="comment">
<div id="post-30189-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The error says "Out of memory for dense node cache, reduce --cache size". Have you tried doing what it suggests?</p>
</div>
<div id="comment-30189-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 17:18)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="30195"></span>
<div id="comment-30195" class="comment">
<div id="post-30195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you guys for your kind responce....</p>
<p>Actually i am new to this Nominatim and OSM.</p>
<p>i am ubuntu user, i am trying to install Nominatim from the script which taken from</p>
<p><a href="https://github.com/cyclestreets/nominatim-install">https://github.com/cyclestreets/nominatim-install</a></p>
<p>While i am starting the script as per the instruction they given i got the above error.</p>
<p>i know "out of memory for dense node cache,reduce the --cache size", what to do for that,</p>
<p>and also tell me what is the minimum memory needs to install Nominatim.</p>
</div>
<div id="comment-30195-info" class="comment-info">
<span class="comment-age">(25 Jan '14, 06:49)</span> <span class="comment-user userinfo">Arun kmp</span>
</div>
</div>
</div>
<div id="comment-tools-30185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30185-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


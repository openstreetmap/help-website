+++
type = "question"
title = "nominatim search fails when using post codes"
description = '''Hi I have set up Nominatim on my own server. I have tried several searches using just street names and the results have been good. However, whenever I include a postcode in the search I get a lot of errors appearing like as follows: string(125) &quot;select &#x27;AA&#x27;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(S...'''
date = "2013-01-21T10:49:00Z"
lastmod = "2013-01-21T12:58:00Z"
weight = 19226
keywords = [ "nominatim", "osm", "searching" ]
aliases = [ "/questions/19226" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nominatim search fails when using post codes](/questions/19226/nominatim-search-fails-when-using-post-codes)

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
<span id="post-19226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19226-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have set up Nominatim on my own server.</p>
<p>I have tried several searches using just street names and the results have been good.</p>
<p>However, whenever I include a postcode in the search I get a lot of errors appearing like as follows:</p>
<pre><code>string(125) &quot;select &#39;AA&#39;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcode where postcode = &#39;E8 9JH&#39;&quot; object(DB_Error)#2 (8) { [&quot;error_message_prefix&quot;]=&gt; string(0) &quot;&quot; [&quot;mode&quot;]=&gt; int(1) [&quot;level&quot;]=&gt; int(1024) [&quot;code&quot;]=&gt; int(-18) [&quot;message&quot;]=&gt; string(23) &quot;DB Error: no such table&quot; [&quot;userinfo&quot;]=&gt; string(322) &quot;select &#39;AA&#39;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcode where postcode = &#39;E8 9JH&#39; [nativecode=ERROR: relation &quot;gb_postcode&quot; does not exist LINE 1: ...)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcod... ^]&quot; [&quot;backtrace&quot;]=&gt; array(9) { [0]=&gt; array(6) { [&quot;file&quot;]=&gt; string(21) &quot;/usr/share/php/DB.php&quot; [&quot;line&quot;]=&gt; int(966) [&quot;function&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;class&quot;]=&gt; string(10) &quot;PEAR_Error&quot; [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(5) { [0]=&gt; string(23) &quot;DB Error: no such table&quot; [1]=&gt; int(-18) [2]=&gt; int(1) [3]=&gt; int(1024) [4]=&gt; string(322) &quot;select &#39;AA&#39;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcode where postcode = &#39;E8 9JH&#39; [nativecode=ERROR: relation &quot;gb_postcode&quot; does not exist LINE 1: ...)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcod... ^]&quot; } } [1]=&gt; array(7) { [&quot;file&quot;]=&gt; string(23) &quot;/usr/share/php/PEAR.php&quot; [&quot;line&quot;]=&gt; int(531) [&quot;function&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;class&quot;]=&gt; string(8) &quot;DB_Error&quot; [&quot;object&quot;]=&gt; *RECURSION* [&quot;type&quot;]=&gt; string(2) &quot;-&gt;&quot; [&quot;args&quot;]=&gt; array(4) { [0]=&gt; int(-18) [1]=&gt; int(1) [2]=&gt; int(1024) [3]=&gt; string(322) &quot;select &#39;AA&#39;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcode where postcode = &#39;E8 9JH&#39; [nativecode=ERROR: relation &quot;gb_postcode&quot; does not exist LINE 1: ...)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcod... ^]&quot; } } [2]=&gt; array(7) { [&quot;file&quot;]=&gt; string(28) &quot;/usr/share/php/DB/common.php&quot; [&quot;line&quot;]=&gt; int(1908) [&quot;function&quot;]=&gt; string(10) &quot;raiseError&quot; [&quot;class&quot;]=&gt; string(4) &quot;PEAR&quot; [&quot;object&quot;]=&gt; object(DB_pgsql)#1 (28) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;features&quot;]=&gt; array(7) { [&quot;limit&quot;]=&gt; string(5) &quot;alter&quot; [&quot;new_link&quot;]=&gt; string(5) &quot;4.3.0&quot; [&quot;numrows&quot;]=&gt; bool(true) [&quot;pconnect&quot;]=&gt; bool(true) [&quot;prepare&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(true) [&quot;transactions&quot;]=&gt; bool(true) } [&quot;errorcode_map&quot;]=&gt; array(0) { } [&quot;connection&quot;]=&gt; resource(14) of type (pgsql link) [&quot;dsn&quot;]=&gt; array(9) { [&quot;phptype&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;dbsyntax&quot;]=&gt; string(5) &quot;pgsql&quot; [&quot;username&quot;]=&gt; string(8) &quot;www-data&quot; [&quot;password&quot;]=&gt; bool(false) [&quot;protocol&quot;]=&gt; string(3) &quot;tcp&quot; [&quot;hostspec&quot;]=&gt; string(0) &quot;&quot; [&quot;port&quot;]=&gt; bool(false) [&quot;socket&quot;]=&gt; bool(false) [&quot;database&quot;]=&gt; string(9) &quot;nominatim&quot; } [&quot;autocommit&quot;]=&gt; bool(true) [&quot;transaction_opcount&quot;]=&gt; int(0) [&quot;affected&quot;]=&gt; int(0) [&quot;row&quot;]=&gt; array(0) { } [&quot;_num_rows&quot;]=&gt; array(0) { } [&quot;fetchmode&quot;]=&gt; int(2) [&quot;fetchmode_object_class&quot;]=&gt; string(8) &quot;stdClass&quot; [&quot;was_connected&quot;]=&gt; NULL [&quot;last_query&quot;]=&gt; string(125) &quot;select &#39;AA&#39;, ST_X(ST_Centroid(geometry)) as lon,ST_Y(ST_Centroid(geometry)) as lat from gb_postcode where postcode = &#39;E8 9JH&#39;&quot; [&quot;options&quot;]=&gt; array(8) { [&quot;result_buffering&quot;]=&gt; int(500) [&quot;persistent&quot;]=&gt; bool(false) [&quot;ssl&quot;]=&gt; bool(false) [&quot;debug&quot;]=&gt; int(0) [&quot;seqname_format&quot;]=&gt; string(6) &quot;%s_seq&quot; [&quot;autofree&quot;]=&gt; bool(false) [&quot;portability&quot;]=&gt; int(0) [&quot;optimize&quot;]=&gt; string(11) &quot;performance&quot; } [&quot;last</code></pre>
<p>Anyone know why this might be?</p>
<p>I see within the error that it says relation "gb_postcode" does not exist.</p>
<p>I followed the following tutorial: <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Ubuntu.2FDebian"><code>https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Ubuntu.2FDebian</code></a></p>
<p>So I would have thought everything needed should have been installed.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '13, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19226" class="comments-container">
<span id="19232"></span>
<div id="comment-19232" class="comment">
<div id="post-19232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whole question needs rephrasing, and the detail error message removing. It's obvious that you are lacking a table called gb_postcodes &amp; that's why this is failing.</p>
<p>Try something like asking "What is required to run a private nominatim instance for UK postcodes": the question may then be more useful to others.</p>
</div>
<div id="comment-19232-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 11:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19226-form-container" class="comment-form-container">
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

<span id="19233"></span>

<div id="answer-container-19233" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19233-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This isn't really a suitable forum for reporting a bug because once it is fixed it won't be of any help to anyone. Can you create an issue here <a href="https://github.com/twain47/Nominatim/issues">https://github.com/twain47/Nominatim/issues</a>. Please include the version of postgresql that you are running.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '13, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-19233" class="comments-container">
&#10;</div>
<div id="comment-tools-19233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19233-form-container" class="comment-form-container">
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


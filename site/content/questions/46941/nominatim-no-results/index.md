+++
type = "question"
title = "Nominatim, no results"
description = '''Hello, I followed the instructions here to install nominatim: https://wiki.openstreetmap.org/wiki/Nominatim/Installation But no matter the query, search.php always displays &quot;No search results found&quot;. I used a Luxembourg extract (osm file). I have some Luxembourgish rows in the &quot;place&quot; table (this tab...'''
date = "2015-12-03T01:55:00Z"
lastmod = "2015-12-03T01:55:00Z"
weight = 46941
keywords = [ "nominatim", "osm", "results", "placex" ]
aliases = [ "/questions/46941" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim, no results](/questions/46941/nominatim-no-results)

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
<span id="post-46941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46941-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I followed the instructions here to install nominatim: <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
<p>But no matter the query, search.php always displays "No search results found".</p>
<p>I used a Luxembourg extract (osm file). I have some Luxembourgish rows in the "place" table (this table has 76175 rows). The "placex" table has only 32388 rows. Its "street" and "country_code" columns only contain empty values.</p>
<p>When I run the sql query:</p>
<pre><code>&quot;SELECT distinct calculated_country_code street FROM placex&quot;</code></pre>
<p>I get only two rows:</p>
<pre><code>us
ca</code></pre>
<p>(I would expect a row with the "lu" country code, but no, it doesn't appear)</p>
<p>Any idea what step could have gone wrong?</p>
<p>A query like <a href="http://127.0.0.1:8080/nominatim/search.php?q=luxembourg">http://127.0.0.1:8080/nominatim/search.php?q=luxembourg</a> for example, gives no result, which is strange since I should have all the data from Luxembourg.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-results" rel="tag" title="see questions tagged &#39;results&#39;">results</span> <span class="post-tag tag-link-placex" rel="tag" title="see questions tagged &#39;placex&#39;">placex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '15, 01:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1e8df0cb397241565f3e8197bd312e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unecordesvp&#39;s gravatar image" />
<p><span>unecordesvp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unecordesvp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '15, 00:10</strong> </span></p>
</div>
</div>
<div id="comments-container-46941" class="comments-container">
&#10;</div>
<div id="comment-tools-46941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46941-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


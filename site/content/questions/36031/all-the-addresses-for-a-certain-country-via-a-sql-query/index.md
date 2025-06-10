+++
type = "question"
title = "All the addresses for a certain country via a SQL query"
description = '''My goal is get all the addresses for some different countries. So I downloaded an *.osm file from here http://download.geofabrik.de/ for a certain territory which contained a few countries and extracted the data from that file using osm2psql to a db. There were no errors, all went well. The sql quer...'''
date = "2014-08-20T18:58:00Z"
lastmod = "2014-08-20T18:58:00Z"
weight = 36031
keywords = [ "country", "address", "query", "polygon", "sql" ]
aliases = [ "/questions/36031" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All the addresses for a certain country via a SQL query](/questions/36031/all-the-addresses-for-a-certain-country-via-a-sql-query)

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
<span id="post-36031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36031-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My goal is get all the addresses for some different countries. So I downloaded an *.osm file from here <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> for a certain <strong>territory</strong> which contained a few countries and extracted the data from that file using osm2psql to a db. There were no errors, all went well.</p>
<p>The sql query I have to use is something like:</p>
<pre><code>select * from planet_osm_point where addr:housenumber is not null or addr:street is not null.</code></pre>
<p>However, adding <strong>and addr:country = 'SOMETHING'</strong> won't help because I've tried doing that and got around 100 rows which was, obviously, wrong. I know the <strong>polygons</strong> is a way to go, isn't it?</p>
<p>So how do I do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '14, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/391d5e9652dc0dfe9a18d509193653b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="memeran&#39;s gravatar image" />
<p><span>memeran</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="memeran has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '14, 18:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36031" class="comments-container">
&#10;</div>
<div id="comment-tools-36031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


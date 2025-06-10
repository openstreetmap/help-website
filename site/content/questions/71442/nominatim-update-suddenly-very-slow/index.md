+++
type = "question"
title = "Nominatim update suddenly very slow"
description = '''Hi, We&#x27;ve installed Nominatim with world data on our Kubernetes cluster. It has worked fine for several weeks, but since few days, the update is very very slow (from 4 hours to about 22 hours for the daily update). There are no visible errors, but it seems to be stucked on the following requests at ...'''
date = "2019-11-04T09:56:00Z"
lastmod = "2019-11-04T09:56:00Z"
weight = 71442
keywords = [ "nominatim", "update", "osm2pgsql" ]
aliases = [ "/questions/71442" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim update suddenly very slow](/questions/71442/nominatim-update-suddenly-very-slow)

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
<span id="post-71442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
We've installed Nominatim with world data on our Kubernetes cluster. It has worked fine for several weeks, but since few days, the update is very very slow (from 4 hours to about 22 hours for the daily update).</p>
<p>There are no visible errors, but it seems to be stucked on the following requests at the beginning and end of ranks 26 and 30:</p>
<p>2012915 | nominatim | | 2019-11-04 09:09:20.100902+00 | active | select geometry_sector,count(<em>) from placex where rank_search = $1 and indexed_status &gt; 0 group by geometry_sector order by geometry_sector<br />
2049039 | nominatim | | 2019-11-04 09:09:20.100902+00 | active | select geometry_sector,count(</em>) from placex where rank_search = $1 and indexed_status &gt; 0 group by geometry_sector order by geometry_sector<br />
2049040 | nominatim | | 2019-11-04 09:09:20.100902+00 | active | select geometry_sector,count(*) from placex where rank_search = $1 and indexed_status &gt; 0 group by geometry_sector order by geometry_sector</p>
<p>We currently use Nominatim 3.3.0, postgresql 11.2 (on a separate machine) and postgis 2.5.2<br />
Update command : update.php --import-osmosis --osm2pgsql-cache 5000</p>
<p><strong>Postgre:</strong><br />
Database is 700GB on SSD<br />
cpu: 4*2.3Ghz<br />
memory: 14GB</p>
<p><strong>Updater:</strong><br />
cpu: 2*2.3Ghz<br />
memory: 8GB</p>
<p><strong>Postgre custom parameters:</strong><br />
- "shared_buffers=5GB"<br />
- "effective_cache_size=9GB"<br />
- "maintenance_work_mem=128MB"<br />
- "work_mem=32MB"<br />
- "checkpoint_completion_target=0.9"<br />
- "random_page_cost=1.1"<br />
- "effective_io_concurrency=500"</p>
<p>Thanks for any idea about why it became suddenly so slow!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '19, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/11eaecb326084f16b4b902fd7867d2e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="web_heredis&#39;s gravatar image" />
<p><span>web_heredis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="web_heredis has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-71442" class="comments-container">
&#10;</div>
<div id="comment-tools-71442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71442-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


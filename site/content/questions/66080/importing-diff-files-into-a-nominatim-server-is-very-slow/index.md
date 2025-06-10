+++
type = "question"
title = "Importing diff files into a Nominatim server is very slow"
description = '''I have a server where I installed Nominatim, everything works fine but daily imports are very slow. Here is the command I use to import updates: ./utils/update.php --import-osmosis-all --no-npi and here is part of the log from postgresql (it seems it takes 20 seconds to import a single point): 2018-...'''
date = "2018-09-28T11:22:00Z"
lastmod = "2018-09-28T11:22:00Z"
weight = 66080
keywords = [ "import", "nominatim", "osm2pgsql", "osmosis" ]
aliases = [ "/questions/66080" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Importing diff files into a Nominatim server is very slow](/questions/66080/importing-diff-files-into-a-nominatim-server-is-very-slow)

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
<span id="post-66080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a server where I installed Nominatim, everything works fine but daily imports are very slow. Here is the command I use to import updates:</p>
<p><code>./utils/update.php --import-osmosis-all --no-npi</code></p>
<p>and here is part of the log from postgresql (it seems it takes 20 seconds to import a single point):</p>
<p><code>2018-09-28 09:59:26.723 UTCLOG: duration: 20841.622 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 09:59:26.723 UTCDETAIL: parameters: $1 = '1991172' 2018-09-28 09:59:47.644 UTCLOG: duration: 20919.765 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 09:59:47.644 UTCDETAIL: parameters: $1 = '1990890' 2018-09-28 10:00:08.440 UTCLOG: duration: 20794.188 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:00:08.440 UTCDETAIL: parameters: $1 = '1991076' 2018-09-28 10:00:29.293 UTCLOG: duration: 20851.333 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:00:29.293 UTCDETAIL: parameters: $1 = '1991075' 2018-09-28 10:00:50.135 UTCLOG: duration: 20841.083 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:00:50.135 UTCDETAIL: parameters: $1 = '1393309' 2018-09-28 10:01:11.061 UTCLOG: duration: 20924.034 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:01:11.061 UTCDETAIL: parameters: $1 = '559848' 2018-09-28 10:01:31.961 UTCLOG: duration: 20899.036 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:01:31.961 UTCDETAIL: parameters: $1 = '464022' 2018-09-28 10:01:52.865 UTCLOG: duration: 20902.475 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:01:52.865 UTCDETAIL: parameters: $1 = '382641' 2018-09-28 10:02:13.821 UTCLOG: duration: 20953.867 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:02:13.821 UTCDETAIL: parameters: $1 = '131642' 2018-09-28 10:02:35.042 UTCLOG: duration: 21219.991 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:02:35.042 UTCDETAIL: parameters: $1 = '2019829' 2018-09-28 10:02:55.909 UTCLOG: duration: 20864.235 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:02:55.909 UTCDETAIL: parameters: $1 = '2019724' 2018-09-28 10:03:16.708 UTCLOG: duration: 20797.321 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:03:16.708 UTCDETAIL: parameters: $1 = '2004606' 2018-09-28 10:03:37.567 UTCLOG: duration: 20856.796 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:03:37.567 UTCDETAIL: parameters: $1 = '2004610' 2018-09-28 10:03:58.393 UTCLOG: duration: 20823.782 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:03:58.393 UTCDETAIL: parameters: $1 = '945985' 2018-09-28 10:04:19.219 UTCLOG: duration: 20824.386 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:04:19.219 UTCDETAIL: parameters: $1 = '1087915' 2018-09-28 10:04:40.215 UTCLOG: duration: 20994.079 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:04:40.215 UTCDETAIL: parameters: $1 = '525557' 2018-09-28 10:05:00.994 UTCLOG: duration: 20777.332 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:05:00.994 UTCDETAIL: parameters: $1 = '432880' 2018-09-28 10:05:21.794 UTCLOG: duration: 20798.616 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:05:21.794 UTCDETAIL: parameters: $1 = '1440909' 2018-09-28 10:05:42.733 UTCLOG: duration: 20936.692 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:05:42.733 UTCDETAIL: parameters: $1 = '530458' 2018-09-28 10:06:05.307 UTCLOG: duration: 22572.536 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:06:05.307 UTCDETAIL: parameters: $1 = '1487369' 2018-09-28 10:06:26.257 UTCLOG: duration: 20947.926 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:06:26.257 UTCDETAIL: parameters: $1 = '471227' 2018-09-28 10:06:47.082 UTCLOG: duration: 20822.594 ms execute index_placex: update placex set indexed_status = 0 where place_id = $1 2018-09-28 10:06:47.082 UTCDETAIL: parameters: $1 = '1983016'</code></p>
<p>I have another server with the same postgresql.config file which works without this problem. Is there any way I can improve the performance?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '18, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '18, 11:34</strong> </span></p>
</div>
</div>
<div id="comments-container-66080" class="comments-container">
&#10;</div>
<div id="comment-tools-66080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


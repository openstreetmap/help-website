+++
type = "question"
title = "Planet replication url"
description = '''Hi, I setup nominatim with planet data from planet.openstreetmap.org, now want to update daily/hourly data. Got following error, when use planet.openstreetmap.org/replication for update.  Warning: file_get_contents(https://planet.openstreetmap.org/replication/hour/state.txt): failed to open stream: ...'''
date = "2018-08-27T12:36:00Z"
lastmod = "2018-08-30T07:29:00Z"
weight = 65576
keywords = [ "nominatim", "update", "mirror" ]
aliases = [ "/questions/65576" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Planet replication url](/questions/65576/planet-replication-url)

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
<span id="post-65576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I setup nominatim with planet data from planet.openstreetmap.org, now want to update daily/hourly data.</p>
<p>Got following error, when use planet.openstreetmap.org/replication for update.</p>
<p><strong>Warning: file_get_contents(<a href="https://planet.openstreetmap.org/replication/hour/state.txt):">https://planet.openstreetmap.org/replication/hour/state.txt):</a> failed to open stream: HTTP request failed! HTTP/1.1 421 Misdirected Request</strong></p>
<p>How to fix this?</p>
<p>Or must be use any mirror from <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Planet.osm_mirrors">https://wiki.openstreetmap.org/wiki/Planet.osm#Planet.osm_mirrors</a> instead of planet.openstreetmap.org ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-mirror" rel="tag" title="see questions tagged &#39;mirror&#39;">mirror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '18, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '18, 12:45</strong> </span></p>
</div>
</div>
<div id="comments-container-65576" class="comments-container">
<span id="65587"></span>
<div id="comment-65587" class="comment">
<div id="post-65587-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you download the state file manually, e.g. with <code>wget -O - </code><a href="https://planet.openstreetmap.org/replication/hour/state.txt"><code>https://planet.openstreetmap.org/replication/hour/state.txt</code></a>?</p>
</div>
<div id="comment-65587-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 19:26)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="65604"></span>
<div id="comment-65604" class="comment">
<div id="post-65604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2921/lonvia"></a><a href="https://help.openstreetmap.org/users/2921/lonvia">@lonvia</a>: Yes. i can download via wget. But in php got above error. Also tried in separate php file as follows(but met same err).</p>
<p>stream_context_set_default(['http'=&gt;['proxy'=&gt;'proxy:3128', 'header'=&gt;'Proxy-Authorization: Basic '.base64_encode('user:password')]]); echo file_get_contents("https://planet.openstreetmap.org/replication/hour/state.txt");</p>
<p>I can get state.txt from <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/state.txt">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/state.txt</a> . Can I use the same for update?</p>
</div>
<div id="comment-65604-info" class="comment-info">
<span class="comment-age">(28 Aug '18, 08:11)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="65607"></span>
<div id="comment-65607" class="comment">
<div id="post-65607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to be 100% sure - your PHP is definitely downloading via https not http ?</p>
</div>
<div id="comment-65607-info" class="comment-info">
<span class="comment-age">(28 Aug '18, 10:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65610"></span>
<div id="comment-65610" class="comment">
<div id="post-65610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Yes, My PHP downloading via https. Also got 400 response code for <a href="https://free.nchc.org.tw">https://free.nchc.org.tw</a></p>
<p>my php file:</p>
<p>stream_context_set_default(['http'=&gt;['proxy'=&gt;'proxy:3128', 'header'=&gt;'Proxy-Authorization: Basic '.base64_encode('user:pwdl')]]); echo file_get_contents("https://download.geofabrik.de/europe/andorra-updates/state.txt"); echo file_get_contents("https://planet.openstreetmap.org/replication/day/state.txt"); echo file_get_contents("https://free.nchc.org.tw/osm.planet/replication/day/state.txt"); echo file_get_contents("https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/state.txt");</p>
<p>Response:</p>
<h1 id="original-osm-minutely-replication-sequence-number-3121624">original OSM minutely replication sequence number 3121624</h1>
<p>timestamp=2018-08-27T20\:14\:02Z sequenceNumber=1987</p>
<p>Warning: file_get_contents(<a href="https://planet.openstreetmap.org/replication/day/state.txt):">https://planet.openstreetmap.org/replication/day/state.txt):</a> failed to open stream: HTTP request failed! HTTP/1.1 421 Misdirected Request</p>
<p>Warning: file_get_contents(<a href="https://free.nchc.org.tw/osm.planet/replication/day/state.txt):">https://free.nchc.org.tw/osm.planet/replication/day/state.txt):</a> failed to open stream: HTTP request failed! HTTP/1.1 400 Bad Request</p>
<h1 id="tue-aug-28-000642-utc-2018">Tue Aug 28 00:06:42 UTC 2018</h1>
<p>sequenceNumber=2176 timestamp=2018-08-28T00\:00\:00Z</p>
</div>
<div id="comment-65610-info" class="comment-info">
<span class="comment-age">(28 Aug '18, 11:17)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="65619"></span>
<div id="comment-65619" class="comment">
<div id="post-65619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This looks like an issue with your proxy, likely a misconfiguration of HTTPS forwarding or SSL. I recommend that you get in touch with your system administrator to find out more.</p>
</div>
<div id="comment-65619-info" class="comment-info">
<span class="comment-age">(28 Aug '18, 22:14)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="65639"></span>
<div id="comment-65639" class="comment not_top_scorer">
<div id="post-65639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can get state.txt from <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/state.txt">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/state.txt</a> . Can I use the same as CONST_Replication_Url for update ?</p>
</div>
<div id="comment-65639-info" class="comment-info">
<span class="comment-age">(30 Aug '18, 07:29)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-65576" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65576-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


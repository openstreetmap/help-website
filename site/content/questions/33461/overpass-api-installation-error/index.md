+++
type = "question"
title = "Overpass API installation error"
description = '''Hi,  I am trying to install the overpass API on my server but im getting an error. I&#x27;m following these instructions. After importing a .bz2 file of great Britain (wget -O planet.osm.bz2 &quot;http://download.geofabrik.de/europe/great-britain/england-latest.osm.bz2&quot;), I&#x27;m now trying to populate the databa...'''
date = "2014-05-25T16:22:00Z"
lastmod = "2014-05-26T07:57:00Z"
weight = 33461
keywords = [ "overpass", "api", "install", "error" ]
aliases = [ "/questions/33461" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API installation error](/questions/33461/overpass-api-installation-error)

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
<span id="post-33461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to install the overpass API on my server but im getting an error. I'm following <a href="https://wiki.openstreetmap.org/wiki/OSM3S/install">these instructions</a>.</p>
<p>After importing a .bz2 file of great Britain (<code>wget -O planet.osm.bz2 "http://download.geofabrik.de/europe/great-britain/england-latest.osm.bz2"</code>), I'm now trying to populate the database with the following command:</p>
<pre><code>nohup /root/osm-3s_v0.7.3/src/bin/init_osm3s.sh ../root/planet.osm.bz2 `pwd`/../ /root/osm-3s_v0.7.3 &amp;
tail -f nohup.out</code></pre>
<p>But halfway through the import I'm getting the error:</p>
<pre><code>Reading XML file ... elapsed node 2125784163. Flushing to database ...... done.
Reading XML file ... elapsed node 2368197335. Flushing to database ...... done.
Reading XML file ... elapsed node 2598221903. Flushing to database ...... done.
Reading XML file ... finished reading nodes. Flushing to database ...... done.
Reorganizing the database .../root/osm-3s_v0.7.3/src/bin/init_osm3s.sh: line 43: 11607 Broken pipe             bunzip2 &lt; $PLANET_FILE
     11608 Killed                  | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ $META</code></pre>
<p>Anybody know what's causing this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '14, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '14, 07:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-33461" class="comments-container">
<span id="33471"></span>
<div id="comment-33471" class="comment">
<div id="post-33471-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><em>Killed</em> can have many reasons. Maybe you did run out of memory? Check <code>dmesg</code> for <em>OOM</em> messages.</p>
</div>
<div id="comment-33471-info" class="comment-info">
<span class="comment-age">(26 May '14, 07:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


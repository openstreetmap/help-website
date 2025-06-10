+++
type = "question"
title = "How to clean up map data on my local tile server"
description = '''Hi, I have a local tile server. I use osm2pgsql to import the osm map data to local server. I want to clean up all the existing data and import fresh data. How can i do it?'''
date = "2016-02-09T11:21:00Z"
lastmod = "2016-02-09T13:35:00Z"
weight = 48013
keywords = [ "osm2pgsql", "clean_up" ]
aliases = [ "/questions/48013" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to clean up map data on my local tile server](/questions/48013/how-to-clean-up-map-data-on-my-local-tile-server)

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
<span id="post-48013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48013-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a local tile server. I use osm2pgsql to import the osm map data to local server.</p>
<p>I want to clean up all the existing data and import fresh data. How can i do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-clean_up" rel="tag" title="see questions tagged &#39;clean_up&#39;">clean_up</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '16, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '16, 11:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48013" class="comments-container">
&#10;</div>
<div id="comment-tools-48013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48013-form-container" class="comment-form-container">
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

<span id="48015"></span>

<div id="answer-container-48015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48015-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you run osm2pgsql without <code>--append</code> it will automatically clear the database and import afresh. You might also want to manually clear your tile cache, likely in <code>/var/lib/mod_tile</code> to so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '16, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48015" class="comments-container">
<span id="48016"></span>
<div id="comment-48016" class="comment">
<div id="post-48016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I executed following commands. But still map is not correctly displayed. Upper zoom level map is not displayed. On detailed zoom level only map shows.</p>
<p>sudo -u www-data osm2pgsql -C 2048 --slim --number-processes 4 india-latest.osm.pbf --cache-strategy sparse</p>
<p>touch /mod_tile/planet-import-complete</p>
<p>/etc/init.d/renderd restart</p>
<p>Path of my mod_tile directory is different than /var/lib. This path is mentioned in renderd.conf. Do I need to mention the path in osm2pgsql command also?</p>
<p>Also, after i execute above command, data of other countries which was renered previously should have been cleaned up. But it is not. It shows on map.</p>
</div>
<div id="comment-48016-info" class="comment-info">
<span class="comment-age">(09 Feb '16, 11:34)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="48020"></span>
<div id="comment-48020" class="comment">
<div id="post-48020-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are at least three places that "old data" can lurk. One is in the database; as Frederik has said osm2pgsql without --append will empty that and replace with whatever you're replacing it with.</p>
<p>The next is the metatile cache. If you look in "/var/lib/mod_tile" you'll see directories for each style you're displaying; if you haven't changed the name from "default" you'll see a directory called "default".</p>
<p>Below there you'll see subdirectories for each zoom level, perhaps something like this:</p>
<pre><code>ls /var/lib/mod_tile/ajt
0  1  10  11  12  13  14  15  16  17  18  2  3  4  5  6  7  8  9</code></pre>
<p>Below each subdirectory you'll eventually find ".meta" files such as:</p>
<pre><code>ls /var/lib/mod_tile/ajt/0/0/0/0/0/0.meta
/var/lib/mod_tile/ajt/0/0/0/0/0/0.meta</code></pre>
<p>To remove this cache, just delete these files.</p>
<p>Finally, there's the cache in your browser itself - usually a refresh will sort things out there.</p>
</div>
<div id="comment-48020-info" class="comment-info">
<span class="comment-age">(09 Feb '16, 13:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48015-form-container" class="comment-form-container">
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


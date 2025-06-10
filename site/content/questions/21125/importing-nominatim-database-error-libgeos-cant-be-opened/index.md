+++
type = "question"
title = "Importing Nominatim database error: libgeos can&#x27;t be opened"
description = '''Hello everyone. I don&#x27;t have much to say about. I executed setup.php, the import started running, and then this happened: /root/Nominatim/osm2pgsql/osm2pgsql: error while loading shared libraries: libgeos-3.3.3.so: cannot open shared object file: No such file or directory ERROR: Error executing exte...'''
date = "2013-04-01T23:32:00Z"
lastmod = "2013-04-01T23:32:00Z"
weight = 21125
keywords = [ "nominatim", "installation", "osm2pgsql", "php" ]
aliases = [ "/questions/21125" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Importing Nominatim database error: libgeos can't be opened](/questions/21125/importing-nominatim-database-error-libgeos-cant-be-opened)

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
<span id="post-21125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21125-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>I don't have much to say about. I executed setup.php, the import started running, and then this happened:</p>
<pre><code>/root/Nominatim/osm2pgsql/osm2pgsql: error while loading shared libraries: libgeos-3.3.3.so: cannot open shared object file: No such file or directory
ERROR: Error executing external command: /root/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 486 -P 5432 -d nominatim /root/brazil-latest.osm.pbf
Error executing external command: /root/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 486 -P 5432 -d nominatim /root/brazil-latest.osm.pbf</code></pre>
<p>I'm lost at this one. I've ran in some errors already, regarding postgres and postgis versions, but I just can't understand this one.</p>
<p>I'm running this on a CentOS 6.2 machine. Postgis 1.5, PGSQL 9.1.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '13, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/dc06a3de85eb8aa3a8331e85c1390a79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel_casado&#39;s gravatar image" />
<p><span>gabriel_casado</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel_casado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21125" class="comments-container">
&#10;</div>
<div id="comment-tools-21125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21125-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


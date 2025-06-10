+++
type = "question"
title = "Missing data after importing into postgis with osmosis"
description = '''Hello everyone, I have successfully imported a .bz2 OSM extract to PostGIS with osmosis using --read-xml , but when I have displayed the data in ID Editor, I noticed that there are some missing geometries (highways especially). I remember that I had the same problem with osm2pgsql and I solved it wi...'''
date = "2015-10-27T09:55:00Z"
lastmod = "2015-10-27T09:55:00Z"
weight = 46146
keywords = [ "ideditor", "osm", "osmosis" ]
aliases = [ "/questions/46146" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing data after importing into postgis with osmosis](/questions/46146/missing-data-after-importing-into-postgis-with-osmosis)

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
<span id="post-46146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46146-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I have successfully imported a .bz2 OSM extract to PostGIS with osmosis using --read-xml , but when I have displayed the data in ID Editor, I noticed that there are some missing geometries (highways especially).</p>
<p>I remember that I had the same problem with osm2pgsql and I solved it with the --slim option.</p>
<p>Here is the command I used:</p>
<pre><code>osmosis --read-pbf country.osm.bz2 --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;postgres&quot; password=&quot;*********&quot; validateSchemaVersion=&quot;no&quot;</code></pre>
<p>Maybe I have commited a mistake, which is ?? thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '15, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/7355dafb903301c43c303a104c75f265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AYARI&#39;s gravatar image" />
<p><span>AYARI</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AYARI has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '15, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-46146" class="comments-container">
&#10;</div>
<div id="comment-tools-46146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


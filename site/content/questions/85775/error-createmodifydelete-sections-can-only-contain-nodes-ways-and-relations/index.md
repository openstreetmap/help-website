+++
type = "question"
title = "ERROR: create/modify/delete sections can only contain nodes, ways, and relations"
description = '''After run osm2pgsql --append --style /home/basil/src/openstreetmap-carto/openstreetmap-carto.style --tag-transform-script /home/basil/src/openstreetmap-carto/openstreetmap-carto.lua --database gis --username basil --prefix planet_osm --slim --cache 2048 --hstore /home/basil/src/planet/diff_api_chang...'''
date = "2022-10-01T13:03:00Z"
lastmod = "2022-10-03T08:21:00Z"
weight = 85775
keywords = [ "osm2pgsql", "osmosis" ]
aliases = [ "/questions/85775" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ERROR: create/modify/delete sections can only contain nodes, ways, and relations](/questions/85775/error-createmodifydelete-sections-can-only-contain-nodes-ways-and-relations)

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
<span id="post-85775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After run osm2pgsql --append --style /home/basil/src/openstreetmap-carto/openstreetmap-carto.style --tag-transform-script /home/basil/src/openstreetmap-carto/openstreetmap-carto.lua --database gis --username basil --prefix planet_osm --slim --cache 2048 --hstore /home/basil/src/planet/diff_api_changes.osc</p>
<p>I get error ERROR: create/modify/delete sections can only contain nodes, ways, and relations</p>
<p>file diff_api_changes.osc genetated by osmosis, and it included tag "modify"</p>
<p>&lt;modify&gt; &lt;bounds minlon="-180.00000" minlat="-90.00000" maxlon="180.00000" maxlat="90.00000" origin="Osmosis 0.48.3"/&gt; &lt;/modify&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '22, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d62e54797d1ded39d9497ab5f7889fae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="basil_str&#39;s gravatar image" />
<p><span>basil_str</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="basil_str has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85775" class="comments-container">
<span id="85779"></span>
<div id="comment-85779" class="comment">
<div id="post-85779-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What command line did you use with Osmosis to create that diff_api_changes.osc file? Having a &lt;bounds&gt; inside a &lt;modify&gt; doesn't look right to me.</p>
</div>
<div id="comment-85779-info" class="comment-info">
<span class="comment-age">(02 Oct '22, 15:03)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="85782"></span>
<div id="comment-85782" class="comment">
<div id="post-85782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osmosis --read-apidb database="drsk_osm" user="user" password="password" validateSchemaVersion=no --read-xml /home/basil/src/planet/map.osm --derive-change --write-xml-change /home/basil/src/planet/diff_api_changes.osc</p>
</div>
<div id="comment-85782-info" class="comment-info">
<span class="comment-age">(03 Oct '22, 06:28)</span> <span class="comment-user userinfo">basil_str</span>
</div>
</div>
<span id="85783"></span>
<div id="comment-85783" class="comment">
<div id="post-85783-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interesting. Looks like a bug in Osmosis to me. I suggest opening an issue with them. If you remove that &lt;bounds&gt; XML element manually (it is superfluous anyway), osm2pgsql should be able to read the file.</p>
</div>
<div id="comment-85783-info" class="comment-info">
<span class="comment-age">(03 Oct '22, 08:14)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="85785"></span>
<div id="comment-85785" class="comment">
<div id="post-85785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is true. Everything works fine if I remove the &lt;bounds&gt; tag. Tell me how to solve this problem? Any help or idea would be greatly appreciated</p>
</div>
<div id="comment-85785-info" class="comment-info">
<span class="comment-age">(03 Oct '22, 08:21)</span> <span class="comment-user userinfo">basil_str</span>
</div>
</div>
</div>
<div id="comment-tools-85775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85775-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


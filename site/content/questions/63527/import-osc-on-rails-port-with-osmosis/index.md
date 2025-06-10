+++
type = "question"
title = "import OSC on rails port with osmosis"
description = '''I installed the rails port, imported North Dakota from http://download.geofabrik.de/north-america.html, edited an area with ID editor, then extracted the diff. Upon looking at the diff output file XML (8 kb), I see all the nodes there and it all looks correct. I truncated the db, imported the same p...'''
date = "2018-05-16T23:41:00Z"
lastmod = "2018-05-16T23:41:00Z"
weight = 63527
keywords = [ "osmosis" ]
aliases = [ "/questions/63527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [import OSC on rails port with osmosis](/questions/63527/import-osc-on-rails-port-with-osmosis)

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
<span id="post-63527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63527-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed the rails port, imported North Dakota from <a href="http://download.geofabrik.de/north-america.html,">http://download.geofabrik.de/north-america.html,</a> edited an area with ID editor, then extracted the diff. Upon looking at the diff output file XML (8 kb), I see all the nodes there and it all looks correct.</p>
<p>I truncated the db, imported the same pbf from Geofabrik, and then I tried to import the diff but it's not working.</p>
<p>Running Osmosis V 0.44.1</p>
<pre><code>osmosis --read-xml-change testChange3.osc --write-apidb-change dbType=&quot;postgresql&quot; host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;openstreemapPGuser&quot; password=&quot;secretPW&quot; validateSchemaVersion=&quot;no&quot;</code></pre>
<p>Says it completed, but the test road is not actually showing in ID editor.</p>
<p>I also tried truncating the DB again, then importing a combined file which also seems to not work.</p>
<pre><code>osmosis  --read-xml-change file=&quot;testChange3.osc&quot; --read-pbf file=&quot;north-dakota-latest.osm.pbf&quot; --apply-change --write-xml file=&quot;output.osm&quot;</code></pre>
<p>I also tried downloading an OSC from ID editor which provides "new" node ids such as "&lt;node id="-8"..." Osmosis generates the error "The entity timestamp attribute is missing."</p>
<p><strong>How is an OSC supposed to be imported so that it's visible within the ID editor?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '18, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/68f84c8e0856685a35ea0704673dbd83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caleb87z&#39;s gravatar image" />
<p><span>caleb87z</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caleb87z has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '18, 00:44</strong> </span></p>
</div>
</div>
<div id="comments-container-63527" class="comments-container">
&#10;</div>
<div id="comment-tools-63527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63527-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


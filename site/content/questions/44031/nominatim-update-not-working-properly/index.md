+++
type = "question"
title = "Nominatim update not working properly"
description = '''Hi to all, I have successfully installed nominatim. When I update data, i feel something may went to be wrong. My Last osmId in my DB is 2810212908.  &amp;lt;osm version=&quot;0.6&quot; generator=&quot;CGImap 0.4.0 (29973 thorn-03.openstreetmap.org)&quot; copyright=&quot;OpenStreetMap and contributors&quot; attribution=&quot;http://www.o...'''
date = "2015-07-08T07:27:00Z"
lastmod = "2015-07-08T07:27:00Z"
weight = 44031
keywords = [ "state.txt", "timestamps", "nominatim", "update", "osmosis" ]
aliases = [ "/questions/44031" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim update not working properly](/questions/44031/nominatim-update-not-working-properly)

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
<span id="post-44031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I have successfully installed nominatim. When I update data, i feel something may went to be wrong. My Last osmId in my DB is 2810212908.</p>
<blockquote>
<p>&lt;osm version="0.6" generator="CGImap 0.4.0 (29973 thorn-03.openstreetmap.org)" copyright="OpenStreetMap and contributors" attribution="https://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/"&gt; &lt;node id="2810212908" visible="true" version="1" changeset="21875316" timestamp="**2014-04-22T23:58:31Z**" user="SomeoneElse" uid="61942" lat="53.1106656" lon="-1.5713721"/&gt; &lt;/osm&gt;</p>
</blockquote>
<p>Now i want to update 1 hr data. My configuration.txt :</p>
<blockquote>
<p>baseUrl=<a href="https://planet.openstreetmap.org/replication/hour">https://planet.openstreetmap.org/replication/hour</a></p>
<p>maxInterval = 3600</p>
</blockquote>
<p>and my state.txt</p>
<blockquote>
<p>sequenceNumber=14109</p>
<p>timestamp=<strong>2014-04-23T04\:00\:00Z</strong></p>
</blockquote>
<p>Note: My state.txt shows 4 hrs diff(I expect 1 hr)</p>
<p>Also it will download data(osmosischange.osc) for 1 hr between 2014-04-23T02\:59\:00Z and 2014-04-23T03\:59\:00Z. I feel this is incorrect, bcoz i expect data from 2014-04-22T23\:59\:00Z to 2014-04-23T00\:59\:00Z</p>
<p>If I update this data in DB, I may loss 3 hrs data from 2014-04-22T23\:59\:00Z to 2014-04-23T02\:59\:00Z</p>
<p>Why this would happen? Kindly help me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-state.txt" rel="tag" title="see questions tagged &#39;state.txt&#39;">state.txt</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '15, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '15, 07:31</strong> </span></p>
</div>
</div>
<div id="comments-container-44031" class="comments-container">
&#10;</div>
<div id="comment-tools-44031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


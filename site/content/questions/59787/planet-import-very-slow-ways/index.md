+++
type = "question"
title = "Planet import very slow @ Ways"
description = '''Hey All, Been reading similar topics but really can&#x27;t find the answer. Trying to do a full planet import on a dell R230 32gb ram/ 4core 3Ghz / 2x 7200RPM drives in raid0 (I know don&#x27;t have SSD&#x27;s)  I followed the setup guides for centos7 and below is the command used for import. import line: ./utils/...'''
date = "2017-09-23T00:43:00Z"
lastmod = "2017-09-23T00:43:00Z"
weight = 59787
keywords = [ "ways", "import", "planet_osm" ]
aliases = [ "/questions/59787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Planet import very slow @ Ways](/questions/59787/planet-import-very-slow-ways)

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
<span id="post-59787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59787-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey All,</p>
<p>Been reading similar topics but really can't find the answer.</p>
<p>Trying to do a full planet import on a dell R230 32gb ram/ 4core 3Ghz / 2x 7200RPM drives in raid0 (I know don't have SSD's)</p>
<ul>
<li>I followed the setup guides for centos7 and below is the command used for import.</li>
<li>import line: ./utils/setup.php --osm-file /srv/osm/planet-latest.osm.pbf --all --osm2pgsql-cache 24000 2&gt;&amp;1 | tee setup.log</li>
<li>Nodes processed at about 1300k/s while the perform of Ways only seems to be processing at .78k/s. (Other threads seemed to indicate I should be getting in the 10's eg. 40k/s with my HW)</li>
<li><p>Processing: Node(4076728k 1344.6k/s) Way(183316k 0.78k/s) Relation(0 0.00/s)</p></li>
<li><p>Looking at htop I see it's still processing, cpu is nowhere near busy, ram is 28.8/31.3GB and using approx 6G of swap.</p></li>
<li>Trying to figure out if I screwed up somewhere or just poor hardware. I have no idea how many ways even need processing so I don't know if I'm in for a week or a month of waiting.</li>
</ul>
<p>If it helps my ultimate use case is reverse geocode lat/lon in large batches. I only need Country/State/City or similar (town/suburb/county etc)/Postal Code not sure if -slim or something else might have helped there.</p>
<p>Any insight is appreciated.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '17, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/aafc8a304b041ce4ccd7e0ca592e97f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="felix2001&#39;s gravatar image" />
<p><span>felix2001</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="felix2001 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59787" class="comments-container">
&#10;</div>
<div id="comment-tools-59787" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59787-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


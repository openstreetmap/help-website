+++
type = "question"
title = "osm2pgsql  data import - non-responsive UBUNTU"
description = '''I&#x27;ve previously imported a single country&#x27;s pbf file using osm2pgsql. I&#x27;m now attempting this with the whole of europe. I&#x27;m doing this on an UBUNTU VM with 2 cores and 8GB RAM. The host is an i7 930 quadcore clocked to 4000Mhz with 16GB RAM Things were going well, it processed the nodes, and ways an...'''
date = "2013-06-18T15:34:00Z"
lastmod = "2013-06-20T15:07:00Z"
weight = 23490
keywords = [ "osm2pgsql", "ubuntu" ]
aliases = [ "/questions/23490" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql data import - non-responsive UBUNTU](/questions/23490/osm2pgsql-data-import-non-responsive-ubuntu)

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
<span id="post-23490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23490-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've previously imported a single country's pbf file using osm2pgsql. I'm now attempting this with the whole of europe.</p>
<p>I'm doing this on an UBUNTU VM with 2 cores and 8GB RAM. The host is an i7 930 quadcore clocked to 4000Mhz with 16GB RAM</p>
<p>Things were going well, it processed the nodes, and ways and had just started on the relations - was up to about 10k I think last check. This had taken about a week. That was 3 days ago, since then the VM has been running at ~100% CPU - the host is clocking between 35-50% utilization from the VM. I cannot get the unlock prompt to appear on the VM, so I cannot get in to see the console output.</p>
<p>The VM still appears active - no error messages, and the vmx file is periodically being updated. ResourceMonitor on the host, shows the VM is reading from it's disk at around 40Mb/sec and writing at around 5kb/sec. I'm loathe to kill it and potentially waste nearly 2 weeks of importing.</p>
<p>Does anyone know if this is normal?</p>
<p>Is processing the relations more CPU intensive than the nodes and ways?</p>
<p>Has anyone got any idea of the relative lengths of the processes of importing nodes, ways and relations? (Obviously the absolute values will depend on hardware.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '13, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d0323e670bafa590ec131e5d08f1b85e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tangotonyb&#39;s gravatar image" />
<p><span>Tangotonyb</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tangotonyb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '13, 15:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-23490" class="comments-container">
<span id="23496"></span>
<div id="comment-23496" class="comment">
<div id="post-23496-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what are the parameters with which you imported?</p>
</div>
<div id="comment-23496-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 19:01)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="23505"></span>
<div id="comment-23505" class="comment">
<div id="post-23505-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think: osm2pgsql --slim -d gis -C 1500 --number-processes 2 ~/planet/planet-latest.osm.pbf - not sure about cache-size, tried with 6000 and it failed, again with 5000 and it failed, both after running for over a day, so I played safe and dropped it to under 3000</p>
</div>
<div id="comment-23505-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 20:23)</span> <span class="comment-user userinfo">Tangotonyb</span>
</div>
</div>
<span id="23560"></span>
<div id="comment-23560" class="comment">
<div id="post-23560-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Bah - came back to life for a day, and then process got killed with 900k relations imported. That's with 2000 cache.</p>
</div>
<div id="comment-23560-info" class="comment-info">
<span class="comment-age">(20 Jun '13, 15:07)</span> <span class="comment-user userinfo">Tangotonyb</span>
</div>
</div>
</div>
<div id="comment-tools-23490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23490-form-container" class="comment-form-container">
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

<span id="23491"></span>

<div id="answer-container-23491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23491-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible that the relations are meanwhile completed and the system is building the indexes which can take quite a long time and lead to intense disk I/O which might well be very taxing for your VM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '13, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23491" class="comments-container">
<span id="23494"></span>
<div id="comment-23494" class="comment">
<div id="post-23494-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks - that makes sense - I'd have expected the relations to have completed - the intense disk I/O is exactly what I'm seeing. I'll leave it a few days to see what happens.</p>
</div>
<div id="comment-23494-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 18:39)</span> <span class="comment-user userinfo">Tangotonyb</span>
</div>
</div>
<span id="23497"></span>
<div id="comment-23497" class="comment">
<div id="post-23497-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It is also possible that it has moved into the "going over pending ways" phase, which pulls in a list of all pending way ids (typically about half of all ways), which might have pushed you into using swap.</p>
</div>
<div id="comment-23497-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 19:04)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-23491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23491-form-container" class="comment-form-container">
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


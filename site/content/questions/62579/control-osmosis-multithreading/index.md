+++
type = "question"
title = "Control osmosis &quot;multithreading&quot;"
description = '''I would like to control how much CPUs osmosis can use?  My typicaly run looks like: bin/osmosis --rb inputs/france.pbf --lp &#92;  --tf reject-relations --lp &#92;  --tf accept-ways highway=motorway,trunk,primary,secondary &#92; # maybe more...  natural=coastline junction=roundabout --lp &#92;  --used-node --lp &#92;  ...'''
date = "2018-03-08T11:03:00Z"
lastmod = "2018-03-08T12:20:00Z"
weight = 62579
keywords = [ "osmosis" ]
aliases = [ "/questions/62579" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Control osmosis "multithreading"](/questions/62579/control-osmosis-multithreading)

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
<span id="post-62579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62579-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to control how much CPUs osmosis can use?</p>
<p>My typicaly run looks like:</p>
<pre><code>bin/osmosis --rb inputs/france.pbf --lp \
            --tf reject-relations --lp \
            --tf accept-ways highway=motorway,trunk,primary,secondary \ # maybe more...
                 natural=coastline junction=roundabout --lp \
            --used-node --lp \
            --osm2graph file=france.mapgr id=FR name=France</code></pre>
<p>The last task (<code>osm2graph</code>) is single-threaded but when I run this on a 8-cores machine, I get CPU usage above 100%.</p>
<p>I plan on running <code>osmosis</code> on a shared platform, so I need to either control its CPU usage, or know its maximum CPU usage so that I can reserve enough without impacting other users.</p>
<p>Is there a way to tell osmosis not to use more than X CPUs/Threads? Or to know how much osmosis is going to use?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '18, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/746dd23bbe20769fbd758421e67f455c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Holt59&#39;s gravatar image" />
<p><span>Holt59</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Holt59 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '18, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-62579" class="comments-container">
<span id="62583"></span>
<div id="comment-62583" class="comment">
<div id="post-62583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use the tool <code>cpulimit</code> to limit the CPU usage of arbitrary processes. A more advanced way is to use <em>cgroups</em> if your kernel supports them.</p>
</div>
<div id="comment-62583-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 12:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62579-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


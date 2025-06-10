+++
type = "question"
title = "Multiple nominatim instances, one per region."
description = '''Hi, I have successfully installed Nominatim with a single Postgres Database in my infrastructure. However, our infrastructure team has informed me that the planet database is too large, and they recommend working with smaller databases for better performance. My initial idea is to set up separate in...'''
date = "2023-10-31T14:31:00Z"
lastmod = "2023-10-31T18:10:00Z"
weight = 87968
keywords = [ "region", "nominatim", "database" ]
aliases = [ "/questions/87968" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple nominatim instances, one per region.](/questions/87968/multiple-nominatim-instances-one-per-region)

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
<span id="post-87968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87968-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have successfully installed Nominatim with a single Postgres Database in my infrastructure. However, our infrastructure team has informed me that the planet database is too large, and they recommend working with smaller databases for better performance. My initial idea is to set up separate instances of Nominatim for different regions and create a gateway to expose the API as a unified deployment.</p>
<p>To achieve this, I'm considering making the 'countryCode' mandatory in user requests and then forwarding the request to the appropriate Nominatim instance based on the country code. For example, if the 'countryCode' is 'Austria,' I would route the request to the Europe region instance.</p>
<p>However, I'm concerned about potential issues, especially when a user requests an address in a place like Hawaii, which falls within the Oceania region. In this case, for a 'countryCode' of 'US,' I may need to query at least two regions simultaneously and somehow combine the results.</p>
<p>My primary concern is not the increased complexity of this deployment (multiple databases and API servers) as the infrastructure constraints take precedence. I'm more interested in understanding potential functional issues that I might not be aware of at the moment. Has anyone faced a similar challenge or has insights to share on the best practices for handling such a multi-region Nominatim deployment?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '23, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0900332f0ef93125d5acc2bf12fbae47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattCon&#39;s gravatar image" />
<p><span>MattCon</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattCon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87968" class="comments-container">
&#10;</div>
<div id="comment-tools-87968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87968-form-container" class="comment-form-container">
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

<span id="87969"></span>

<div id="answer-container-87969" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87969-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Let me guess, your IT people want to run everything "in the cloud" and somehow a single cloud node (or whatever the term in the particular cloud infrastructure is) cannot allocate the resources needed. And now you are on a quest to spend several person-weeks of design time to implement a workaround for this infrastructure shortcoming, resulting in a system that is more complex and more prone to failure and where (unlike when running a "standard" Nominatim) your organisation will be the only group on earth using it, so the chances of finding others with similar problems (should problems arise) are near zero. Brilliant plan!</p>
<p>Less cynically, I think your plan can work as long as you avoid splitting countries. Nominatim doesn't like it if a country boundary is not fully there. This could require some work if you are dealing with countries that have overseas territories, like France. You might have to cut out your regions from a planet file with Osmium and ensure referential integrity on county border relations, something that is not granted in e.g. Geofabrik download files (where the Europe file will not contain French Dom-Tom areas like Martinique).</p>
<p>I would still strongly advise against your plan. If you cannot allocate the ~ 1 TB of disk space and 64 GB of RAM to run a full-blown Nominatim server (and finding these resources will almost certainly be cheaper than continuing down the path you have started on!), then you might consider</p>
<ul>
<li>doing the Nominatim <em>import</em> on a beefy machine that is non-production and therefore maybe sits outside the strict requirements by your infrastructure team, then only replicating the necessary bits of the database to a production machine with less resources. This way you might get away with something like 16 GB RAM, 500 GB disk space for the client machine</li>
<li>switching to "Photon" altogether for which you can download ready-made database files that will only need ~250 GB of disk space; Photon may not do everything that Nominatim does but if it is sufficient for you then things are way easier.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '23, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87969" class="comments-container">
<span id="87970"></span>
<div id="comment-87970" class="comment">
<div id="post-87970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik for your answer, you made me smile. I want to assure you than except for this question, no more time was spent on this cursed path and no more will be spent.</p>
<p>The critical resource here is space, so I'm interested in the first option you pictured. Could you please elaborate or point me to existing resources on this? Thanks a lot!</p>
</div>
<div id="comment-87970-info" class="comment-info">
<span class="comment-age">(31 Oct '23, 16:00)</span> <span class="comment-user userinfo">MattCon</span>
</div>
</div>
<span id="87971"></span>
<div id="comment-87971" class="comment">
<div id="post-87971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When Nominatim does the initial import it uses a number of extra database tables that are not required for production use, but are needed during the import process and - if later incremental updates are desired - also during updates.</p>
<p>If you do not need incremental updates (and instead can live with, say, doing a full new data load once a month) then you can simply remove the excess information from your database after the import, see <a href="https://nominatim.org/release-docs/latest/admin/Import/#dropping-data-required-for-dynamic-updates">https://nominatim.org/release-docs/latest/admin/Import/#dropping-data-required-for-dynamic-updates</a> - and after that copy the much-reduced database to the actual production machine.</p>
<p>If you would like to do incremental updates, then a variant of the above can be achieved by setting up PostgreSQL logical replication between a beefy "import server" (that has the extra tables needed for updates, and keeps them), and one (or more - there's an easy option for scaling here) "followers" that do the actual request serving but only have the subset of tables required for that. PostgreSQL replication allows you to selectively replicate tables.</p>
</div>
<div id="comment-87971-info" class="comment-info">
<span class="comment-age">(31 Oct '23, 18:10)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87969-form-container" class="comment-form-container">
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


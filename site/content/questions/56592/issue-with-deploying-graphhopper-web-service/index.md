+++
type = "question"
title = "Issue with deploying GraphHopper Web Service"
description = '''Hi, We are trying to deploy GraphHopper Web Service on our AWS server to use your routing data in our mobile application. We downloaded the code from the below mentioned Github link - https://github.com/graphhopper/graphhopper/tree/0.9 We are trying to deploy it per your documentation. We wish to us...'''
date = "2017-06-12T17:06:00Z"
lastmod = "2017-06-13T12:35:00Z"
weight = 56592
keywords = [ "directions", "api", "graphhopper", "webservice" ]
aliases = [ "/questions/56592" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue with deploying GraphHopper Web Service](/questions/56592/issue-with-deploying-graphhopper-web-service)

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
<span id="post-56592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We are trying to deploy GraphHopper Web Service on our AWS server to use your routing data in our mobile application. We downloaded the code from the below mentioned Github link -</p>
<p><strong><a href="https://github.com/graphhopper/graphhopper/tree/0.9">https://github.com/graphhopper/graphhopper/tree/0.9</a></strong></p>
<p>We are trying to deploy it per your documentation. We wish to use GraphHopper API's or GraphHopper Directions API.</p>
<p>However, we were faced with a lot of issues during the deployment, where this process was just not completing. Once the process started, it took up a lot of memory and then the process went into a hung state.</p>
<p>We started the process with 32 GB RAM and then as memory utilization grew, we increased RAM to 64 GB, but even that was being consumed very soon and once again it would go into a hung state. The process wouldn't complete. All we could see at that point was the server memory utilization, but we couldn't make out what exactly was going on with the OSM deployment process.</p>
<p>We went through multiple unsuccessful rounds of the deployment process and then we tried with MMAP configuration for data reader.dataacess and were finally able to complete one cycle of deployment this morning after the process ran for around 20 hours.</p>
<p>This has raised a few questions for us about the OSM (world data) deployment -</p>
<ol>
<li><p>Why does the deployment process take such a long time to complete? 20 hours is a very long time, although we are deploying world content, which is relatively larger.</p></li>
<li><p>Memory utilization is very high during the process - The recommended server config given to us was 32 GB RAM and 1 TB HDD. We had to upgrade RAM to 64 GB and that too didn't seem to suffice until the last time we tried when it actually utilized around 62 GB at peak time. We felt that garbage collection process was probably not functioning properly.</p></li>
<li><p>What is the recommended CPU configuration?</p></li>
<li><p>We found some information on the web that once the server is stopped and then re-started, OSM has to be re-deployed on the server. Why is that the case? If this deployment process actually takes 20 hours to complete on average, this will be a huge problem for getting this much downtime on the production server.</p></li>
<li><p>Once OSM planet file is deployed, what is the facility provided for updating a newer version? How often are new updates released? Is there a provision for only updating the incremental changes in the new file?</p></li>
</ol>
<p>It would be of great help if you could please provide your answers to the above and any other useful information at the earliest as this is required very urgently. Please mail it to pradeep_nair@neovasolutions.com.</p>
<p>Thank You</p>
<p>Pradeep Nair</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span> <span class="post-tag tag-link-webservice" rel="tag" title="see questions tagged &#39;webservice&#39;">webservice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '17, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/137e7cde90776fc8963c97e3c74c18d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nairpradeepp&#39;s gravatar image" />
<p><span>nairpradeepp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nairpradeepp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56592" class="comments-container">
<span id="56602"></span>
<div id="comment-56602" class="comment">
<div id="post-56602-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Graphhopper has a dedicated <a href="https://discuss.graphhopper.com/">forum</a>, which might be a better place to ask this question as it seems to be related to their deployment. While Graphhopper works with OSM data, it is a project from an an independent company.</p>
</div>
<div id="comment-56602-info" class="comment-info">
<span class="comment-age">(13 Jun '17, 12:35)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-56592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56592-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


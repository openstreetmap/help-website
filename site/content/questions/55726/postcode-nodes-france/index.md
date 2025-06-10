+++
type = "question"
title = "Postcode nodes - France"
description = '''Hi - Total newb how to modify this query to get all the available postcode nodes for France in http://overpass-turbo.eu/ . I&#x27;m mostly interested in just getting the json returned (if possible). Edit: An example of a postcode &#x27;node&#x27; is this: http://www.openstreetmap.org/node/2445940960 I did find the...'''
date = "2017-04-21T01:23:00Z"
lastmod = "2017-04-22T06:55:00Z"
weight = 55726
keywords = [ "overpass-turbo", "postcode" ]
aliases = [ "/questions/55726" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Postcode nodes - France](/questions/55726/postcode-nodes-france)

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
<span id="post-55726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55726-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi -</p>
<p>Total newb how to modify this query to get all the available postcode nodes for France in <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> . I'm mostly interested in just getting the json returned (if possible).</p>
<p>Edit:</p>
<p>An example of a postcode 'node' is this: <a href="http://www.openstreetmap.org/node/2445940960">http://www.openstreetmap.org/node/2445940960</a> I did find the postcode 'relation' that corresponds here: <a href="http://www.openstreetmap.org/relation/252642">http://www.openstreetmap.org/relation/252642</a></p>
<p>...I am mostly interested in just getting the lat/long (point location) of all available 'addr:postcode' tags....is that plausible to do without querying for the relations (or will I miss nodes in the process if I do NOT query the relations?</p>
<blockquote>
<p>/ <em>This shows the postal code points in france.</em> /</p>
<p>[out:json];</p>
<p>area[name="France"]; (node<a href="area">"addr"~"postcode"</a>; );</p>
<p>out meta;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '17, 01:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d8301f4449cd62755a06bd46e11db349?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goldfishinriver&#39;s gravatar image" />
<p><span>goldfishinriver</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goldfishinriver has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '17, 17:34</strong> </span></p>
</div>
</div>
<div id="comments-container-55726" class="comments-container">
<span id="55727"></span>
<div id="comment-55727" class="comment">
<div id="post-55727-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what is a postcode node ? Can you post a link to an example ?</p>
<p>If you look e.g. at Saint-Etienne via Nominatim: <a href="http://nominatim.openstreetmap.org/details.php?place_id=159077530">http://nominatim.openstreetmap.org/details.php?place_id=159077530</a> you see that the postcode is not coming from a unique node. But if you look at the boundary relation <a href="http://www.openstreetmap.org/relation/117905,">http://www.openstreetmap.org/relation/117905,</a> you see a addr:postcode there.</p>
<p>Please clarify your goal by updating the original question or as a comment.</p>
</div>
<div id="comment-55727-info" class="comment-info">
<span class="comment-age">(21 Apr '17, 06:14)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-55726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55726-form-container" class="comment-form-container">
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

<span id="55743"></span>

<div id="answer-container-55743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55743-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So you are looking for all nodes in France whose address information include a postcode ?</p>
<p>The query is <a href="http://overpass-turbo.eu/s/oxp">http://overpass-turbo.eu/s/oxp</a> but you will need a much longer timeout.</p>
<p>I cannot speak for France, but e.g. in Flanders, we attempt to not map the postal code on individual nodes. We prefer to use postal code relations.</p>
<p>I also do not know how may of the addresses are mapped as nodes in France. Perhaps addresses are also mapped on ways. So be prepared to end up with a large collection of nodes that do not represent anything at all, because data is mapped in another way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '17, 06:55</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-55743" class="comments-container">
&#10;</div>
<div id="comment-tools-55743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55743-form-container" class="comment-form-container">
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


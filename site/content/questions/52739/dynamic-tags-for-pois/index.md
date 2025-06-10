+++
type = "question"
title = "Dynamic tags for POIs"
description = '''Hello,  I am currently working on updating the charging_station POIs arround me. Also I am testing with an experimental UI which shows the kind of data optimised for that. Special for this use case I ask myself if there is any function within OSM to create &quot;dynamic&quot; POIs. What I have in mind is that...'''
date = "2016-10-30T14:32:00Z"
lastmod = "2016-10-30T19:43:00Z"
weight = 52739
keywords = [ "dynamic", "poi" ]
aliases = [ "/questions/52739" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamic tags for POIs](/questions/52739/dynamic-tags-for-pois)

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
<span id="post-52739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52739-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am currently working on updating the charging_station POIs arround me. Also I am testing with an experimental UI which shows the kind of data optimised for that.</p>
<p>Special for this use case I ask myself if there is any function within OSM to create "dynamic" POIs. What I have in mind is that (as for example ChargeNow) the status of the station (free, out of service etc.) comes from the operator. From my perspective it is great that all the mappers update all the tags, but some information must be delivered by the operator as they are nearly realtime.</p>
<p>Is there any way to archive this requirement and if not where can I discuss my proposal how this could be done?</p>
<p>Best regards</p>
<p>Malte</p>
<p>PS.: Technically it could be set a tag with a REST endpoint which delivers some Key / Values which match the OSM tags.</p>
<p>On the POI: <code>dynamic_data:url = </code><span><code>ttps://api.operator.com/station/1234</code></span></p>
<p>Response from operator: <code>socket:type2 = 2 socket:type2:free: 1 in_service: true</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '16, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/423db5ffe6a01cc1c6663f6fc37a30b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derBroBro&#39;s gravatar image" />
<p><span>derBroBro</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derBroBro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52739" class="comments-container">
&#10;</div>
<div id="comment-tools-52739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52739-form-container" class="comment-form-container">
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

<span id="52740"></span>

<div id="answer-container-52740" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52740-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the proper way to do this is having existing tags like these on the POI:</p>
<pre><code>operator=XYZ Corp
ref=1234</code></pre>
<p>Then you'd write a charging station map that knows "if I want to know the status of a charging station run by operator XYZ, I need to call this URL..." - and take it from there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '16, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52740" class="comments-container">
<span id="52743"></span>
<div id="comment-52743" class="comment">
<div id="post-52743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think this is a great "option C". But I would like to prefer a more standard way. If there is no existing solution for this, where is the right place to make a proposal?</p>
</div>
<div id="comment-52743-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 16:35)</span> <span class="comment-user userinfo">derBroBro</span>
</div>
</div>
<span id="52744"></span>
<div id="comment-52744" class="comment">
<div id="post-52744-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To solve this in a "standard" way, you would not only have to add the URL of the service to OSM but also the algorithm how to parse the response. This is out of scope for OSM.</p>
</div>
<div id="comment-52744-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 17:07)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="52745"></span>
<div id="comment-52745" class="comment">
<div id="post-52745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am absolutely with you but the interface should be defined. If I create it just for me no one else will be able to use it. Also I think the "problem" of just holding handpicked data is not only affecting this use case (which was only an example). It could bring the project forward if 3rd parties have a standard way of providing data.</p>
<p>What I am looking for is just the interface how to set the "link" in osm to a system which holds the data and define how a default answer could look like. It is for me totaly out of scope to include this to the rendered tiles nor to make it part of osm in general by deliver the data to the API request.</p>
<p>I am already a little bit confused how to come forward with this. From my persepective it is not direct an osm topic but (possibly) a related project which should also make use of the exsting osm experience and ideas.</p>
<p>So, my question is still where to discuss this? There are forums, wikis, mailing lists and irc etc.. It is still totaly unclear where to start and I am also getting already the feeling that such ideas are not welcome.</p>
</div>
<div id="comment-52745-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 18:18)</span> <span class="comment-user userinfo">derBroBro</span>
</div>
</div>
<span id="52746"></span>
<div id="comment-52746" class="comment">
<div id="post-52746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The URL doesn't belong into OSM. What if the API changes? Then you have to update every URL. Instead just go for Frederik's suggestion by adding just the <code>operator</code> and <code>ref</code> tags. This is already sufficient. The client just needs to query all objects for the operator he is interested in and then construct the corresponding URLs based on the ref tags.</p>
</div>
<div id="comment-52746-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 19:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52747"></span>
<div id="comment-52747" class="comment">
<div id="post-52747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The ref tag should be one documented elsewhere too.</p>
</div>
<div id="comment-52747-info" class="comment-info">
<span class="comment-age">(30 Oct '16, 19:43)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-52740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52740-form-container" class="comment-form-container">
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


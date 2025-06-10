+++
type = "question"
title = "Compute length of a bus route"
description = '''Looking at a bus route like this one, I would like to know how I could compute the total distance of the route.  I can see that the route is compose of &quot;ways&quot; that I can export to XML. Adding up the lengths of all the &quot;ways&quot; comprising a route should give me what I want. But there is no length infor...'''
date = "2021-01-02T10:10:00Z"
lastmod = "2021-01-03T10:37:00Z"
weight = 78183
keywords = [ "busroute" ]
aliases = [ "/questions/78183" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Compute length of a bus route](/questions/78183/compute-length-of-a-bus-route)

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
<span id="post-78183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78183-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Looking at a bus route like <a href="https://www.openstreetmap.org/relation/299720">this one</a>, I would like to know how I could compute the total distance of the route.</p>
<p>I can see that the route is compose of "ways" that I can export to XML. Adding up the lengths of all the "ways" comprising a route should give me what I want. But there is no length information nor any begin/end position in the XML.</p>
<p>How can I get the length information about the "ways" comprising a route?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '21, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fb024713b2d983ef5a8ce424f3fcf826?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbus&#39;s gravatar image" />
<p><span>tbus</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '21, 10:39</strong> </span></p>
</div>
</div>
<div id="comments-container-78183" class="comments-container">
&#10;</div>
<div id="comment-tools-78183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78183-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="78186"></span>

<div id="answer-container-78186" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could also use the Relation Analyzer<br />
<a href="https://wiki.openstreetmap.org/wiki/Relation_Analyzer">https://wiki.openstreetmap.org/wiki/Relation_Analyzer</a><br />
<a href="http://ra.osmsurround.org/analyzeRelation?relationId=299720&amp;_noCache=on">http://ra.osmsurround.org/analyzeRelation?relationId=299720&amp;_noCache=on</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '21, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '21, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-78186" class="comments-container">
<span id="78187"></span>
<div id="comment-78187" class="comment">
<div id="post-78187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is what I was looking for, thank you! Unfortunately I believe either the ways measurements or something else is wrong, because the real total length is considerably longer than that (~14 km vs 10.3km).</p>
</div>
<div id="comment-78187-info" class="comment-info">
<span class="comment-age">(02 Jan '21, 15:59)</span> <span class="comment-user userinfo">tbus</span>
</div>
</div>
<span id="78204"></span>
<div id="comment-78204" class="comment">
<div id="post-78204-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes you are correct.<br />
I plotted the round trip using AllTrails and covered 13.6 km.<br />
<a href="https://www.alltrails.com/explore/map/sun-03-jan-2021-10-17-979a3f1">https://www.alltrails.com/explore/map/sun-03-jan-2021-10-17-979a3f1</a><br />
I assume the parts of the route where the bus follows the same part of the road in each direction count once unfortunately?<br />
Maybe one of the public transport apps that use the OSM data solve the task.</p>
</div>
<div id="comment-78204-info" class="comment-info">
<span class="comment-age">(03 Jan '21, 10:37)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-78186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78186-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78184"></span>

<div id="answer-container-78184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't used an XML file but GPS Babel might convert it to a GPX. The GPX could then be read by several mapping apps to read the distance you want. I rough solution could be to use the route arrow on the map page to measure sections of the bus route.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Route_Measuring.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '21, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '21, 16:59</strong> </span></p>
</div>
</div>
<div id="comments-container-78184" class="comments-container">
&#10;</div>
<div id="comment-tools-78184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78185"></span>

<div id="answer-container-78185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using JOSM:<br />
You could copy the relation id from the link you gave.<br />
In JOSM File&gt;Download object (in this case it will be relation 299720), then select the object via Selection&gt;Select all.<br />
Then activate the measurement tool via Windows&gt;Measured values or activate it from the edit toolbar along the left side. You will see the 'selection length'. You can change the units used by clicking on the ruler icon along the bottom strip of the screen.</p>
<p>The measurement tool is a plugin and you may also need the utilsplugin2, also may need to check 'Expert Mode' at the bottom left of the plugins page.<br />
JOSM&gt;Preferences&gt;Plug-ins</p>
<p>Edit: distance of total bus route is incorrect because segments of road that are travelled in both directions are only counted once in the measured total.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Josm_8oiUax9.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '21, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '21, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-78185" class="comments-container">
&#10;</div>
<div id="comment-tools-78185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78185-form-container" class="comment-form-container">
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


+++
type = "question"
title = "How to access the timestamp value from Overpass meta requests with Openlayers.Format.OSM?"
description = '''I am using Overpass-api to request data, then display it in an interactive webpage using Openlayers. When user clicks on some feature, the information is shown in popup. As of now, the page is working nicely and displays all the tags. I want to add the &quot;last updated time&quot; of the feature in the popup...'''
date = "2013-03-05T04:56:00Z"
lastmod = "2013-03-05T13:57:00Z"
weight = 20499
keywords = [ "overpass", "popup", "openlayers", "update", "timestamps" ]
aliases = [ "/questions/20499" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to access the timestamp value from Overpass meta requests with Openlayers.Format.OSM?](/questions/20499/how-to-access-the-timestamp-value-from-overpass-meta-requests-with-openlayersformatosm)

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
<span id="post-20499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20499-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Overpass-api to request data, then display it in an interactive webpage using Openlayers. When user clicks on some feature, the information is shown in popup.</p>
<p>As of now, the page is working nicely and displays all the tags.</p>
<p>I want to add the <strong>"last updated time"</strong> of the feature in the popup, which will correspond to the <strong>"timestamp"</strong> value in the <strong>"Overpass-api meta request"</strong> but i cannot access that value.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '13, 04:56</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-20499" class="comments-container">
<span id="20500"></span>
<div id="comment-20500" class="comment">
<div id="post-20500-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you please give an example query URL?</p>
</div>
<div id="comment-20500-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 05:15)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-20499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20499-form-container" class="comment-form-container">
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

<span id="20504"></span>

<div id="answer-container-20504" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20504-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume this is not Overpass API specific, but a general issue when reading OSM XML with OpenLayers. Then you could give <a href="https://github.com/nrenner/olex/blob/master/js/OSMMeta.js">Format.OSMMeta</a> a try, an extension to Format.OSM I wrote. Not well tested, but worked for me.</p>
<p>Include the file/code in your project and replace references to "OpenLayers.Format.OSM" with "OpenLayers.Format.OSMMeta" in your code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '13, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-20504" class="comments-container">
<span id="20507"></span>
<div id="comment-20507" class="comment">
<div id="post-20507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you want to contribute that to the main OpenLayers source tree?</p>
</div>
<div id="comment-20507-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 11:57)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20509"></span>
<div id="comment-20509" class="comment">
<div id="post-20509-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I plan to, but right now my focus is on making progress with my projects and gather candidates for sharing along the way. Then do some clean up, documentation and tests.</p>
<p>In this case I would like to discuss implementation details first, like: really mix meta info with tags? use a prefix? merge with OSM class? Also, I'm thinking about refactoring the OSM.read method and using one of the implementations for Relation support out there.</p>
</div>
<div id="comment-20509-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 13:57)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-20504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20504-form-container" class="comment-form-container">
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


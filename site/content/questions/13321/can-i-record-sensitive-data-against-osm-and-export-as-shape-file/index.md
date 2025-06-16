+++
type = "question"
title = "Can I record sensitive data against OSM and export as shape file?"
description = '''I want to create some data using the open street map supplied imagery from openstreetmap.org by marking features like polling places and political organizational unit boundaries. Some of data would be sensitive in nature and I cannot contribute that to OSM; and the other non-sensitive data I would b...'''
date = "2012-06-07T21:53:00Z"
lastmod = "2013-10-04T13:24:00Z"
weight = 13321
keywords = [ "shapefile", "data", "private" ]
aliases = [ "/questions/13321" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can I record sensitive data against OSM and export as shape file?](/questions/13321/can-i-record-sensitive-data-against-osm-and-export-as-shape-file)

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
<span id="post-13321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create some data using the open street map supplied imagery from openstreetmap.org by marking features like polling places and political organizational unit boundaries.</p>
<p>Some of data would be sensitive in nature and I cannot contribute that to OSM; and the other non-sensitive data I would be able to contribute to OSM,</p>
<p>Can I do that, and can I create a shape file from the sensitive data?</p>
<p>Thanks, John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '12, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6290d7090ea2280af9ffdc1e300b454e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitchelljj&#39;s gravatar image" />
<p><span>mitchelljj</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitchelljj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '12, 00:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-13321" class="comments-container">
&#10;</div>
<div id="comment-tools-13321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13321-form-container" class="comment-form-container">
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

<span id="13330"></span>

<div id="answer-container-13330" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13330-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two sides to this.</p>
<p>First, the license side. If you create data based on OSM - i.e. you display the OSM map and based on that you draw stuff - then that stuff inherits OSM's open license, currently CC-BY-SA 2.0. This does not mean that you have to contribute the data to OSM but it does mean that <em>if</em> you give the data to anyone, you must do so under the CC-BY-SA 2.0 license. Now if you need the data for use among yourself and a group of others and you can be relatively sure that those who have access to your data will not pass it on then that's fine; but you cannot slap on a legal restriction that says "you <em>must not</em> pass this on".</p>
<p>Second, the technical side. So you want to create a shape file that contains the stuff you have recorded against OSM. This is possible, but depends on the software you have used. You could conceivably use any GIS application that allows displaying tiles in the background, and save directly as shape file from there. Or you could use an OSM editor like JOSM, making sure that you put the sensitive data on a different layer; then save that sensitive data to an OSM file, and run osm2shp or any other osm-to-shape converter on that file. You will probably have to furnish the osm-to-shape converter with some rules so that it generates the columns you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '12, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13330" class="comments-container">
<span id="26947"></span>
<div id="comment-26947" class="comment">
<div id="post-26947-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and recently there were new examples added at Frederik's geofabrik.de showroom,</p>
<p>so have a look at <a href="http://www.geofabrik.de/en/projects/separatedata/index.html">http://www.geofabrik.de/en/projects/separatedata/index.html</a></p>
</div>
<div id="comment-26947-info" class="comment-info">
<span class="comment-age">(04 Oct '13, 13:24)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-13330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13324"></span>

<div id="answer-container-13324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes that is certainly possible. It would be a simple matter of separating the two data-sets from one another. Could you share what file formats this data is in? That would allow us to tell you what software &amp; what procedure you would follow.</p>
<p>Cheers, ingalls</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '12, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/5c34b9dddd033da37483a8634fab6a82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingalls&#39;s gravatar image" />
<p><span>ingalls</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13324" class="comments-container">
&#10;</div>
<div id="comment-tools-13324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19536"></span>

<div id="answer-container-19536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This was a duplicate of <a href="/questions/19537/create-map-with-markers">this question</a></p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '13, 05:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c82d01966f6cd0b4ef4843e4f9907c31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyususu&#39;s gravatar image" />
<p><span>yuyususu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyususu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '13, 09:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span></p>
</div>
</div>
<div id="comments-container-19536" class="comments-container">
&#10;</div>
<div id="comment-tools-19536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19536-form-container" class="comment-form-container">
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


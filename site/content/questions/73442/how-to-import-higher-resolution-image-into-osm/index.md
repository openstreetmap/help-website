+++
type = "question"
title = "How to import higher resolution image into OSM"
description = '''Hello, I am samith. I am interested to learn about OSM editing. Normally OSM satellite map is not a higher resolution image. So, I have difficulty to digitize buildings with higher accuracy. So, I got a new Lidar image with 1 m resolution. That image is a georeferenced image. Now I want to import th...'''
date = "2020-03-09T06:28:00Z"
lastmod = "2020-03-13T15:04:00Z"
weight = 73442
keywords = [ "import", "satellite-images", "editing", "aerial_imagery" ]
aliases = [ "/questions/73442" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to import higher resolution image into OSM](/questions/73442/how-to-import-higher-resolution-image-into-osm)

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
<span id="post-73442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am samith. I am interested to learn about OSM editing. Normally OSM satellite map is not a higher resolution image. So, I have difficulty to digitize buildings with higher accuracy. So, I got a new Lidar image with 1 m resolution. That image is a georeferenced image. Now I want to import that image into OSM. then I can take good resolution and good accuracy of the building layer. Plz explain the process that we can import our images into OSM</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-satellite-images" rel="tag" title="see questions tagged &#39;satellite-images&#39;">satellite-images</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '20, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/8c7a74069411f64a0d22e93e2e451e2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Samith%20Madusanka123&#39;s gravatar image" />
<p><span>Samith Madus...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Samith Madusanka123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73442" class="comments-container">
&#10;</div>
<div id="comment-tools-73442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73442-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="73449"></span>

<div id="answer-container-73449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73449-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>first we do not import imagery in OpenStreetMap, we use it as a background layer to trace data.</p>
<p>Second, when you buy a license to use an image, you don't necessarily buy to right to do everything with it, I think you should check that.</p>
<p>One of the most tricky point is that people sell OSM data, and the license allow this. So they will sell data coming from your interpretation of this imagery. I see three results possible :</p>
<ol>
<li>You really can do anything, including sharing it with others.</li>
<li>You can use it to produce other work, which you can share.</li>
<li>You can't share anything coming from that data.</li>
</ol>
<p>If 1., then I think you best bet would be to upload it to <a href="https://openaerialmap.org/">OpenAerialMap</a>, so that anybody will be able to use it also. This platform is meant for UAV imagery, but I think Lidar could fit as well. There might be other platforms.</p>
<p>If 2., the problem is that you'll be able to trace from your imagery, but nobody will be able to <a href="https://wiki.openstreetmap.org/wiki/Verifiability">check your work</a>. If you use it to fine-tune geometry of objects visible on other imagery, that should be fine. But if you add objects, other people might delete them.</p>
<p>Disclaimer, I'm no lawyer, I might be wrong on my interpretation of the license.</p>
<p>If you need help for the technical part, please tell at least the file format of your data. JOSM should be able to open most geo-referenced image, for example with this <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/ImportImagePlugin">plugin</a>.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '20, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73449" class="comments-container">
<span id="73450"></span>
<div id="comment-73450" class="comment">
<div id="post-73450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Realy appreciate your valuable answer sir. The format of the image is tif. it is a georeferenced Lidar image. i want to use it as a background image to edit map. Plz, guide me to know this process, sir.</p>
</div>
<div id="comment-73450-info" class="comment-info">
<span class="comment-age">(09 Mar '20, 18:18)</span> <span class="comment-user userinfo">Samith Madus...</span>
</div>
</div>
<span id="73504"></span>
<div id="comment-73504" class="comment">
<div id="post-73504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you familiar with JOSM ?</p>
<p>You can use the previously mentioned plugin if your tif is not WGS84. Otherwise, I think you just have to open your file with JOSM, and it will load as a background layer.</p>
<p>Unfortunately I don't have access to geotiff files, so I can't test. If you can share a sample of your files, or one of the same source, it would be easier to help you.</p>
<p>Best regards.</p>
</div>
<div id="comment-73504-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 15:04)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73449-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73443"></span>

<div id="answer-container-73443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need permissions from the owners of the images before they can used for OSM mapping see <a href="https://wiki.openstreetmap.org/wiki/Copyright">https://wiki.openstreetmap.org/wiki/Copyright</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '20, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-73443" class="comments-container">
<span id="73444"></span>
<div id="comment-73444" class="comment">
<div id="post-73444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. I have bought it Sir. I have ownership of that. But I can not sell it again. Then how I can import it.</p>
</div>
<div id="comment-73444-info" class="comment-info">
<span class="comment-age">(09 Mar '20, 09:18)</span> <span class="comment-user userinfo">Samith Madus...</span>
</div>
</div>
<span id="73445"></span>
<div id="comment-73445" class="comment">
<div id="post-73445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That may not be good enough. But hopefully it is. Someone with better legal knowledge can answer it for you. The JOSM editor may have a plugin that can use the image, but i haven't used it. <a href="https://help.openstreetmap.org/questions/14552/is-there-an-editor-to-drag-and-drop-imagesicons-and-rotate-them-into-the-map">https://help.openstreetmap.org/questions/14552/is-there-an-editor-to-drag-and-drop-imagesicons-and-rotate-them-into-the-map</a></p>
</div>
<div id="comment-73445-info" class="comment-info">
<span class="comment-age">(09 Mar '20, 09:49)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-73443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73443-form-container" class="comment-form-container">
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


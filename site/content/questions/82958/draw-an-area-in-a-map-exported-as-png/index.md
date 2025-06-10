+++
type = "question"
title = "Draw an area in a map exported as PNG"
description = '''Hi, I have exported a map with OpenStreetMap as a PNG-file. Now I want to select an area an highlight it to visualize in the image where I am going to conduct research. What is the best way to do this, considering I do not have any experience with Photoshop?  Thanks!'''
date = "2022-01-05T13:45:00Z"
lastmod = "2022-01-06T14:04:00Z"
weight = 82958
keywords = [ "image", "area" ]
aliases = [ "/questions/82958" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Draw an area in a map exported as PNG](/questions/82958/draw-an-area-in-a-map-exported-as-png)

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
<span id="post-82958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have exported a map with OpenStreetMap as a PNG-file. Now I want to select an area an highlight it to visualize in the image where I am going to conduct research. What is the best way to do this, considering I do not have any experience with Photoshop?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '22, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bdfc141c579a0698c28c07f909b4503d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koen&#39;s gravatar image" />
<p><span>Koen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82958" class="comments-container">
&#10;</div>
<div id="comment-tools-82958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82958-form-container" class="comment-form-container">
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

<span id="82967"></span>

<div id="answer-container-82967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82967-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>Is your research area defined in OSM, such as a district of an administrative area, etc?</p>
<p><a href="https://overpass-turbo.eu/s/1eRc">https://overpass-turbo.eu/s/1eRc</a></p>
<pre><code>rel[name=&quot;Greater London&quot;];
way(r);
out geom;</code></pre>
<p>Then Export-&gt;Map-&gt;PNG</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '22, 02:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '22, 14:37</strong> </span></p>
</div>
</div>
<div id="comments-container-82967" class="comments-container">
<span id="82973"></span>
<div id="comment-82973" class="comment">
<div id="post-82973-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should mention that this is using overpass-turbo website.</p>
</div>
<div id="comment-82973-info" class="comment-info">
<span class="comment-age">(06 Jan '22, 14:04)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-82967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82959"></span>

<div id="answer-container-82959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82959-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>this is not an OSM related question.</p>
<p>But usually I use GIMP instead of photoshop (open-source).</p>
<p>Here are a few pointers to help you :</p>
<ul>
<li><a href="https://docs.gimp.org/2.10/en/gimp-using-rectangular.html">GIMP official doc</a></li>
<li><a href="https://superuser.com/questions/167873/how-do-i-draw-a-box-in-gimp">SuperUser question</a></li>
</ul>
<p>But you might want to use other, simpler, tools, like LibreOffice Draw, InkScape and so on. GIMP and photoshop are not designed for this kind of task.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '22, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82959" class="comments-container">
&#10;</div>
<div id="comment-tools-82959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82959-form-container" class="comment-form-container">
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


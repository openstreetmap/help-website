+++
type = "question"
title = "Problem with SVG export"
description = '''Maps exported from OSM in SVG file format contain a large black background that extend beyond the map area I&#x27;ve selected. So far, I&#x27;ve been unable to remove this black background. I&#x27;ve tried about 6 vector graphics applications and none allow me to edit / remove this black area surrounding the area ...'''
date = "2020-03-17T14:01:00Z"
lastmod = "2020-03-17T18:32:00Z"
weight = 73576
keywords = [ "svg", "export" ]
aliases = [ "/questions/73576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with SVG export](/questions/73576/problem-with-svg-export)

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
<span id="post-73576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Maps exported from OSM in SVG file format contain a large black background that extend beyond the map area I've selected. So far, I've been unable to remove this black background. I've tried about 6 vector graphics applications and none allow me to edit / remove this black area surrounding the area I've selected in OSM.</p>
<p>Is there a setting I've missed or some other way to prevent this extended black background from the SVG export?</p>
<p>The attached screenshot shows the problem. This is a cropped screenshot. The black background in the actual file exported from OPS is much larger.</p>
<p>Thank you for any advise or help.</p>
<p><img src="/upfiles/OSM_ss_2020-03-17_qmS8RLu.png" alt="Screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '20, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1adb0022bbbc4f7788d82985630e5b26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sccardais&#39;s gravatar image" />
<p><span>Sccardais</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sccardais has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73576" class="comments-container">
&#10;</div>
<div id="comment-tools-73576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73576-form-container" class="comment-form-container">
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

<span id="73585"></span>

<div id="answer-container-73585" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73585-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's probably not a black background in the file. My guess is that some of the features (like the roads and railway lines in your example) stretch beyond the area that you've selected, so they are included in the file. When you are viewing your map, you see the area that you select, plus extra space around it so that the long roads are shown too. So you aren't trying to remove the black background, what you want to do is trim off (crop) all the extra bits that stick out around the selected area.</p>
<p>Or you could set a background colour for your document, or add a big rectangle below everything with the same colour as the land. But you would need to be aware that only some features are shown beyond the original extent of the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '20, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-73585" class="comments-container">
<span id="73586"></span>
<div id="comment-73586" class="comment">
<div id="post-73586-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A tutorial for cropping osm.org exports with Sketch : <a href="https://medium.com/@sam__rye/a-guide-to-creating-scalable-vector-maps-92e891f0ad3e">https://medium.com/@sam__rye/a-guide-to-creating-scalable-vector-maps-92e891f0ad3e</a></p>
<p>The general documentation to do this with InkScape (Free Software) : <a href="https://inkscapetutorials.wordpress.com/2014/04/22/inkscape-faq-how-do-i-crop-in-inkscape/#clipping">https://inkscapetutorials.wordpress.com/2014/04/22/inkscape-faq-how-do-i-crop-in-inkscape/#clipping</a></p>
<p>More details and alternatives on the wiki : <a href="https://wiki.openstreetmap.org/wiki/SVG">https://wiki.openstreetmap.org/wiki/SVG</a></p>
</div>
<div id="comment-73586-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 18:32)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73585-form-container" class="comment-form-container">
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


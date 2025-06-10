+++
type = "question"
title = "How to copy grass from one JOSM file to another?"
description = '''Right now I have two main .OSM files: one where the buildings have all been traced in more detail and have been given accurate height values, and one that has all the grass in the right places. Because, somehow, a few patches of grass were removed from the main OSM I&#x27;m working on, and I need to tran...'''
date = "2015-12-17T17:40:00Z"
lastmod = "2015-12-18T11:10:00Z"
weight = 47199
keywords = [ "josm", "osmconvert", "landuse", "grass", "osm" ]
aliases = [ "/questions/47199" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to copy grass from one JOSM file to another?](/questions/47199/how-to-copy-grass-from-one-josm-file-to-another)

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
<span id="post-47199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47199-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Right now I have two main .OSM files: one where the buildings have all been traced in more detail and have been given accurate height values, and one that has all the grass in the right places. Because, somehow, a few patches of grass were removed from the main OSM I'm working on, and I need to transplant them back from the other OSM file. But I can't, because JOSM doesn't let you select parts of the map with the tag landuse=grass, and the clipboards of two instances of JOSM are separate, so I couldn't copy the grass from one to the other in JOSM even if I could select it. I've tried to put the grass back in by merging the files with osmconvert, but that always screws up a bunch of the buildings, and sometimes duplicates the buildings as well. I need a way to isolate and copy those two sections of grass to the other OSM file. Does anyone know how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-grass" rel="tag" title="see questions tagged &#39;grass&#39;">grass</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '15, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/8d4fb71b578dcbdaaee8353dbf349326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bgiglione&#39;s gravatar image" />
<p><span>bgiglione</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bgiglione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47199" class="comments-container">
&#10;</div>
<div id="comment-tools-47199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47199-form-container" class="comment-form-container">
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

<span id="47208"></span>

<div id="answer-container-47208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47208-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Save your two osm files locally if not done already.</li>
<li>Close all your JOSM instances, start only one.</li>
<li>Open both osm files, as separated layers.</li>
<li>Switch to the grass layer, seach (Ctrl-F) for landuse=grass, copy (Ctrl-C).</li>
<li>Switch to the main layer, Paste (Ctrl-V).</li>
<li>Check for duplicate data, save your work.</li>
<li>Profit !</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '15, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-47208" class="comments-container">
&#10;</div>
<div id="comment-tools-47208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47208-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47202"></span>

<div id="answer-container-47202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47202-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry to say so, but your problem doesn't make a lot of sense.</p>
<p>Naturally you can select, copy and then paste an element to a different layer in JOSM and landuse=grass is no different than anything else.</p>
<p>Note: it is not quite clear if your "two" instances is just a typo or serious. You should -not- be running two instances of JOSM in parallel, you simply load your data files in to two different layers in the same instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '15, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '15, 20:47</strong> </span></p>
</div>
</div>
<div id="comments-container-47202" class="comments-container">
&#10;</div>
<div id="comment-tools-47202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47202-form-container" class="comment-form-container">
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


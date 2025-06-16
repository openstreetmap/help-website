+++
type = "question"
title = "How should I export OSM data to .PBF for use in Globalmapper for proper rendering?"
description = '''Hi, I have downloaded latest .pbf files for arizona ans washington regions. I converted them to .osm files using osmconvert(windows platform) and I extracted sub regions from them using bounding box command. When I open those output files in Globalmapper road networks are coming like irregular multi...'''
date = "2013-08-28T09:53:00Z"
lastmod = "2013-08-29T11:26:00Z"
weight = 25885
keywords = [ "osmconvert", "export", "globalmapper" ]
aliases = [ "/questions/25885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How should I export OSM data to .PBF for use in Globalmapper for proper rendering?](/questions/25885/how-should-i-export-osm-data-to-pbf-for-use-in-globalmapper-for-proper-rendering)

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
<span id="post-25885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25885-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have downloaded latest .pbf files for arizona ans washington regions. I converted them to .osm files using osmconvert(windows platform) and I extracted sub regions from them using bounding box command. When I open those output files in Globalmapper road networks are coming like irregular multiple radial lines crossing through other features.</p>
<p>I could not find where the problem occurs. Could you please help? <img src="/upfiles/washington_osm_2.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-globalmapper" rel="tag" title="see questions tagged &#39;globalmapper&#39;">globalmapper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '13, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/3bbb39efe1f2875e439ef6145dc83ce2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phanindra&#39;s gravatar image" />
<p><span>Phanindra</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phanindra has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '13, 11:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-25885" class="comments-container">
&#10;</div>
<div id="comment-tools-25885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25885-form-container" class="comment-form-container">
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

<span id="25886"></span>

<div id="answer-container-25886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try using the option <code>--drop-broken-refs</code> on osmconvert when you extract a bounding box. It is possible that GlobalMapper has problems when a way includes references to nodes that are not contained in the extract; this option will remove those references.</p>
<p>Having said that, I have seen other people having similar issues with GlobalMapper even when their data had full referential integrity; you'd probably have to check with the makers of GlobalMapper then because it is a malfunction on their part.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '13, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25886" class="comments-container">
<span id="25887"></span>
<div id="comment-25887" class="comment">
<div id="post-25887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>Thanks for your suggestion. I tried using the option as u said, but still the problem exists. Yeah...this could be due to GlobalMapper incapability. could u please suggest me what are other enviroments which support osm. i have ArcGIS desktop with me please let me know how to open in this environment.</p>
</div>
<div id="comment-25887-info" class="comment-info">
<span class="comment-age">(28 Aug '13, 10:55)</span> <span class="comment-user userinfo">Phanindra</span>
</div>
</div>
</div>
<div id="comment-tools-25886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25918"></span>

<div id="answer-container-25918" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25918-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is most probably a bug in GlobalMapper.</p>
<p>My first suggestion would be to ask GlobalMapper support (as you seem to have a registered version).</p>
<p>Even before that, update the version - <a href="http://www.bluemarblegeo.com/products/global-mapper-download.php">the current version is 14.2</a>!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '13, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MagicFab has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-25918" class="comments-container">
&#10;</div>
<div id="comment-tools-25918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25918-form-container" class="comment-form-container">
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

